import gradio as gr

import numpy as np
import tensorflow as ts
import pandas as pd
import pysentimiento
import csv
from pysentimiento import create_analyzer
import matplotlib.pyplot as plt



def evaluate(text):
	output = analyzer.predict(text).__dict__['probas']
	NEG = output['NEG']
	NEU = output['NEU']
	POS = output['POS']
	return f"Negative:{NEG * 100:.2f}%\n Neutral:{NEU * 100:.2f}%\n Positive:{POS * 100:.2f}%\n"

analyzer = create_analyzer(task="sentiment", lang="en")
iface = gr.Interface(fn=evaluate, inputs="text", outputs="text")
iface.launch()