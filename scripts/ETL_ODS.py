import pandas as pd
from app.models import ODS_FTD
from covid_project.settings import DATA_DIR

def run():
    """ Remplis la table ods_clubs
    """
    try:
        # Lire CSV
        df = pd.read_csv(f"{DATA_DIR}/clubs-data-2021.csv", delimiter=';')

        # Truncate
        ODS_CLUBS.objects.all().delete()

        objs = []
        for index, row in df.iterrows():
            obj = ODS_CLUBS(
                code_commune = row["Code Commune"],
                commune = row["Commune"],
                code_QPV = row["Code QPV"],
                nom_QPV = row["Nom QPV"],
                departement = row["Département"],
                region = row["Région"],
                statut_geo = row["Statut géo"],
                code = row["Code"],
                federation = row["Fédération"],
                clubs = row["Clubs"],
                EPA = row["EPA"],
                Total = row["Total"]
            )
            objs.append(obj)

        # Bulk create des objets
        ODS_CLUBS.objects.bulk_create(objs)
    except KeyError as e:
        print(e)
