"""
Holds Time Interval Constants

ffire.constants.time_intervals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Time interval constants are concerned with declaring reusable
ways to specify and quantify elapsed time.
"""
from collections import OrderedDict


TIME_INTERVALS = OrderedDict()

TIME_INTERVALS.ONE_HOUR = 60 * 60
TIME_INTERVALS.TWO_HOURS = TIME_INTERVALS.ONE_HOUR * 2
