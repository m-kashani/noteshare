
def index(data,col):
    x=col.insert_one(data)
    return x.inserted_id
def update(data,col):
    myquery = {"_id":data['_id']}
    newvalues = { "$set": data }
    col.update_one(myquery,newvalues)
    _ret=[]
    for x in col.find():
        _ret.append(x)
    return _ret
def find(data,col):
    myquery=data
    limit=data.pop('limit')
    _ret=[]
    for x in col.find(data).limit(limit):
        _ret.append(x)
    return _ret
def clear(data,col):
    for x in col.find():
        col.delete_one({"_id":x["_id"]})
        print(x)
    return {"status":"you are updating"}