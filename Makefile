serve:
	python manage.py runserver
migrations:
	python manage.py makemigrations 
migrate:
	python manage.py migrate
user:
	python manage.py createsuperuser
test:
	python manage.py test awwards