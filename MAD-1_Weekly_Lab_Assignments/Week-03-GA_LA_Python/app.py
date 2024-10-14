import jinja2
import sys
import matplotlib.pyplot as plt


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

def output(html_content):
    #Write HTML to file output.html
    outputFile=open('output.html','w')
    outputFile.write(html_content)
    outputFile.close()

def html_for_student_id(Fulldata,values):
    #Get Required Data
    data=[]
    for line in Fulldata:
        if line["student_id"] in values:
            data.append(line)
    #Calculate Total
    total=0
    for line in data:
        total+=int(line["marks"])   
    #Jinja2 Template
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Details</title>
    </head>
    <body>
        <h1>Student Details</h1>
        <table border="1">
            <thead><tr>
                <th>Student ID</th>
                <th>Course ID</th>
                <th>Marks</th>
            </tr></thead>
        <tbody>
        {% for line in data %}
            <tr>
                <td>{{ line.student_id }}</td>
                <td>{{ line.course_id }}</td>
                <td>{{ line.marks }}</td>
            </tr>
        {% endfor %}
            <tr>
                <td colspan="2">Total</td>
                <td>{{ total }}</td
            </tr>
            </tbody>
        </table>
    </body>
    </html>
    '''
    #Render HTML using jinja2
    html_content = jinja2.Template(html_template).render(data=data,total=total)

    return html_content
def html_for_course_id(Fulldata,values):
    #Get Required Data
    data=[]
    for line in Fulldata:
        if line["course_id"] in values:
            data.append(line)
    if len(data)==0:
        output(Invalid())
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

    #Jinja2 Template
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Course Data</title>
    </head>
    <body>
        <h1>Course Data</h1>
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
    </body>
    </html>
    '''
    # Create a bar chart for marks frequency
    img="plot.png"

    marks = [int(line["marks"]) for line in data]
    marks_frequency = {mark: marks.count(mark) for mark in set(marks)}
    plt.figure(figsize=(10, 5))
    plt.bar(marks_frequency.keys(), marks_frequency.values(), color='blue')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig(img)
    plt.close()

    #Render HTML using jinja2
    html_content = jinja2.Template(html_template).render(avgMarks=avgMarks,maxMarks=maxMarks,image=img)
    
    return html_content

def Invalid():
    #Jinja2 Template
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Something Went Wrong</title>
    </head>
    <body>
        <h1>Wrong Inputs</h1>
        <p>Something went wrong</p>
    </body>
    </html>
    '''
    #Render HTML using jinja2
    html_content = jinja2.Template(html_template).render()
    return html_content

def main():
    #Get Whole Data
    Fulldata=get_whole_data("data.csv")


    #Get arguments from command line
    args=sys.argv
    if len(args)<3:
        getby="Invalid"
    elif args[1]=="-s":
        values=args[2:]
        output(html_for_student_id(Fulldata,values))
    elif args[1]=="-c":
        values=args[2:]
        output(html_for_course_id(Fulldata,values))
            
    else:
        output(Invalid())


if __name__ == '__main__':
    main()


