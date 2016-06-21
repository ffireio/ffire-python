"""
Holds Time Interval Constants

ffire.constants.time_intervals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Time interval constants are concerned with declaring reusable
ways to specify and quantify elapsed time.
"""
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict


TIME_INTERVALS = OrderedDict()

TIME_INTERVALS.ONE_HOUR = 60 * 60
TIME_INTERVALS.TWO_HOURS = TIME_INTERVALS.ONE_HOUR * 2
