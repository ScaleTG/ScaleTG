Structure
==========

A typical ScaleTG project consists of these files and directories:

**apps**
   the directory containing all the app packages

   apps are essentially the main code for your bot, they're responsible for interacting with users
   and utilizing framework capabilities.
**modules**
   the directory containing all the functionality provided in the framework
   
   by default, only the core module is present which provides the main functionality and features present in the framework,
   the core module and modules in general will be discussed in length.
**config.py**
   all configuration that must be hard-coded into the code.

   it is generally containing the necessary and non-changing data such as the api token for your bot.
**wsgi.py**
   the module responsible for running a local WSGI server

   due to performance reasons in mind when building ScaleTG, WebHook is the only supported method of receiving updates.
**main.py**
   responsible for passing incoming requests to apps

   this may just be the heart of ScaleTG: it loads all active apps set in the config file and passes the request unto them

   it is also responsible for returning a response so it is provided back to webhook

**Note:** *this structure does not go over the included authorized app modules.*