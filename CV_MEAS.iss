; Script de Inno Setup para CV measurements

[Setup]
; Nombre de la aplicación
AppName=CV measurements
; Versión de la aplicación
AppVersion=2.0
; Carpeta donde se generará el instalador
OutputDir=C:\Users\arnau\Desktop
; Nombre del archivo instalador
OutputBaseFilename=CV_measurements_Installer
; Carpeta de instalación por defecto (en Program Files)
DefaultDirName={pf}\CV measurements
; Nombre del grupo en el menú de inicio
DefaultGroupName=CV measurements
; Permisos elevados para la instalación
PrivilegesRequired=admin

SetupIconFile=C:\Users\arnau\Downloads\CV.ico

; Definición de los archivos que se copiarán
[Files]
; Incluir el ejecutable principal
Source: "C:\Users\arnau\Documents\GitHub\Practicas-CNM\Programas finales\exes\CV\CV.exe"; DestDir: "{app}"; Flags: ignoreversion
; Incluir todos los archivos de la carpeta '_internal'
Source: "C:\Users\arnau\Documents\GitHub\Practicas-CNM\Programas finales\exes\CV\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs

; Crear accesos directos
[Icons]
; Acceso directo en el menú de inicio
Name: "{group}\CV measurements"; Filename: "{app}\CV.exe"
; Acceso directo en el escritorio
Name: "{commondesktop}\CV measurements"; Filename: "{app}\CV.exe"

; Sección de desinstalación
[UninstallDelete]
Type: filesandordirs; Name: "{app}"
