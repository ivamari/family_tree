from django.contrib import admin

from peoples.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'mother_id', 'father_id')
    list_display_links = ('id', 'first_name', 'last_name')
