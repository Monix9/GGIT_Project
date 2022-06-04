from django.contrib import admin

# Register your models here.
from movies.models import Movie, Director # Author dodany
admin.site.register(Movie)
admin.site.register(Director) # nowe