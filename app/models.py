from django.db import models

# Table d'ODS
class ODS_FTD(models.Model):
    code_region = models.CharField(max_length = 100, default='0')
    libelle_region = models.CharField(max_length = 100, default='0')
    code_departement = models.CharField(max_length = 100, default='0')
    libelle_departement = models.CharField(max_length = 100, default='0')
    date_fin_semaine = models.CharField(max_length = 100, default='0')
    type_de_vaccin = models.CharField(max_length = 100, default='0')
    nb_ucd = models.CharField(max_length = 100, default='0')
    nb_doses = models.CharField(max_length = 100, default='0')
    
    def __str__(self) -> str:
        return f"{self.code_region} - {self.code_departement}"

# region Tables Dimensions
class D_Depart(models.Model):
    code_region = models.IntegerField()
    code_depart = models.IntegerField()
    label_region = models.CharField(max_length = 100, default=None)
    label_depart = models.CharField(max_length = 100, default=None)
    
    pk_depart = models.CharField(max_length=100, primary_key=True, default=None)
    
class D_Type(models.Model):
    label = models.CharField(max_length = 100, primary_key=True, default=None)

class D_Date(models.Model):
    date = models.DateField(primary_key=True)
# endregion

# Table de Fait
class F_Dose(models.Model):
    nb_ucd = models.IntegerField()
    nb_dose = models.IntegerField()
    
    pk_dose = models.CharField(max_length=100, primary_key=True, default=None)
    
    Type = models.ForeignKey(D_Type, on_delete=models.CASCADE)
    Date = models.ForeignKey(D_Date, on_delete=models.CASCADE)
    Depart = models.ForeignKey(D_Depart, on_delete=models.CASCADE)