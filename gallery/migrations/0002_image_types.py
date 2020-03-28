# Generated by Django 3.0.3 on 2020-03-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='types',
            field=models.CharField(choices=[('PA', 'Paisajes'), ('VA', 'Variado'), ('AT', 'Atardecer')], default='VA', max_length=2),
        ),
    ]