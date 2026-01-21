#!/usr/bin/env python3
"""
Script pour creer des donnees de test
"""

import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monapp.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Article, Comment

def create_test_data():
    """Cree des donnees de test pour demonstration"""
    
    print("Creation des donnees de test...")
    
    # Creer des utilisateurs de test
    users_data = [
        ('gaetane', 'gaetane@example.com', 'Gaetane MVIBUNDULU'),
        ('alice', 'alice@example.com', 'Alice Dubois'),
        ('bob', 'bob@example.com', 'Bob Martin'),
    ]
    
    users = {}
    for username, email, full_name in users_data:
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'first_name': full_name.split()[0],
                'last_name': ' '.join(full_name.split()[1:]) if len(full_name.split()) > 1 else ''
            }
        )
        if created:
            user.set_password('password123')
            user.save()
            print(f"Utilisateur cree: {username}")
        users[username] = user
    
    # Creer des articles de test
    articles_data = [
        {
            'title': 'Bienvenue sur Cosmos Blog',
            'content': '''Bienvenue dans notre espace d'expression et de partage ! 

Ce blog interactif a ete concu pour favoriser les echanges et les discussions constructives. Vous pouvez publier vos articles, reagir avec des "J'aime" et participer aux conversations via les commentaires.

N'hesitez pas a explorer toutes les fonctionnalites : publication d'articles avec images, systeme de likes, commentaires hierarchiques avec possibilite de repondre specifiquement a chaque message.

Bonne decouverte !''',
            'author': 'gaetane'
        },
        {
            'title': 'Les fonctionnalites du blog',
            'content': '''Notre plateforme offre un ensemble complet de fonctionnalites sociales :

**Authentification securisee**
- Inscription simple avec email
- Connexion/deconnexion
- Gestion des permissions

**Gestion des articles**
- Creation avec titre, contenu et image
- Modification et suppression par l'auteur
- Affichage chronologique

**Systeme de likes**
- Un like par utilisateur
- Toggle pour aimer/ne plus aimer
- Comptage en temps reel

**Commentaires hierarchiques**
- Commentaires sur les articles
- Reponses aux commentaires
- Affichage indente pour la clarte

L'interface moderne avec son theme sombre et ses effets de transparence offre une experience utilisateur agreable et intuitive.''',
            'author': 'alice'
        },
        {
            'title': 'Conseils pour une bonne utilisation',
            'content': '''Pour tirer le meilleur parti de cette plateforme, voici quelques conseils :

**Pour les articles :**
- Choisissez des titres accrocheurs
- Structurez votre contenu avec des paragraphes
- Ajoutez une image de couverture si possible

**Pour les interactions :**
- Likez les articles qui vous plaisent
- Participez aux discussions dans les commentaires
- Repondez specifiquement aux messages pour maintenir le fil de conversation

**Bonnes pratiques :**
- Respectez les autres utilisateurs
- Evitez le spam et les messages hors-sujet
- Signalez tout contenu inapproprie aux administrateurs

Ensemble, creons une communaute bienveillante et enrichissante !''',
            'author': 'bob'
        }
    ]
    
    articles = []
    for article_data in articles_data:
        article, created = Article.objects.get_or_create(
            title=article_data['title'],
            defaults={
                'content': article_data['content'],
                'author': users[article_data['author']]
            }
        )
        if created:
            print(f"Article cree: {article.title}")
        articles.append(article)
    
    # Ajouter quelques likes
    articles[0].likes.add(users['alice'], users['bob'])
    articles[1].likes.add(users['gaetane'], users['bob'])
    articles[2].likes.add(users['gaetane'], users['alice'])
    
    # Creer des commentaires de test
    comments_data = [
        {
            'article': articles[0],
            'author': users['alice'],
            'body': 'Excellente initiative ! J\'ai hate de voir ce que cette communaute va produire.'
        },
        {
            'article': articles[0],
            'author': users['bob'],
            'body': 'Interface tres reussie, bravo pour le design !'
        },
        {
            'article': articles[1],
            'author': users['gaetane'],
            'body': 'Merci pour ce recapitulatif complet des fonctionnalites.'
        },
        {
            'article': articles[2],
            'author': users['alice'],
            'body': 'Ces conseils sont tres utiles, surtout pour les nouveaux utilisateurs.'
        }
    ]
    
    for comment_data in comments_data:
        comment, created = Comment.objects.get_or_create(
            article=comment_data['article'],
            author=comment_data['author'],
            body=comment_data['body']
        )
        if created:
            print(f"Commentaire cree sur: {comment.article.title}")
    
    # Creer quelques reponses aux commentaires
    first_comment = Comment.objects.filter(article=articles[0]).first()
    if first_comment:
        reply, created = Comment.objects.get_or_create(
            article=articles[0],
            author=users['gaetane'],
            parent=first_comment,
            body='Merci Alice ! Votre enthousiasme fait plaisir a voir.'
        )
        if created:
            print(f"Reponse creee au commentaire de {first_comment.author}")
    
    print("Donnees de test creees avec succes !")
    print("\nComptes de test crees :")
    for username in users.keys():
        print(f"   - {username} / password123")

if __name__ == '__main__':
    create_test_data()