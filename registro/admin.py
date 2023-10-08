from django.contrib import admin
from .models import *

admin.site.register(Batalhao)
admin.site.register(TipoVtCarros)
admin.site.register(TipoVtMotos)
admin.site.register(PneusCarros)
admin.site.register(PneusMotoDianteiro)
admin.site.register(PneusMotoTraseiro)


class PedidoCarrosInline(admin.TabularInline):
    readonly_fields = ('pim', 'data','viatura', 'quantidade')
    list_display = ('pim', 'data', 'quantidade')
    model = PedidosCarros
    extra = 0

class PedidoMotosInline(admin.TabularInline):
    readonly_fields = ('pim', 'data','viatura', 'quantidade')
    list_display = ('pim', 'data', 'quantidade')
    extra = 0
    model = PedidosMotos

@admin.register(ViaturasCarros)
class ViaturaCarrosAdmin(admin.ModelAdmin):
    inlines = [PedidoCarrosInline]

@admin.register(ViaturasMotos)
class ViaturaMotosAdmin(admin.ModelAdmin):
    inlines = [PedidoMotosInline]

@admin.register(PedidosCarros)
class PedidoCarrosAdmin(admin.ModelAdmin):
    readonly_fields = ('pim', 'data','viatura', 'quantidade')

@admin.register(PedidosMotos)
class PedidoMotosAdmin(admin.ModelAdmin):
    readonly_fields = ('pim', 'data','viatura', 'quantidade')







