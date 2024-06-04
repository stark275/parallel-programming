from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('ajout/',views.ajout,name="ajout"),
    path("ajoutvalider/",views.ajoutvalider,name="ajoutvalider"),
    path("supprimer/<int:id>/",views.supprimer,name="supprimer"),
    path("modifier/<int:id>/",views.modifier,name="modifier"),
    path("modifier/modifiervalider/<int:id>/",views.modifiervalider,name="modifiervalider")
]
