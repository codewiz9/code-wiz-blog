from django.contrib import admin
from .models import Blog_Post

@admin.register(Blog_Post)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Blog_Post._meta.get_fields() if not field.many_to_many]
