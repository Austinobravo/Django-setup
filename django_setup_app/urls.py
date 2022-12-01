from django.urls import path

urlspatterns=[
    path('', myview, name="myview"),
]
#Change the myview to your view function in your views.py file