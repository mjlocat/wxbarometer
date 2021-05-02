#!/bin/bash

WXPID=`ps x | grep wxbarometer.py | grep -v grep | awk '{ print $1 }'`

if [ -z "${WXPID}" ]; then
  python3 wxbarometer.py &
fi
