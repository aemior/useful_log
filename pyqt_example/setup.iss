   [Setup]
   AppName=PYQTӦ��
   AppVersion=1.0
   DefaultDirName={pf}\PYQTӦ��
   DefaultGroupName=PYQTӦ��
   OutputDir=.
   OutputBaseFilename=PYQTӦ�ð�װ����
   Compression=lzma2
   
   [Files]
   Source: "main\*"; DestDir: "{app}"; Flags: recursesubdirs

   [Icons]
   Name: "{group}\PYQTӦ��"; Filename: "{app}\main.exe"

   [Run]
   Filename: "{app}\main.exe"; WorkingDir: "{app}"