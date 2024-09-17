from django.contrib import admin
from .models import suggestion,gamegenre
# Register your models here.
class suggestionAdmin(admin.ModelAdmin):
    list_display=("id","gamename")
admin.site.register(suggestion)
admin.site.register(gamegenre)