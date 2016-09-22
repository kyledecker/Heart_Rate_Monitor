
if __name__ == "__main__":
    
    if (len(sys.argv)<2):
        print('Please specify a filename')
        sys.exit()
    else:
        filename = sys.argv[1]
        print('Analyzing the heart rate of data contained in: %s ...' %filename)
        
    import numpy as np
    import time
    import sys
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
    total_elapsed_time = 0
    while (buffer<file_size):
        start_time = time.time() 
        data = read_binary(filename,offset=buffer,count_read=num_samples,init_flag=0)
        ECG_data = data[0::2]
        PP_data = data[1::2]
        buffer = buffer + num_samples*sample_size

        # Take in defined time of ECG and PP data at a time, estimate inst. HR
       inst_HR =  est_hr(ECG_data,PP_data,delta_t = (1/fs))

        # Check for too high / too low heart rate
        HR_proc_data = proc_hr(inst_HR,HR_proc_data)
        # Get 1 minute average
        HR_avg_1min = np.mean(HR_proc_data[0:(1*60/time_var)])
        #Get 5 minute average
        HR_avg_5min = np.mean(HR_proc_data[0:(5*60/time_var)])
        # Keep track of elapsed time
        elapsed_time = time.time() - start_time
        total_elapsed_time = total_elapsed_time + elapsed_time
        if (elapsed_time>10):
            print("Elapsed Time: %d seconds \n" % total_elapsed_time)
            print("Current Heart Rate = %d bpm \n" % inst_HR)
            if (total_elapsed_time>60):
                print("1 Minute Average Heart Rate = %d bpm \n" % HR_avg_1min)
                print("5 Minute Average Heart Rate = %d bpm \n" % HR_avg_5min)

print("Reached the end of the data...")
sys.exit()
