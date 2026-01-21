# Guide de déploiement PythonAnywhere

## 1. Créer un compte sur PythonAnywhere
- Allez sur https://www.pythonanywhere.com
- Créez un compte gratuit

## 2. Cloner votre projet
Dans la console Bash de PythonAnywhere :
```bash
git clone https://github.com/guychelviemadingou2-svg/claudia.git
cd claudia
```

## 3. Installer les dépendances
```bash
pip3.10 install --user django pillow
```

## 4. Configuration de la base de données
```bash
python3.10 manage.py migrate
python3.10 manage.py createsuperuser
```

## 5. Configurer l'application web
- Onglet "Web" → "Add a new web app"
- Choisir "Manual configuration"
- Python 3.10
- Dans "Code" section :
  - Source code: /home/VOTRE_USERNAME/claudia
  - Working directory: /home/VOTRE_USERNAME/claudia
- Dans "WSGI configuration file" :
  - Remplacer le contenu par celui de wsgi_pythonanywhere.py
  - Remplacer VOTRE_USERNAME par votre nom d'utilisateur

## 6. Configurer les fichiers statiques
- Static files section :
  - URL: /static/
  - Directory: /home/VOTRE_USERNAME/claudia/static

## 7. Variables d'environnement (optionnel)
Dans l'onglet "Files", éditez settings.py :
- Remplacez VOTRE_USERNAME par votre nom d'utilisateur dans ALLOWED_HOSTS

## 8. Redémarrer l'application
Cliquez sur "Reload" dans l'onglet Web

Votre blog sera accessible sur : https://VOTRE_USERNAME.pythonanywhere.com