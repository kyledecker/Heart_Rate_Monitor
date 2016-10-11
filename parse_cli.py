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

    # note that type isn't specified since argparse will default to a str                                                                                                                                         
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
