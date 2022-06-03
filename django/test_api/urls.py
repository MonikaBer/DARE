from django.urls import path
from . import views

# kolejność patterns ma znaczenie! Wybiera pierwsze dopasowanie
# pamiętać na końcu ścieżki o '/', inaczej różne błędy mogą się pojawić
urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/create/', views.createNote),
    path('notes/<str:pk>/update/', views.updateNote),
    path('notes/<str:pk>/delete/', views.deleteNote),
    path('notes/<str:pk>/', views.getNotes),
]