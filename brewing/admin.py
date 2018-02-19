from django.contrib import admin
from .models import Batch, Brix, Container, Fermentable, Hop, Salt, Misc, Yeast, Recipe
# Register your models here.

admin.site.register(Brix)
admin.site.register(Container)
admin.site.register(Fermentable)
admin.site.register(Hop)
admin.site.register(Salt)
admin.site.register(Misc)
admin.site.register(Yeast)
admin.site.register(Recipe)

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
	list_display = ('gyle', 'recipe', 'brew_date', 'brewer', 'current_tank' )


