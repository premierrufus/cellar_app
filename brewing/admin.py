from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe 
from django.utils.translation import ugettext as _

from .models import Batch, Barrel, Container, Fermentable, Hop, Salt, Misc, Yeast, Recipe

from brewing.forms import TransferForm

# Register your models here.


admin.site.register(Barrel)
admin.site.register(Fermentable)
admin.site.register(Salt)
admin.site.register(Misc)
admin.site.register(Yeast)
#admin.site.register(Recipe)

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('gyle', 'recipe', 'brew_date', 'brewer', 'ferm_tank', 'transfer_tank')
    fieldsets = (
        ('Batch Data', {
            'classes': ('wide',),
            'fields': (
                'double_batch',
                'brew_date',
                'gyle',
                'recipe', 
                'ferm_tank', 
                'brewer',
                'asst_brewer',
                'mash_temperature',
                'mash_ph',
                'pre_boil_ph',
                'post_boil_ph',
                'preboil_gravity',
                'preboil_volume',
                'postboil_gravity',
                'postboil_volume',
                'final_gravity', 
                'attenuation', 
                'final_abv', 
                'first_dry_hop',
                'second_dry_hop',
                'd_rest'
            )
        }),

        ('Oxygen Data', {
            'classes': ('collapse',),
            'fields': ('post_dry_hop_oxygen_ppb', 'pre_transfer_oxygen_ppb', 'post_transfer_oxygen_ppb')
        }),

        ('Gravity Log', {
            'classes': ('collapse',),
            'fields': (('gravity_1', 'gravity_1_date'), ('gravity_2', 'gravity_2_date'), ('gravity_3', 'gravity_3_date'))
        }),
        ('Transfer Data', {
            'classes': ('collapse',),
            'fields': ('post_transfer_vol', 'transfer_cip', 'transfer_date', 'transfer_tank', 'transfer_log')
        }),
        ('Logs', {
            'classes': ('collapse',),
            'fields': ('cellaring_log', 'notes')
        })
    )
    actions = ['set_transfer_tank']


    def set_transfer_tank(modeladmin, request, queryset):
        if 'do_action' in request.POST:
            form = TransferForm(request.POST)
            if form.is_valid():
                transfer_tank = form.cleaned_data['transfer_tank']
                updated = queryset.update(transfer_tank=transfer_tank)
                messages.success(request, '{0} batches were updated'.format(updated))
                return
        else:
            form = TransferForm()

        return render(request, 'admin/brewing/action_transfer.html',
            {'title': u'Choose tank',
            'objects': queryset,
            'form': form})
    set_transfer_tank.short_description = u'Transfer selected batches'


@admin.register(Hop)
class HopAdmin(admin.ModelAdmin):
    pass


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'container_type', 'capacity', 'get_contents')



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'view_link')
    filter_horizontal = ('hops', 'fermentables')

    def view_link(self, obj):
        return mark_safe(
            '<a href="{0}">{1}</a>'.format(
                obj.get_absolute_url(),
                _("View")
            )
        )
    view_link.allow_tags = True
    view_link.short_description = _("Recipe Details")
