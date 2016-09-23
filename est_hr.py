def est_hr(ECG_data,PP_data,delta_t):
    """ Estimate HR from ECG and PP data

    :param ECG_data: numpy array of ECG data for given time interval
    :param PP_data: numpy array of PP data for given time interval 
    :param delta_t: time spacing between samples 
    :returns: inst_HR (estimate of HR from given time interval)
    """

    import numpy as np
    import peakutils
    from scipy import signal
    
    # Predefined variable
    max_HR = 400
    conversion = 60 # 60 seconds = 1 minute

    # Find the peaks using a percentile threshold and min_dist
    pk_dist = (conversion/max_HR)/delta_t# Define the min distance between peaks - HR will not go over 400 bpm
    signal_comb = ECG_data*PP_data
    signal_comb.astype(int)
    thresh_val = 0.5
    peak_ind = peakutils.indexes(signal_comb,thres=thresh_val,min_dist = pk_dist)
    peak_separation = np.diff(peak_ind) # Find separation between peak indices
    inst_HR = (1/(np.mean(peak_separation)*delta_t))*60 # Find Frequency and convert to bpm
    return(inst_HR)
