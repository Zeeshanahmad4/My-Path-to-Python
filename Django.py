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


    
 


