import sys,os
from src.yoloproject.utils.common import decodeImage, encodeImageIntoBase64, decodeBase64Image
from ultralytics import YOLO

class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("models", "trained_model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)/255
        test_image = np.expand_dims(test_image, axis = 0)

        result = model.predict(test_image)
        print(result)
        result1 = np.argmax(result, axis = 1)
        print(result1)

        if result1 == [0]:
            prediction = 'Normal'
            return [{ "image" : prediction}]
        else:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
