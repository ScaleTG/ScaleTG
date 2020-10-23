Getting Started
===============
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

Once you're done, all you need to do is edit the config.py file and you'll be good to go! navigate to :ref:`structure` to get a better understanding of how ScaleTG works.
