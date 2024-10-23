from flask import Flask, request, render_template
import jinja2
import matplotlib.pyplot as plt

# Function to get whole data from file
def get_whole_data(file):
    #Get Whole Data from file
    f=open(file,'r')
    f.readline() #header
    Fulldata=[]
    for line in f.readlines():
        line=line.strip().split(',')
        Fulldata.append({"student_id":line[0].strip(),"course_id":line[1].strip(),"marks":line[2].strip()})
    f.close()
    return Fulldata
#Function to get required data from WholeData
def get_required_data(file,idType,idValue):
    FullData=get_whole_data(file)
    #Get Required Data
    data=[]
    for line in FullData:
        if line[idType]==idValue:
            data.append(line)
   
    return data

#Function to get HTML Content if ID is Student ID
def get_HTML_byStudentID(data):
    #Calculate Total Marks
    total=0
    for line in data:
        line['marks']=int(line['marks'])
        total+=line['marks']
    
    #Using Jinja2 Template
    HTML_Template="""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Data</title>
    </head>

    <body>
        <h1>Student Details</h1>
        <table border="2" id="student-details-table">
            <thead>
                <tr>
                    <th>Student ID</th>
                    <th>Course ID</th>
                    <th>Marks</th>
                </tr>
            </thead>
            <tbody>
                {% for line in data %}
                <tr>
                    <td>{{ line.student_id }}</td>
                    <td>{{ line.course_id }}</td>
                    <td>{{ line.marks }}</td>
                </tr>
                {% endfor %}
                <tr>
                    <td colspan="2" style="text-align:center">Total Marks</td>
                    <td>{{ total }}</td>
                </tr>
            </tbody>
        </table>
        <br>
        <a href="/">Go Back</a>

    </body>
    </html>
    """
    html_content = jinja2.Template(HTML_Template).render(data=data,total=total)
    return html_content
#Function to get HTML Content if ID is Course ID
def get_HTML_byCourseID(data):
    
    #Calculate Average and Maximum
    totalMarks=0
    maxMarks=0
    count=0
    for line in data:
        count+=1
        totalMarks+=int(line["marks"])
        if int(line["marks"])>maxMarks:
            maxMarks=int(line["marks"])
    avgMarks=totalMarks/count

    # Create a bar chart for marks frequency
    marks = [int(line["marks"]) for line in data]
    marks_frequency = {mark: marks.count(mark) for mark in set(marks)}
    
    # Use Agg backend for matplotlib
    plt.switch_backend('Agg')

    img="static/plot.png"
    plt.bar(marks_frequency.keys(), marks_frequency.values(), color='blue')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig(img)
    plt.close()

    #Using Jinja2 Template
    HTML_Template="""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Course Data</title>
    </head>
    <body>
        <h1>Course Details</h1>
        <table border="1">
            <thead>
                <tr>
                    <th>Average Marks</th>
                    <th>Maximum Marks</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{{ avgMarks }}</td>
                    <td>{{ maxMarks}}</td>
                </tr>
            </tbody>
        </table>
        <br>
        <img src="{{ image }}">
        <br>
        <a href="/">Go Back</a>
    </body>
    </html>
    """

    #Render HTML using jinja2
    html_content = jinja2.Template(HTML_Template).render(avgMarks=avgMarks,maxMarks=maxMarks,image=img)
    return html_content


#Function to get HTML Content
def get_HTML(data,idType):

    if idType=='student_id':
        return get_HTML_byStudentID(data)
    else:
        return get_HTML_byCourseID(data)

#Fuction to write content to file
def write_content(file,content):
    f=open(file,'w')
    f.write(content)
    f.close()

   

# Flask app
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])

def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        try:
            idType=request.form['ID']
            idValue=request.form['id_value']
        except:
            return render_template('wronginput.html')
        #Get Required Data
        file='data.csv'
        data= get_required_data(file,idType,idValue)
        #If data is empty
        if not data:
            return render_template('wronginput.html')
        #Get HTML Content
        html_content=get_HTML(data,idType)
        #Write Content to file
        write_content('templates/show.html',html_content)

        return render_template('show.html')
    else:
        return render_template('wronginput.html')

if __name__=="__main__": 
    app.run()
