def read_binary(filename,offset,count_read,init_flag):
    """ read in raw data from binary file

    :param filename: name of binary file
    :param offset: offset for reading
    :param count_read: determines how many data points to read
    :param init_flag: init_flag == 1 simply determines fs and file size
    :returns: fs(sampling frequency), ECG data (np.array), and PP data (np.array)
    """

    import numpy as np
    import os

    if (init_flag == 1):
        f = open(filename)
        # Read in the first number which is the frequency in Hz
        fs = np.fromfile(f,dtype='uint16',count=1)
        # Determine the file size in bytes (1 byte = 8 bits)
        file_size = os.path.getsize(filename)
        return(np.array([fs,file_size]))
    else:
        f = open(filename)
        f.seek(offset,os.SEEK_SET)
        data = np.fromfile(f,dtype='uint16',count=count_read)
        return(data)
