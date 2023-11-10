from django.contrib import admin
from .models import News,Category

# @admin.register(news)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('__all__')

admin.site.register(News)
admin.site.register(Category)


