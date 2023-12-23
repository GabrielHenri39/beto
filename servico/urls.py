from django.urls import path
from . import views

urlpatterns = [
    path('testform/', views.test, name='testform'),
    path('test2/', views.test2, name='test2'), # type: ignore

]