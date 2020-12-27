from flask import Flask, render_template,url_for,flash,redirect
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
