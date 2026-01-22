#!/bin/bash
# Script de déploiement pour PythonAnywhere

echo "=== Configuration PythonAnywhere ==="

# 1. Installer les dépendances
echo "Installation des dépendances..."
pip3.10 install --user -r requirements.txt

# 2. Migrations de la base de données
echo "Migrations de la base de données..."
python3.10 manage.py makemigrations
python3.10 manage.py migrate

# 3. Collecter les fichiers statiques
echo "Collection des fichiers statiques..."
python3.10 manage.py collectstatic --noinput

# 4. Créer un superutilisateur (optionnel)
echo "Pour créer un superutilisateur, exécutez:"
echo "python3.10 manage.py createsuperuser"

echo "=== Déploiement terminé ==="