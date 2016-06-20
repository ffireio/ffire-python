"""
Fire module

ffire.core.fire
~~~~~~~~~~~~~~~

Some names say everything.
"""
import requests
import validators

from requests import ConnectionError
from requests import Request, Session
from validators import ValidationFailure


from ffire.constants import EVENT_INDEX, PAYLOAD_INDEX, TIME_INTERVALS
from ffire.constants.all import AUTHENTICATION_ENDPOINT, CONSUME_EVENTS_ENDPOINT
from ffire.constants.all import CREATE_EVENT_ENDPOINT, DELETE_EVENT_ENDPOINT
from ffire.constants.all import FIRE_EVENT_ENDPOINT, SUBSCRIBE_EVENT_ENDPOINT

from ffire.exc.failed import AuthenticationError
from ffire.exc.invalid import InvalidInputError, InvalidEndpointError

_configuration = {}
_connection = {}

_session = Session()
_request = Request()


class Fire(object):
    """
    Fire class is the main class

    ffire.core.ffire.Fire
    ~~~~~~~~~~~~~~~~~~~~

    It holds all the major APIs and points of interaction.

    >>> ffire = Fire()
    >>> success_json = {"status": "success", "data": {"key": "value"}}
    >>> failure_json = {"status": "failed", "message": "testing purposes only"}
    >>> malformed_json = {"rice": "and beans"}

    >>> ffire.__init_connection("test-username", "test-password")
    True

    >>> ffire.__get_event_endpoint("abracadabra")
    "events/abracadabra/ffire"

    """

    global _connection

    def __init__(self):
        self.truer = True

    def __call__(self, *args):
        """
        Make the class itself callable, this is done purely for the syntactic sugar
        effect it provides.
        """
        if len(args) == 2:
            event_name = args[EVENT_INDEX]
            payload = args[PAYLOAD_INDEX]
            res = self.event(event_name, payload)
            return res
        else:
            raise InvalidInputError("To ffire an event you must pass in the name and payload message")

    @staticmethod
    def __get_authenticated_request(http_method, url):
        """
        Returns a request object primed with the correct headers for authentication to work

        :return req:        The primed request object to be returned
                            :type <type, 'requests'>
        """
        pass

    @staticmethod
    def __get_event_endpoint(event_name, **filters):
        """
        Builds the restful https api to hit for working with an event

        :param event_name:              The event name to use in replacing format placeholders that
                                        might be present in the api endpoint constant string
                                        :type <type, 'str'>

        :param filters:                 Key value collection of parameters renderable to the api
                                        string endpoint
                                        :type <type, 'dict'>

        :return subscribe_endpoint:     The fully formatted ready to ffire endpoint
                                        :type <type, 'str'>

        """
        return FIRE_EVENT_ENDPOINT.format(event_name=event_name)

    @staticmethod
    def __handle_request_response(response):
        """
        Ensures the request response is resolved appropriately across method calls

        :param response:        The http response to handle and ensure correct resolution
                                :type <type, 'requests.Response'>
        :return:
        """
        if response.status_code == 401:
            raise Exception("Initialize ffire by calling ffire.init(username, password) before usage")
        if str(response.status_code).startswith('20') and Fire._is_success(response.json()):
            return True
        return False

    @staticmethod
    def __init_connection(username=None, password=None):
        """
        Initialize the connections necessary to use ffire for communication with
        necessary backing system.

        :param username:        The username that uniquely identifies and qualifies this
                                client
                                :type <type, 'str'>

        :param password:        The password used to qualify the username
                                :type <type, 'str'>

        :return status:         Boolean value stating the result of the operation
                                :type <type, 'bool'>
        """
        global _configuration
        #: content validation has been performed before invoking this private method
        authentication_json = {"username": username, "password": password}
        try:
            response = requests.post(AUTHENTICATION_ENDPOINT, json=authentication_json)
        except ConnectionError:
            return False
        else:
            if response.status_code == 200:
                json_response = response.json()
                _configuration["Authentication-Token"] = json_response.get("token")
                _configuration["Authentication-Key"] = json_response.get("key")
                _configuration['initialized'] = True

                global _session
                _session.headers.update(_configuration)
                return True
            return False

    @staticmethod
    def _get_auth_credentials():
        global _configuration
        return _configuration

    @staticmethod
    def _is_initialized():
        global _configuration
        initialized = _configuration.get('initialized', False)
        return initialized

    @staticmethod
    def _is_success(json_payload):
        """
        Returns the status of the response  based on the json content of the response

        :param json_payload:    The json payload to test for a truth value content
                                :type <type, 'dict'>
        :return:
        """
        validity = True if json_payload.get("status") == "success" else False
        return validity

    @staticmethod
    def _is_sendable(payload):
        return isinstance(payload, (int, str, dict))

    @staticmethod
    def all():
        """
        List all the events that have been created within the current session
        :return:
        """
        pass

    @staticmethod
    def create(event_name, category='event', protected=True):
        """
        Create ubiquitous Ffire artifacts, from events to hooks. Events are straightforward and
        need no explanation.

        Hooks are logic proxies, sent to the ffire server. Whenever they are invoked they perform
        a preset functionality and return data, making them almost similar to cron jobs.
        This makes it easy to expose and conceal functionality by creating a hook and deleting
        it when no longer needed, or even changing the function that fulfills the hook.

        :param event_name:              The name to give to the created artifact for identification
                                        within the ffire event server.
                                        :type <type, 'str'>

        :param category:                The type of artifact to create within the ffire events
                                        server.
                                        :type <type, 'str'>

        :param protected:               Protect this artifact from being recreated in another
                                        location.
                                        :type <type, 'bool'>
        :return:
        """
        endpoint_url = CREATE_EVENT_ENDPOINT
        try:
            response = _session.post(endpoint_url, json={"event_name": event_name})
        except ConnectionError:
            print 'No internet connection'
        else:
            valid = Fire.__handle_request_response(response)
            return valid
        return False

    @staticmethod
    def consume(event_name, endpoint, time_interval=TIME_INTERVALS.ONE_HOUR, paginate=None):
        """
        Fetch all events that have occurred within the duration of the :param `type_interval`

        :param event_name:              The name of the event to limit the consumption to
                                        :type <type, 'str'>

        :param endpoint:                The endpoint that will receive the resent messages,
                                        Ideally this should represent only endpoints that were down
                                        during the time interval and as such missed ffired events
                                        :type <type, 'str'>

        :param time_interval:           The time interval to use to limit or filter out events
                                        not interested in consuming.
                                        :type <type, 'ffire.constants.time_interval.TIME_INTERVALS'>

        :param paginate:                The amount of items to fetch or return if the amount of events
                                        within the interval are numerous and pagination is desired.

        :return events_collection:      Collection of event payloads that occurred within the specified
                                        interval.
                                        :type <type, 'list'>
        """
        endpoint_url = CONSUME_EVENTS_ENDPOINT.format(event_name=event_name, interval=time_interval)
        try:
            validators.url(endpoint_url)
        except ValidationFailure:
            raise InvalidEndpointError()

        try:
            response = _session.post(endpoint_url, json={"event_name": event_name, "endpoint": endpoint})
        except ConnectionError:
            print 'No internet connection'
        else:
            return response.status_code == 200 or False

    @staticmethod
    def delete(event_name, drop_messages=False):
        endpoint_url = DELETE_EVENT_ENDPOINT.format(event_name=event_name)
        try:
            response = _session.delete(endpoint_url, json={"event_name": event_name})
        except ConnectionError:
            print 'No internet connection'
        else:
            return response.status_code == 204 or False

    @staticmethod
    def event(event_name, payload):
        """
        Default method for firing or raising an event. This is the actual and only implementation
        of event firing.
        Ffire __call__ magic method acts as a proxy and hooks into this method to raise events.

        :param event_name:          The name of the event to raise, prior to an event being raised it
                                    expects that it has been created.
                                    Failure to create an event before firing it will raise an error.
                                    Ideally the only services that should ffire events are the ones that
                                    registered the events in the first place.
                                    In Essence it is considered good practice to ffire only the events
                                    you raise.
                                    :type <type, 'str'>

        :param payload:             The payload or message body to send to all parties that have subscribed
                                    to the event.
                                    Defaults to a dict but can be any valid python type that can be pickled.
                                    :type <type, 'dict'>
        :return:
        """
        endpoint_url = Fire.__get_event_endpoint(event_name)
        if Fire._is_sendable(payload):
            try:
                response = _session.post(endpoint_url, json={"payload": payload})
                if response.status_code == 401:
                    raise Exception("Initialize ffire by calling ffire.init(username, password) before usage")
                if response.status_code == 200 and Fire._is_success(response.json()):
                    return True
            except ConnectionError:
                print 'No Internet Connection'
        return False

    @staticmethod
    def fire(event_name, payload):
        """
        Proxy method for firing event, uses the internal event implementation and exists
        solely as syntactic sugar for those that want an easy to remember method call

        :param event_name:      The name of the event that is to be fired, must have been prior
                                created.
                                :type <type, 'str'>

        :param payload:         The payload to fire with the event
                                :type <type, 'dict'>

        :return:
        """
        res = Fire.event(event_name, payload)
        return res

    def init(self, username=None, password=None, configuration=None):
        """
        Initializes ffire for use by authenticating with the ffire io platform and priming for communication.

        :param configuration:                   The configuration to use for the initialization of the ffire
                                                library.
                                                :type <type, 'ffire.core.configuration.Configuration'>

        :param username:                        The usename to use in authentication for all ffire actions
                                                :type <type, 'str'>

        :param password:                        The access qualifier credential to use in validation of token
                                                :type <type, 'str'>

        :return initialized:                    Status of the initialization call
                                                :type <type, 'bool'>
        """
        if username and password:
            return self.__init_connection(username, password)
        return False

    @staticmethod
    def subscribe(event_name, endpoint):
        """
        Subscribe to the event specified in the :param `event_name` by providing an endpoint to receive
        messages whenever the event is fired.

        :param event_name:                  The event to subscribe to. Event names are unique within a ffire
                                            server.
                                            :type <type, 'str'>

        :param endpoint:                    The endpoint that will receive messages whenever the event is fired or
                                            raised. Ffire assumes that a handler or broker exists at that endpoint.
                                            Ideally this endpoint should be a broker, however this is not mandatory
                                            especially in scenarios where the processing of the event is not of
                                            extreme importance and lost messages are tolerable.
                                            :type <type, 'str'>

        :return:
        """
        endpoint_url = SUBSCRIBE_EVENT_ENDPOINT.format(event_name=event_name)
        try:
            validators.url(endpoint)
        except ValidationFailure:
            raise InvalidEndpointError()

        try:
            response = _session.post(endpoint_url, json={"endpoint": endpoint})
        except ConnectionError:
            print 'No internet connection'
        else:
            valid = Fire.__handle_request_response(response)
            return valid
        return False
