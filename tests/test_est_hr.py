def test_est_hr():
    import os.path
    import sys
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    from est_hr import est_hr
    import peakutils
    import numpy as np
    
    # Simulate Data with Peaks and Noise
    # Assume 75 bpm -> 1.25/second
    delta_t = 0.01 # seconds
    signal_choice = 3 # Both ECG and PP combined
    x = np.linspace(0, 10, 10/delta_t)
    x_ind = np.array(range(len(x)))
    centers = (1/delta_t,1.8/delta_t,2.6/delta_t,3.4/delta_t,4.2/delta_t,5/delta_t,5.8/delta_t,6.6/delta_t)
    
    tmp = np.zeros(len(x_ind))
    for i in range(len(centers)):
        tmp = tmp + (peakutils.gaussian(x_ind, 5, centers[i], 5))
    ECG_data = tmp + np.random.rand(x_ind.size)
    PP_data = tmp + np.random.rand(x_ind.size)

    inst_HR = est_hr(ECG_data,PP_data,delta_t,signal_choice)
    eps = 5 # Range of 5 bpm accepted for accuracy
    assert (inst_HR>(75-eps/2) and inst_HR<(75+eps/2))

    # Robustness Test (handle NaN values)
    #inst_HR = est_hr()
    #assert 
