#!/bin/bash
#!/usr/bin/env /usr/local/bin/node
# <bitbar.title>Zoom Meeting Status</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Ferry Djaja</bitbar.author>
# <bitbar.author.github>Ferry Djaja</bitbar.author.github>
# <bitbar.desc>Simply run a Python script to detect an active meeting</bitbar.desc>

pythonenv="/usr/local/opt/python@3.9/bin/python3.9"
script="/Users/ferry/zoom.py"

$pythonenv $script
