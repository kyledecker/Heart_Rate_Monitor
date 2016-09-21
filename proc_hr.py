def proc_hr(inst_HR,HR_proc_data):
    """ Estimate HR from ECG and PP data

    :param inst_HR: inst HR estimated for given time interval
    :param HR_proc_data: numpy array of 10 minute HR data 
    :returns: HP_proc_data, return the data with new timepoint added, oldest dropped
    """

    import numpy as np
    import os

    
