from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///week7_database.sqlite3"
app.app_context().push()

db=SQLAlchemy(app)

#Database Models
class Student(db.Model):
    student_id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    roll_number=db.Column(db.String,unique=True,nullable=False)
    first_name=db.Column(db.String,nullable=False)
    last_name=db.Column(db.String)

class Course(db.Model):
    course_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    course_code=db.Column(db.String,unique=True,nullable=False)
    course_name=db.Column(db.String,nullable=False)
    course_description=db.Column(db.String)

class Enrollments(db.Model):
    enrollment_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    estudent_id=db.Column(db.Integer,db.ForeignKey("student.student_id"),nullable=False)
    ecourse_id=db.Column(db.Integer,db.ForeignKey("course.course_id"),nullable=False)



#Routes
@app.route("/",methods=["GET"])
def home():
    all_students=Student.query.all()
    return render_template('index.html',allstudents=all_students)

@app.route("/student/create",methods=["GET","POST"])
def createStudent():
    if request.method=="POST":
        r_no=request.form.get("roll")
        f_name=request.form.get("f_name")
        l_name=request.form.get("l_name")
        
        #Duplicate Error
        stu=Student.query.filter(Student.roll_number==r_no).first()
        if stu:
            return render_template("error.html",error="Student Already Exists")

        #Add to database
        db.session.add(Student(roll_number=r_no,first_name=f_name,last_name=l_name))
        db.session.commit()

        return redirect('/')
    return render_template('create_student.html')



@app.route("/student/<int:student_id>/update",methods=["GET","POST"])
def updateStudent(student_id):
    SelectedStudent=Student.query.get(student_id)
    all_courses=Course.query.all()
    
    if request.method == "POST":
        f_name=request.form.get("f_name")
        l_name=request.form.get("l_name")
        crs_id = request.form.get("course")

        if f_name:
            SelectedStudent.first_name = f_name
            SelectedStudent.last_name = l_name
             
            if crs_id:
                existing_enrollment = Enrollments.query.filter_by(estudent_id=student_id, ecourse_id=crs_id).first()

                if not existing_enrollment:
                    new_enrollment=Enrollments(estudent_id=student_id, ecourse_id=crs_id)
                    db.session.add(new_enrollment)
                    
        else:
            return render_template('error.html',error="First Name is Required!!")

        db.session.commit()
        return redirect('/')       

    return render_template('update_student.html',allcourses=all_courses,student=SelectedStudent,student_id=student_id)


@app.route("/student/<int:student_id>/delete",methods=["GET"])
def deleteStudent(student_id):
    stu=Student.query.get(student_id)
    db.session.delete(stu)
    #Delete enrollments
    Enrollments.query.filter_by(estudent_id=student_id).delete()
    db.session.commit()

    return redirect('/')

@app.route("/student/<int:student_id>",methods=["GET"])
def getStudent(student_id):
    stu=Student.query.get(student_id)
    Enrolls=db.session.query(Enrollments,Course).join(Course,Enrollments.ecourse_id==Course.course_id).filter(Enrollments.estudent_id==student_id).all()

    return render_template("student_details.html",student=stu,enrollments=Enrolls,student_id=student_id)

@app.route("/student/<int:student_id>/withdraw/<int:course_id>")
def withdrawCourse(student_id,course_id):
    Enrollments.query.filter(Enrollments.estudent_id==student_id, Enrollments.ecourse_id==course_id).delete()
    db.session.commit()

    return redirect('/')

#CRUD on Courses
@app.route("/course")
def coursesList():
    all_courses=Course.query.all()
    return render_template('courses.html',allcourse=all_courses)

@app.route("/course/create",methods=["GET","POST"])
def createCourse():
    if request.method=="POST":
        c_code=request.form.get("code")
        c_name=request.form.get("c_name")
        c_desc=request.form.get("desc")
        
        #Duplicate Error
        Cou=Course.query.filter(Course.course_code==c_code).first()
        if Cou:
            return render_template("error.html",error="Course Already Exists!!")

        #Add to database
        db.session.add(Course(course_code=c_code,course_name=c_name,course_description=c_desc))
        db.session.commit()

        return redirect('/')
    return render_template('create_course.html')

@app.route("/course/<int:course_id>/update",methods=["GET","POST"])
def updateCourse(course_id):
    SelectedCourse=Course.query.get(course_id)

    if request.method == "POST":
       
        c_name=request.form.get("c_name")
        c_desc=request.form.get("desc")

        if c_name:  # Ensure code and c_name are not None
            SelectedCourse.course_name = c_name
            SelectedCourse.course_description = c_desc

            db.session.commit()
            return redirect('/')
        else:
            # Handle the case where code or c_name is None
            return render_template("error.html",error="Course code and name are required.")    
    
    return render_template('update_course.html',course=SelectedCourse, course_id=course_id)

@app.route("/course/<int:course_id>/delete")
def deleteCourse(course_id):
    cou=Course.query.get(course_id)
    db.session.delete(cou)
    #Delete enrollments
    Enrollments.query.filter_by(ecourse_id=course_id).delete()
    db.session.commit()

    return redirect('/')

@app.route("/course/<int:course_id>")
def courseDetails(course_id):
    cou=Course.query.get(course_id)
    Enrolls=db.session.query(Enrollments,Student).join(Student,Enrollments.estudent_id==Student.student_id).filter(Course.course_id==course_id).all()

    return render_template("course_details.html",course=cou,enrollments=Enrolls,course_id=course_id)

if __name__=="__main__":
    # db.create_all() #For Creating Database
    app.run(
        debug=True
    )