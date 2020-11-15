from django.urls import path
from . import views

urlpatterns = [
    # Designate a view to render from views.py file
    path('', views.home, name='home'),
]