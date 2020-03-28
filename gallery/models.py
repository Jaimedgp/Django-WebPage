from django.db import models

# Create your models here.
class Image(models.Model):
    
    Tipos_FotoGrafia = [
            ('PA', 'Paisajes'),
            ('VA', 'Variado'),
            ('AT', 'Atardecer'),
            ]

    types = models.CharField(max_length=2, 
            choices=Tipos_FotoGrafia, 
            default='VA',)

    image = models.ImageField(upload_to = 'gallery',
            default='gallery/static/images/no-img.jpg')
    name = models.CharField(max_length=200)
