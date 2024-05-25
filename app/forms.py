import datetime
from django import forms

from app.models import *



# #Creating Validations for Topic Form 
# topic_name shouls not start with letter 'a'
#     creating User Defined Validators for this using Normal Forms


def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('started with a')
    

#topic_name , name -->webpage length should be >4
def validate_len(value):
    if len(value)<4:
        raise forms.ValidationError('length must be greater than 5')
    
def validate_url(value):
    if not value.endswith('in'):
        raise forms.ValidationError('url should end with in')
    
def validate_email(value):
    if not value.endswith('gmail.com'):
        raise forms.ValidationError('url should end with com')
    
def date_validate(value):
    if value > datetime.date.today():
        raise forms.ValidationError("date should be in the past!")
    

    

class TopicForm(forms.Form):
    topic_name = forms.CharField(validators=[validate_for_a,validate_len]) #this is the name shown in fornt end in TitleCase


class WebpageForm(forms.Form):
    #Queryset = Topic.objects.all()
    topic_name=forms.ModelChoiceField(queryset = Topic.objects.all() ) # for selecting options 
    name=forms.CharField(max_length=100,validators=[validate_len])
    url=forms.URLField(validators=[validate_url])
    email=forms.EmailField(validators=[validate_email])

class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset= Webpage.objects.all() ) #    Queryset =Webpage.objects.all()
    date=forms.DateField(validators=[date_validate])
    author=forms.CharField(max_length=100,validators=[validate_len])
