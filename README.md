<p align="center">
    An Already Django setup project.
  </p>

This is a fully setup project with app for django.
### *** Pre-requisties ***

You must have python running in your os.

# Procedures
Run pip install -r requirements.txt in your terminal to download the dependencies needed for your project.
Create a virtual environment using virtualenv venv
Activate your virtualenv for windows: venv\scripts\activate, for mac/linux: source venv/bin/activate.
Then you need to change the django_setup to your project name and the django_setup_app to your app name.
Go to your asgi.py file in your project, change the 'django_setup.settings' to 'your_project_name.settings'.
Go to your settings.py file in  your project, change the INSTALLED_APPS,ROOT_URLCONF,WSGI_APPLICATION appropriately.
Go to the urls.py file in your project, change the 'django_setup_app.urls' to 'your_app_name.urls'.
Go to your wsgi.py file in your project, change the 'django_setup.settings' to 'your_project_name.settings'.
Go to your apps.py file in your project, change the 'django_setup_app' to 'your_app_name'.
Go to your manage.py file in your project, change the 'django_setup.settings' to 'your_project_name.settings'.
An admin with the information:Username:admin, email:admin@gmail.com,password:admin have already been setup, just run python manage.py runserver and go to http://127.0.0.1:8000/admin and login to the admin dashboard.
Add your html files to the template folder and render them properly through yor views.py and urls.py file.
Add your css, js, image files in their different folders in the static folder.
For more information contact me : github.com/austinobravo and i'll help you.