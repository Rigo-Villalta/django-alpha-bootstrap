Django Alpha Bootstrap is a simple scaffolding for Django projects with Bootstrap 4.

The main goal is don't repeat all initial steps for every django project.

It includes:

	- An extended Django User with only username, email and password fields
	- The Path includes apps, templates and static directories
	- Minimal templates easy to overwrite
	- Authentication views
	- Internationalization support
	- django-debug-toolbar
	- Separated local setting
	- Integration with Bootstrap 4
	- Django Crispy Forms

How to use it:
Django Alpha Bootstrap is not a reusable Django App, is a scaffolding, so the best way to use it is:
	- Clone the repository
	- Don't migrate, firts review User model in users.models
	- After you are done with the User model migrate
	- Now you can overwrite templates

In production:
	- run: python manage.py runserver --setting=config.setting.production
