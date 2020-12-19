
def index(data,col):
    x=col.insert_one(data)
    return x.inserted_id
def update(data,col):
    for x in col.find():
        col.delete_one({"_id":x["_id"]})
        print(x)
    return {"status":"you are updating"}