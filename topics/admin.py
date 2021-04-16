from django.contrib import admin
from topics.models import Topics

# Register your models here.
@admin.register(Topics)
class AdminTopics(admin.ModelAdmin):
    pass
