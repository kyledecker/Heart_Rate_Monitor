def read_binary(filename,offset,count_read,init_flag):
    """ read in raw data from binary file

    :param filename: name of binary file
    :param offset: offset for reading
    :param count_read: determines how many data points to read
    :param init_flag: init_flag == 1 simply determines fs and file size
    :returns: fs(sampling frequency) and file_size (in bytes) if init_flag == 1
    :returns: ECG and PP data (single np.array) if init_flag == 0
    """

    import numpy as np
    import os

    if (init_flag == 1):
        f = open(filename)
        # Read in the first number which is the frequency in Hz
        tmp = np.fromfile(f,dtype='uint16',count=count_read)
        fs = tmp[0]
        # Determine the file size in bytes (1 byte = 8 bits)
        file_size = os.path.getsize(filename)
        data_info = np.array([file_size,fs])
        return(data_info)
    else:
        f = open(filename)
        f.seek(offset,os.SEEK_SET)
        data = np.fromfile(f,dtype='uint16',count=count_read)
        # If any Nan's are present, convert to 0
        data = np.nan_to_num(data)
        return(data)
