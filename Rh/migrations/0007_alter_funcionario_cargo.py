# Generated by Django 4.0.5 on 2022-07-05 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0006_alter_funcionario_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(choices=[('ES', 'Estagiário'), ('AS', 'Assistente'), ('JR', 'Junior'), ('PL', 'Pleno'), ('SR', 'Sênior'), ('GR', 'Gerente'), ('SP', 'Super'), ('SN', 'Suplente')], max_length=2),
        ),
    ]
