#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  run_this.py
#  
#  Copyright 2019  Chantal Bisson
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import easygopigo3 as easy
import sys

def main(args):
    gopigo3 = easy.EasyGoPiGo3()
    servo1 = gopigo3.init_servo("SERVO1")
    servo2 = gopigo3.init_servo("SERVO2")

    servo1_position = 86
    servo1.rotate_servo(servo1_position)

    servo2_position = 90
    servo2.rotate_servo(servo2_position)
        
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv))
    except IOError as error:
        # if the GoPiGo3 is not reachable
        # then print the error and exit
        print(str(error))
        sys.exit(1)
