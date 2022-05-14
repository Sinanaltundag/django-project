
from django.urls import path
from .views import home, sinan

urlpatterns = [
    path('', home, name='home'),
    path('sinan/', sinan, name='sinan'),
]
