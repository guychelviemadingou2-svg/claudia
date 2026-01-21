#!/usr/bin/env python3
"""
Script de configuration initiale pour le Blog Interactif
Développé pour Gaetane MVIBUNDULU
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_project():
    """Configure le projet Django"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monapp.settings')
    django.setup()
    
    print("🚀 Configuration du Blog Interactif...")
    
    # Créer les migrations
    print("📦 Création des migrations...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    # Appliquer les migrations
    print("🔧 Application des migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Créer un superutilisateur si nécessaire
    from django.contrib.auth.models import User
    if not User.objects.filter(is_superuser=True).exists():
        print("👤 Création du compte administrateur...")
        print("Nom d'utilisateur: admin")
        print("Mot de passe: admin123")
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    
    print("✅ Configuration terminée!")
    print("🌐 Lancez le serveur avec: python manage.py runserver")
    print("🔑 Admin: http://127.0.0.1:8000/admin (admin/admin123)")

if __name__ == '__main__':
    setup_project()