from django.contrib import admin

from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
  list_display = ("id","name","genus","user","is_domesticated")
  list_editable = ("name","genus","user","is_domesticated")
  
