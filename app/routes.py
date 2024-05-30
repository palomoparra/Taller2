from flask import jsonify
import random
import socket
from app import objects 
from app import app


IdContainer= socket.gethostname()


@app.route('/json')
def get_json():
    num_ale1 = random.randint(0,10)
    res_json = {
        objects[num_ale1][0],
        objects[num_ale1][1],
        objects[num_ale1][2],
        objects[num_ale1][3],
        IdContainer
    }
    return jsonify(res_json)

@app.route('/image')
def get_image():
    num_ale2 = random.randint(0,10)
    res_imag={
        objects[num_ale2][4],
        objects[num_ale2][5],
        IdContainer
    }
    return jsonify(res_imag)



