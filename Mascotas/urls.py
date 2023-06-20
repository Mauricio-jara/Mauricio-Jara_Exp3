from django.urls import path
from .views import index,vision,tienda,adopcion,registrar,crear,modificar,eliminar

urlpatterns = [
    path('', index, name="index"),
    path('vision/', vision, name="vision"),
    path('tienda/', tienda, name="tienda"),
    path('adopcion/', adopcion, name="adopcion"),
    path('registrar/', registrar, name="registrar"),
    path('crear/', crear, name="crear"),
    path('modificar/<id>', modificar, name="modificar"),
    path('eliminar/<id>', eliminar, name="eliminar")
]
