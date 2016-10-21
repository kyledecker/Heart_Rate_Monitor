def test_read_hdf5():
    import os.path
    import sys
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    from read_hdf5 import read_hdf5
    import os
    import numpy as np
    import h5py
    
    # Make tmp mat file and save
    fs = np.uint16(np.array([100]))
    ecg = np.uint16(np.array([2,3]))
    pp = np.uint16(np.array([4,5]))
    f = h5py.File('tmp.h5', 'w')
    f.create_dataset('fs',data=fs)
    f.create_dataset('ecg',data=ecg)
    f.create_dataset('pp',data=pp)
    f.close()
    data = read_hdf5('tmp.h5',offset=0,count_read=4,init_flag=0)
    os.system('rm tmp.h5')
    assert np.array_equal(data,[2,4,3,5])

    # Make tmp mat file and save
    fs = np.uint16(np.array([100]))
    ecg = np.uint16(np.array([2,3]))
    pp = np.uint16(np.array([4,5]))
    f = h5py.File('tmp.h5', 'w')
    f.create_dataset('fs',data=fs)
    f.create_dataset('ecg',data=ecg)
    f.create_dataset('pp',data=pp)
    f.close()
    data_info = read_hdf5('tmp.h5',offset=0,count_read=2,init_flag=1)
    os.system('rm tmp.h5')
    assert np.array_equal(data_info,[5*2,100])
