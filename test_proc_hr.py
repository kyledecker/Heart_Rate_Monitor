def test_proc_hr():
    from proc_hr import proc_hr
    import numpy as np
    import os

    # Test Boxcar Averager 
    HR_proc_data = np.array([70,71,72,73,74])
    inst_HR = 65
    HR_proc_data_new = proc_hr(inst_HR,HR_proc_data)
    assert np.array_equal(HR_proc_data_new,[65,70,71,72,73])


    # Test case where Bradycardia occurs
    HR_proc_data = np.array([70,71,72,73,74])
    inst_HR = 15
    HR_proc_data_new = proc_hr(inst_HR,HR_proc_data)
    assert np.array_equal(HR_proc_data_new,[15,70,71,72,73])
    assert (os.path.isfile('ALARM.txt')==True)
    os.system("rm ALARM.txt")
