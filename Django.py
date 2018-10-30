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
done url mapping is complete your new url for this app is http://127.0.0.1:8000/mynewextension/


