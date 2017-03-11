---
layout: post
title:  "Extrayendo los datos de Twitter"
date:   2017-03-11
categories: project
---

# API REST de Twitter y Tweepy

Twitter ofrece una _API_ muy fácil de usar que nos permite extraer una gran cantidad de información útil sobre un usuario, sus tweets, retweets, quién ha hecho retweet, y un montón de cosas más. Pero, existe una librería para Python llamada [Tweepy](http://www.tweepy.org/) que nos permite manejar la API desde Python de una forma muy cómoda y sencilla

Para instalar esta librería, podemos instalarla gracias a ___pip___ de la siguiente manera:

{% highlight bash %}
pip install tweepy
{% endhighlight %}

Una vez instalado, ya podremos empezar a trabajar con Twitter y Python.

# Conectando con Twitter 

Antes de comenzar a extraer datos, es necesario obtener unas claves de acceso para Twitter. Esto se puede hacer accediendo a la página de [Twitter Aps](https://apps.twitter.com/), creando una nueva _app_ y obteniendo las claves siguientes:

* __Consumer Key (API Key)__.
* __Consumer Secret Key (API Secret)__.
* __Access Token__.
* __Access Token Secret__.

Una vez que tengamos nuestras claves, ya podremos conectarnos a la api a través de Python. 

Una buena práctica a la hora de tratar con claves de acceso privadas, es no ponerlas en nuestro código, por si accidentalmente, estas claves se suben al repositorio, quedando totalmente expuestas. La solución a esto, es poner las claves como variables de entorno en nuestro _bash_, realizando un export.

{% highlight bash %}
export TWITTER_CONSUMER_KEY=clave_de_twitter
{% endhighlight %}

Una vez exportadas las cuatro claves como variables de entorno, podemos leerlas desde Python importando del módulo `os` la función `environ` para poder leer las variables de entorno, pasando solo como un string el nombre de la variable. 

{% highlight python %}
import tweepy  # Manage Twitter API
import pandas as pd  # to create dataframes
from os import environ  # To get the environment variables

# Use your Twitter API keys to connect

auth = tweepy.OAuthHandler(environ["TWITTER_CONSUMER_KEY"],
                           environ["TWITTER_CONSUMER_SECRET"])

auth.set_access_token(environ["TWITTER_ACCESS_TOKEN"],
                      environ["TWITTER_ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth_handler=auth, wait_on_rate_limit_notify=True,
                 wait_on_rate_limit=True)
{% endhighlight  %}

Con esto, ya estaremos conectados a la API de Twitter para poder extaer los datos que necesitemos. 

Además de esto, hemos importado `pandas` para poder crear DataFrames para manejar los datos con una mayor comodidad y poder representarlos de una manera más fácil. 

La extracción de los datos de los tweets, se realiza con la función `get_timeline_data`, en la que extraeremos de nuestro timeline el __id__ del tweet, __número de Retweets__, __número de Me Gusta__ y la __fecha__ del tweet, y generamos un DataFrame con estos datos.

{% highlight python %}
def get_timeline_data():

    tweets_list = []
    # construct the dataframe
    for tweet in tweepy.Cursor(api.user_timeline, include_rts=False).items():

        tweets_list.append([str(tweet.id), int(tweet._json['favorite_count']),
                            str(tweet._json['retweet_count']), tweet.created_at])

    tweets = pd.DataFrame(data=tweets_list,
                          columns=['id', 'like', 'retweet', 'date'])

    return tweets
{% endhighlight  %}

Con esto, tendremos nuestro DataFrame listo para ser usado.