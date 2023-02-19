from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name= StringField("Name", validators= [DataRequired()], description= " Please enter your Fullname")
    email= StringField("E-emai", validators= [DataRequired(), Email()], description= "Please enter your Emaill address")
    subject= StringField( "Subject", validators= [DataRequired()], description= "Please enter your Subject")
    body= TextAreaField("Body", validators=[DataRequired()], description= "Please enter your Message") 
    submit = SubmitField("Submit")


