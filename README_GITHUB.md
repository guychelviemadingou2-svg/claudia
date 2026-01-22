# 🌌 Cosmos Blog - Blog Interactif avec Design Violet

Application web de blog avec système d'interaction sociale complet développée pour **Gaetane MVIBUNDULU**.

![Cosmos Blog](https://img.shields.io/badge/Django-4.x-green) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![Design](https://img.shields.io/badge/Design-Violet%20Cosmique-purple)

## ✨ Fonctionnalités

### 🔐 Authentification
- Inscription avec nom d'utilisateur, email et mot de passe
- Connexion/Déconnexion sécurisée
- Compte test : `test` / `test123`

### 📝 Gestion des Articles
- **Création** : Titre, contenu et image de couverture
- **Lecture** : Liste chronologique et pages détaillées
- **Modification/Suppression** : Réservée à l'auteur ou admin

### 💜 Système de "J'aime"
- Un like par utilisateur par article
- Toggle (aimer/ne plus aimer)
- Comptage en temps réel

### 💬 Commentaires Hiérarchiques
- Commentaires principaux sur les articles
- Réponses aux commentaires (imbrication)
- Affichage indenté avec avatars
- Comptage total (parents + réponses)

## 🎨 Design Violet Cosmique

- Interface moderne avec palette violette/lavande
- Effets glassmorphism et animations fluides
- Design responsive avec Bootstrap 5
- Thème sombre "Cosmos" immersif

## 🛠 Technologies

- **Backend** : Python 3.x + Django 4.x
- **Base de données** : SQLite
- **Frontend** : HTML5, CSS3, JavaScript, Bootstrap 5
- **Templates** : Django Template Language (DTL)

## 📦 Installation

1. **Cloner le projet**
   ```bash
   git clone https://github.com/votre-username/cosmos-blog.git
   cd cosmos-blog
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration automatique**
   ```bash
   python setup.py
   ```

4. **Créer un utilisateur test**
   ```bash
   python create_test_user.py
   ```

5. **Lancer le serveur**
   ```bash
   python manage.py runserver
   ```

## 🚀 Utilisation

### Accès
- **Site** : http://127.0.0.1:8000
- **Admin** : http://127.0.0.1:8000/admin (admin/admin123)
- **Test** : test/test123

### Workflow
1. **Visiteurs** : Peuvent lire articles et commentaires
2. **Utilisateurs connectés** : Peuvent publier, liker, commenter
3. **Auteurs** : Peuvent modifier/supprimer leurs articles
4. **Admins** : Accès complet via l'interface d'administration

## 🏗 Structure du Projet

```
cosmos-blog/
├── blog/                 # Application principale
├── templates/           # Templates HTML
├── static/             # CSS, JS, images
├── media/              # Uploads utilisateurs
├── requirements.txt    # Dépendances
├── setup.py           # Configuration automatique
└── manage.py          # Commandes Django
```

## 🔒 Sécurité

- Protection CSRF sur tous les formulaires
- Authentification requise pour les actions sensibles
- Validation des permissions (auteur/admin)
- Échappement automatique des données utilisateur

## 🤝 Contribution

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -m 'Ajout nouvelle fonctionnalité'`)
4. Push vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

**Développé avec 💜 pour Gaetane MVIBUNDULU**  
*Interactions sociales complètes - Django Framework*