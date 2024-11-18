from flask import Flask,jsonify,request

app=Flask(__name__)

data=[
    {"id":1,"name":"Admin","salary":10000},
    {"id":2,"name":"ram","salary":80010},
    {"id":3,"name":"shyam","salary":5000}
    ]

@app.route("/employees")
def get_employees():
    return jsonify(data)

@app.route("/emp_id/<int:id>")
def search_emp(id):
    for e in data:
        if e["id"]==id:
            return jsonify(e)
    return jsonify({"Error":"Employee ID %s Not Found"%(id)}),404

@app.route("/add_emp",methods=["POST"])
def add_employee():
    id=request.json["id"]
    name=request.json["name"]
    salary=request.json["salary"]

    data.append({"id":id,"name":name,"salary":salary})
    return jsonify({"Message":"New Record Added"}),201


app.run(debug=True)