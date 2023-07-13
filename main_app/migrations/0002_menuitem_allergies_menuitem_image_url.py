# Generated by Django 4.2.3 on 2023-07-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='allergies',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]