from typing import ItemsView, ValuesView
from flask import Flask , request , url_for
import json, os, requests
app = Flask(__name__)
@app.route('/' , methods=['POST', 'GET', 'PUT', 'DELETE'])
def a_operations():
    if(request.method=='GET'):
       a=open("student.json", 'r')
       a= a.read()
       #a.close()
       #return str((type(b)))
       return a 
    if(request.method=='POST'):
        data= request.get_json()
        print(data)
        print(type(data))
        path = os.path.join(os.getcwd(),'student.json')
        a= open(path, 'r+')
        a= a.read()
        a= json.loads(a)
        b= a["students"]
        b[data['id']]={}
        b[data['id']]["name"]= data['name']
        print(a)
        return "update successful"
    if(request.method=='PUT'):
        data= request.get_json()
        print(data)
        print(type(data))
        path = os.path.join(os.getcwd(),'student.json')
        a= open(path, 'r+')
        a= a.read()
        a= json.loads(a)
        for i in a["students"] :
            if (i==data['id']):
                a["students"][i]= data['name']
                a.append(data)
                return "update successful"
            else:
                return "update unsuccessful"
    if(request.method=='DELETE'):
        data= request.get_json()
        print(data)
        print(type(data))
        path = os.path.join(os.getcwd(),'student.json')
        a= open(path, 'r+')
        a= a.read()
        a= json.loads(a)
        for i in a["students"] :
            if (i==data['id']):
                a["students"][i]= data['name']
                a=open("student.json", 'w')
                a.write(None)
                return "delete successful"
            else:
                return "delete unsuccessful"
if __name__ == '__main__' :
  app.run(debug=True, port=5000)



