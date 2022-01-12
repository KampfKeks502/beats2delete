@echo off
set ver=1.0
title Beats2Delete v%ver% by KampfKeks502


rem only change this variable =================   no backslashes!  ==============
rem environment variables like "%username%" don't work

set gamedir="G:/Steam/steamapps/common/Beat Saber"

rem =================================================================================

python main.py -p %gamedir% -pl -f
pause