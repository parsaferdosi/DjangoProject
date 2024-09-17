from django.contrib import admin
from .models import suggestion,gamegenre
# Register your models here.
class suggestionAdmin(admin.ModelAdmin):
    list_display=("id","gamename","genre","suggestion")
    list_editable=("genre","suggestion")
    prepopulated_fields={"slug":('gamename',)}
class gamegenreAdmin(admin.ModelAdmin):
    list_display=("id","title")
    prepopulated_fields={"slug":('title',)}
admin.site.register(suggestion,suggestionAdmin)
admin.site.register(gamegenre,gamegenreAdmin)