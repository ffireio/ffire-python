"""
Fire module

ffire.core.fire
~~~~~~~~~~~~~~~

Some names say everything.
"""
import requests


from ffire.constants import EVENT_INDEX, PAYLOAD_INDEX, TIME_INTERVALS
from ffire.exc.invalid import InvalidInputError


_configuration = {}
_connection = {}


class Fire(object):
    """
    Fire class is the main class

    ffire.core.ffire.Fire
    ~~~~~~~~~~~~~~~~~~~~

    It holds all the major APIs and points of interaction.
    """

    global _connection

    def __call__(self, *args):
        """
        Make the class itself callable, this is done purely for the syntactic sugar
        effect it provides.
        """
        if len(args) == 2:
            import pdb; pdb.set_trace()
            event_name = args[EVENT_INDEX]
            payload = args[PAYLOAD_INDEX]
            self.event(event_name, payload)
        else:
            raise InvalidInputError("To ffire an event you must pass in the name and payload message")

    @staticmethod
    def all():
        """
        List all the events that have been created within the current session
        :return:
        """
        print __file__

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
        #: query the api endpoint for the existence of the event in the clients event pool
        #: if it already exists raise an error or exception
        #: if it does not create the event and return True
        #: requests.post(create_event_endpoint, {"event_name": event_name}
        pass

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
        #: send a request to the ffire api endpoint and get json response on status
        #: if success it means that such an event exists and the payload from that interval has been sent
        pass

    @staticmethod
    def delete(event_name, drop_messages=False):
        #: shoot to ffire api and sit back and eat cake
        pass

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
        #: validate that the payload is not empty, a payload MUST never be empty or else what's the point
        #: if is not empty then automatically encode to json
        #: send the payload to the event ffiring api endpoint
        print "%r Event Ffired" % event_name
        return False

    @staticmethod
    def init(username=None, password=None, configuration=None):
        """
        Initializes ffire for use. If no other parameter is passed in with the mandatory :param `broker_type`
        parameter then ffire assumes the broker is configured on localhost and as such tries to create
        the events on the same machine.

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
        #: was a config provided? use it or dump it and continue
        #: send the credentials to the ffire authentication init endpoint and process the response
        pass

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
        #: slight endpoint validation
        #: shoot to ffire api and process results
        pass


def __init_connection(username=None, password=None):
    """
    Initialize the connections necessary to use ffire for communication with
    necessary brokers and backing systems.

    :param username:        The username that uniquely identifies and qualifies this
                            client
                            :type <type, 'str'>

    :param password:        The password used to qualify the username
                            :type <type, 'str'>

    :return status:         Boolean value stating the result of the operation
                            :type <type, 'bool'>
    """
    global _configuration
    global _connection

    if _configuration.get('config'):
        #: do the configuration initialization here
        config = {
            'username': username,
            'password': password,
        }
        #: add the authentication token and key to the request headers
        authentication_credentials = requests.post('', {})
        _connection['username'] = authentication_credentials.get('token')
        _connection['authentication_key'] = authentication_credentials.get('key')
        _configuration['config'] = config
    return _configuration.get('config')


def __get_authentication_endpoint():
    """
    Returns properly built authentication endpoint

    :return authentication_endpoint:    The fully formatted ready to ffire endpoint for
                                        authentication on the ffire api.
                                        :type <type, 'str'>
    """
    pass


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
    pass
