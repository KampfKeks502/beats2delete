@echo off
set ver=1.0
title Beats2Delete v%ver% by KampfKeks502


rem only change this variable =================   no backslashes!  ==============

set gamedir="G:/Steam/steamapps/common/Beat Saber"

rem =================================================================================

python main.py -p %gamedir% -pl -f
pause