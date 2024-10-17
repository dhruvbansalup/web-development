from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/form',methods=['GET','POST'])
def hello_world():
    # return render_template('P008_hello.html')
    if request.method == 'GET':
        return render_template('P008_getdetails.html')
    elif request.method == 'POST':
        username=request.form['user_name']
        return render_template('P008_displaydetails.html',display_name=username)
    else:
        print('Invalid request')

if __name__ == '__main__':
    app.debug=True
    app.run()