from django.contrib import admin
from .models import Batch, Fermentable, Hop, Salt, Misc, Yeast, Recipe
# Register your models here.

admin.site.register(Batch)
admin.site.register(Fermentable)
admin.site.register(Hop)
admin.site.register(Salt)
admin.site.register(Misc)
admin.site.register(Yeast)
admin.site.register(Recipe)