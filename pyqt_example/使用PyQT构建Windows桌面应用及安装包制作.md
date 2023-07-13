# 使用PyQT构建Windows桌面应用及安装包制作

[TOC]



## 1. 开发环境

### Conda

annaconda https://www.anaconda.com/download

miniconda https://docs.conda.io/en/latest/miniconda.html

### VScode

https://code.visualstudio.com/download

### Inno Setup

https://jrsoftware.org/isdl.php#stable

## 2. Python环境（Conda）

```
conda create -n pyqt pyqt
```
```
conda activate pyqt
```
```
pip install pyinstaller>=5.12 -i https://pypi.tuna.tsinghua.edu.cn/simple
```
```
conda install -c conda-forge pyside2
```

## 3. 应用开发

### designer设计界面

designer.exe

### pyuic转换ui文件到py文件

```shell
pyuic5 -x .\form.ui  -o .\form.py
```

### 应用编写

main.py

```python
import sys
from form import Ui_Form
from PyQt5 import QtWidgets
from PySide2.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
```

信号连接

```python
ui.pushButton.clicked.connect(self.open_img)
```



## 4. 打包成EXE

```shell
pyinstaller  main.py --hidden-import=PyQt5 --hidden-import=PySide --hidden-import=numpy --hidden-import=cv2 --icon assets/logo.png --windowed --add-data "assets;assets"
```

--hidden-import：该参数用于包含在PyInstaller打包过程中未被自动检测到的模块。当你的脚本动态导入模块或PyInstaller无法检测到所需模块时，它非常有用。要使用此选项，你可以将模块名称作为参数传递，例如--hidden-import=模块名称。

--icon：该参数允许你为应用程序指定自定义图标。图标文件应该是平台特定的格式（对于Windows为.ico，对于macOS为.icns）。要使用此选项，请将图标文件作为参数传递，例如--icon=test.ico。

--windowed：该参数用于在Windows和macOS上创建一个没有控制台窗口的应用程序。当你的脚本具有图形用户界面（GUI）且不需要控制台进行用户输入或输出时，这个选项非常有用。

--add-data：该参数用于将数据文件添加到你的PyInstaller二进制文件中。这些数据文件可以是应用程序运行时所需的任何文件，例如配置文件、图像或帮助文件。要使用此选项，请使用路径分隔符（Windows为;，POSIX系统为:）将数据文件的源和目标分隔开，例如--add-data="源文件;目标文件"。

## 5. 制作安装包

```
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
```

这个Inno Setup脚本（ISS文件）用于创建一个名为"PYQT应用"的程序的安装程序。该脚本分为几个部分，每个部分控制安装过程的不同方面。

下面是各个部分及其含义的解析：

1. `[Setup]`：该部分包含安装程序的一般设置，如应用程序名称、版本、默认安装目录和输出设置。

在你的脚本中，应用程序名称为"B因子计算程序"，版本为1.0。默认安装目录设置为`{pf}\PYQT应用`，其中`{pf}`是代表Program Files文件夹的常量。编译安装程序的输出目录设置为当前目录（.），输出文件名为"PYQT应用安装程序"。安装程序使用LZMA2压缩。

2. `[Files]`：该部分指定要包含在安装程序中的文件及其目标目录。

在你的脚本中，"main"文件夹及其子文件夹中的所有文件将被包含在安装程序中，并将安装到`{app}`文件夹中，该文件夹表示应用程序的安装目录。

3. `[Icons]`：该部分定义安装过程中要创建的快捷方式。

在你的脚本中，将在开始菜单的程序组中创建一个名为"PYQT应用"的快捷方式，指向`{app}`文件夹中的"main.exe"文件。

4. `[Run]`：该部分指定安装完成后要执行的任何命令。

在你的脚本中，安装完成后将执行`{app}`文件夹中的"main.exe"文件，并将工作目录设置为`{app}`。

要使用该脚本创建安装程序，你需要使用Inno Setup Compiler。在Inno Setup Compiler中打开该脚本，然后编译它以生成可执行的安装程序文件。