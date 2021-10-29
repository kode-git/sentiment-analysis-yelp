# loading models from the dump folder
import os

from keras.models import load_model

print(f"Current directory: {os.path.abspath(__file__)}")

try:
    path = "./dump/model"
    models = os.listdir(path)
except FileNotFoundError:
    print('Dump directory not found...')
    print('Terminate...')
    exit(1)

model_list = {}
for model in models:
    model_list[model] = load_model(model)

while True:
    text = input('Digit a review to classify: ')
    for model in models:
        print(f"Model {model} prediction: {model_list[model].predict(text)}")

    res = input('Do you want to retry? Digit Y for yes, other keys for no')
    if res == 'Y':
        break
