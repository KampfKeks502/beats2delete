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
echo    *********************************************************************************************
echo    *                              [44mBeats2Delete by KampfKeks502[0m                       Ver: [95m%ver%[0m  *
echo    *********************************************************************************************
echo    * Please select the maps you want to keep:                                                  *
echo    *                                                                                           *
echo    *       1.  Favorites                                                                       *
echo    *       2.  Playlists                                                                       *
echo    *       3.  Favorites and Playlists                                                         *
echo    *                                                                                           *
echo    *       4.  [94mHelp[0m                                                                            *
echo    *                                                                                           *
echo    *********************************************************************************************
echo.
echo Enter selection and then press the ENTER key:
echo.
set /p M=
if "%M%"=="1" set "par1=-f" && goto mover
if "%M%"=="2" set "par1=-pl" && goto PL
if "%M%"=="3" set "par1=-f -pl" && goto PL
if "%M%"=="4" goto menu_help
if "%M%"=="x" cls && cmd.exe /k title CommandShell 
if "%M%"=="exit" exit
if "%M%"=="q" exit
goto menu


:menu_help
cls
echo [95mGithub:[0m  [1mhttps://github.com/KampfKeks502/beats2delete/releases[0m     [92m(for newer versions)[0m
echo. 
echo.
echo [91mWhat it does:[0m This script will remove songs depending on your selection.
echo. 
echo.
echo [94mMove maps to temp folder or delete them indefinitely:[0m 
echo At the end of the program you'll be asked if you want to delete all non-matching maps or
echo just move them to a different folder (in case you want to recover the maps)
echo. 
echo.
echo [92mYou can find more detailed informations in the corresponding menus under "Help"[0m
echo. 
pause
goto menu

:PL
cls
echo.
echo.
echo    *********************************************************************************************
echo    *                              [44mBeats2Delete by KampfKeks502[0m                       Ver: [95m%ver%[0m  *
echo    *********************************************************************************************
echo    * Please select the Compare-Mode you want to use (for Playlists):                           *
echo    *                                                                                           *
echo    *       [1m1.  Map name and map author  [Recommended][0m                                          *
echo    *       2.  Hash ID                                                                         *
echo    *                                                                                           *
echo    *       3.  [94mHelp[0m                                                                            *
echo    *                                                                                           *
echo    *********************************************************************************************
echo.
echo Enter selection and then press the ENTER key:
echo.
set /p M=
if "%M%"=="1" goto mover
if "%M%"=="2" set "par2=-H" && goto mover
if "%M%"=="3" goto PL_help
if "%M%"=="x" cls && cmd.exe /k title CommandShell 
if "%M%"=="exit" exit
if "%M%"=="q" exit
goto PL

:PL_help
rem mode con: cols=120 lines=40
cls
echo [44mTL;DR:[0m  [1mIf you're not sure then just use the first option (Map name and map author)[0m
echo. 
echo The option to change the Compare-Mode is only available for Playlists (not for favorites)
echo.
pause
cls
echo.
echo [44mThe Long Answer ...[0m
echo.
echo [95mMap name and map author:[0m
echo The script will compare the maps by their names and authors to decide whether or not to keep a song.
echo Some authors release multiple songs with the same name. Therefore, both versions of the map are preserved
echo even if only one of them is saved in a playlist.
echo.
echo [95mHash ID:[0m
echo To solve the problem of the first version, the Hash-ID-Compare mode is used. Each map has a unique hash,
echo even if the title and author are exactly the same. The second option compares both hashes,
echo the current map hash (calculated just-in-time) and the hash stored inside of the playlist files.
echo (located inside the Game Directory [e.g.: "G:\Steam\steamapps\common\Beat Saber\Playlists\*.bplist"])
echo Therefore, only the exact map saved in a playlist is retained.
echo.
echo.
echo [91mThe Problem with Hash ID:[0m
echo The only useable informations for map comparison inside the playlist files (*.bplist) are:
echo - songName
echo - levelAuthorName
echo - hash
echo I discovered an anomaly in the hashes stored in the playlist files. Some of them (rather small percentage)
echo differ from the actual map hashes and therefore are not kept in Hash-ID-Compare mode.
echo As a result it's [94mrecommended[0m to use the first option until I figure out what's causing this discrepancy
echo and how to fix it.
echo.
echo [1mIf you know more about this problem, feel free to contact me. I'd love to hear what's causing this behavior :%)[0m
echo.
pause
goto PL


:mover
cls
echo.
echo.
echo    *********************************************************************************************
echo    *                              [44mBeats2Delete by KampfKeks502[0m                       Ver: [95m%ver%[0m  *
echo    *********************************************************************************************
echo    * Please select the action you want to perform:                                             *
echo    *                                                                                           *
echo    *       [1m1.  Move maps to temp folder  [Recommended][0m                                         *
echo    *       2.  Delete maps                                                                     *
echo    *                                                                                           *
echo    *       3.  [94mHelp[0m                                                                            *
echo    *                                                                                           *
echo    *********************************************************************************************
echo.
echo Enter selection and then press the ENTER key:
echo.
set /p M=
if "%M%"=="1" goto start
if "%M%"=="2" set "par3=-d" && goto start
if "%M%"=="3" goto mover_help
if "%M%"=="x" cls && cmd.exe /k title CommandShell 
if "%M%"=="exit" exit
if "%M%"=="q" exit
goto mover


:mover_help
rem mode con: cols=120 lines=40
cls
echo.
echo This is straight forward...
echo.
echo [95mMove maps to temp folder:[0m
echo Moves all maps that don't match the previously selected criteria to a "temporary" folder.
echo This directory is located inside the default game Folder and is called "_beats2delete"
echo E.g.: "G:\Steam\steamapps\common\Beat Saber\_beats2delete"
echo There you'll find all the maps that have been sorted out.
echo If you're sure that you don't need these songs anymore you can just delete the entire "_beats2delete" folder
echo.
echo [91mRestore maps:[0m
echo To restore the maps just move them back into the "Beat Saber_Data\CustomLevels" folder
echo and restart BeatSaber
echo.
echo.
echo [95mDelete maps:[0m
echo Well... this option will delete all maps that don't match the previously selected criteria.
echo Remember: This can't be undone!
echo.
pause
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
exit