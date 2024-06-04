from django.contrib import admin
from .models import Clients

class ClientsAdmin(admin.ModelAdmin):
    list_display="nom","prenom","age","sexe"
admin.site.register(Clients,ClientsAdmin)
