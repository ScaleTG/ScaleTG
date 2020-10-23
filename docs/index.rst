Welcome to ScaleTG's documentation!
===================================

**ScaleTG** is an open-source Python framework created to make creation and maintenance of Telegram Bots easier.

.. toctree::
   :maxdepth: 2
   
   structure


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


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
