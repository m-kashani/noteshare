from flask import Flask,jsonify,request
from flask_cors import CORS
import src.Core.routes as routes
import pymongo
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017")
db=conn['noteshare']
app=Flask(__name__)
CORS(app)
@app.route("/api",methods=["POST"])
def endNode():
    try:

        data=request.get_json()
        
    except:data={}
    try:

        action=request.headers["action"]
    except:
        return {"status":"no action found"}
    #edit this
    # try:
    #     
    #     # token=request.get_header["Utoken"]
        
    # except:
    #     pass
    # if("action" in action):
    """remeber all functions should get data"""
    _ret=routes.dispacther()[action.split('-')[0]](data,db[action.split('-')[1]])
    
    return jsonify(_ret)
app.run(debug=True)

        