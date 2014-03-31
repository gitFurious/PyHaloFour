PyHalo
======

A simple wrapper for HaloWaypoint's Halo 4 API written in Python.

## Features

+ Windows Live OAuth authentication.
+ Spartan Token generation.
+ HaloWaypoint API endpoint mapping.

### Usage

See [example.py](https://github.com/gitFurious/PyHalo/blob/master/example.py) for further usages.

#### Authentication

```python
import pyhalo.authentication

auth = pyhalo.authentication.HaloFour('user@exmaple.com', 'Passw0rd!')

auth_token = auth.get_new_token()

print(auth_token.__dict__)
# {
#    'gamertag': 'Furiousn00b', 
#    'analytics_token': 'C97F9C24...', 
#    'spartan_token': 'v2=ede2N...', 
#    'live_username': 'user@exmaple.com',
#    'live_password': 'Passw0rd!'
# }
```

#### API Requests

```python
import pyhalo.api

api = pyhalo.api.HaloFour(auth_token)

api_version = api.get_api_version()

print(api_version)
# {
#    'Current': '1.0.14056.1'
# }
```

### Requirements

[Requests](http://docs.python-requests.org/en/latest/ "Requests: HTTP For Humans")

> pip install -r requirements.txt

### Author

Damon Pollard ([@DamonLPollard](https://twitter.com/DamonLPollard "Tweet Me"))
