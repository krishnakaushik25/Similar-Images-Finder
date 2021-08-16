from keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.models import Model
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
import tensorflow.keras.layers as layers
import numpy as np


class FeatureExtraction:
    """
    Class to extract features from pretrained model
    Model used : MobileNetV2
    feature_size : After flattening size will be (1280,1)
    """

    def __init__(self):
        """ Models MobileNetV2 for the weights for imagenet and remove top layer"""
        base = MobileNetV2(weights='imagenet', include_top=False)
        base.trainable = False
        self.model = Model(inputs=base.input, outputs=layers.GlobalAveragePooling2D()(base.output))

    def extract(self, filename):
        """Extracts features ,by first resizing image  by (224,224),expand dims,and flatten it
           If file is corrupt or something ,send None
        """
        try:
            img = image.load_img(filename, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array_expanded = np.expand_dims(img_array, axis=0)
            image_preprocessed = preprocess_input(img_array_expanded)
            features = self.model.predict(image_preprocessed)
            features_reduce = features.squeeze()
            features_reduce = features_reduce.tolist()
        except Exception as err:
            print(str(err))
            features_reduce = None

        return features_reduce
