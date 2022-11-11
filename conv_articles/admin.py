from django.contrib import admin
from .models import Article, Vente, Approvisionnement

# Register your models here.
admin.site.register(Article)
admin.site.register(Vente)
admin.site.register(Approvisionnement)