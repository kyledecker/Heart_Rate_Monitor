#####################################################################

This is a software package that takes in Multi-plexed ECG & PP data
and performs heart rate monitoring on the data. The elapsed
signal time, instant HR, 1 minute average HR, and 5 minute average HR
will be displayed to the terminal window. In addition if conditions
of bradycardia or tachycardia an alarm will be displayed on the 
terminal and the software will return a plot of the 10 minute
trace for inspection. 

####################################################################

Kyle Decker
BME 590
Fall 2016

####################################################################

The only dependencies outside of having anaconda installed is
a peak detection utility (PeakUtils 1.0.3) availabile via pip.

    pip install peakutils

Author of PeakUtils 1.0.3 : Lucas Hermann Negri

####################################################################

The program can be called from the command line with a
call such as:

    ipython heart_rate_monitor.py filename

In the command line call filename should be the name of the
file containing the heart rate data (i.e. example_data.bin)

####################################################################

License for this software is under MIT License- please see LICENSE.txt
