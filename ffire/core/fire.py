"""
Fire module

ffire.core.fire
~~~~~~~~~~~~~~~

Some names say everything.
"""
from ffire.constants import EVENT_INDEX, PAYLOAD_INDEX, TIME_INTERVALS
from ffire.exc.invalid import InvalidInputError


class Fire(object):
    """
    Fire class is the main class

    ffire.core.fire.Fire
    ~~~~~~~~~~~~~~~~~~~~

    It holds all the major APIs and points of interaction.
    """

    def __call__(self, *args):
        """
        Make the class itself callable, this is done purely for the syntactic sugar
        effect it provides.
        """
        if len(args) == 3:
            event_name = args[EVENT_INDEX]
            payload = args[PAYLOAD_INDEX]

            self.event(event_name, payload)
        else:
            raise InvalidInputError("To fire an event you must pass in the name and payload message")

    @staticmethod
    def all():
        """
        List all the events that have been created within the fire server
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
        pass

    @staticmethod
    def consume(event_name, time_interval=TIME_INTERVALS.ONE_HOUR, paginate=None):
        """
        Fetch all events that have occured within the duration of the :param `type_interval`

        :param event_name:              The name of the event to limit the consumption to
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
        pass

    @staticmethod
    def delete(event_name, drop_messages=False):
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
                                    Ideally the only services that should fire events are the ones that
                                    registered the events in the first place.
                                    In Essence it is considered good practice to fire only the events
                                    you raise.
                                    :type <type, 'str'>

        :param payload:             The payload or message body to send to all parties that have subscribed
                                    to the event.
                                    Defaults to a dict but can be any valid python type that can be pickled.
                                    :type <type, 'dict'>
        :return:
        """
        pass

    @staticmethod
    def init(broker, configuration=None, host=None, port=None, username=None, password=None):
        """
        Initializes ffire for use. If no other parameter is passed in with the mandatory :param `broker_type`
        parameter then ffire assumes the broker is configured on localhost and as such tries to create
        the events on the same machine.

        :param broker:                          The broker to use as the underlying technology for creating,
                                                subscribing to, and firing events.
                                                Currently only RABBIT MQ, and SQS - SNS Combo is supported.
                                                :type <type, 'str'>

        :param configuration:                   The configuration to use for the initialization of the ffire
                                                library.
                                                :type <type, 'ffire.core.configuration.Configuration'>

        :param host:                            The host name or computer name upon which the underlying
                                                broker or technology resides.

        :param port:                            The port to which to forward all communications targeted at
                                                the underlying broker, technology.

        :param username:                        The username credential to use in authentication and authorized
                                                access restriction broker operations. (If applicable)

        :param password:                        The password credential to use in validation and authorization of
                                                access restriction broker operations.

        :return:
        """
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
        pass
