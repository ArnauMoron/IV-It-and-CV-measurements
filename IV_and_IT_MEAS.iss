; Script de Inno Setup para CV measurements

[Setup]
; Nombre de la aplicación
AppName=IV and It measurements
; Versión de la aplicación
AppVersion=2.0
; Carpeta donde se generará el instalador
OutputDir=C:\Users\arnau\Desktop
; Nombre del archivo instalador
OutputBaseFilename=IV_It__measurements_Installer
; Carpeta de instalación por defecto (en Program Files)
DefaultDirName={pf}\IV and It measurements
; Nombre del grupo en el menú de inicio
DefaultGroupName=IV and It measurements
; Permisos elevados para la instalación
PrivilegesRequired=admin

SetupIconFile=C:\Users\arnau\Downloads\IV.ico

; Definición de los archivos que se copiarán
[Files]
; Incluir el ejecutable principal
Source: "C:\Users\arnau\Documents\GitHub\Practicas-CNM\Programas finales\exes\IV_It\IV_It.exe"; DestDir: "{app}"; Flags: ignoreversion
; Incluir todos los archivos de la carpeta '_internal'
Source: "C:\Users\arnau\Documents\GitHub\Practicas-CNM\Programas finales\exes\IV_It\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs

; Crear accesos directos
[Icons]
; Acceso directo en el menú de inicio
Name: "{group}\IV and It measurements"; Filename: "{app}\IV_It.exe"
; Acceso directo en el escritorio
Name: "{commondesktop}\IV and It measurements"; Filename: "{app}\IV_It.exe"

; Sección de desinstalación
[UninstallDelete]
Type: filesandordirs; Name: "{app}"
