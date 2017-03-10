---
layout: post
title:  "Infiriendo el género de una persona a partir de su nombre"
date:   2017-03-10
categories: project
---

# Nuestro problema
A pesar de que _Facebook_ da estadísticas a los administradores de las páginas, queríamos obtener nuestros propios datos. Ahora bien, debido a la política de privacidad de la empresa los datos que podemos obtener de las personas que interactúan con nosotras son sólo __su nombre__, su id de Facebook y poco más. 

En ese momento nos preguntamos, ¿habrá alguna forma de saber el género de una persona a partir de su nombre? Y buscando un poco por internet encontramos [genderator](https://github.com/davidmogar/genderator)! :heart:

# Código
¿Cómo usar esta librería? Muy simple: debemos crear una instancia de la clase `Parser` y llamar al método `guess_gender` pasándole el nombre como parámetro, ¿fácil no?

{% highlight python %}
import genderator

guesser = genderator.Parser()
answer = guesser.guess_gender(name)
{% endhighlight %}

Si el objeto `guesser` ha encontrado una respuesta, devolverá un `OrderedDict` con los datos de la respuesta. En caso contario, no devolverá nada. Debemos controlar esta situación, haciendo que, en caso de no devolver nada, se devuelva un `OrderedDict` con género desconocido:

{% highlight python %}
import genderator

guesser = genderator.Parser()
answer = guesser.guess_gender(name)

if answer:
    print(answer)
else:
    print(OrderedDict([('names', name), ('gender', 'Unknown')]))
{% endhighlight %}

Por último, debido a que queremos hacer un _gráfico de barras_ con el número de personas de cada sexo que interacciona con nosotras, debemos hacer un diccionario más reducido en el que se recojan el número de interacciones obtenidas para cada género. Para ello, hemos definido la siguiente función:

{% highlight python %}
def export_to_json(data_list):
    results = {'Female':0, 'Male':0, 'Unknown':0}

    for d in data_list:
        results[d['gender']] += 1

return results
{% endhighlight %}
