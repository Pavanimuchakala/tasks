import pymongo
from flask import Flask, request,jsonify

client = pymongo.MongoClient("mongodb+srv://pavani:MONGOPav123@clusterp.tlvbf.mongodb.net/?retryWrites=true&w=majority")


app=Flask(__name__)
@app.route('/dbops/mongo/insert', methods=['GET','POST'])
def insert_dat():
    if (request.method=='POST'):
        a=request.json['database']
        b = request.json['collection']
        c=request.json['data']
        database=client[a]
        collection = database[b]
        collection.insert_one(c)


@app.route('/dbops/mongo/fetch', methods=['GET', 'POST'])
def fetch_dat():
    if (request.method == 'POST'):
        a = request.json['database']
        b = request.json['collection']
        l=[]
        database = client[a]
        collection = database[b]
        result=list(collection.find({},{'_id':0}))
        for i in result:
            l.append(i)
        return l

@app.route('/dbops/mongo/update', methods=['GET', 'POST'])
def update_dat():
    if (request.method == 'POST'):
        a = request.json['database']
        b = request.json['collection']
        l=[]
        database = client[a]
        collection = database[b]
        database.students.update_one({'name':"pavani"},{'$set':{'phone':"000"}})
        result=list(collection.find({},{'_id':0}))
        for i in result:
            l.append(i)
        return l


if __name__=='__main__' :
    app.run()

