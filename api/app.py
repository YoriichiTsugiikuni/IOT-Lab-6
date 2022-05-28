from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from marshmallow import Schema, ValidationError
from bson.json_util import dumps
from json import loads
import os
from dotenv import load_dotenv
from datetime import datetime



if __name__ == '__main__':
  app.run(debug=True, port=3000, host="0.0.0.0")
  
load_dotenv()

info = {}

app = Flask(__name__)
CORS(app)
#setup location of database
app.config["MONGO_URI"] = os.getenv("MONGO_CONNECTION_STRING") 
mongo = PyMongo(app)


#Rules database information has to conform to
class TankSchema(Schema):
    tank_id = fields.String(required=True)
    percentage_full = fields.Integer(required=True)


@app.route("192.168.216.5:3000/tank", methods = ["POST"])
def add_new_tank():
    request_dict = request.json()
    try: 
        new_tank = TankSchema().load(request_dict)
    except ValidationError as err:
        return(err.messages, 400)
    
    tank_document = mongo.db.tanks.insert_one(new_tank)
    tank_id = tank_document.inserted_id

    tank = mongo.db.tanks.find_one({"_id": tank_id})

    tank_json = loads(dumps(tank))

    status = False
    if TankSchema.percentage_full >=80 :
        if TankSchema.percentage_full<=100 :
        {
            status = True
        }

        else:
        {
            status = False
        }
    }

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
return {"led": status, "msg": "Data was saved in database successfully", "date": "current_time"} 


