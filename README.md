# Pentagon
A Django Powered Form Application. In this repo pentagon is configured to be a school admission form application, It can be customised according to your needs, first clone and try the distributed package in the pentagon_dist and then go the project/app folder, customise models, forms, templates and urls according to you needs !!


## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Demo 
Demo Video - [Demo](https://drive.google.com/file/d/1W8E-kGiWyf6TzFZHq9hPbFgbtHnDoG6p/view)

## Requirements -
- django (Obviously !)
- django-crispy-forms
- django-simple-captcha

use pip to install these packages, needed for both dist package and the app in the folder ...



## Using dist package -

- Install Django by - 
```
pip install Django
```
- Install Crispy forms - 
```
pip install django-crispy-formsInstall Captcha - -pip install  
django-simple-captcha
```
- Start a django project by - 

```
django-admin startproject admission_form
```
- Change the followinf in settings.py -
```
# timezone -
    TIME_ZONE = 'Asia/Kolkata'
# installed_apps -
    INSTALLED_APPS = [
    'pentagon.apps.PentagonConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'captcha',
]

    CRISPY_TEMPLATE_PACK = 'bootstrap4'
    CAPTCHA_FONT_SIZE = 26
```
- Install pentagon package by - 
```
pip install django-pentagon-0.1.tar.gz
```

- Run migrations - 
```
python manage.py migrate
```
- Finally run the test server by - 
```
python manage.py runserver
```

> You can also directly use this repo by cloning it and running python manage.py runserver but don't forget to install the dependencies ...


## UrlConf of project for reference

```
from pentagon import views
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'),
    path('new_admission/', include('pentagon.urls')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
]
```
