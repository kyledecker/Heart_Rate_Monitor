def test_proc_hr():
    import os.path
    import sys 
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    from proc_hr import proc_hr
    import numpy as np
    import os

    # Test Boxcar Averager 
    HR_proc_data = np.array([70,71,72,73,74])
    inst_HR = 65
    brady_thresh = 30
    tachy_thresh = 240
    HR_proc_data_new = proc_hr(inst_HR,HR_proc_data,brady_thresh,tachy_thresh)
    assert np.array_equal(HR_proc_data_new,[65,70,71,72,73])


    # Test case where Bradycardia occurs
    HR_proc_data = np.array([70,71,72,73,74])
    inst_HR = 15
    brady_thresh = 30
    tachy_thresh = 240
    HR_proc_data_new = proc_hr(inst_HR,HR_proc_data,brady_thresh,tachy_thresh)
    assert np.array_equal(HR_proc_data_new,[15,70,71,72,73])
    assert (os.path.isfile('ALARM.txt')==True)
    os.system("rm ALARM.txt")
