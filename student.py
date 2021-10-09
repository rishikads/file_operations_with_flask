from flask import Flask , request , url_for, status
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
        a= open(path, 'r')
        a= a.read()
        a= json.loads(a)
        b= a["students"]
        a_list = list(a)
        overlap = data['id']
        if(overlap in a_list):
            def index():
                return "same id exists", status.HTTP_400_BAD_REQUEST
        else:
            b[data['id']]["name"] = data['name']
            new_path = os.path.join(path)
            with open(new_path, 'w') as file:  
                document = json.dump(a, file)
            return "Updated Successfully"
    if(request.method=='PUT'):
        data= request.get_json()
        print(data)
        print(type(data))
        path = os.path.join(os.getcwd(),'student.json')
        a= open(path, 'r+')
        a= a.read()
        a= json.loads(a)
        b= a["students"]
        a_list = list(a)
        overlap = data['id']
        if(overlap not in a_list):
            def index():
                return "Record not found", status.HTTP_400_BAD_REQUEST
        else:
            b[data['id']]["name"] = data['name']
            new_path = os.path.join(path)
            with open(new_path, 'w') as file:  
                document = json.dump(a, file)
            return "Updated Successfully"
    if(request.method=='DELETE'):
        data= request.get_json()
        print(data)
        print(type(data))
        path = os.path.join(os.getcwd(),'student.json')
        a= open(path, 'r+')
        a= a.read()
        a= json.loads(a)
        i=0
        for a["students"][i] in a["students"]:
            if (a["students"][i]==data['id']):
                a["students"][i]["name"]= data['name']
                del a["students"][i]
                new_path = os.path.join(path)
                with open(new_path, 'w') as file:  
                    document = json.dump(a, file)
            else:
                i=i+1
        return a
            
if __name__ == '__main__' :
  app.run(debug=True, port=5000)



