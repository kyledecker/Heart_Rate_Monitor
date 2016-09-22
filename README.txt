This is a software package that takes in Multi-plexed ECG & PP data
and performs heart rate monitoring on the data. The elapsed
signal time, instant HR, 1 minute average HR, and 5 minute average HR
will be displayed to the terminal window. In addition if conditions
of bradycardia or tachycardia an alarm will be displayed on the 
terminal and the software will return a plot of the 10 minute
trace for inspection. 

The program can be claaed from the command line with a
call such as:

ipython heart_rate_monitor.py filename

in the command line call filename should be the name of the
file containing the heart rate data (i.e. example_data.bin)
