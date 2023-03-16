import gradio as gr
from tensorflow import keras
from PIL import Image
import numpy as np

def greet(image):
	img = Image.fromarray(np.uint8(image)).convert('RGB')
	img = img.resize((224, 224))
	img_arr = keras.preprocessing.image.img_to_array(img)
	img_arr = np.expand_dims(img_arr, axis=0)
	img_arr = keras.applications.resnet50.preprocess_input(img_arr)
	prediction = model.predict(img_arr)
	decoded_predictions = keras.applications.resnet50.decode_predictions(prediction, top=3)[0]
	rtn = {t[1]:t[2] for t in decoded_predictions}
	final = []
	for key, value in rtn.items():
		final.append(str(f"{key}".title() + f" ({value:.2%})"))
	return("Image Prediction:\n".join(['\n'.join(str(e) for e in final)]))

model = keras.applications.resnet50.ResNet50(weights="imagenet")
iface = gr.Interface(fn=greet, inputs="image", outputs="text", title="BorzoiRecognitionMachine")
iface.launch()