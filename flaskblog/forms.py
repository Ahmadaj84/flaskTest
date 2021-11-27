from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User,Institute



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
class InstituteForm(FlaskForm):

    """ Add new institute in the database form linked to the file newinst.html"""

    instName = StringField('إسم المنشأة',validators=[DataRequired(message='يجيب إدخال إسم للمنشأة')])
    supName = StringField('إسم المشرف' ,validators=[DataRequired(message='يجيب إدخال إسم المشرف')])
    mobile = StringField('رقم الجوال' ,validators=[DataRequired(message='أدخل رقم الجوال') ,Length(min=10, max=10 , message='أدخل رقم الجوال بشكل صحيح') ])
    email = StringField('البريد الإلكتروني', validators=[DataRequired(), Email()])
    studenMaxNum = IntegerField('عدد الطلاب المسموح' , validators=[DataRequired(message='يجيب تحديد عدد الطلاب المسموح بتدريبهم')])
    submit = SubmitField('Add Institute')

class StudintOption(FlaskForm ):
    """docstring for StudintOption. so that a student can register in three diffrent institute"""

    option1 = SelectField('الإختيار الأول'  )
    option2 = SelectField('الإختيار الثاني')
    option3 = SelectField('الإختيار الثالث' )
    submit = SubmitField('تسجيل')
