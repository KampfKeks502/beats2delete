@echo off
set ver=1.0
title Beats2Delete v%ver%


rem only change this variable =======================================================
rem environment variables like "%username%" don't work

set gamedir="G:\Steam\steamapps\common\Beat Saber"

rem =================================================================================



:menu
cls
echo.
echo.
echo.
echo    *********************************************************************************************
echo    *                              Beats2Delete by KampfKeks502                       Ver: %ver%  *
echo    *********************************************************************************************
echo    * Please select the maps you want to keep:                                                  *
echo    *                                                                                           *
echo    *       1.  Favorites                                                                       *
echo    *       2.  Playlists                                                                       *
echo    *       3.  Favorites and Playlists                                                         *
echo    *       4.  Help                                                                            *
echo    *                                                                                           *
echo    *       5. Quit                                                                             *
echo    *                                                                                           *
echo    *********************************************************************************************
echo.
echo Enter selection and then press the ENTER key:
echo.
set /p M=
if "%M%"=="1" goto Fav
if "%M%"=="2" goto PL
if "%M%"=="3" goto Fav_PL
if "%M%"=="4" goto Help
if "%M%"=="5" goto exit
if "%M%"=="x" cls && cmd.exe /k title CommandShell 
if "%M%"=="exit" exit
if "%M%"=="q" exit
goto menu




:Fav
title Beats2Delete v%ver% - Favorites
cls
python main.py -p %gamedir% -f
pause
exit

:PL
title Beats2Delete v%ver% - Playlists
cls
:PL_menu
cls
echo.
echo.
echo.
echo    *********************************************************************************************
echo    *                              Beats2Delete by KampfKeks502                       Ver: %ver%  *
echo    *********************************************************************************************
echo    * Please select the Compare-Mode you want to use:                                           *
echo    *                                                                                           *
echo    *       1.  Map name and map author  [Recommended]                                          *
echo    *       2.  Hash ID                                                                         *
echo    *                                                                                           *
echo    *       3.  Help                                                                            *
echo    *                                                                                           *
echo    *********************************************************************************************
echo.
echo Enter selection and then press the ENTER key:
echo.
set /p M=
if "%M%"=="1" goto PL_name
if "%M%"=="2" goto PL_hash
if "%M%"=="3" goto Fav_PL
if "%M%"=="x" cls && cmd.exe /k title CommandShell 
if "%M%"=="exit" exit
if "%M%"=="q" exit
goto PL_menu


:PL_name
cls
python main.py -p %gamedir% -pl
pause
exit

:PL_hash
cls
title Beats2Delete v%ver% - Playlists [Hash]
python main.py -p %gamedir% -pl -H
pause
exit


:mover
cls
echo.
echo.
echo.
echo    *********************************************************************************************
echo    *                              Beats2Delete by KampfKeks502                       Ver: %ver%  *
echo    *********************************************************************************************
echo    * Please select the Compare-Mode you want to use:                                           *
echo    *                                                                                           *
echo    *       1.  Map name and map author  [Recommended]                                          *
echo    *       2.  Hash ID                                                                         *
echo    *                                                                                           *
echo    *       3.  Help                                                                            *
echo    *                                                                                           *
echo    *********************************************************************************************
echo.
echo Enter selection and then press the ENTER key:
echo.
set /p M=
if "%M%"=="1" goto PL_name
if "%M%"=="2" goto PL_hash
if "%M%"=="3" goto Fav_PL
if "%M%"=="x" cls && cmd.exe /k title CommandShell 
if "%M%"=="exit" exit
if "%M%"=="q" exit
goto PL_menu




python main.py -p %gamedir% -pl -f
pause