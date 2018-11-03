#making a virtual env for dejango
#comands for linux and windows
#https://www.codingforentrepreneurs.com/blog/install-django-on-linux-ubuntu/
 
mkdir venv && cd venv
virtualenv .
source bin/activate                                               .\Scripts\activate    # for windows activation
pip install django
django-admin startproject testpro3
django-admin startapp testapp3

"""
Things 2 do's after setting up project
1.add app name to the seeting.py file in installed app
2.add this to views.py file"""
from django.http import HttpResponse
def index(request):
    return HttpResponse("zeeshan")
  
 

""""
project own url maping
steps
1.add this to project urls"""
from firstapp import views
url(r'^$',views.index,name='index'),



 
"""
url mapping through apps 
application can have his own url mapping whihc we can call from urlpattrens which
step 1"""
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





































THINGS I STUCK OFF FOR A WHILE

1.not adding my name in the app folder
2.not changing names of files when copy code from referance code
