# Generated by Django 4.0.4 on 2022-05-23 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_projetos_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='nome_do_projeto',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
