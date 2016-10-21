def parse_cli():
    """parse CLI                                                                                                                                                                                                  
                                                                                                                                                                                                                  
    :returns: args                                                                                                                                                                                                
    """
    import argparse as ap

    par = ap.ArgumentParser(description="Heart rate monitor for ECG + PP data",
                            formatter_class=ap.ArgumentDefaultsHelpFormatter)

    par.add_argument("--f",
                     dest="f",
                     help="File Name",
                     default='simulated_data.bin')

    par.add_argument("--b",
                     dest="b",
                     help="Threshold for Bradycardia (BPM)",
                     type=int,
                     default=30)

    par.add_argument("--t",
                     dest="t",
                     help="Threshold for Tachycardia (BPM)",
                     type=int,
                     default=240)

    par.add_argument("--sig",
                     dest="s",
                     help="Choice of signal for Heart Rate Estimation (1 = ECG only, 2 = PP only, 3 = both",
                     type=int,
                     default=3)

    par.add_argument("--avg",
                     dest="a",
                     help="Duration of multi-minute HR avergaes",
                     type=int,
                     nargs="+",
                     default=[1,5])

    par.add_argument("--plt",
                     dest="p",
                     help="Flag to plot 10 minute trace during alarm (1 = yes, 0 = no)",
                     type=int,
                     default=1)

    par.add_argument("--log",
                     dest="l",
                     help="Logging Level",
                     default='DEBUG')


    par.add_argument("--shoutout",
                     dest="shoutout",
                     help="shoutout message",
                     default="Heart rate monitor for ECG + PP data")

    par.add_argument("--noshoutout",
                     dest="noshoutout",
                     help="suppress shoutout message printing",
                     action="store_true")

    args = par.parse_args()

    return(args)
