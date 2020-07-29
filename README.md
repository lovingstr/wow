# 视频渲染
视频由基于[python](https://www.python.org)开源数学动画引擎 [manim](https://github.com/3b1b/manim)库 渲染\
\
环境依赖 :[ffmpeg](https://www.ffmpeg.org), [miktex](https://miktex.org), [sox](http://sox.sourceforge.net)\
\
其实还有[pycairo](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo)
# 安装manim引擎
## 注意
当进行
```
python -m pip install -r requirements.txt
```
或
```
pip install -r requirements.txt
```
打开`requirements.txt`\
将
```
argparse
colour
numpy
Pillow
progressbar
scipy
tqdm
opencv-python
pycairo
pydub
pygments
pyreadline; sys_platform == 'win32'
```
改为\
```
argparse
colour
numpy
Pillow
progressbar
scipy
tqdm
opencv-python
pydub
pygments
pyreadline; sys_platform == 'win32'
```
\
不过建议不要自己研究\
推荐[MK官方](https://manim.ml/)文档 的安装[教程](https://manim.ml/problems/v2.3.html#)

# 测试 & 渲染

## 测试

测试代码
```
python -m manim example_scenes.py SquareToCircle -pl
python -m manim example_scenes.py WriteStuff -pl
```
\
可直接
```
python -m manim example_scenes.py OpeningManimExample -pl
```

进行测试\
\
\
测试完到`yourpath\manim_name\media\videos\example_scenes\480p15`打开测试视频
### 注意:`yourpath` 和 `manim_name` 分别是你manim文件保存路径和文件名
## 渲染
cmd代码
```
python -m manim Math_Exercise_1.py Classname -pw
```

# 关于
我的数学[讨论Q群](https://jq.qq.com/?_wv=1027&k=HS2d1hsW) @_2,~0\_.making \
[群问题](http://paste.ubuntu.com/p/3MDRrBtYNv/) (马上会改) \
[傻逼吉祥物](https://user.qzone.qq.com/1776471067) 
