How ScaleTG Functions
=====================
ScaleTG is built with modularity, OOP and scale in mind.

Modularity
----------
ScaleTG aims to replicate a modularity similar to those of Django. Functions of a bot can be broken down into what we call apps.

ScaleTG also allows for added functionality to the framework, this is achieved by what we call modules. The main difference between
an app and a module is that an app is meant to process incoming requests and user data, while a module is solely providing extra functionality
to an app.

Object-Oriented
---------------
ScaleTG's core module is responsible for turning the basic Telegram dictionary into an object. 

Currently, Telegram types `User`, `Chat` and `Message` are turned into their own object. Every key present in an incoming Telegram dictionary 
is accessible as an attribute to every object.

Scale
-----
Although the current version of ScaleTG still lacks builtin support for scale and load balancing, efforts to release solutions for scale will be coming soon.

Processing Lifecycle
--------------------
Once the configuration of the framework is done, and the bot is deployed (see :ref:`deploy`), ScaleTG has a set system of processing every request.

1. First, the request arrives to our WSGI server at **wsgi.py** then,
2. the request data is turned into a dict and passed to **main.py** then,
3. in main.py, all apps enabled through the config file are loaded in
4. in main.py main function, 
5. main.py loops through all enabled apps, passing the request object to their processor function
6. apps return either a Telegram response object or None, main.py collects all returned values
7. main.py iterates through the list of returned values, the first instance of a not None value is returned to **wsgi.py** as result
    7.1 if no apps return a value, the value return to wsgi.py is blank
8. wsgi.py returns the result to Telegram in response.

Currently, the first not None value returned by an app is taken as result and the rest are discarded. This will remain as the default
behavior since only one app is expected to be responding to a request. if you are planning to do multiple actions in response to one request,
you must utilize the core functionalities for sending a request to Telegram and return a blank string instead of None.