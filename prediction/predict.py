import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model
import os
import json

class DogBreed:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogbreed(self):
        model = load_model(os.path.join("model", "inception_model.h5"))
        # Load the class names from the file
        with open('breed_names.json', 'r') as f:
            breed_names = json.load(f)
         

        imagename = self.filename
        
        test_image = load_img(imagename, target_size = (299,299))
        test_image = img_to_array(test_image)
        test_image /= 255.0  # Scale pixel values to between 0 and 1
        test_image = np.expand_dims(test_image, axis = 0)
        prediction = model.predict(test_image)
        index = np.argmax(prediction)
        breed = breed_names[index]
        conf = round(np.max(prediction)*100, 2)
        print(index, breed, conf)

        return [{
            "breed name": breed,
            "confidence score": conf
        }]
