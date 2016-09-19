def read_binary(filename,offset):
    """ read in raw data from binary file

    :param filename: name of binary file
    :param offset: offset for reading
    :returns: fs(sampling frequency), ECG data (np.array), and PP data (np.array)
    """

    import numpy as np
    import os
    f = open(filename)
    f.seek(offset,os.SEEK_SET)
    data = np.fromfile(f,dtype='uint16')
    return(data)
