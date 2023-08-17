from django.urls import path

from . import views

urlpatterns = [
    path('testform/',views.test, name='testform') # type: ignore
]
