from keras.preprocessing import image
from keras.models import load_model
from django.db import models
import numpy as np
import sys
import os

sys.path.insert(1, 'gallery/src')
from predict import predict_image

# Create your models here.
class Image(models.Model):

    Tipos_FotoGrafia = [
            ('AT', 'Atardecer'),
            ('PA', 'Paisajes'),
            ('VA', 'Variado'),
            ]

    #types = models.CharField(max_length=2, 
            #choices=Tipos_FotoGrafia, 
            #default='VA',)

    image = models.ImageField(upload_to = 'gallery',
            default='gallery/static/images/no-img.jpg')
    name = models.CharField(max_length=200)


    def open_img(pht):
        img = image.load_img(pht, target_size=(150, 150))
        x = np.expand_dims(image.img_to_array(img), axis=0)

        return x.astype('float32') / 255


    def save(self, **kwargs):
        model = load_model("gallery/src/model.h5")
        img = open_img(self.image.url)

        ind_types = model.predict_classes()[0][0]
        self.types = Tipos_FotoGrafia[ind_types]

        super(NameReplacements, self).save(**kwargs)
