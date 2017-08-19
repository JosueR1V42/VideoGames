from django.contrib import admin
from .models import creator, games, review, score
# Register your models here.

admin.site.register(creator)
admin.site.register(games)
admin.site.register(review)
admin.site.register(score)
