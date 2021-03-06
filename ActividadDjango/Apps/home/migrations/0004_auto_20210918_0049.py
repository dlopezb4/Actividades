# Generated by Django 3.2.6 on 2021-09-18 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_cliente_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.tipocliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='documento',
            field=models.CharField(choices=[('D', 'DPI'), ('C', 'CEDULA')], default='C', max_length=20),
        ),
    ]
