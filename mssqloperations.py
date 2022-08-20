from flask import Flask, request, jsonify
import mysql.connector as connection
mydb=connection.connect (host='localhost',user='root',password='mysqlpavani',use_pure=True)
curs=mydb.cursor()


app=Flask(__name__)

@app.route('/dbops/sql/fetch', methods=['GET','POST'])
def fetch_dat():
    if (request.method=='POST'):
        a=request.json['table']
        b=request.json['db']
        c=request.json['condition']
        if c == '':
            curs.execute('select * from ' + str(b) + '.' + str(a))
        else:
            curs.execute('select * from ' + str(b) + '.' + str(a) + ' where ' + str(c))
        return jsonify((str(curs.fetchall())))

@app.route('/dbops/sql/insert', methods=['GET','POST'])
def insert_data():
    if (request.method=='POST'):
        a=request.json['table']
        b=request.json['db']
        c=request.json['data']
        l=str(tuple((c.values())))
        cmd="insert into "+b+"."+a+" values"+l
        print(cmd)
        curs.execute(cmd)
        mydb.commit()
        curs.execute('select * from ' + str(b) + '.' + str(a))
        return jsonify((str(curs.fetchall())))
        #return jsonify(l)


@app.route('/dbops/sql/update', methods=['GET','POST'])
def update_data():
    if (request.method=='POST'):
        a=request.json['table']
        b=request.json['db']
        c=request.json['data']
        d=request.json['condition']
        cond = " where "
        upd=''
        for i in range(len(d)):
            cond=cond + str(tuple(d.keys())[i])+ " ='"+str(tuple(d.values())[i]) +"' and "
        for i in range(len(c)):
            upd=upd + str(tuple(c.keys())[i])+" = '"+str(tuple(c.values())[i]) +"', "
        cmd = "update " + b + "." + a + " set " + upd[:-2:] + cond[:-5:]
        print(cmd)
        curs.execute(cmd)
        curs.execute('select * from ' + str(b) + '.' + str(a))
        return jsonify((str(curs.fetchall())))

@app.route('/dbops/sql/delete', methods=['GET','POST'])
def delete_data():
    if (request.method=='POST'):
        a=request.json['table']
        b=request.json['db']

        d=request.json['condition']
        cond = " where "

        for i in range(len(d)):
            cond=cond + str(tuple(d.keys())[i])+ " ='"+str(tuple(d.values())[i]) +"' and "
        cmd = "delete from " + b + "." + a + cond[:-5:]
        print(cmd)
        curs.execute(cmd)
        curs.execute('select * from ' + str(b) + '.' + str(a))
        return jsonify((str(curs.fetchall())))

if __name__=='__main__' :
    app.run()

