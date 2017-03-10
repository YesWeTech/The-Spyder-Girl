---
layout: post
title:  "Extrayendo datos de Facebook"
date:   2017-03-10
categories: project
---

# Sobre la API Graph

La [API Graph](https://developers.facebook.com/docs/graph-api/overview) de Facebook es la API por referencia para extraer información de esta red social. Podéis explorar las posibilidades que ofrece con su [explorador](https://developers.facebook.com/tools/explorer).

En nuestro caso, vamos a centrarnos en obtener el _feed_ (posts que publicamos desde nuestra página) y, para cada post, el nombre de las personas que han dado me gusta a ese post.

# Código
Para poder trabajar con esta API de forma sencilla se utiliza la librería [facebook-sdk](https://github.com/mobolic/facebook-sdk). 

La forma de trabajar es bastante sencilla: creamos un objeto `facebook.Graph.API` pasándole como parámetro nuestra clave de acceso y, a partir de ahí, tenemos un objeto `graph` al que podemos llamar usando los mismos métodos que en el explorador de la API.

{% highlight python %}
import facebook
from os import environ

# connect to facebook
graph = facebook.GraphAPI(access_token=environ['FACEBOOK_ACCESS_TOKEN'], version='2.7')
# download notifications and likes from facebook.
data = graph.get_object(id="me", fields="feed{likes{id,name}},notifications{from}")
{% endhighlight  %}

Como habréis notado, tenemos la clave de acceso definida como variable de entorno :wink: