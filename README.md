>Django Alpha Bootstrap is a simple scaffolding for Django projects with Bootstrap 5.

>The main goal is don't repeat all initial steps for every django project.

>It includes:
    * Support for Django 3.2
	* An extended Django User with only username, email and password.
	* Exclusive support for Postgresql
	* The Path includes apps, templates and static directories
	* Minimal templates easy to overwrite
	* Authentication views
	* Internationalization support
	* django-debug-toolbar
	* Separated local setting
	* Integration with Bootstrap 5
	* Django Crispy Forms and Crispy Bootstrap 5
	* Templates for 403, 404 and 500 HTTP errors.

>How to use it:
>Django Alpha Bootstrap is not a reusable Django App, is a scaffolding, so the best way to use it is:
	* Fork the repository
	* Delete .git directory
	* Don't migrate, first review the User model in users.models and customize it as needed.
	* After you are done with the User model, migrate it.
	* Now you can overwrite templates and start new apps.

>In production:
	* run: python manage.py runserver --setting=config.setting.production

>I am a Django developer but I don't consider my self nearly an expert,
however you can use this project under your on risk using the [BSD License](https://opensource.org/licenses/BSD-3-Clause)
