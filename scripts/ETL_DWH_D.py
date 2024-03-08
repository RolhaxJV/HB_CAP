from app.models import ODS_FTD,D_Date,D_Depart,D_Type

def run():
    """
    A function that attempts to call three other functions and catches a KeyError if it occurs.
    """
    try:
        colonnes_Type()
        colonnes_Date()
        colonnes_Departement()
    except KeyError as e:
        print(e)


def colonnes_Date():
    """
    This function retrieves distinct date_fin_semaine values from ODS_FTD and creates D_Date objects for each value. It then bulk creates the D_Date objects. If a KeyError occurs during the process, it prints the error message.
    """
    queryset = ODS_FTD.objects.values('date_fin_semaine').distinct()

    l = []
    D_Date.objects.all().delete()
    try :
        for item in queryset:
            obj = D_Date(
                date = item["date_fin_semaine"]
                )
            l.append(obj)
        D_Date.objects.bulk_create(l)
        
        print("Date : OK")
    except KeyError as e:
        print(e)

def colonnes_Departement():
    """
    This function retrieves unique values for code_region, code_departement, libelle_region, and libelle_departement from the ODS_FTD model, creates D_Depart objects based on the retrieved values, and bulk creates them. It also prints "Depart : OK" if successful, or prints the KeyError if it occurs.
    """
    queryset = ODS_FTD.objects.values('code_region', 'code_departement', 'libelle_region', 'libelle_departement').distinct()

    l = []
    existing_pks = set()
    D_Depart.objects.all().delete()
    try :
        for item in queryset:
            pk_depart = "_".join([item['code_region'], item['code_departement'], item['libelle_departement']])

            if pk_depart in existing_pks or len(item['code_departement']) < 2:
                continue
            existing_pks.add(pk_depart)

            obj = D_Depart(
                code_region = item['code_region'],
                code_depart = item['code_departement'],
                label_region = item['libelle_region'],
                label_depart = item['libelle_departement'],
                pk_depart = pk_depart
                )
            l.append(obj)
        D_Depart.objects.bulk_create(l)
        
        print("Depart : OK")
    except KeyError as e:
        print(e)
    

def colonnes_Type():
    """ """
    queryset = ODS_FTD.objects.values('type_de_vaccin').distinct()

    l = []
    D_Type.objects.all().delete()
    try :
        for item in queryset:
            obj = D_Type(
                label = item["type_de_vaccin"]
                )
            l.append(obj)
        D_Type.objects.bulk_create(l)
        
        print("Type : OK")
    except KeyError as e:
        print(e)