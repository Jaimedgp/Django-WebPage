# Generated by Django 3.0.4 on 2020-03-26 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='gallery/static/images/no-img.jpg', upload_to='gallery')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]