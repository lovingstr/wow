# 视频渲染
视频由基于[python](https://www.python.org)开源数学动画引擎 [manim](https://github.com/3b1b/manim)库 渲染\
\
环境依赖: [ffmpeg](https://www.ffmpeg.org), [miktex](https://miktex.org), [sox](http://sox.sourceforge.net)\
\
当然还有[pycairo](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo)
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
改为
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
或直接
```
python -m manim example_scenes.py OpeningManimExample -pl
```

进行测试\
\
\
测试完到`yourpath\manim_name\media\videos\example_scenes\480p15`打开测试视频
### 注意: `yourpath` 和 `manim_name` 分别是你manim文件保存路径和文件名, 不要直接复制到命令行窗口
## 渲染
cmd代码
```
python -m manim Math_Exercise_1.py Classname -pw
```
### 注意: `Classname`是类名, 不要直接复制到命令行窗口
将所有视频渲染完了后到`ffmpeg`用
```
ffmpeg -i video1.mp4 -c copy video1.ts
ffmpeg -i video2.mp4 -c copy video2.ts
ffmpeg -i "concat:video1.ts|video2.ts" -c copy video.mp4
```
缝合起来`😂`\
你不会这么无聊的吧

### 注意: video1, video2, t等都是代指, 不要直接复制到命令行窗口

# 注意事项
## 文字显示问题
本代码使用了`TextMobject("中文")`之类的代码, 为了能够正常渲染, 建议不要使用将`TextMobject("其他语言文字")`废弃掉的官方文件夹, 建议使用[MK修改后的文件夹](https://github.com/manim-kindergarten/manim)， 
并将`manimlib\constants.py`中的`TEX_USE_CTEX=False`改为`TEX_USE_CTEX=True`, 并在`manimlib\tex_template.tex`加入一行`\usepackage{mhchem}`以便显示我这开头什么都不是的错误公式
## 视频风格
视频风格仿照MK官方给出的示例代码

## 视频引用文件

`from `[我是害羞的向量](https://space.bilibili.com/215499610)写的`几何沙雕bug修复版.py`并重命名为` import *`\
`import` 引用[Elteoremadebeethoven](https://github.com/Elteoremadebeethoven)的[WriteRandom](https://github.com/Elteoremadebeethoven/MyAnimations/blob/master/my_projects/my_projects2.py#L48)和[UnWriteRamdon](https://github.com/Elteoremadebeethoven/MyAnimations/blob/master/my_projects/my_projects2.py#L62) 并重命名为`to_draw.py`

## 视频音乐
爱用什么用什么`🤣`

# 关于
本人是一名爱好数学与编程的男孩\
本视频关于的是为本县(市)2019-2020学年初二数学期末考卷\
如爱好数学者, 可加入
我的数学[讨论Q群](https://jq.qq.com/?_wv=1027&k=HS2d1hsW) @_2,~0\_.making \
当然, 本人一个初二的, 回答不了什么问题 \
但是有需要尽管问(不是说回答不了什么吗😉) ([本人](https://user.qzone.qq.com/3515674727)qq3515674727)\
[群问题](http://paste.ubuntu.com/p/3MDRrBtYNv/) (马上会改) \
[沙逼吉祥物](https://user.qzone.qq.com/1776471067) 
# 文档
如若文档有错误, 不喜勿喷

