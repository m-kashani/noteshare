from flask import Flask,jsonify,request
import src.Core.routes as routes

app=Flask(__name__)
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
    _ret=routes.dispacther()[action](data)
    
    return jsonify(_ret)
app.run(debug=True)

        