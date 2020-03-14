# -*- coding: utf-8 -*-
"""
Script to run functions on the LED strip.
"""


# Import python modules.
import sys
import time

# Import led stuff.
from led_strip import LEDStrip, Color


def main(strip):
    """
    Main function to be executed.
    """

    # Color the whole strip.
    strip.flush(Color(0, 0, 255))


if __name__ == '__main__':
    """
    Execution part of script.

    This will end in an infinite loop, which can only be canceled by the user
    with crtl+c.
    """

    try:
        # Setup the strip object.
        strip = LEDStrip(60, 18)

        # Call the main function.
        main(strip)

        # Run forever and wait for user input to cancel the script.
        print('to stop the program, press CRTL+C')
        while True:
            # Sleep here, because a simple pass would result in 100% load.
            time.sleep(0.01)

    except KeyboardInterrupt:
        # Clear the strip, so all LEDs will be deactivated.
        strip.clear()
        print('')
        sys.exit()
