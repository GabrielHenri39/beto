# Generated by Django 4.2.4 on 2023-08-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicofeito',
            name='valor_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]