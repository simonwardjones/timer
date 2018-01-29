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
                    print("And They are off!!  " + timer.get_time_hhmmss(countdown - timer.get_elapsed()), end= '\r',flush=True)
                elif clean==0:
                    print("                                 ",end='\r')
                    clean = 1
                else:
                    print(timer.get_time_hhmmss(countdown - timer.get_elapsed()), end= '\r',flush=True)
        else:
            while timer._is_running:
                if timer.get_elapsed() < 2:
                    print("And They are off!!  " + timer.get_time_hhmmss(timer.get_elapsed()), end= '\r',flush=True)
                elif clean==0:
                    print("                                 ",end='\r')
                    clean = 1
                else:
                    print(timer.get_time_hhmmss(timer.get_elapsed()), end= '\r',flush=True)
    except KeyboardInterrupt:
        timer.stop()
        print("                                 ",end='\r')
        print(timer.get_time_hhmmss(timer.get_time()))
        sys.exit()



class Timer:
    def __init__(self):
        self.start = time.time()
        self.end = time.time()
        self._is_running = False

    def start_timer(self):
        """restarts the time
        """
        self.start = time.time()
        self._is_running = True


    def restart(self):
        """restarts the time
        """
        self.end = self.start = time.time()

    def stop(self):
        """stop the current time
        """
        if self._is_running:
            self.end = time.time()
        else:
            print("Can't Stop until you start")

    def get_time(self):
        '''
        Returns the time elapsed (Does not stop the counter).

        Returns:
            TYPE: string
        '''
        return self.end - self.start

    def get_elapsed(self):
        '''
        Returns the time elapsed (Does not stop the counter).

        Returns:
            TYPE: string
        '''
        return time.time() - self.start

    def get_time_hhmmss(self,duration):
        """Returns the duration in HH:mm:ss (Does not reset the counter).
        
        Returns:
            TYPE: Description
        """
        m, s = divmod(duration, 60) 
        h, m = divmod(m, 60)
        return f'{int(h):0>2}:{int(m):0>2}:{s:05.4f}'


def main():
    args = docopt(__doc__)
    if args['--countdown']:
        countdown = int(args['--countdown'])
    else:
        countdown = None
    cli(countdown)


if __name__ == '__main__':
    main()