# Twitch API 

Clase creada sobre un entorno con python 3.7, realiza varias llamadas a la nueva API de Twitch para diversos propósitos, para inicializar la clase debemos hacer algo como lo siguiente:
```python
from twitchapi import TwitchAPI
t = TwitchAPI('<Client-ID>','<OAuth Token>')
```

Todas las funciones devuelven en formato JSON la respuesta con los datos.
Por el momento no esta hecha a prueba de errores, por lo que si se la llama de manera incorrecta, no funcionará.
Si no se pasa alguno de los parámetros al instanciar la clase, ciertas funciones puede que no funcionen, ya que estas dependen de ello.