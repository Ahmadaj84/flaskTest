from flask import Flask, render_template,url_for
from forms import RegisterationForm , LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '0329feb15fe89e480a7c333ef64c0d8c'

posts = [{
'author': 'corey scherfl',
'title': 'Blog post 1',
'content': 'First post content',
'date_posted': 'April 20,2017'} ,
{
'author': 'Ahmad jifry',
'title': 'Blog post 5',
'content': 'second post content',
'date_posted': 'April 15,2018'},
{
'author': 'Ahmad ALi',
'title': 'Blog post 8',
'content': '3rd post content',
'date_posted': 'April 30,2018'}]


@app.route("/")
def hellow():
    return render_template('home.html' ,  posts= posts , title = "HOME")
@app.route("/about")
def toAbout():
    return render_template ('about.html' , title="Testtttting")
@app.route("/register")
def register():
    form = RegisterationForm()
    return render_template('register.html', title = 'Register' , form= form)
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login' , form= form)



if __name__ == '__main__':
    app.run(debug=True)
