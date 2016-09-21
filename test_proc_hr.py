def test_proc_hr():
    from proc_hr import proc_hr
    import os
    import numpy as np
    
    # Test Boxcar Averager for 10 minute data
    assert np.array_equal(data,[2,3])


    # Test case where there is not sufficient data for averages (<1min elapsed)
    assert np.array_equal(data_info[1],2*4)
