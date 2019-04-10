#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import json

class TwitchAPI:

    '''
        Clase provista de varias funciones para la realización de peticiones a la nueva
        API de Twitch (Helix), algunas de las funciones se realizan mediante el Client ID,
        mientras que otras lo hacen mediente el OAuth Token, por lo que para un mejor funcionamiento,
        se recomienda pasar ambas al inicializar la clase.
    '''

    # Crea un constructor para la clase donde se le pasa los datos del Twitch Dev.
    def __init__(self, client_id, client_oauth=''):
        self.c_id = client_id
        self.c_oauth = client_oauth
        self.auth_header = {'Client-ID': self.c_id}
        self.oauth_header = {'Authorization': 'Bearer ' + self.c_oauth}

    # (OAUTH) Se le pasa como parámetro el nombre de un canal de tw, y devuelve en json la información.
    def get_user_data(self, user_name):
        r = requests.get('https://api.twitch.tv/helix/users?login=' + user_name, headers=self.oauth_header)
        print(json.dumps(r.json(), sort_keys=True, indent=4))

    # (CLIENT ID) Devuelve un json con contenido en caso de que el usuario pasado se encuentre en streaming.
    def get_user_stream(self, user_name):
        r = requests.get('https://api.twitch.tv/helix/streams?user_login=' + user_name, headers=self.auth_header)
        print(json.dumps(r.json(), sort_keys=True, indent=4))

    # (CLIENT ID) Devuelve todos los videos del usuario indicado mediante el parámetro user_id.
    def get_all_videos(self, user_id):
        r = requests.get('https://api.twitch.tv/helix/videos?user_id=' + user_id, headers=self.auth_header)
        print(json.dumps(r.json(), sort_keys=True, indent=4))

    # (CLIENT ID) Devuelve información sobre el video que se le pasa en el parámetro video_id.
    def get_video(self, video_id):
        r = requests.get('https://api.twitch.tv/helix/videos?id=' + video_id, headers=self.auth_header)
        print(json.dumps(r.json(), sort_keys=True, indent=4))