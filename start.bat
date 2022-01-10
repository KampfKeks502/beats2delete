@echo off
title Beats2Delete

rem only change this variable =================   no backslashes!  ==============

set gamedir="G:/Steam/steamapps/common/Beat Saber"

rem =================================================================================

python main.py -p %gamedir% -pl -f
pause