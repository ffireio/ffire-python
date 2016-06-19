"""
All project constants

ffire.constants.all
~~~~~~~~~~~~~~~~~~~

Major project constants are declared here, this file imports from no one
"""


API_ENDPOINT = 'https://api.ffire.io/v1/'

AUTHENTICATION_ENDPOINT = API_ENDPOINT + 'init'

CREATE_EVENT_ENDPOINT = API_ENDPOINT + 'events'
CONSUME_EVENTS_ENDPOINT = API_ENDPOINT + 'events/{event_name}/updates/{interval}'
DELETE_EVENT_ENDPOINT = API_ENDPOINT + 'events/{event_name}'  #: Placeholder will be replaced with event name

FIRE_EVENT_ENDPOINT = API_ENDPOINT + 'events/{event_name}/ffire'

SUBSCRIBE_EVENT_ENDPOINT = API_ENDPOINT + 'events/{event_name}/subscriptions'


EVENT_INDEX = 0


PASSWORD = 'password'
PAYLOAD_INDEX = 1
PORT = 'port'

USERNAME = 'username'

__all__ = [
    'EVENT_INDEX',
    'USERNAME',
    'PASSWORD',
    'PAYLOAD_INDEX',
    'PORT'
]
