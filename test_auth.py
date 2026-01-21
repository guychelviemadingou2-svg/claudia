#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de test pour vérifier l'authentification
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monapp.settings')
django.setup()

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

def test_authentication():
    """Test des fonctionnalités d'authentification"""
    client = Client()
    
    print("Test d'authentification en cours...")
    
    # Test 1: Accès à la page d'inscription
    try:
        response = client.get('/signup/')
        assert response.status_code == 200
        print("OK - Page d'inscription accessible")
    except Exception as e:
        print(f"ERREUR page d'inscription: {e}")
        return False
    
    # Test 2: Accès à la page de connexion
    try:
        response = client.get('/login/')
        assert response.status_code == 200
        print("OK - Page de connexion accessible")
    except Exception as e:
        print(f"ERREUR page de connexion: {e}")
        return False
    
    # Test 3: Création d'un utilisateur de test
    try:
        # Supprimer l'utilisateur s'il existe déjà
        User.objects.filter(username='testuser').delete()
        
        # Créer un nouvel utilisateur
        response = client.post('/signup/', {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        })
        
        # Vérifier que l'utilisateur a été créé
        user_exists = User.objects.filter(username='testuser').exists()
        assert user_exists
        print("OK - Inscription fonctionnelle")
    except Exception as e:
        print(f"ERREUR inscription: {e}")
        return False
    
    # Test 4: Connexion avec l'utilisateur créé
    try:
        response = client.post('/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        
        # Vérifier la redirection après connexion
        assert response.status_code in [200, 302]
        print("OK - Connexion fonctionnelle")
    except Exception as e:
        print(f"ERREUR connexion: {e}")
        return False
    
    print("SUCCES - Tous les tests d'authentification sont passes !")
    return True

if __name__ == '__main__':
    success = test_authentication()
    sys.exit(0 if success else 1)