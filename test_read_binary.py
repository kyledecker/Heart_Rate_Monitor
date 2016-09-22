def test_read_binary():
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
    assert np.array_equal(data_info[0],[5000]) 
    assert np.array_equal(data_info[1],2*4)
