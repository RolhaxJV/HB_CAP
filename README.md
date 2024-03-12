# HB_CAP

Ce dépôt contient un projet Django visant à créer une API permettant la mise en base de données de fichiers CSV contenant des données sur les doses de vaccins contre le COVID-19.

## Objectif du projet

Le projet HB_CAP a pour objectif de faciliter la gestion et l'analyse des données relatives aux doses de vaccins contre le COVID-19. Il permet de stocker ces données dans une base de données, d'y accéder via une API RESTful et de les manipuler selon les besoins.

## Contenu du dépôt

```
- api/
  - ...
- data/
  - ...
- scripts/
  - ...
- tests/
  - ...
- README.md
- requirements.txt
- .gitignore
```

## Structure du projet

- **api/** : Contient les fichiers Django définissant les endpoints de l'API.
- **data/** : Répertoire pour stocker les fichiers CSV contenant les données sur les doses de vaccins.
- **scripts/** : Scripts utilitaires pour le traitement et l'importation des données dans la base de données.
- **tests/** : Tests unitaires et tests d'intégration pour assurer le bon fonctionnement de l'API.
- **README.md** : Ce fichier README.
- **requirements.txt** : Liste des dépendances Python requises pour exécuter le projet.
- **.gitignore** : Fichier spécifiant les fichiers et répertoires à ignorer lors des opérations Git.

## Utilisation

1. Assurez-vous d'avoir Python et Django installés sur votre système.
2. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/RolhaxJV/HB_CAP.git
   ```

3. Installez les dépendances requises :

   ```bash
   pip install -r requirements.txt
   ```

4. Configurez votre base de données dans les paramètres Django.
5. Exécutez les migrations pour créer les tables de base de données :

   ```bash
   python manage.py migrate
   ```

6. Lancez le serveur de développement Django :

   ```bash
   python manage.py runserver
   ```

7. Accédez à l'API à l'adresse `http://localhost:8000/api/`.

## Contributions

Les contributions à ce projet sont les bienvenues. Si vous souhaitez contribuer, veuillez soumettre une Pull Request avec vos modifications.
