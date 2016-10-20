def proc_hr(inst_HR,HR_proc_data,brady_thresh,tachy_thresh,plt_flag):
    """ Estimate HR from ECG and PP data

    :param inst_HR: inst HR estimated for given time interval
    :param HR_proc_data: numpy array of 10 minute HR data
    :param brady_thresh: Threshold for Bradycardia
    :param tachy_thresh: Threshold for Tachycardia
    :param plt_flag: Flag to plot trace (1) or not (0)
    :returns: HP_proc_data, return the data with new timepoint added, oldest dropped
    """

    import numpy as np
    import matplotlib.pyplot as plt
    import os

    # Roll the data by one point and replace the first element (replacing oldest sample w/ new)
    HR_proc_data = np.roll(HR_proc_data,1)
    HR_proc_data[0] = inst_HR
    
    # Predefined variables
    trace_time = 10
    tachy_limit = tachy_thresh
    brady_limit = brady_thresh

    # Check for tachycardia
    if (inst_HR > tachy_limit):
        print("ALARM: Subject is in state of Tachycardia with heart rate of %d bpm" % (inst_HR))
        time_index = np.linspace(0,trace_time,len(HR_proc_data))
        if (plt_flag != 0):
            plt.plot(time_index,HR_proc_data[::-1]) # Plot data (flip order to make sense)
            plt.title("10 Minute Trace of Heart Rate")
            plt.xlabel("Time (minutes)")
            plt.ylabel("Heart Rate (BPM)")
            plt.show(block=True)
        os.system("echo 'An Alarm was triggered indicating tachycardia' > ALARM.txt")

    # Check for bradycardia
    if (inst_HR < brady_limit):
        print("ALARM: Subject is in state of Bradycardia with heart rate of %d bpm" % (inst_HR))
        time_index = np.linspace(0,trace_time,len(HR_proc_data))
        if (plt_flag != 0):
            plt.plot(time_index,HR_proc_data[::-1]) # Plot data (flip order to make sense)
            plt.title("10 Minute Trace of Heart Rate")
            plt.xlabel("Time (minutes)")
            plt.ylabel("Heart Rate (BPM)")
            plt.show(block=True)
        os.system("echo 'An Alarm was triggered indicating bradycardia' > ALARM.txt")
    
    return(HR_proc_data)
