#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monapp.settings')
django.setup()

from django.contrib.auth.models import User

# Créer un utilisateur test simple
username = 'test'
password = 'test123'
email = 'test@example.com'

if not User.objects.filter(username=username).exists():
    user = User.objects.create_user(username=username, email=email, password=password)
    print(f"Utilisateur '{username}' cree avec succes!")
    print(f"Mot de passe: {password}")
else:
    print(f"L'utilisateur '{username}' existe deja.")