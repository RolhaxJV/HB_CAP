import pandas as pd
from app.models import ODS_FTD,D_Date,D_Depart,D_Type,F_Dose

def run():
    """ Remplis les tables DWH """
    try:
        # Table de dimension
        type_cache = {type.label: type for type in D_Type.objects.all()}
        date_cache = {date.date: date for date in D_Date.objects.all()} 
        depart_cache = {depart.pk_depart: depart for depart in D_Depart.objects.all()}

        # Tables de Fait Dose
        print("Dose")

        F_Dose.objects.all().delete()
        df = pd.DataFrame(list(ODS_FTD.objects.all().values())).query('nb_ucd != "nan" and nb_doses != "nan"')
        
        existing_pks = set()
        doses = []
        for index, row in df.iterrows():
            if len(row['code_departement']) == 1:
                row['code_departement'] = "0" + row['code_departement']
            
            nb_ucd = row['nb_ucd']
            nb_dose = row['nb_doses']
            date = next((value for value in date_cache.values() if str(value.date) == row['date_fin_semaine']), None)
            depart = next((value for value in depart_cache.values() if value.pk_depart == "_".join([row['code_region'], row['code_departement'], row['libelle_departement']])), None)
            typ = next((value for value in type_cache.values() if value.label == row['type_de_vaccin']), None)
            pk_dose = "_".join([str(typ.label), str(date.date), str(depart.pk_depart)])
            if pk_dose in existing_pks:
                continue
            existing_pks.add(pk_dose)
            dose = F_Dose(
                nb_dose = nb_dose,
                nb_ucd = nb_ucd,

                pk_dose = pk_dose,

                Type = typ,
                Date = date,
                Depart = depart
            )
            doses.append(dose)
            if len(doses) % 1000 == 0 :
                print("Insert")
                F_Dose.objects.bulk_create(doses)
                doses.clear()

        F_Dose.objects.bulk_create(doses)
        doses.clear()
    except KeyError as e:
        print(e)
