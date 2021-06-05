# Thrillophia - A Travel wesite

## Technology Stack
### Frontend
* HTML
* CSS
* Bootstrap
### Backend
* Django
### DBMS
* SQLite3

## Folder Structure
In our repository, we have 4 folders & 2 files. Lets see the funtionality of them one by one :-
1. **Hello** - This is our main project folder. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).These hello folder will further have some ".py" files which will play the following roles :-
* **Hello/__init__.py:** An empty file that tells Python that this directory should be considered a Python package.
* **Hello/asgi.py file**, new to Django as of version 3.0 which allows for an optional Asynchronous Server Gateway Interface to be run.ASGI can be considered as a succeeder interface to the WSGI. It also has the work similar to WSGI but this is better than the previous one as it gives better freedom in Django development. That’s why WSGI is now being increasingly replaced by ASGI.
* **Hello/settings.py** file controls our project’s settings.As the name suggests this file stores the configurations or settings of our Django project, like database configuration, main URL configurations, static file addresses, templating engines, security keys, allowed hosts, and much more.
* **Hello/urls.py** tells Django which pages to present in response to a URL request.
* **Hello/wsgi.py** , which stands for Web Server Gateway Interface, helps Django serve our eventual web pages means it is used for deploying our applications on to servers like Apache etc. 
