Deploying ScaleTG
=================
ScaleTG comes pre-equpped with a Flask WSGI server meant to take Telegram requests, this documentation covers how a ScaleTG bot is deployed.

As ScaleTG comes with no web server functionality, it relies on a common web server (i.e nginx, apache, etc) to handle its requests.

Path
----
as advised by Telegram themselves, one way to ensure no one but Telegram can send requests to the server is using the api key in webhook path.
because of that, ScaleTG's Flask instance listens at the `/<api_key>` path.

Setup a WSGI Server (Gunicorn)
------------------------------
By default, ScaleTG uses gunicorn to serve its wsgi instance. When deploying, 
you should make sure you're binding Gunicorn to localhost instead of 0.0.0.0 for extra security.

Here's an example of how to use gunicorn for your project:

.. code-block::bash
    gunicorn wsgi:app -b 127.0.0.1:8000


Setup a reverse proxy (Nginx)
-----------------------------
You may use the web server of your choice for pointing requests to your bot. However, we recommend using nginx as it is wsgi-friendly and easy to setup.

Below as an example of what your virtual host configuration may look like:

.. code-block::json
    server {
        server_name example.com;

        location /bots/example {
            proxy_pass http://127.0.0.1:8000/;
        }
        
        location /bots/helloworld {
            proxy_pass http://127.0.0.1:8001/;
        }

        # Telegram requires HTTPS for webhooks, we recommend using Let's Encrypt 
        listen [::]:443 ssl; # managed by Certbot
        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    }
