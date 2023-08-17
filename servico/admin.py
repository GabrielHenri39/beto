import locale
from django.contrib import admin
from django.db.models import Sum
from .models import Servico, ServicoFeito


# Register your models here.

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco']
    search_fields = ['nome']
    list_filter = ['nome', 'preco']
    list_editable = ['preco']

@admin.register(ServicoFeito)
class ServicoFeitoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'valor_total', 'data', 'pago']
    search_fields = ['servico__nome', 'cliente__nome']
    list_filter = ['servico__nome', 'cliente__nome', 'data', 'pago']
    list_editable = ['pago']

    def valor_total_display(self, obj):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Configura a localização para o Brasil
        return locale.currency(self.calculate_valor_total(obj), grouping=True, symbol='R$ ') # type: ignore

    
    def calculate_valor_total(self, obj):
        return obj.servico.aggregate(total=Sum('preco'))['total'] or 0

    def save_model(self, request, obj, form, change):
        obj.valor_total = self.calculate_valor_total(obj)
        super().save_model(request, obj, form, change)
