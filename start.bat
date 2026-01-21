@echo off
echo.
echo ========================================
echo   COSMOS BLOG - Blog Interactif
echo   Developpe pour Gaetane MVIBUNDULU
echo ========================================
echo.

echo Verification de l'installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou pas dans le PATH
    pause
    exit /b 1
)

echo Installation des dependances...
pip install -r requirements.txt

echo Configuration de la base de donnees...
python manage.py migrate

echo.
echo ========================================
echo   LANCEMENT DU SERVEUR
echo ========================================
echo.
echo Site web: http://127.0.0.1:8000
echo Admin: http://127.0.0.1:8000/admin
echo.
echo Appuyez sur Ctrl+C pour arreter le serveur
echo.

python manage.py runserver