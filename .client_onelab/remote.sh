#!/bin/bash

sudo -S <<< 123 x11vnc -display :0  -auth /var/run/lightdm/root/\:0 --loop
