find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
rm -rf db.sqlite3
source ../_env/bin/activate &&
python manage.py makemigrations &&
python manage.py migrate &&
deactivate