#!/bin/bash

rsync -a --progress --delete . pi@10.0.0.17:/home/pi/led_strip
