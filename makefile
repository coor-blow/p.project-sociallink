dev-start:
	python manage.py runserver --settings=config.settings.dev
dev-install:
	pip install -r requirements/dev.txt

dev-makemigrations:
	python manage.py makemigrations --settings=config.settings.dev

dev-migrate:
	python manage.py migrate --settings=config.settings.dev

dev-showmigrations:
	python manage.py showmigrations --settings=config.settings.dev
