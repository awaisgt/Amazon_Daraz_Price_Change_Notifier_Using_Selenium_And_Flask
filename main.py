import myselenium
from flask import Flask, redirect, url_for, render_template, request,session
app= Flask(__name__)
@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST','GET'])
def my_form_post():
    if request.method == 'POST':
        link = request.form['username']
        email = request.form['password']
        minutes = request.form['minutes']
        file = open("abc.txt",'w')
        strx = link+ "\n" + email+"\n"+minutes
        file.write(strx)
        myselenium.run_script(link,email,minutes)
        return render_template('show.html', username=link ,password = email ,minutes = minutes, txt = "You will soon receive the confirmation email." )


@app.route('/show')
def my_formx():
    file = open("abc.txt",'r')
    first = file.readline()
    second = file.readline()
    minutes = file.readline()
    return render_template('show.html', username=first ,password = second ,minutes=minutes, txt ="")
