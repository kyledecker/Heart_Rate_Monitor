
if __name__ == "__main__":
    
    if (len(sys.argv)<2):
        print('Please specify a filename')
        sys.exit()
    else:
        filename = sys.argv[1]
        print('Analyzing the heart rate of data contained in: %s ...' %filename)
        
    import numpy as np
    # First attain necessary info (fs and size) from data                                                                                                                                              
    data_info = read_binary(filename,offset=0,count_read=1,init_flag=1)
    fs = data_info[0]
    file_size = data_info[1]

    # Define Amount of time to read in at once (10 seconds)
    time_var = 10
    num_samples = fs*time_var
    sample_size = 2*2 #2 bytes per sample assuming uint16, 2 samples (1 ECG, 1 PP)
    HR_proc_data = np.zeros(num_samples*10*60/time_var) #Preallocate 10 minute trace

    # Read in defined amount of time of data until end of file
    buffer = sample_size
    while (buffer<file_size):
        data = read_binary(filename,offset=buffer,count_read=num_samples,init_flag=0)
        ECG_data = data[0::2]
        PP_data = data[1::2]
        buffer = buffer + num_samples*sample_size

        # Take in defined time of ECG and PP data at a time, estimate inst. HR
       inst_HR =  est_hr(ECG_data,PP_data,delta_t = (1/fs))

        # Check for too high / too low heart rate
        HR_proc_data = proc_hr(inst_HR,HR_proc_data)

        # Keep track of elapsed time
        # Update inst. HR every 10 seconds
        # Update 1, and 5 minute avg every 10 seconds if exists
        # If alarm occurs, output 10 minute trace
        gen_output()
