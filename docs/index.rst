Welcome to ScaleTG's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

**ScaleTG** is an open-source Python framework created to make creation and maintenance of Telegram Bots easier.

Getting Started
---------------
To get started with ScaleTG, run the following commands:

.. code-block:: bash

   git clone --depth 1 https://github.com/WiGeeky/ScaleTG.git
   cd ScaleTG
   git submodule sync
   git submodule update --init --force --recursive modules/core apps/authorization
   rm -rf .git && git init # This is optional, but it is reccommended that you initialize a new git repository
   python3 -m venv .env
   ./.env/bin/pip3 install -r requirements.txt
   cp config.example.py config.py
   git add . && git commit -m "initial commit"

Once you're done, all you need to do is edit the config.py file and you'll be good to go!

Project Structure
-----------------
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

**Note:** *this structure does not go over the included authorized app modules*


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
