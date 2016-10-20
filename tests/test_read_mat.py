def test_read_mat():
    import os.path
    import sys
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    from read_mat import read_mat
    import os
    import numpy as np
    from scipy.io import loadmat
    from scipy.io import savemat
    
    # Make tmp mat file and save
    fs = np.uint16(np.array([100]))
    ecg = np.uint16(np.array([2,3]))
    pp = np.uint16(np.array([4,5]))
    savemat('tmp.mat',{'fs':fs, 'ecg':ecg, 'pp':pp})
    data = read_mat('tmp.mat',offset=0,count_read=4,init_flag=0)
    os.system('rm tmp.mat')
    assert np.array_equal(data,[2,4,3,5])

    # Make tmp mat file and save
    fs = np.uint16(np.array([100]))
    ecg = np.uint16(np.array([2,3]))
    pp = np.uint16(np.array([4,5]))
    savemat('tmp.mat',{'fs':fs, 'ecg':ecg, 'pp':pp})
    data_info = read_mat('tmp.mat',offset=0,count_read=2,init_flag=1)
    os.system('rm tmp.mat')
    assert np.array_equal(data_info,[5*2,100])
