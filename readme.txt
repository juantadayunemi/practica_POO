python de forma global se instala desde afuera descargando el instaldor desde la web

#luego se instala virtualenv
pip install install virtualenv

# dentro de la carpeta del proyecto instalar entorno virtual
virtualenv venv

# activar 
.\venv\Scripts\activate

# abro el projecto con visual studio code y activo con visual studio en termial
.\venv\Scripts\activate

# instalo django 
pip install django

# creación del proyecto 

django-admin startproject system_pay .


#iniciar una aplicación
python manage.py startapp app_payment

  # registra la app en el proyecto 


# agregar la aplicacion en el proyecto 


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_payment'
]



# agregar las rutas en la carpeta de app 

agregar archivo urls.py
drentro del archivo esto 

urlpatterns = [
  path('', auth.home, name='home'),
]

# rentro de la aplicación agregar  , en urls 

urlpatterns = [
    path('', auth.home, name='home'),
    path('', include('app_payment.urls')),
]

