@echo off
set ver=1.0
title Beats2Delete v%ver%


rem only change this variable ====================================================================
rem environment variables like "%username%" don't work; also "\" as the last char is not allowed

set gamedir="G:\Steam\steamapps\common\Beat Saber"

rem ==============================================================================================



:menu
set "par1="
set "par2="
set "par3="
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
if "%M%"=="1" set "par1=-f" && goto mover
if "%M%"=="2" set "par1=-pl" && goto PL
if "%M%"=="3" set "par1=-f -pl" && goto PL
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
if "%M%"=="1" goto mover
if "%M%"=="2" set "par2=-H" && goto mover
if "%M%"=="3" goto help
if "%M%"=="x" cls && cmd.exe /k title CommandShell 
if "%M%"=="exit" exit
if "%M%"=="q" exit
goto PL


:mover
cls
echo.
echo.
echo.
echo    *********************************************************************************************
echo    *                              Beats2Delete by KampfKeks502                       Ver: %ver%  *
echo    *********************************************************************************************
echo    * Please select the action you want to perform:                                             *
echo    *                                                                                           *
echo    *       1.  Move maps to temp folder  [Recommended]                                         *
echo    *       2.  Delete maps                                                                     *
echo    *                                                                                           *
echo    *       3.  Help                                                                            *
echo    *                                                                                           *
echo    *********************************************************************************************
echo.
echo Enter selection and then press the ENTER key:
echo.
set /p M=
if "%M%"=="1" goto start
if "%M%"=="2" set "par3=-d" && goto start
if "%M%"=="3" goto help
if "%M%"=="x" cls && cmd.exe /k title CommandShell 
if "%M%"=="exit" exit
if "%M%"=="q" exit
goto mover


:start
cls
echo python main.py -p %gamedir% %par1% %par2% %par3%
echo.
echo Start?  [y/n]
set /p M=
if "%M%"=="y" goto run
if "%M%"=="Y" goto run
if "%M%"=="n" goto menu
if "%M%"=="N" goto menu
goto start

:run
cls
python main.py -p %gamedir% %par1% %par2% %par3%
pause