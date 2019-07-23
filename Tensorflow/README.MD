
https://www.tensorflow.org/install/pip

https://colab.research.google.com/drive/1y_VuPLZDKUKaTiz8wL5ztprhQRXcBI7u#scrollTo=lIQHlv3YV2Gg


在虚拟机ubuntu里安装
## 安装 tensorflow

```bash
$    sudo apt update
$    sudo apt install python3-dev python3-pip
$    sudo pip3 install -U virtualenv  # system-wide install
    

$ pip install -U pip virtualenv #安装Virtualenv

$ source ./venv/bin/activate  # sh, bash, ksh, or zsh #创建一个新的虚拟环境，方法是选择 Python 解析器并创建一个 .\venv 目录来存放它：

$ .\venv\Scripts\activate #激活虚拟环境：

#在不影响主机系统设置的情况下，在虚拟环境中安装软件包。首先升级 pip：
$ pip install --upgrade pip

$ pip list  # show packages installed within the virtual environment

$ pip install tensorflow==1.5.0
      

#之后要退出 virtualenv，请使用以下命令：
$ deactivate  # don't exit until you're done using TensorFlow

 


 ```