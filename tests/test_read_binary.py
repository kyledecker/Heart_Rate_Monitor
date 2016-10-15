def test_read_binary():
    import os.path
    import sys
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    from read_binary import read_binary
    import os
    import numpy as np
    
    # Make tmp binary file and save
    f = open('tmp.bin','wb')
    x = np.uint16(np.array([2,3]))
    f.write(x)
    f.close()
    data = read_binary('tmp.bin',offset=0,count_read=2,init_flag=0)
    os.system('rm tmp.bin')
    assert np.array_equal(data,[2,3])


    # Make tmp binary file and save
    f = open('tmp.bin','wb')
    x = np.uint16(np.array([5000,300,200,100]))
    f.write(x)
    f.close()
    data_info = read_binary('tmp.bin',offset=0,count_read=1,init_flag=1)
    os.system('rm tmp.bin')
    assert np.array_equal(data_info[1],5000) 
    assert np.array_equal(data_info[0],2*4)

    # Make tmp binary file with Nan's and save
    # If encountering a Nan value, should replace with 0
    f = open('tmp.bin','wb')
    x = np.uint16(np.array([2,3,4,np.nan,5,6,7,8]))
    f.write(x)
    f.close()
    data = read_binary('tmp.bin',offset=0,count_read=8,init_flag=0)
    os.system('rm tmp.bin')
    assert np.array_equal(data,[2,3,4,0,5,6,7,8])
