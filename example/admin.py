from django.contrib import admin
from .models import FlashcardsModel, GeeksModel

class FlashCardAdmin(admin.ModelAdmin):
  list_display = ("id", "frontside", "backside", "answer", )

admin.site.register(GeeksModel)
admin.site.register(FlashcardsModel, FlashCardAdmin)
