from io import BytesIO
import PySimpleGUI as sg
from PIL import Image
import requests, json

def image_to_data(im):
    with BytesIO() as output:
        
        im = im.resize((400, 720), Image.ANTIALIAS)
        im.save(output, format="PNG",optimize=True)
        data = output.getvalue()
    return data

def get_data():
    cutURL = 'https://meme-api.com/gimme/wholesomememes'
    
    imageURL = json.loads(requests.get(cutURL).content)["url"]
    data = requests.get(imageURL).content
    stream = BytesIO(data)
    img = Image.open(stream)
    giy = image_to_data(img)
    return giy

control_col = sg.Column([[sg.Button('next meme', key = '_3_')],])
image_col = sg.Column([[sg.Image(get_data(), key = '-IMAGE-')]])
layout = [[control_col,image_col]]
window = sg.Window('meme gen', layout,finalize=True)
w1, h1 = window.size
w2, h2 = sg.Window.get_screen_size()
if w1>w2 or h1>h2:
    window.move(0, 0)
while True:
    event, values = window.read()

    if event is None:
        break
    if event == '_3_':
        window['-IMAGE-'].update(get_data())

window.close()

