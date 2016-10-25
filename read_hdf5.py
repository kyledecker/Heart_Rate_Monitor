def read_hdf5(filename, offset, count_read, init_flag):
    """ read in raw data from hdf5 file

    :param filename: name of hdf5 file
    :param offset: offset for reading
    :param count_read: determines how many data points to read
    :param init_flag: init_flag == 1 simply determines fs and file size
    :returns: fs(sampling frequency) and file_size (in bytes) if init_flag == 1
    :returns: ECG and PP data (single np.array) if init_flag == 0
    """

    import numpy as np
    import os
    import sys
    import h5py
    import logging

    sample_size = 2*2

    if (init_flag == 1):
        logging.debug('Reading hdf5 file with init_flag == 1')
        f = h5py.File(filename)
        # Read in the frequency in Hz
        fs = np.squeeze(np.array(f.get('fs')))
        ecg = np.squeeze(np.array(f.get('ecg')))
        pp = np.squeeze(np.array(f.get('pp')))
        # Determine the file size in bytes (1 byte = 8 bits)
        file_size = (1+len(ecg)+len(pp))*2
        data_info = np.array([file_size, fs])
        return(data_info)
    else:
        logging.debug('Reading hdf5 file with init_flag == 0')
        # Adjust the offset
        offset = int(offset/sample_size)
        try:
            f = h5py.File(filename)
            ecg = np.squeeze(np.array(f.get('ecg')))
            pp = np.squeeze(np.array(f.get('pp')))
            ecg_data = ecg[offset:offset+count_read]
            pp_data = pp[offset:offset+count_read]
            data = np.zeros(len(ecg_data) + len(pp_data))
            data[0::2] = ecg_data
            data[1::2] = pp_data

            # plt.plot(ecg)
            # plt.show(block=True)
        except EOFError:
            logging.error('Reached end of input file, can not read another '
                          'block')
            print('Finished processing all data...')
            print('Heart Rate Monitor Finished')
            sys.exit()
        # If any Nan's are present, convert to 0
        data = np.nan_to_num(data)
        return(data)
