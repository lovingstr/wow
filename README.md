# 视频渲染
视频由基于[python](https://www.python.org)开源数学动画引擎 [manim](https://github.com/3b1b/manim)库 渲染\
\
环境依赖: [ffmpeg](https://www.ffmpeg.org), [miktex](https://miktex.org), [sox](http://sox.sourceforge.net)\
\
当然其实还有[pycairo](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo)
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
本代码使用了`TextMobject("中文")`之类的代码, 为了能够正常渲染, 建议不要使用`TextMobject("其他语言文字")`功能已经失效的官方文件夹, 建议使用[MK修改后的文件夹](https://github.com/manim-kindergarten/manim)， 
并将`manimlib\constants.py`中的`TEX_USE_CTEX=False`改为`TEX_USE_CTEX=True`, 并在`manimlib\tex_template.tex`加入一行`\usepackage{mhchem}`以便显示我这开头什么都不是的错误公式

### 如果你想使用官方文件夹
主要改`manimlib`文件中的`tex_template.tex`, `ctex_template.tex`, `config.py`, `constants.py`文件

- 复制以下内容替代`tex_template.tex`
```tex
\documentclass[preview]{standalone}

\usepackage[english]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{dsfont}
\usepackage{setspace}
\usepackage{tipa}
\usepackage{relsize}
\usepackage{textcomp}
\usepackage{mathrsfs}
\usepackage{calligra}
\usepackage{wasysym}
\usepackage{ragged2e}
\usepackage{physics}
\usepackage{xcolor}
\usepackage{microtype}
\usepackage{mhchem}
\DisableLigatures{encoding = *, family = * }
%\usepackage[UTF8]{ctex}
\linespread{1}

\begin{document}

YourTextHere

\end{document}

```
# 
- 复制以下内容替代`ctex_template.tex`
```tex
\documentclass[preview]{standalone}
\usepackage[UTF8]{ctex}

\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{dsfont}
\usepackage{setspace}
\usepackage{tipa}
\usepackage{relsize}
\usepackage{textcomp}
\usepackage{mathrsfs}
\usepackage{calligra}
\usepackage{wasysym}
\usepackage{ragged2e}
\usepackage{physics}
\usepackage{xcolor}
\usepackage{microtype}
%\DisableLigatures{encoding = *, family = * }
\linespread{1}

\begin{document}

YourTextHere

\end{document}

```
# 
- 复制以下内容替代`constants.py`
```python
import numpy as np
import os

MEDIA_DIR = ""
VIDEO_DIR = ""
VIDEO_OUTPUT_DIR = ""
TEX_DIR = ""
TEXT_DIR = ""


def initialize_directories(config):
    global MEDIA_DIR
    global VIDEO_DIR
    global VIDEO_OUTPUT_DIR
    global TEX_DIR
    global TEXT_DIR

    video_path_specified = config["video_dir"] or config["video_output_dir"]

    if not (video_path_specified and config["tex_dir"]):
        if config["media_dir"]:
            MEDIA_DIR = config["media_dir"]
        else:
            MEDIA_DIR = os.path.join(
                os.path.expanduser('~'),
                "Dropbox (3Blue1Brown)/3Blue1Brown Team Folder"
            )
        if not os.path.isdir(MEDIA_DIR):
            MEDIA_DIR = "./media"
        print(
            f"Media will be written to {MEDIA_DIR + os.sep}. You can change "
            "this behavior with the --media_dir flag."
        )
    else:
        if config["media_dir"]:
            print(
                "Ignoring --media_dir, since both --tex_dir and a video "
                "directory were both passed"
            )

    TEX_DIR = config["tex_dir"] or os.path.join(MEDIA_DIR, "Tex")
    TEXT_DIR = os.path.join(MEDIA_DIR, "texts")
    if not video_path_specified:
        VIDEO_DIR = os.path.join(MEDIA_DIR, "videos")
        VIDEO_OUTPUT_DIR = os.path.join(MEDIA_DIR, "videos")
    elif config["video_output_dir"]:
        VIDEO_OUTPUT_DIR = config["video_output_dir"]
    else:
        VIDEO_DIR = config["video_dir"]

    for folder in [VIDEO_DIR, VIDEO_OUTPUT_DIR, TEX_DIR, TEXT_DIR]:
        if folder != "" and not os.path.exists(folder):
            os.makedirs(folder)

NOT_SETTING_FONT_MSG='''
Warning:
You haven't set font.
If you are not using English, this may cause text rendering problem.
You set font like:
text = Text('your text', font='your font')
or:
class MyText(Text):
    CONFIG = {
        'font': 'My Font'
    }
'''
START_X = 30
START_Y = 20
NORMAL = 'NORMAL'
ITALIC = 'ITALIC'
OBLIQUE = 'OBLIQUE'
BOLD = 'BOLD'

TEX_USE_CTEX = True
TEX_TEXT_TO_REPLACE = "YourTextHere"
TEMPLATE_TEX_FILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "tex_template.tex" if not TEX_USE_CTEX else "ctex_template.tex"
)
with open(TEMPLATE_TEX_FILE, "r") as infile:
    TEMPLATE_TEXT_FILE_BODY = infile.read()
    TEMPLATE_TEX_FILE_BODY = TEMPLATE_TEXT_FILE_BODY.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{align*}",
    )

HELP_MESSAGE = """
   Usage:
   python extract_scene.py <module> [<scene name>]
   -p preview in low quality
   -s show and save picture of last frame
   -w write result to file [this is default if nothing else is stated]
   -o <file_name> write to a different file_name
   -l use low quality
   -m use medium quality
   -a run and save every scene in the script, or all args for the given scene
   -q don't print progress
   -f when writing to a movie file, export the frames in png sequence
   -t use transperency when exporting images
   -n specify the number of the animation to start from
   -r specify a resolution
   -c specify a background color
"""
SCENE_NOT_FOUND_MESSAGE = """
   {} is not in the script
"""
CHOOSE_NUMBER_MESSAGE = """
Choose number corresponding to desired scene/arguments.
(Use comma separated list for multiple entries)
Choice(s): """
INVALID_NUMBER_MESSAGE = "Fine then, if you don't want to give a valid number I'll just quit"

NO_SCENE_MESSAGE = """
   There are no scenes inside that module
"""

# There might be other configuration than pixel shape later...
PRODUCTION_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 1080,  # 1440
    "pixel_width": 1920,  # 2560
    "frame_rate": 60,
}

HIGH_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 1080,
    "pixel_width": 1920,
    "frame_rate": 60,
}

MEDIUM_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 720,
    "pixel_width": 1280,
    "frame_rate": 30,
}

LOW_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 480,
    "pixel_width": 854,
    "frame_rate": 15,
}

DEFAULT_PIXEL_HEIGHT = PRODUCTION_QUALITY_CAMERA_CONFIG["pixel_height"]
DEFAULT_PIXEL_WIDTH = PRODUCTION_QUALITY_CAMERA_CONFIG["pixel_width"]
DEFAULT_FRAME_RATE = 60

DEFAULT_POINT_DENSITY_2D = 25
DEFAULT_POINT_DENSITY_1D = 250

DEFAULT_STROKE_WIDTH = 4

FRAME_HEIGHT = 8.0
FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / DEFAULT_PIXEL_HEIGHT
FRAME_Y_RADIUS = FRAME_HEIGHT / 2
FRAME_X_RADIUS = FRAME_WIDTH / 2

SMALL_BUFF = 0.1
MED_SMALL_BUFF = 0.25
MED_LARGE_BUFF = 0.5
LARGE_BUFF = 1

DEFAULT_MOBJECT_TO_EDGE_BUFFER = MED_LARGE_BUFF
DEFAULT_MOBJECT_TO_MOBJECT_BUFFER = MED_SMALL_BUFF


# All in seconds
DEFAULT_POINTWISE_FUNCTION_RUN_TIME = 3.0
DEFAULT_WAIT_TIME = 1.


ORIGIN = np.array((0., 0., 0.))
UP = np.array((0., 1., 0.))
DOWN = np.array((0., -1., 0.))
RIGHT = np.array((1., 0., 0.))
LEFT = np.array((-1., 0., 0.))
IN = np.array((0., 0., -1.))
OUT = np.array((0., 0., 1.))
X_AXIS = np.array((1., 0., 0.))
Y_AXIS = np.array((0., 1., 0.))
Z_AXIS = np.array((0., 0., 1.))

# Useful abbreviations for diagonals
UL = UP + LEFT
UR = UP + RIGHT
DL = DOWN + LEFT
DR = DOWN + RIGHT

TOP = FRAME_Y_RADIUS * UP
BOTTOM = FRAME_Y_RADIUS * DOWN
LEFT_SIDE = FRAME_X_RADIUS * LEFT
RIGHT_SIDE = FRAME_X_RADIUS * RIGHT

PI = np.pi
TAU = 2 * PI
DEGREES = TAU / 360

FFMPEG_BIN = "ffmpeg"

# Colors
COLOR_MAP = {
    "DARK_BLUE": "#236B8E",
    "DARK_BROWN": "#8B4513",
    "LIGHT_BROWN": "#CD853F",
    "BLUE_E": "#1C758A",
    "BLUE_D": "#29ABCA",
    "BLUE_C": "#58C4DD",
    "BLUE_B": "#9CDCEB",
    "BLUE_A": "#C7E9F1",
    "TEAL_E": "#49A88F",
    "TEAL_D": "#55C1A7",
    "TEAL_C": "#5CD0B3",
    "TEAL_B": "#76DDC0",
    "TEAL_A": "#ACEAD7",
    "GREEN_E": "#699C52",
    "GREEN_D": "#77B05D",
    "GREEN_C": "#83C167",
    "GREEN_B": "#A6CF8C",
    "GREEN_A": "#C9E2AE",
    "YELLOW_E": "#E8C11C",
    "YELLOW_D": "#F4D345",
    "YELLOW_C": "#FFFF00",
    "YELLOW_B": "#FFEA94",
    "YELLOW_A": "#FFF1B6",
    "GOLD_E": "#C78D46",
    "GOLD_D": "#E1A158",
    "GOLD_C": "#F0AC5F",
    "GOLD_B": "#F9B775",
    "GOLD_A": "#F7C797",
    "RED_E": "#CF5044",
    "RED_D": "#E65A4C",
    "RED_C": "#FC6255",
    "RED_B": "#FF8080",
    "RED_A": "#F7A1A3",
    "MAROON_E": "#94424F",
    "MAROON_D": "#A24D61",
    "MAROON_C": "#C55F73",
    "MAROON_B": "#EC92AB",
    "MAROON_A": "#ECABC1",
    "PURPLE_E": "#644172",
    "PURPLE_D": "#715582",
    "PURPLE_C": "#9A72AC",
    "PURPLE_B": "#B189C6",
    "PURPLE_A": "#CAA3E8",
    "WHITE": "#FFFFFF",
    "BLACK": "#000000",
    "LIGHT_GRAY": "#BBBBBB",
    "LIGHT_GREY": "#BBBBBB",
    "GRAY": "#888888",
    "GREY": "#888888",
    "DARK_GREY": "#444444",
    "DARK_GRAY": "#444444",
    "DARKER_GREY": "#222222",
    "DARKER_GRAY": "#222222",
    "GREY_BROWN": "#736357",
    "PINK": "#D147BD",
    "LIGHT_PINK": "#DC75CD",
    "GREEN_SCREEN": "#00FF00",
    "ORANGE": "#FF862F",
}
PALETTE = list(COLOR_MAP.values())
locals().update(COLOR_MAP)
for name in [s for s in list(COLOR_MAP.keys()) if s.endswith("_C")]:
    locals()[name.replace("_C", "")] = locals()[name]

# Streaming related configuration
LIVE_STREAM_NAME = "LiveStream"
TWITCH_STREAM_KEY = "YOUR_STREAM_KEY"
STREAMING_PROTOCOL = "tcp"
STREAMING_IP = "127.0.0.1"
STREAMING_PORT = "2000"
STREAMING_CLIENT = "ffplay"
STREAMING_URL = f"{STREAMING_PROTOCOL}://{STREAMING_IP}:{STREAMING_PORT}?listen"
STREAMING_CONSOLE_BANNER = """
Manim is now running in streaming mode. Stream animations by passing
them to manim.play(), e.g.
>>> c = Circle()
>>> manim.play(ShowCreation(c))
"""
code_languages_list = {"abap": "abap", "as": "as", "as3": "as3", "ada": "ada", "antlr": "antlr",
                       "antlr_as": "antlr-as",
                       "antlr_csharp": "antlr-csharp", "antlr_cpp": "antlr-cpp", "antlr_java": "antlr-java",
                       "antlr_objc": "antlr-objc", "antlr_perl": "antlr-perl", "antlr_python": "antlr-python",
                       "antlr_ruby": "antlr-ruby", "apacheconf": "apacheconf", "applescript": "applescript",
                       "aspectj": "aspectj",
                       "aspx_cs": "aspx-cs", "aspx_vb": "aspx-vb", "asy": "asy", "ahk": "ahk", "autoit": "autoit",
                       "awk": "awk",
                       "basemake": "basemake", "bash": "bash", "console": "console", "bat": "bat",
                       "bbcode": "bbcode",
                       "befunge": "befunge", "blitzmax": "blitzmax", "boo": "boo", "brainfuck": "brainfuck",
                       "bro": "bro",
                       "bugs": "bugs", "c": "c", "csharp": "csharp", "cpp": "cpp", "c_objdump": "c-objdump",
                       "ca65": "ca65",
                       "cbmbas": "cbmbas", "ceylon": "ceylon", "cfengine3": "cfengine3", "cfs": "cfs",
                       "cheetah": "cheetah",
                       "clojure": "clojure", "cmake": "cmake", "cobol": "cobol", "cobolfree": "cobolfree",
                       "coffee_script": "coffee-script", "cfm": "cfm", "common_lisp": "common-lisp", "coq": "coq",
                       "cpp_objdump": "cpp-objdump", "croc": "croc", "css": "css", "css_django": "css+django",
                       "css_genshitext": "css+genshitext", "css_lasso": "css+lasso", "css_mako": "css+mako",
                       "css_myghty": "css+myghty", "css_php": "css+php", "css_erb": "css+erb",
                       "css_smarty": "css+smarty",
                       "cuda": "cuda", "cython": "cython", "d": "d", "d_objdump": "d-objdump", "dpatch": "dpatch",
                       "dart": "dart",
                       "control": "control", "sourceslist": "sourceslist", "delphi": "delphi", "dg": "dg",
                       "diff": "diff",
                       "django": "django", "dtd": "dtd", "duel": "duel", "dylan": "dylan",
                       "dylan_console": "dylan-console",
                       "dylan_lid": "dylan-lid", "ec": "ec", "ecl": "ecl", "elixir": "elixir", "iex": "iex",
                       "ragel_em": "ragel-em",
                       "erb": "erb", "erlang": "erlang", "erl": "erl", "evoque": "evoque", "factor": "factor",
                       "fancy": "fancy",
                       "fan": "fan", "felix": "felix", "fortran": "fortran", "Clipper": "Clipper",
                       "fsharp": "fsharp", "gas": "gas",
                       "genshi": "genshi", "genshitext": "genshitext", "pot": "pot", "Cucumber": "Cucumber",
                       "glsl": "glsl",
                       "gnuplot": "gnuplot", "go": "go", "gooddata_cl": "gooddata-cl", "gosu": "gosu", "gst": "gst",
                       "groff": "groff",
                       "groovy": "groovy", "haml": "haml", "haskell": "haskell", "hx": "hx", "html": "html",
                       "html_cheetah": "html+cheetah", "html_django": "html+django", "html_evoque": "html+evoque",
                       "html_genshi": "html+genshi", "html_lasso": "html+lasso", "html_mako": "html+mako",
                       "html_myghty": "html+myghty", "html_php": "html+php", "html_smarty": "html+smarty",
                       "html_velocity": "html+velocity", "http": "http", "haxeml": "haxeml", "hybris": "hybris",
                       "idl": "idl",
                       "ini": "ini", "io": "io", "ioke": "ioke", "irc": "irc", "jade": "jade", "jags": "jags",
                       "java": "java",
                       "jsp": "jsp", "js": "js", "js_cheetah": "js+cheetah", "js_django": "js+django",
                       "js_genshitext": "js+genshitext", "js_lasso": "js+lasso", "js_mako": "js+mako",
                       "js_myghty": "js+myghty",
                       "js_php": "js+php", "js_erb": "js+erb", "js_smarty": "js+smarty", "json": "json",
                       "julia": "julia",
                       "jlcon": "jlcon", "kconfig": "kconfig", "koka": "koka", "kotlin": "kotlin", "lasso": "lasso",
                       "lighty": "lighty", "lhs": "lhs", "live_script": "live-script", "llvm": "llvm",
                       "logos": "logos",
                       "logtalk": "logtalk", "lua": "lua", "make": "make", "mako": "mako", "maql": "maql",
                       "mason": "mason",
                       "matlab": "matlab", "matlabsession": "matlabsession", "minid": "minid",
                       "modelica": "modelica",
                       "modula2": "modula2", "trac_wiki": "trac-wiki", "monkey": "monkey", "moocode": "moocode",
                       "moon": "moon",
                       "mscgen": "mscgen", "mupad": "mupad", "mxml": "mxml", "myghty": "myghty", "mysql": "mysql",
                       "nasm": "nasm",
                       "nemerle": "nemerle", "newlisp": "newlisp", "newspeak": "newspeak", "nginx": "nginx",
                       "nimrod": "nimrod",
                       "nsis": "nsis", "numpy": "numpy", "objdump": "objdump", "objective_c": "objective-c",
                       "objective_c_+": "objective-c++", "objective_j": "objective-j", "ocaml": "ocaml",
                       "octave": "octave",
                       "ooc": "ooc", "opa": "opa", "openedge": "openedge", "perl": "perl", "php": "php",
                       "plpgsql": "plpgsql",
                       "psql": "psql", "postgresql": "postgresql", "postscript": "postscript", "pov": "pov",
                       "powershell": "powershell", "prolog": "prolog", "properties": "properties",
                       "protobuf": "protobuf",
                       "puppet": "puppet", "pypylog": "pypylog", "python": "python", "python3": "python3",
                       "py3tb": "py3tb",
                       "pycon": "pycon", "pytb": "pytb", "qml": "qml", "racket": "racket", "ragel": "ragel",
                       "ragel_c": "ragel-c",
                       "ragel_cpp": "ragel-cpp", "ragel_d": "ragel-d", "ragel_java": "ragel-java",
                       "ragel_objc": "ragel-objc",
                       "ragel_ruby": "ragel-ruby", "raw": "raw", "rconsole": "rconsole", "rd": "rd",
                       "rebol": "rebol",
                       "redcode": "redcode", "registry": "registry", "rst": "rst", "rhtml": "rhtml",
                       "RobotFramework": "RobotFramework", "spec": "spec", "rb": "rb", "rbcon": "rbcon",
                       "rust": "rust",
                       "splus": "splus", "sass": "sass", "scala": "scala", "ssp": "ssp", "scaml": "scaml",
                       "scheme": "scheme",
                       "scilab": "scilab", "scss": "scss", "shell_session": "shell-session", "smali": "smali",
                       "smalltalk": "smalltalk", "smarty": "smarty", "snobol": "snobol", "sp": "sp", "sql": "sql",
                       "sqlite3": "sqlite3", "squidconf": "squidconf", "stan": "stan", "sml": "sml",
                       "systemverilog": "systemverilog",
                       "tcl": "tcl", "tcsh": "tcsh", "tea": "tea", "tex": "tex", "text": "text",
                       "treetop": "treetop", "ts": "ts",
                       "urbiscript": "urbiscript", "vala": "vala", "vb.net": "vb.net", "velocity": "velocity",
                       "verilog": "verilog",
                       "vgl": "vgl", "vhdl": "vhdl", "vim": "vim", "xml": "xml", "xml_cheetah": "xml+cheetah",
                       "xml_django": "xml+django", "xml_evoque": "xml+evoque", "xml_lasso": "xml+lasso",
                       "xml_mako": "xml+mako",
                       "xml_myghty": "xml+myghty", "xml_php": "xml+php", "xml_erb": "xml+erb",
                       "xml_smarty": "xml+smarty",
                       "xml_velocity": "xml+velocity", "xquery": "xquery", "xslt": "xslt", "xtend": "xtend",
                       "yaml": "yaml"}

code_styles_list = {0: "autumn", 1: "borland", 2: "bw", 3: "colorful", 4: "default", 5: "emacs",
                    6: "friendly", 7: "fruity", 8: "manni", 9: "monokai", 10: "murphy", 11: "native",
                    12: "pastie", 13: "perldoc", 14: "rrt", 15: "tango", 16: "trac", 17: "vim", 18: "vs"}
FILE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"path/to/yoursvg.svg")

```
### 注意 `path/to/yoursvg.svg` 指像小π一样的svg路径, 不要直接复制 当然删去也行
#
以下内容替代`config.py`
```python
import argparse
import colour
import importlib.util
import os
import sys
import types

import manimlib.constants


def parse_cli():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "file",
            help="path to file holding the python code for the scene",
        )
        parser.add_argument(
            "scene_names",
            nargs="*",
            help="Name of the Scene class you want to see",
        )
        parser.add_argument(
            "-p", "--preview",
            action="store_true",
            help="Automatically open the saved file once its done",
        ),
        parser.add_argument(
            "-w", "--write_to_movie",
            action="store_true",
            help="Render the scene as a movie file",
        ),
        parser.add_argument(
            "-s", "--save_last_frame",
            action="store_true",
            help="Save the last frame",
        ),
        parser.add_argument(
            "-l", "--low_quality",
            action="store_true",
            help="Render at a low quality (for faster rendering)",
        ),
        parser.add_argument(
            "-m", "--medium_quality",
            action="store_true",
            help="Render at a medium quality",
        ),
        parser.add_argument(
            "--high_quality",
            action="store_true",
            help="Render at a high quality",
        ),
        parser.add_argument(
            "-uhd", "--ultra_high_quality",
            action="store_true",
            help="Render at a ultra high quality",
        ),
        parser.add_argument(
            "-g", "--save_pngs",
            action="store_true",
            help="Save each frame as a png",
        ),
        parser.add_argument(
            "-i", "--save_as_gif",
            action="store_true",
            help="Save the video as gif",
        ),
        parser.add_argument(
            "-f", "--show_file_in_finder",
            action="store_true",
            help="Show the output file in finder",
        ),
        parser.add_argument(
            "-t", "--transparent",
            action="store_true",
            help="Render to a movie file with an alpha channel",
        ),
        parser.add_argument(
            "-q", "--quiet",
            action="store_true",
            help="",
        ),
        parser.add_argument(
            "-a", "--write_all",
            action="store_true",
            help="Write all the scenes from a file",
        ),
        parser.add_argument(
            "-o", "--file_name",
            help="Specify the name of the output file, if"
                 "it should be different from the scene class name",
        )
        parser.add_argument(
            "-n", "--start_at_animation_number",
            help="Start rendering not from the first animation, but"
                 "from another, specified by its index.  If you pass"
                 "in two comma separated values, e.g. \"3,6\", it will end"
                 "the rendering at the second value",
        )
        parser.add_argument(
            "-r", "--resolution",
            help="Resolution, passed as \"height,width\"",
        )
        parser.add_argument(
            "-c", "--color",
            help="Background color",
        )
        parser.add_argument(
            "--sound",
            action="store_true",
            help="Play a success/failure sound",
        )
        parser.add_argument(
            "--leave_progress_bars",
            action="store_true",
            help="Leave progress bars displayed in terminal",
        )
        parser.add_argument(
            "--media_dir",
            help="directory to write media",
        )
        video_group = parser.add_mutually_exclusive_group()
        video_group.add_argument(
            "--video_dir",
            help="directory to write file tree for video",
        )
        video_group.add_argument(
            "--video_output_dir",
            help="directory to write video",
        )
        parser.add_argument(
            "--tex_dir",
            help="directory to write tex",
        )
        return parser.parse_args()
    except argparse.ArgumentError as err:
        print(str(err))
        sys.exit(2)


def get_module(file_name):
    if file_name == "-":
        module = types.ModuleType("input_scenes")
        code = "from manimlib.imports import *\n\n" + sys.stdin.read()
        try:
            exec(code, module.__dict__)
            return module
        except Exception as e:
            print(f"Failed to render scene: {str(e)}")
            sys.exit(2)
    else:
        module_name = file_name.replace(os.sep, ".").replace(".py", "")
        spec = importlib.util.spec_from_file_location(module_name, file_name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module


def get_configuration(args):
    module = get_module(args.file)
    file_writer_config = {
        # By default, write to file
        "write_to_movie": args.write_to_movie or not args.save_last_frame,
        "save_last_frame": args.save_last_frame,
        "save_pngs": args.save_pngs,
        "save_as_gif": args.save_as_gif,
        # If -t is passed in (for transparent), this will be RGBA
        "png_mode": "RGBA" if args.transparent else "RGB",
        "movie_file_extension": ".mov" if args.transparent else ".mp4",
        "file_name": args.file_name,
        "input_file_path": args.file,
    }
    if hasattr(module, "OUTPUT_DIRECTORY"):
        file_writer_config["output_directory"] = module.OUTPUT_DIRECTORY
    config = {
        "module": module,
        "scene_names": args.scene_names,
        "open_video_upon_completion": args.preview,
        "show_file_in_finder": args.show_file_in_finder,
        "file_writer_config": file_writer_config,
        "quiet": args.quiet or args.write_all,
        "ignore_waits": args.preview,
        "write_all": args.write_all,
        "start_at_animation_number": args.start_at_animation_number,
        "end_at_animation_number": None,
        "sound": args.sound,
        "leave_progress_bars": args.leave_progress_bars,
        "media_dir": args.media_dir,
        "video_dir": args.video_dir,
        "video_output_dir": args.video_output_dir,
        "tex_dir": args.tex_dir,
    }

    # Camera configuration
    config["camera_config"] = get_camera_configuration(args)

    # Arguments related to skipping
    stan = config["start_at_animation_number"]
    if stan is not None:
        if "," in stan:
            start, end = stan.split(",")
            config["start_at_animation_number"] = int(start)
            config["end_at_animation_number"] = int(end)
        else:
            config["start_at_animation_number"] = int(stan)

    config["skip_animations"] = any([
        file_writer_config["save_last_frame"],
        config["start_at_animation_number"],
    ])
    return config


def get_camera_configuration(args):
    camera_config = {}
    if args.low_quality:
        camera_config.update(manimlib.constants.LOW_QUALITY_CAMERA_CONFIG)
    elif args.medium_quality:
        camera_config.update(manimlib.constants.MEDIUM_QUALITY_CAMERA_CONFIG)
    elif args.high_quality:
        camera_config.update(manimlib.constants.HIGH_QUALITY_CAMERA_CONFIG)
    elif args.ultra_high_quality:
        camera_config.update(manimlib.constants.ULTRA_HD_CAMERA_CONFIG)
    else:
        camera_config.update(manimlib.constants.PRODUCTION_QUALITY_CAMERA_CONFIG)

    # If the resolution was passed in via -r
    if args.resolution:
        if "," in args.resolution:
            height_str, width_str = args.resolution.split(",")
            height = int(height_str)
            width = int(width_str)
        else:
            height = int(args.resolution)
            width = int(16 * height / 9)
        camera_config.update({
            "pixel_height": height,
            "pixel_width": width,
        })

    if args.color:
        try:
            camera_config["background_color"] = colour.Color(args.color)
        except AttributeError as err:
            print("Please use a valid color")
            print(err)
            sys.exit(2)

    if args.transparent:
        camera_config["background_opacity"] = 0

    return camera_config
```
# 
## 
## 视频风格
视频风格仿照MK官方给出的示例代码

## 视频引用文件

`from `[我是害羞的向量](https://space.bilibili.com/215499610)写的`几何沙雕bug修复版.py` ` import *`\
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

