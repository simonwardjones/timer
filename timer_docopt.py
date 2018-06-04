"""
Timer tool with default stop watch, ctrl+c to stop

Usage:
    timer [options]

Options
    -c countdown, --countdown countdown    Converrting stopwatch to countdown with given seconds
"""

import os
import sys
from time import sleep
import time
from docopt import docopt
from timer import Timer
# good old fasioned stop watch


def cli(countdown=None):
    """cli timer using docopt"""
    timer = Timer()
    timer.start_timer()
    clean = 0
    try:
        if countdown:
            while timer.get_elapsed() < countdown:
                if timer.get_elapsed() < 2:
                    print("And They are off!!  " + timer.get_time_hhmmss(countdown -
                                                                         timer.get_elapsed()), end='\r', flush=True)
                elif clean == 0:
                    print("                                   ", end='\r')
                    clean = 1
                else:
                    print(timer.get_time_hhmmss(countdown -
                                                timer.get_elapsed()), end='\r', flush=True)
        else:
            while timer._is_running:
                if timer.get_elapsed() < 2:
                    print("And They are off!!  " +
                          timer.get_time_hhmmss(timer.get_elapsed()), end='\r', flush=True)
                elif clean == 0:
                    print("                                   ", end='\r')
                    clean = 1
                else:
                    print(timer.get_time_hhmmss(
                        timer.get_elapsed()), end='\r', flush=True)
    except KeyboardInterrupt:
        timer.stop()
        print("                                 ", end='\r')
        print(timer.get_time_hhmmss(timer.get_time()))
        sys.exit()


def main():
    args = docopt(__doc__)
    if args['--countdown']:
        countdown = int(args['--countdown'])
    else:
        countdown = None
    cli(countdown)


if __name__ == '__main__':
    main()
