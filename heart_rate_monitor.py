
if len(sys.argv)<2:
    print('Please specify a filename')
    sys.exit()
else:
    filename = sys.argv[1]
    print('Analyzing the heart rate of data contained in: %s ...' %filename

if __name__ == "__main__":
    # First attain necessary info (fs, and size) from data                                                                                                                                                                      
    data_info = read_binary(filename,offset=0,count_read=1,init_flag=1)
    fs = data_info[0]
    file_size = data_info[1]

    # Read in 10 seconds of data at a time until end of file
    
    # Take in 10 seconds of ECG and PP data at a time, estimate inst. HR
    est_hr()

    # Take in new inst. HR, drop old if it exists
    # Add new inst. HR to 1 minute data, drop oldest if exists
    # Add new inst. HR to 5 minute data, drop oldest if exists
    # Add new inst. HR to 10 minute data, drop oldest if exists
    # Check for too high / too low heart rate
    proc_hr()

    # Keep track of elapsed time
    # Update inst. HR every 10 seconds
    # Update 1, and 5 minute avg every 10 seconds if exists
    # If alarm occurs, output 10 minute trace
    gen_output()
