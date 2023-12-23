from django.db import models
from cliente.models import Cliente

# Create your models here.


class Servico(models.Model):
    servico = models.CharField(max_length=50, verbose_name='Serviço')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    

    def __str__(self):
        return self.servico
    
    class Meta:
        verbose_name_plural = "Serviços"
        verbose_name = "Serviço"
    
class ServicoFeito(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    servico = models.ManyToManyField(Servico)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0) # type: ignore
    data = models.DateField()
    pago = models.BooleanField(default=False)
    
    def __str__(self):
        return self.cliente.nome
    
   

    class Meta:
        
        verbose_name_plural = "Serviços Feitos"
        verbose_name = "Serviço Feito"
