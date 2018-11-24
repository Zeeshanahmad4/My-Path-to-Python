#making a virtual env for dejango
#comands for linux and windows
#https://www.codingforentrepreneurs.com/blog/install-django-on-linux-ubuntu/
 
 
 
 
 #python3.5
#install vir in linux
apt-get install python3-venv
#make the virual env
virtualenv -p python3 .
source bin/activate 
pip install Django==2.1.3
django-admin startproject testpro3
django-admin startapp testapp3
python3 manage.py runserver







 #pyhton2.5 do not use this
mkdir venv && cd venv
virtualenv .
source bin/activate                                               .\Scripts\activate    # for windows activation
pip install django
django-admin startproject testpro3
django-admin startapp testapp3
python manage.py runserver

"""
Things 2 do's after setting up project
1.add app name to the seeting.py file in installed app
2.add this to views.py file"""
from django.http import HttpResponse
def index(request):
    return HttpResponse("zeeshan")


 


#project own url maping
#steps
#1.add this to project urls"""
from firstapp import views
url(r'^$',views.index,name='index'),



 

#url mapping through apps 
#application can have his own url mapping whihc we can call from urlpattrens which
#step 1"""
from django.conf.urls import include
url(r'^',include('firstapp.urls'))#add into project url patterens 

#step 2
#creal a urls.py file in app folder and add this into it 
from django.conf.urls import url
from firstapp import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
#done url mapping is complete your new url for this app is http://127.0.0.1:8000/
  
  
  
  
 """ 
 making new templates and templates tags
 steps 
       1-creating a dict name "Tamplates" in the same dic in which project and first_app is held and put index.html file there
       2-enter the details in project setting.py about your templates injecting code in the setting.py"""
  import os
  TEMPLATES_DIR = os.path.join (BASE_DIR,"templates")
  
  'DIRS': [TEMPLATES_DIR,]#in Templates in setting.py file 
      #3-comeback to views.py of firs_app inject code
from django.http import HttpResponse
def index(request):
    my_dict = {'insert_me':"hello i am from ttemplates firstapp index"}#this is the templates variable i.e dynamic content
    return render(request,'first_app/index.html',context=my_dict)
  #4-in the templates index.htnml insert the template variables in the body of html as
  {{ insert_me }}#syntax of templates variables
  
 #we can also use templates tags or variables for injecting static files like pics and css javascript 
 #we will make a direcory folder "statics" in src and then we will make an entry in the project of that director 
  
 #steps 
STATIC_DIR = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [STATIC_DIR,]#add with the static url in setting.py
{% load staticfiles %}#place this code in the html under doctype tag
<img src="{% static "images/Z.jpeg" %}" alt="oh fuck">#this is how we can add static content now



#creating models and setting admin panel 
#steps
1.#creat classes for models in models.py of app file i created 3 class for 3 models.
from django.db import models
class Topic(models.Model):
    top_name = models.CharField(max_length =264 ,unique = True)

    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length = 264,unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name 

class AccssRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

#step 2 do migration 
python manage.py migrate

#step 3 register your models in admin file of the app 
from django.contrib import admin
from firstapp.models import Topic, Webpage, AccssRecord
admin.site.register(AccssRecord )
admin.site.register(Webpage)
admin.site.register(Topic)

#steps 4 migrates your app this time
python manage.py makemigrations firstapp
python manage.py migrate#again migration
 
#step 5 creating first super user 
python manage.py createsuperuser
#give name and password
#finish by 
python manage.py runserver



#papulating the data base 


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn.settings')

import django
django.setup()

import random
from firstapp.models import Topic, Webpage, AccssRecord
from faker import Faker


fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get a topic
        top = add_topic()

        #create fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create new webpage entry
        webpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccssRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]


def populate_user(N=5):
    for entry in range(N):
        # get a topic
        name = fakegen.name().split()
        #create fake data for entry
        fake_first_name = name[0]
        fake_last_name = name[1]
        fake_email = fakegen.safe_email()



if __name__ == '__main__':
    print('populating script')
    populate(20)
    populate_user(20)
    print('populating complete')








#RELATIVES URLS
#STEPS
#make sure to define func in the views.py 
#1.make the desire dic and the desire files in htat dics
#2.project urls.py

from django.conf.urls import url,include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name = 'index'),#main page
    url(r'^basic_app/',include('first_app.urls')),#telling that look in the app urls.py the variable *basic_app and includes frist app urls
]
#3.app urls.py
from django.conf.urls import url
from first_app import views


app_name = 'first_app'#the urls varibales *

urlpatterns = [
url(r'^relatives/$',views.rel,name = 'relatives'),
url(r'^other/$', views.other, name='other')
]

#4.in the html 
<!DOCTYPE html>
<html>

<head>
    <title>Hello World HTML</title>
</head>

<body>
    <h1>Hello World reltive</h1>
    <a href="{% url 'first_app:other' %}">the rel page</a># looking for urls varibales * and then other 
</body>

</html>





#Temoplates inheritance
#steps
#1.add this soce snipts after the code which you want to inhert this is the parent file 

    {% block body_block %}
    {# Anything outside of this will be inherited if you use extend.#}
    {% endblock %}
    
#2.sytax of the child file will be following 
<!DOCTYPE html>
{% extends "basic_app/base.html" %}#parent app tag 
    {% block body_block%}#child own html will goes here

    <h1>Hello and welcome to the site!</h1>
    <h1>This is the index.html page</h1>

    {% endblock %}

     
  
#Djanto forms starts
     
 #steps
     #step 1
     
 #creat a file forms.py in app and and forms.html file and give its url patteren in prject url
     
 #forms.html file 
 
     
  <body>
<h1>Welcome to the Form Page!</h1>

<div class="container">
    <form action="" method="POST">
        {{ form.as_p }}#templates tag of the django form 
        {% csrf_token %}#token for security
        <input type="submit" class="btn btn-primary" value="Submit">
    </form>
</div>
     

     
#forms.py this is the django form 
from django import forms
class formname(forms.Form):
    name = forms.CharField()#fields
    email = forms.EmailField()
    varfiy_email = forms.EmailField(label="enter your email again")
    text = forms.CharField(widget = forms.Textarea)
     
     
 #views.py 
 
from basicapp import forms

def index(request):#home fun
    return render (request,"basicapp/index.html")


def form_fun(request):#form function
    form = forms.formname()


    if request.method == "POST":#security check
        form = forms.formname(request.POST)
        if form.is_valid():
            print("Form Validation Success. Prints in console.")
            print("Name"+form.cleaned_data['name'])
            print("Email"+form.cleaned_data['email'])
            print('Text'+form.cleaned_data['text'])

    return render (request,"basicapp/form_page.html",{"form": form })
     
     
#project url 
    
     
url(r'^formpage/',views.form_fun,name="form_page")


     
 #connecting forms and models
     
 #forms.py  
 
 from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):#this form model is connected to the model user which we import from apptwo.models
    class Meta():
        model = User
        fields = '__all__'
     
     
#in models.py
 
 from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)

#in views 
 
     
 from django.shortcuts import render
from appTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    form = NewUserForm()#form instant


    if request.method == 'POST':#if user make post
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)#return user to index
        else:
            print("ERROR!")

    return render(request,'appTwo/users.html',{'form':form})

     
 
     
   #in forms.html
   <body>
    <h1>Please Sign Up:</h1>
    <div class="container">
      <form method="POST">
        {{ form.as_p }}#form tag
        {% csrf_token %}#security token
        <input type="submit" class='btn btn-primary' value="Submit">
      </form>

    </div>

  </body>
     
#make sure all the url patteren is called 
#end of connecting fomrs with models
     

     
     
#Validators for validations
 
#custom validator getting value of the field as an arguments
     
from django.core import validators
def check_for_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("nAME SHOULD START WITH Z")

#actuall forms
class formname(forms.Form):
    name = forms.CharField(validators=[check_for_z])#custom validators value checking
    email = forms.EmailField()
    varfiy_email = forms.EmailField(label="enter your email again")
    text = forms.CharField(widget = forms.Textarea)
    #django bulit.in validotrs 
    #bulit in validators calling maxlenth value checking
    botcater = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    




#there is differrence between python 2 and 3 for referance 
#https://stackoverflow.com/questions/43252801/overriding-clen-method-and-call-super-in-it
    
    
    
    #cleaning all the form at once  
    def clean(self):
        all_clean_data = super(formname,self).clean()
        emial =all_clean_data["email"]
        vmail = all_clean_data["varfiy_email"]

        if emial != vmail:
            raise forms.ValidationError("makesure email match")
 

 #end of validators
     #end of django forms
     
     #CBVs class based views not very usefull no listtemplates
     
     #url patteren will be like this
     
     url(r'^$',views.indexview.as_view()) #views classname.as_view()
     
     
     #index.html
     
     {% extends "base.html"  %}



{% block body_block%}

<h1>Testing the templates</h1>

<h2> injected content : {{ injecttime }}</h2>#injecting material from cbvs

{% endblock %}
     
     #views.py (important)
     from django.views.generic import View,TemplateView

class indexview(TemplateView):#class
    template_name = 'index.html'#vairable name is equal to file name into templates folder
    

    def get_context_data(self,**kwargs): #fun for templates taging
        context = super(indexview, self).get_context_data(**kwargs)#syntax is diiferent in both python for super
        context['injecttime'] = 'basic injecttion'#tagging into html
        return context

     #CBVs class based views with listtemplates
     
     #base.html (header)
     #making a nav bar and to links on it 
       <body>
    <nav class="navbar navbar-default navbar-static-top">
        <ul class="nav navbar-nav">
          <li><a class="navbar-brand" href="{% url 'basic_app:list' %}">Schools</a></li>#defining relative url
          <li><a class="navbar-link" href="{% url 'admin:index' %}">Admin</a></li>
          <li><a class="navbar-link" href="#"></a></li>
        </ul>
    </nav>

    <div class="container">
      {% block body_block %}

      {% endblock %}
    </div>

  </body>
     
     
     
            #school list
  {% extends "basic_app/basic_app_base.html" %}#inherting the html header from basic_app.html
{% block body_block %}
  <div class="jumbotron">

    <h1>Welcome to the List of Schools Page!</h1>
      <ol>
        {% for school in school_list %}
          <h2><li><a href="{{school.id}}/">{{ school }}.name}} </a></li></h2>#template tagiing for loop
        {% endfor %}
      </ol>

  </div>


{% endblock %}


     
     
     
 
     #school details.html
     
     {% extends "basic_app/basic_app_base.html" %}#inheriting the templates
{% block body_block %}
  <div class="jumbotron">
    <h1>Welcome to the School Detail Page</h1>
    <h2>School Details:</h2>
    <p>Id_num: {{school_details.id}}</p>#template tagging of model school
    <p>Name: {{ school_details }}.name}}</p>
    <p>Principal: {{school_details.principal}}</p>
    <p>Location: {{school_details.location}}</p>
    <h3>Students:</h3>

      {% for student in school_details.students.all %}
        <p>{{student.name}} who is {{student.age}} years old.</p>
      {% endfor %}

  </div>
  <div class="container">
    <p><a class='btn btn-warning' href="{% url 'basic_app:update' pk=school_details.pk %}">Update</a></p>

  </div>

{% endblock %}
     
 
 
     #models.py
  
  
  from django.db import models


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name
     
     
     
     
class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students')

    def __str__(self):
        return self.name

 
 
    #views.py
 from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView)
from . import models
 
 
 class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):#nothing special just sending data with class and templates tags ,data is basic
        context  = super(IndexView,self).get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context
       
       
       class SchoolListView(ListView):
    context_object_name = 'school_l'#using in template tagging in school_list.html

    #tag will creat automaticall called school_list
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    model = models.School
    
    
    
    class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    
    
    #urls.py
    
 from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),

]


       
       
       
       




 
 
     
     
     
     
THINGS I STUCK OFF FOR A WHILE

1.not adding my name in the app folder
3.templates tagging is white space senstive
2.not changing names of files when copy code from referance code
4.if you can not find the syntax eroor from a given line of exception ,simply rewrite the code 
