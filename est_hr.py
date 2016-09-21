def est_hr(ECG_data,PP_data,delta_t):
    """ Estimate HR from ECG and PP data

    :param ECG_data: numpy array of ECG data for given time interval
    :param PP_data: numpy array of PP data for given time interval 
    :param delta_t: time spacing between samples 
    :returns: inst_HR (estimate of HR from given time interval)
    """

    import numpy as np
    import os

    
