@ECHO OFF

REM This script is for running Qpy scripts on Windows standalone by forcing it to be run in the OSGeo4W shell.

REM Check if OSGeo4W exists 
IF NOT EXIST C:\OSGeo4W GOTO PROGRAMFILES
Set "folder=C:\OSGeo4W"
GOTO CALLPYTHON


:PROGRAMFILES
for /d %%a in (
  "C:\Program Files\QGIS*"
) do (
  Set "folder=%%~fa"
)


:CALLPYTHON

REM Call the python script passed in

IF NOT EXIST "%folder%\bin\python-qgis-ltr.bat" GOTO NONLTR
"%folder%\OSGeo4W.bat" "%folder%\bin\python-qgis-ltr.bat" %1

GOTO END

:NONLTR
"%folder%\OSGeo4W.bat" "%folder%\bin\python-qgis.bat" %1

:END

for %%* in (.) do set CurrDirName=%%~nx*


set PATH=%PATH%;%CurrDirName%