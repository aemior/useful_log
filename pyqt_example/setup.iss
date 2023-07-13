   [Setup]
   AppName=PYQT应用
   AppVersion=1.0
   DefaultDirName={pf}\PYQT应用
   DefaultGroupName=PYQT应用
   OutputDir=.
   OutputBaseFilename=PYQT应用安装程序
   Compression=lzma2
   
   [Files]
   Source: "main\*"; DestDir: "{app}"; Flags: recursesubdirs

   [Icons]
   Name: "{group}\PYQT应用"; Filename: "{app}\main.exe"

   [Run]
   Filename: "{app}\main.exe"; WorkingDir: "{app}"