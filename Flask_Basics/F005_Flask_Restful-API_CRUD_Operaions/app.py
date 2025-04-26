from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

#Create Flask Instance
app=Flask(__name__)

#Adding database path
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///emp_db.sqlite3"

#Creating Database instance i.e app is connected to db
db=SQLAlchemy(app)

#application access from outside modules
app.app_context().push()

#API instance i.e app is connected to api
api=Api(app)

#Defining Database Model
class Employee(db.Model):
    # __tablename__="employee" #Default is classname in smallcaps
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    salary=db.Column(db.Float, nullable=False)
    

#CRUD using Restful API
class EmployeeApi(Resource):
    #Standard Methods of request
    def get(self): #Read the Data
        emp_data=Employee.query.all()
        #convering in json
        emp_list=[]
        for e in emp_data:
            emp_list.append({"id":e.id,"name":e.name,"salary":e.salary})
        return emp_list

    def post(self): #Create new record
        new_emp=Employee(name=request.json["name"],salary=request.json["salary"])
        db.session.add(new_emp)
        db.session.commit()
        return {"Message":"New Employee is added!"}, 201
            
    def put(self,id): #Update a record
        emp=Employee.query.filter_by(id=id).first()
        if emp:    
            #request body
            new_name=request.json["name"]
            new_salary=request.json["salary"]
            emp.name=new_name
            emp.salary=new_salary
            db.session.commit()
            return {"Success":"Employee Record Updated"},200
        return {"Error":"Employee Not Found"},404

    def delete(self,id): #Delete a record
        emp=Employee.query.filter_by(id=id).first()
        if emp:    
            db.session.delete(emp)
            db.session.commit()
            return {"Success":"Employee Record Deleted"},200
        return {"Error":"Employee Not Found"},404
        
    
class EmployeeSearchAPI(Resource):
    def get(self,id):
        emp_data=Employee.query.filter_by(id=id).first()
        #convering in json
        if emp_data:
            json_emp={"id":emp_data.id,"name":emp_data.name,"salary":emp_data.salary}
            return json_emp
        else:
            return {"Error":"Employee ID Not Found!"},404
        


api.add_resource(EmployeeApi,"/myapi/emp","/myapi/emp/update/<id>","/myapi/emp/delete/<id>") # Based on method, it will hit get()/post()

api.add_resource(EmployeeSearchAPI,"/myapi/emp/search/<id>")



#Run App
app.run(debug=True)