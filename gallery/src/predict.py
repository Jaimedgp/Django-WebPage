from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import sys

classes = {0 : 'Atardecer',
           1 : 'Paisaje'}


def read_model(model):
    return load_model(model)


def predict_image(pht, model):
    if type(model) == str:
        model = read_model(model)

    img = image.load_img(pht, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x.astype('float32') / 255

    pred = model.predict_classes(x)
    return pred[0][0]


if __name__ == '__main__':

    print(sys.argv[1])
    model = read_model(sys.argv[1])
    classification = predict_image(sys.argv[2], model)

    print(classification)
