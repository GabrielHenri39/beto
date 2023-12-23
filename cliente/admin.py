from django.contrib import admin
from .models import Cliente,Agendamento
from django.utils.formats import get_format
# Register your models here.

admin.site.register(Cliente)


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):


    list_display = ['cliente', 'data', 'horario', 'status']
    list_filter = ['cliente','data','horario','status']
    list_editable = ['status']  
    search_fields = ['cliente__nome']


    def data_display(self, agendamento):
        return agendamento.data.strftime(get_format('%d/%m/%Y'))
    

    def cliente_display(self, agendamento):
        return agendamento.cliente.nome


    def horario_display(self, agendamento):
        return agendamento.horario.strftime('%H:%M')


    def status_display(self, agendamento):
        return agendamento.status.nome
    
    class Meta:
        model = Agendamento
        fields = ['cliente', 'data', 'horario', 'status']
        list_display = ['cliente_display', 'data_display', 'horario_display', 'status_display']
        list_filter = ['cliente','data','horario','status']
        list_editable = ['status']  
        search_fields = ['cliente__nome']
