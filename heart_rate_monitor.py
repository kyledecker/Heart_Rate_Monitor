
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
    import math
    # First attain necessary info (fs and size) from data, as well as first 10 seconds                                                                                                                                              
    data_info = read_binary(filename,offset=0,count_read=(1+2*fs*10),init_flag=1)
    file_size = data_info[0]
    fs = data_info[1]
    start_data = data_info[2:]

    # Define Amount of time to read in at once (1 second)
    time_var = 1
    num_samples = fs*time_var
    sample_size = 2*2 #2 bytes per sample assuming uint16, 2 samples (1 ECG, 1 PP)
    HR_proc_data = np.zeros(num_samples*10*60/time_var) #Preallocate 10 minute trace
    HR_proc_data[0:len(start_data)] = start_data
    
    ECG_data = HR_proc_data[0::2]
    PP_data = HR_proc_data[1::2]

    # Read in defined amount of time of data until end of file
    buffer = sample_size + sample_size*fs*10
    total_elapsed_time = 0
    while (buffer<file_size):
        start_time = time.time() #Start time for counter
        data = read_binary(filename,offset=buffer,count_read=num_samples,init_flag=0)
        
        new_ecg = data[0::2]
        new_pp = data[1::2]

        # Replace old data with new in 10 second array
        ECG_data = np.roll(ECG_data,len(new_ecg))
        ECG_data[0:len(new_ecg)] = new_ecg
        PP_data = np.roll(PP_data,len(new_pp))
        PP_data[0:len(new_pp)] = new_pp
        # Adjust the buffer to determine the offset
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
        
        if (elapsed_time<time_var):
            time.sleep(time_var-elapsed_time) # Delay required time
        os.system("clear")
        print("Elapsed Time: %d seconds" % int(math.down(total_elapsed_time/10))*10 ) # Round 
        print("Current Heart Rate = %d bpm" % inst_HR)
        if (total_elapsed_time>60):
            print("1 Minute Average Heart Rate = %d bpm" % HR_avg_1min)
            if (total_elapsed_time>(60*5)):
                print("5 Minute Average Heart Rate = %d bpm" % HR_avg_5min)
            
print("Reached the end of the data...")
sys.exit()
