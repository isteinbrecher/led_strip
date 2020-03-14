# -*- coding: utf-8 -*-
"""
A wrapper class to handle interactions with the LED strip.
"""

# Import LED driver.
from rpi_ws281x import PixelStrip, Color


class LEDStrip(object):
    """
    An object wrapper for the LED strip.
    """

    def __init__(self, n_led, led_pin):
        """
        Initialize the object.

        Args
        ----
        n_led: int
            Number of LEDs on the strip.
        led_pin: int
            GPIO bin the data line is connected to.
        """

        # Create the led strip object.
        if led_pin in [12, 18]:
            channel = 0
        elif led_pin in [13, 19]:
            channel = 1
        else:
            raise ValueError(('GPIO pin {} can not be used for the LED '
                'strip.').format(led_pin))
        self._strip = PixelStrip(n_led, led_pin, channel=channel)
        self._strip.begin()

    @property
    def n_led(self):
        """
        Return the number of LEDs on the strip.
        """
        return self._strip.numPixels()

    def flush(self, colors):
        """
        Display the colors contained in data on the strip.

        Args
        ----
        colors: Color, [Color]
            If a single color is given, the whole strip is colored with that
            color. If a list is given, colors in the list are set.
        """

        if isinstance(colors, int):
            for i_led in range(self.n_led):
                self._strip.setPixelColor(i_led, colors)
        else:
            for i_led, color in enumerate(colors):
                self._strip.setPixelColor(i_led, color)
        self._strip.show()

    def clear(self):
        """
        Deactivate all LEDs on the strip.
        """

        self.flush(Color(0, 0, 0))
        self._strip.show()
