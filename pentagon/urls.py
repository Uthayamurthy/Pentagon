from django.urls import path

from . import views

app_name = 'pentagon'
urlpatterns = [
    path('', views.guidelines, name='guidelines'),
    path('guidelines_verify/', views.guidelines_verify, name='guidelines_verify'),
    path('admission_form/', views.admission_form, name='admission_form'),
    path('acknowledgement/', views.acknowledgement, name='acknowledgement'),
    path('already_exists/', views.already_exists, name='already_exists'),
]