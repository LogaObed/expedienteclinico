# Generated by Django 4.1.7 on 2023-03-20 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0010_remove_antecedentealimenticio_comidas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='tipo_sexo',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.DeleteModel(
            name='TipoSexo',
        ),
    ]