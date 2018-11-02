# making a virtual env for dejango
#comands for windows

 pip install virtualenv                     #install virtual env

 mkdir dir_name
 cd dir_name
 
virtualenv -p python3                       #make dir virtualenv


.\Scripts\activate                           #activating env


pip install django==1.11.5                  #installing django


django-admin startproject project_name #starting your first project


python3 manage.py runserver #run this to see your project on server make sure you are in right directory


python3 manage.py startapp nameofapp #running first app

#linux installation


https://www.codingforentrepreneurs.com/blog/install-django-on-linux-ubuntu/
#activating env

source path/bin/activate



 





#url mapping 
#application can have his own url mapping whihc we can call from urlpattrens which

#step one

from django.conf.urls import include
url(r'^mynewextension/',include('firstapp.urls'))#add into project url patterens 

#step 2

#creal a urls.py file in app folder and add this into it 

from django.conf.urls import url
from firstapp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
#done url mapping is complete your new url for this app is http://127.0.0.1:8000/mynewextension/
  
  
  
  
  
 #making new templates and templates tags
 
 #steps 
       #1-creating a dict name "Tamplates" in the same dic in which project and first_app is held and put index.html file there
       #2-enter the details in project setting.py about your templates injecting code in the setting.py
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


    
 


