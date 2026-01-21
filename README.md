# Blog Interactif - Cosmos Blog

Application web de blog avec système d'interaction sociale complet développée pour **Gaetane MVIBUNDULU**.

## 🚀 Fonctionnalités

### ✅ Authentification
- Inscription avec nom d'utilisateur, email et mot de passe
- Connexion/Déconnexion sécurisée
- Restrictions d'accès pour les actions (publication, likes, commentaires)

### ✅ Gestion des Articles
- **Création** : Titre, contenu et image de couverture
- **Lecture** : Liste chronologique et pages détaillées
- **Modification/Suppression** : Réservée à l'auteur ou admin

### ✅ Système de "J'aime"
- Un like par utilisateur par article
- Toggle (aimer/ne plus aimer)
- Comptage en temps réel

### ✅ Commentaires Hiérarchiques
- Commentaires principaux sur les articles
- Réponses aux commentaires (imbrication)
- Affichage indenté pour la lisibilité
- Comptage total (parents + réponses)

## 🛠 Technologies

- **Backend** : Python 3.x + Django 4.x
- **Base de données** : SQLite (développement)
- **Frontend** : HTML5, CSS3, JavaScript, Bootstrap 5
- **Templates** : Django Template Language (DTL)

## 📦 Installation

1. **Cloner le projet** (si applicable)
2. **Installer les dépendances** :
   ```bash
   pip install django pillow
   ```
3. **Configuration automatique** :
   ```bash
   python setup.py
   ```
4. **Lancer le serveur** :
   ```bash
   python manage.py runserver
   ```

## 🎯 Utilisation

### Accès
- **Site** : http://127.0.0.1:8000
- **Admin** : http://127.0.0.1:8000/admin (admin/admin123)

### Workflow
1. **Visiteurs** : Peuvent lire articles et commentaires
2. **Utilisateurs connectés** : Peuvent publier, liker, commenter
3. **Auteurs** : Peuvent modifier/supprimer leurs articles
4. **Admins** : Accès complet via l'interface d'administration

## 🏗 Architecture

### Modèles
- **Article** : title, content, cover_image, author, created_at, likes
- **Comment** : article, author, body, created_at, parent (auto-référence)

### Vues Principales
- `ArticleListView` : Liste paginée des articles
- `ArticleDetailView` : Détail + commentaires hiérarchiques
- `toggle_like` : Gestion des likes (AJAX-friendly)
- `add_comment` : Ajout commentaires/réponses

### Templates
- Système de commentaires récursifs avec `comment_tree.html`
- Design responsive avec Bootstrap 5
- Thème sombre "Cosmos" avec effets glassmorphism

## 🎨 Design

Interface moderne avec :
- Palette violette/lavande sur fond sombre
- Effets de transparence (glassmorphism)
- Responsive design
- Animations subtiles

## 🔒 Sécurité

- Protection CSRF sur tous les formulaires
- Authentification requise pour les actions sensibles
- Validation des permissions (auteur/admin)
- Échappement automatique des données utilisateur

## 📝 Développement

Structure du projet :
```
monapp/
├── blog/                 # Application principale
├── templates/           # Templates HTML
├── static/             # CSS, JS, images
├── media/              # Uploads utilisateurs
├── db.sqlite3          # Base de données
└── manage.py           # Commandes Django
```

---

**Développé avec ❤️ pour Gaetane MVIBUNDULU**  
*Interactions sociales complètes - Django Framework*