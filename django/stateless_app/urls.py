from django.urls import path
from . import views

# kolejność patterns ma znaczenie! Wybiera pierwsze dopasowanie
# pamiętać na końcu ścieżki o '/', inaczej różne błędy mogą się pojawić
urlpatterns = [
    path('', views.index, name='index'),
]