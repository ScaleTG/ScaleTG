Getting Started
===============
To get started with ScaleTG, run the following commands:

.. code-block:: bash

   git clone --depth 1 https://github.com/ScaleTG/ScaleTG.git
   cd ScaleTG
   git submodule sync
   git submodule update --init --force --recursive modules/core apps/authorization
   python3 -m venv .env
   ./.env/bin/pip3 install -r requirements.txt
   cp config.example.py config.py

Once you're done, all you need to do is edit the config.py file and you'll be good to go to the next section.