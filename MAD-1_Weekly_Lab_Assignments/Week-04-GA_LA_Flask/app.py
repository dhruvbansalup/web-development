from flask import Flask, request, render_template
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
def get_Total(data):
    #Calculate Total Marks
    total=0
    for line in data:
        line['marks']=int(line['marks'])
        total+=line['marks']
    return total

#Function to get HTML Content if ID is Course ID
def get_Avg_Max_Graph(data,img):
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
    plt.clf()

    plt.bar(marks_frequency.keys(), marks_frequency.values(), color='blue')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig(img)
    plt.close()

    return avgMarks,maxMarks
  

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
            return render_template('wronginput.html',error="Invalid Input")
        
        #Get Required Data
        file='data.csv'
        data= get_required_data(file,idType,idValue)
        #If data is empty
        if not data:
            return render_template('wronginput.html',error="No Data Found")

        if idType=='student_id':
            return render_template('student_data.html',data=data, total=get_Total(data))
        elif idType=='course_id':
            img='static/plot.png'
            avg,max=get_Avg_Max_Graph(data,img)
            return render_template('course_data.html',avgMarks=avg,maxMarks=max,image=img)
        else:
            return render_template('wronginput.html',error="Invalid ID Type")
        
    else:
        return render_template('wronginput.html',error="Invalid Request Method")

if __name__=="__main__": 
    app.run()
