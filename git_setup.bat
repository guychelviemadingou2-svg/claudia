@echo off
echo 🌌 Configuration Git pour Cosmos Blog
echo.

REM Initialiser le repository Git
git init

REM Ajouter tous les fichiers
git add .

REM Premier commit
git commit -m "🚀 Initial commit - Cosmos Blog avec design violet cosmique"

echo.
echo ✅ Repository Git initialisé avec succès !
echo.
echo 📋 Prochaines étapes :
echo 1. Créez un nouveau repository sur GitHub
echo 2. Copiez l'URL de votre repository
echo 3. Exécutez ces commandes :
echo.
echo    git remote add origin https://github.com/VOTRE-USERNAME/cosmos-blog.git
echo    git branch -M main
echo    git push -u origin main
echo.
pause