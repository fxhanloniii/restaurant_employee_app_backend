# Generated by Django 4.2.3 on 2023-07-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_menuitem_allergies_menuitem_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image_url', models.URLField(blank=True)),
            ],
        ),
    ]
