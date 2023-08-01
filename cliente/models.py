from django.db import models

# Create your models here.


class Cliente(models.Model):
    
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    
    def __str__(self):
        return self.nome
    

    
class Agendamento(models.Model):
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    
    def __str__(self):
        return self.cliente.nome 
    
