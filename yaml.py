#!/usr/bin/python3

import requests
import yaml

spaceweb = 'http://api.open-notify.org/astros.json'

groundctrl = requests.get(spaceweb)

helmet = groundctrl.json()

a = yaml.dump(helmet)

print(a)

