# Generated by Django 3.2 on 2021-04-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, help_text='simple description text.', max_length=100, verbose_name='DESCRIPTION'),
        ),
    ]
