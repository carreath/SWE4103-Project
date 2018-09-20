### **Python**
Python is a pretty straight forward language, some people may even call it pseudo code. This comes from it's use of white-space instead of semi-colons and braces as well as it being an interpreted and dynamically typed language. This means that there is no need to compile your .py(Python) files like you would with .java files, instead the intepreter can just run the Python code. Dynamic typing just means you don't have to declare variable types when assigning variables a value, the intpreter 'understands' the typing of your variable.

There are 2 Python versions that are widely used, Python2 and Python3. They are currently both supported, but it is in our best interest to Python3 as it is the future of the language. The release version of Python3 that we'll use for this project is Python3 version 3.6.6

#### Setting up Python
If you're on **Linux** it's most likely the case that you already have Python installed. To check the version of your installation type the following command:
```bash
python3 --version
```

If you're on **Windows** most recent downloads for version can be found here: https://www.python.org/downloads/windows/

#### Some IDEs/Text Editors for Python
Feel free to use whatever you want, but here are some things I've enjoyed using for Python development
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Spyder](https://pythonhosted.org/spyder/installation.html)
- [Sublime Text](http://www.sublimetext.com/3)
- [VS Code](https://code.visualstudio.com/download)


#### Getting to know Python
A basic understanding of the syntax, data structures(dicts, lists, tuples, etc.), how to use functions, and optionally some OOP is all you should need to contribute.
Some useful resources for getting up to speed on reading and writing Python:
- [The Python Tutorial](https://docs.python.org/3.6/tutorial/index.html)
- [Python 101](http://www.davekuhlman.org/python_101.html)
- [Python in 10 Minutes](https://www.stavros.io/tutorials/python/)
- [Google's Python Course](https://developers.google.com/edu/python/)
- [Other Python Resources](https://wiki.python.org/moin/BeginnersGuide/Programmers)



#### Setting up Pip
Pip is the package installer for Python packages.

To setup pip for Python3 packages on **Linux** use the following command:
```bash
sudo apt-get install pip3
```
Be careful you only update your user pip3 installation on Linux or you could end up breaking your OS, bad plan, I've done it.

On **Windows** pip should already be installed with your default Python installation, there is no need to install pip3. To check the version of your pip use the following command:
```bash
pip --version
```
---

### **Flask**

For this project we are planning on using Flask, more speicifically Flask-RESTful to build out the API. First things first what is an API. An API is an Application Programming Interface, but no really, like what is it. An API is just a way for clients/users to send requests(get, post, put, delete) and for us to serve/process them and send back a response. The way requests are handed to the API and the way responses from the API are handled is the frontends job, as backend devs we are solely concerned on handling the request and sending the expected response back.

Now you may be thinking what does it mean for an API to be *restful*, well here are the 6 key principles underlying exactly that:
- **Client-Server**: There should be a separation between the server that offers a service, and the client that consumes it.
- **Stateless**: Each request from a client must contain all the information required by the server to carry out the request. In other words, the server cannot store information provided by the client in one request and use it in another request.
- **Cacheable**: The server must indicate to the client if requests can be cached or not.
- **Layered System**: Communication between a client and a server should be standardized in such a way that allows intermediaries to respond to requests instead of the end server, without the client having to do anything different.
- **Uniform Interface**: The method of communication between a client and a server must be uniform.
- **Code on demand**: Servers can provide executable code or scripts for clients to execute in their context. This constraint is the only one that is optional.

#### What is Flask
Flask is a mircoframework specifically designed for building web applications with Python from the ground up. It is incredibly lightweight and requires very little code to get it up and running. Sounds pretty good to me.

Flask-RESTful, the framework we'll be using for this project is an abstraction on top of the Flask microframework specifically built for creating restful APIs.

Here's a very simple API HelloWorld example built with Flask-RESTful:
```python
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```

#### Installing Flask
To install Flask and Flask-RESTful enter the following command:
```bash
# Linux
pip3 install flask-restful

# Windows
pip install flask-restful
```

Alternatively you can install it from github using the following commands, please note you will have to install Flask 0.10 or greater before doing the github installation as it will not automatically install the dependencies for Flask-RESTful
```bash
git clone https://github.com/flask-restful/flask-restful.git
cd flask-restful
# Linux
python3 setup.py develop

# Windows
python setup.py develops
```

#### Getting started with Flask/Flask-RESTful
The definitive guide for Flask-RESTful: https://flask-restful.readthedocs.io/en/latest/index.html

The documentation on Flask if you're curious about something Flask related: http://flask.pocoo.org/docs/1.0/
