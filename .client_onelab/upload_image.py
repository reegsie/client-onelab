#!/usr/bin/python

import os

os.system("scrot pc_1.png && scp pc_1.png admin@192.168.1.2:/home/admin/OneLab-UI-Status/services/image-tracking && rm pc_1.png")
