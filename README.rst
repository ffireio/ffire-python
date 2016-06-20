FFIRE
=====

Ffire enables you to use GUI Style event driven programming in your web application with
10 lines of code or less.

ffire can be summed up by its simple API.

Installation
++++++++++++

.. code:: shell

    pip install ffire



Creating and Firing Events
++++++++++++++++++++++++++

.. code:: python

    #: Order Creation API/Engine : Application One (France or Germany or Mars)
    from ffire import fire

    #: Create is idempotent. You can call create multiple times without side effects
    #: in addition it is more advisable to use constants i.e. ORDER_CREATED not literals

    ffire.create('order_created', category='event')


    #: Do application logic here

    payload = {"order_id": "abcd", "client_id": "1234"}

    ffire('order_created', payload)
    #: OR
    ffire.fire('order_created', payload)


Subscribing to events
+++++++++++++++++++++

.. code:: python


    # # Biryani Client : Application Two in (Brazil, South Africa or Venus)

    from ffire import fire

    endpoint = 'http://api.example.com/order-created-handler'

    fire.subscribe('order_created', endpoint)

    #: Ffire assumes a handler for the payload sits at that endpoint.

- It is advisable to have a message broker as the endpoint. However this is not mandatory especially for cases where handling the event is not an absolute necessity.

- In such scenarios any endpoint is sufficient.


Consume Events
++++++++++++++

If you wish to consume events from ffire explicitly you can do so.

.. code:: python

    from ffire import ffire

    fire.consume('order_created', ffire.TIME_INTERVALS.ONE_HOUR)
