from datetime import datetime
from flask import Flask, render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterationForm , LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '0329feb15fe89e480a7c333ef64c0d8c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


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

@app.route("/home")
@app.route("/")
def hellow():
    return render_template('home.html' ,  posts= posts , title = "Ahmad Home")
@app.route("/about")
def toAbout():
    return render_template ('about.html' , title="Testtttting")
@app.route("/register", methods = ['GET' , 'POST'] )
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account has been created to the user {form.username.data}!!','success')
        return redirect(url_for('hellow'))
    return render_template('register.html', title = 'Register' , form= form)
@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@a.com' and form.password.data == 'password':
            flash('you have been logged in !!' , 'success')
        else:
            flash('wrong password or username!!', 'danger')
    return render_template('login.html', title = 'Login' , form= form)



if __name__ == '__main__':
    app.run(debug=True)
