import random
import requests
from food_sorter import *

def gen_pass(pass_length):
    elements = "é!'^+%&/()=?_1234567890*-qwertyuıopğüQWERTYUIOPĞÜ@€¨~|asdfghjklşi,;´`>:<zxcvbnmöç.ZXCVBNMÖÇ|"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def emoji_olusturucu():
    emoji = [":grinning:", ":smiley:", ":smile:", ":grin:", ":laughing:", ":face_holding_back_tears:", ":sweat_smile:", ":joy:", ":rofl:", ":smiling_face_with_tear: ", ":relaxed:", ":blush:", ":innocent:", ":slight_smile:", ":upside_down:", ":wink:", ":relieved:", ":heart_eyes:", ":smiling_face_with_3_hearts:", ":kissing_heart:", ":kissing:", ":kissing_smiling_eyes:", ":kissing_closed_eyes:", ":yum:", ":stuck_out_tongue:", ":stuck_out_tongue_closed_eyes: ", ":stuck_out_tongue_winking_eye:", ":zany_face:", ":face_with_raised_eyebrow:"]
    return random.choice(emoji)

def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"

def get_duck_image_url():    
    url1 = 'https://random-d.uk/api/random'
    res1 = requests.get(url1)
    data1 = res1.json()
    return data1['url']

def get_dog_image_url():    
    url2 = 'https://random.dog/woof.json'
    res2 = requests.get(url2)
    data2 = res2.json()
    return data2['url']

def get_fox_image_url():    
    url3 = 'https://randomfox.ca/floof/'
    res3 = requests.get(url3)
    data3 = res3.json()
    return data3['image']

