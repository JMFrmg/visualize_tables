# Visialisation des données contenues dans une base de données sqlite
Projet réalisé dans le cadre de la formation développeur en intelligence artificielle, Strasbourg, 2024/2026

## Créer l'environnement virtuel
A la racine du projet taper dans le terminal ou powershell :
```bash
python -m venv .venv
```

## Activer l'environnement virtuel
### Linux (terminal)
```bash
source .venv/bin/activate
```
### Windows (powershell)
```bash
.venv/Scripts/Activate.ps1
```

## Installer flask
```bash
pip install flask
```

## Lancer l'application
```bash
python -m flask run --debug
```

## Routes
/dataviz/all-data : affiche les données des quatre tables (sans les ids)  
/dataviz/detail/nom_table : affiche les données spécifiques à une table (avec les ids)
