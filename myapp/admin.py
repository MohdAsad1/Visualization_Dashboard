from django.contrib import admin

# Register your models here.
from myapp.models import UserProfile


@admin.register(UserProfile)
class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'sector', 'region')