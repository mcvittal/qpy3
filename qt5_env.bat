@echo off
path %OSGEO4W_ROOT%\apps\qt5\bin;%PATH%

set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\Qt5\plugins

set O4W_QT_PREFIX=%OSGEO4W_ROOT:\=/%/apps/Qt5
set O4W_QT_BINARIES=%OSGEO4W_ROOT:\=/%/apps/Qt5/bin
set O4W_QT_PLUGINS=%OSGEO4W_ROOT:\=/%/apps/Qt5/plugins
set O4W_QT_LIBRARIES=%OSGEO4W_ROOT:\=/%/apps/Qt5/lib
set O4W_QT_TRANSLATIONS=%OSGEO4W_ROOT:\=/%/apps/Qt5/translations
set O4W_QT_HEADERS=%OSGEO4W_ROOT:\=/%/apps/Qt5/include
set O4W_QT_DOC=%OSGEO4W_ROOT:\=/%/apps/Qt5/doc
