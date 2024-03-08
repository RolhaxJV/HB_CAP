import pandas as pd
from app.models import ODS_FTD
from covid_project.settings import DATA_DIR

def run():
	"""
	Run function to read a CSV file, truncate a database table, iterate through the CSV data to create objects, and bulk create the objects in the database. Catches a KeyError and prints the error.
	"""
    try:
        # Lire CSV
        df = pd.read_csv(f"{DATA_DIR}/flux-total-dep.csv", delimiter=',', encoding="'ISO-8859-1")

        # Truncate
        ODS_FTD.objects.all().delete()

        objs = []
        for index,row in df.iterrows():
            obj = ODS_FTD(
                code_region = row["code_region"],
                libelle_region = row["libelle_region"],
                code_departement = row["code_departement"],
                libelle_departement = row["libelle_departement"],
                date_fin_semaine = row["date_fin_semaine"],
                type_de_vaccin = row["type_de_vaccin"],
                nb_ucd = row["nb_ucd"],
                nb_doses = row["nb_doses"]
            )
            objs.append(obj)

        # Bulk create des objets
        ODS_FTD.objects.bulk_create(objs)
    except KeyError as e:
        print(e)
