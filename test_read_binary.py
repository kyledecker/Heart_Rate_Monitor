def test_read_binary():
    from read_binary import read_binary
    import os
    import numpy as np
    
    # Make tmp binary file and save
    f = open('tmp.bin','wb')
    x = np.uint16(np.array([2,3]))
    f.write(x)
    f.close()
    in_read = read_binary('tmp.bin',0)
    os.system('rm tmp.bin')
    assert np.array_equal(in_read,[2,3]) 
