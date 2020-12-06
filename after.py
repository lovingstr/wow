from manimlib.imports import *
from luoluoluo_useful.imports import *
# 准备开新坑


wiggleoti_kwargs = dict(scale_value=1.5, rotation_angle=.05 * TAU)
color_dict1 = {"e^": "#71D9DD", "{\\theta": "#729DDD", "\\theta": "#729DDD", "\\cos": BLUE_B, "i}": GREEN, "i": GREEN,
               "\\sin": BLUE_D, "{\\alpha": "#729DDD", "\\alpha": "#729DDD", "{\\beta": "#729DDD", "\\beta": "#729DDD",
               "+": "#84DDC8", "-": "#84DDC8"}
font_dict1 = {"e^": "e", "{\\theta": "θ", "i}": "i", "\\theta": "θ", "\\cos": "cos", "\\sin": "sin", "{\\alpha": "α",
              "\\alpha": "α", "{\\beta": "β", "\\beta": "β", "\\cdot": "·", "\\\\": "\n"}

class SourceHansfont(Text):
    CONFIG = {
        "font": "思源黑体",
    }


class complex_class(Scene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
        "str1": r"\sin(\alpha\pm \beta)=\sin(\alpha)\cos(\beta)\pm \cos(\alpha)\sin(\beta)",
        "str2": r"\cos(\alpha\pm \beta)=\cos(\alpha)\cos(\beta)\mp \sin(\alpha)\sin(\beta)",

    }

    def setup(self):
        self.change_cap()
        self.set_caption_on()

    def construct(self):

        tex1 = NaOH(TexMobject(self.str1), s=0)
        tex2 = NaOH(TexMobject(self.str2).next_to(tex1, DOWN), s=0)

        self.play(Write(VGroup(tex1.shift(UP), tex2)))
        self.wait()

        self.play(FadeIn(NaOH(self.captions_mob[0])))
        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))
        self.wait()

        self.play(ApplyWave(tex1))
        self.play(to_draw.EveryoneWiggleOutThenIn(tex2[0], anim_kwargs=wiggleoti_kwargs))
        self.wait(2.)

        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))
        self.wait()

        # ------
        EulerFormula = MyText("e^", "{\\pi", "i}", default_font="思源黑体")

        EulerFormula_SourceHansfont = EulerFormula.get_new_font_texs({"e^": "e", "{\\pi": "π", "i}": "i"})
        EulerFormula_SourceHansfont = NaOH(EulerFormula_SourceHansfont, 0, "#000000", "#29ABCA", "#58C4DD", "#C59978")
        eyes = Eyes(EulerFormula_SourceHansfont[-1]).scale(.4)

        eyes[0].set_color(BLACK)
        eyes[1].set_color(WHITE)
        eyes[1][0][1].set_color(BLACK)
        eyes[1][1][1].set_color(BLACK)
        E = VGroup(EulerFormula_SourceHansfont, eyes)
        # ------

        self.play(ReplacementTransform(self.captions_mob[2], E.move_to(self.captions_mob[2])))
        self.wait()

        self.play(to_draw.UnWrite(Group(tex1, tex2)))
        self.wait()

        # ---
        E.generate_target()
        E.target.move_to(ORIGIN).scale(3.)
        # ---

        self.play(MoveToTarget(E))
        self.wait()

        self.play(Blink(eyes))
        self.play(Write(NaOH(self.captions_mob[3])))
        self.wait()

    def set_caption_on(self, t2c={}):
        self.captions_mob = VGroup(
            *[
                SourceHansfont(cap, tex_to_color_map=t2c).to_edge(DOWN * 1.2)
                .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in self.caps
            ]
        )

    def change_cap(self):
        self.caps = ["小学时, 我们常被这样的式子困扰",
                     "它们难记又难背, 似乎毫无规律",
                     " 但是, 只需一个美妙的公式就可以帮助我们记下它",
                     "欧拉恒等式！"]


class Next(complex_class):
    def construct(self):
        EulerFormula = MyText("e^", "{\\theta", "i}", "=", "\\cos", "(", "\\theta", ")", "+", "i", "\\sin", "(", "\\theta", ")", default_font="思源黑体", color=BLACK)

        EulerFormula_SourceHansfont = EulerFormula.set_color(BLACK).set_color_by_tex_to_color_map(color_dict1) \
            .get_new_font_texs(font_dict1)

        self.play(Write(EulerFormula_SourceHansfont))
        self.wait(3.)

        EulerFormula2 = MyText("e^", "{\\alpha", "i}", "=", "\\cos", "(", "\\alpha", ")", "+", "i", "\\sin", "(", "\\alpha", ")", default_font="思源黑体", color=BLACK)
        EulerFormula2_SourceHansfont = EulerFormula2.set_color(BLACK).set_color_by_tex_to_color_map(color_dict1) \
            .get_new_font_texs(font_dict1)
        self.play(ReplacementTransform(EulerFormula_SourceHansfont, EulerFormula2_SourceHansfont))
        self.wait(3.)

        EulerFormula3 = MyText("e^", "{\\beta", "i}", "=", "\\cos", "(", "\\beta", ")", "+", "i", "\\sin", "(", "\\beta", ")", default_font="思源黑体", color=BLACK)
        EulerFormula3_SourceHansfont = EulerFormula3.set_color(BLACK).set_color_by_tex_to_color_map(color_dict1) \
            .get_new_font_texs(font_dict1)
        EulerFormula3_SourceHansfont.next_to(EulerFormula2_SourceHansfont, DOWN)

        self.play(ReplacementTransform(EulerFormula2_SourceHansfont.copy(), EulerFormula3_SourceHansfont))
        self.wait(3.)

        EulerFormula4 = MyText("e^", "{\\alpha", "i}", "\\cdot", "e^", "{\\beta", "i}", "=",
                               "[", "\\cos", "(", "\\alpha", ")", "+", "i", "\\sin", "(", "\\alpha", ")", "]", "\\cdot",
                               "[", "\\cos", "(", "\\beta", ")", "+", "i", "\\sin", "(", "\\beta", ")", "]", default_font="思源黑体", color=BLACK)
        EulerFormula4_SourceHansfont = EulerFormula4.set_color(BLACK).set_color_by_tex_to_color_map(color_dict1) \
            .get_new_font_texs(font_dict1)

        Euler2and3_to_4 = AnimationGroup(
            ReplacementTransform(EulerFormula2_SourceHansfont[:3], EulerFormula4_SourceHansfont[:3]),
            Write(EulerFormula4_SourceHansfont[3]),
            ReplacementTransform(EulerFormula3_SourceHansfont[:3], EulerFormula4_SourceHansfont[4: 7]),
            ReplacementTransform(Group(EulerFormula2_SourceHansfont[3], EulerFormula3_SourceHansfont[3]),
                                 EulerFormula4_SourceHansfont[7]),
            ReplacementTransform(EulerFormula2_SourceHansfont[4: 14], EulerFormula4_SourceHansfont[9: 19]),
            Write(VGroup(EulerFormula4_SourceHansfont[8], EulerFormula4_SourceHansfont[19])),
            Write(EulerFormula4_SourceHansfont[20]),
            ReplacementTransform(EulerFormula3_SourceHansfont[4: 14], EulerFormula4_SourceHansfont[22: 32]),
            Write(VGroup(EulerFormula4_SourceHansfont[21], EulerFormula4_SourceHansfont[32])),
            lag_ratio=.5
        )
        self.play(Euler2and3_to_4)
        self.wait(3.)

        EulerFormula5 = MyText("e^", "{", "(", "\\alpha", "+", "\\beta", ")", "i}", "=",
                               "[", "\\cos", "(", "\\alpha", ")", "+", "i", "\\sin", "(", "\\alpha", ")", "]", "\\cdot",
                               "[", "\\cos", "(", "\\beta", ")", "+", "i", "\\sin", "(", "\\beta", ")", "]",
                               default_font="思源黑体", color=BLACK)
        EulerFormula5_SourceHansfont = EulerFormula5.set_color(BLACK).set_color_by_tex_to_color_map(color_dict1) \
            .get_new_font_texs(font_dict1)
        Euler4_to_5 = AnimationGroup(
            ReplacementTransform(VGroup(EulerFormula4_SourceHansfont[0], EulerFormula4_SourceHansfont[4]), EulerFormula5_SourceHansfont[0]),
            AnimationGroup(
                ReplacementTransform(EulerFormula4_SourceHansfont[6], EulerFormula5_SourceHansfont[7]),
                ReplacementTransform(EulerFormula4_SourceHansfont[2], EulerFormula5_SourceHansfont[7]),
                ReplacementTransform(EulerFormula4_SourceHansfont[1], EulerFormula5_SourceHansfont[3]),
                ReplacementTransform(EulerFormula4_SourceHansfont[5], EulerFormula5_SourceHansfont[5]),
                ReplacementTransform(EulerFormula4_SourceHansfont[3], EulerFormula5_SourceHansfont[4]),
                lag_ratio=.1
            ),
            Write(VGroup(EulerFormula5_SourceHansfont[2], EulerFormula5_SourceHansfont[6])),
            ReplacementTransform(EulerFormula4_SourceHansfont[7:], EulerFormula5_SourceHansfont[8:]),
            lag_ratio=.5
        )
        self.play(Euler4_to_5)
        self.wait(3.)

        EulerFormula6 = MyText("\\cos", "(", "\\alpha", ")", "\\cos", "(", "\\beta", ")", "-", "\\sin", "(", "\\alpha",
                               ")", "\\sin", "(", "\\beta", ")",
                               "+", "i}", "[",
                               "\\sin", "(", "\\alpha", ")", "\\cos", "(", "\\beta", ")", "+", "\\cos", "(", "\\alpha",
                               ")", "\\sin", "(", "\\beta", ")",
                               "]",
                               default_font="思源黑体", color=BLACK)
        EulerFormula6_SourceHansfont = EulerFormula6.set_color(BLACK).set_color_by_tex_to_color_map(color_dict1) \
            .get_new_font_texs(font_dict1)
        EulerFormula6_SourceHansfont.next_to(EulerFormula5_SourceHansfont, DOWN)

        self.play(EulerFormula5_SourceHansfont[: 9].align_to, EulerFormula6_SourceHansfont, {"direction": LEFT})
        self.wait(2.)
        print(EulerFormula6_SourceHansfont[18].get_color())
        """
        {
        10: 14 -> 0:4 -> cos \\alpha 29 ~ 33
        23: 27 -> 4:8 -> cos \\beta  24 ~ 28
        16: 20 -> 9:13 ->sin \\alpha 20 ~ 24
        29: 33 -> 13:17              33~ 37
        
        
        }
        
        """
        Euler5_to_6 = AnimationGroup(
            ReplacementTransform(EulerFormula5_SourceHansfont[10: 14].copy(), EulerFormula6_SourceHansfont[0: 4]),
            ReplacementTransform(EulerFormula5_SourceHansfont[23: 27].copy(), EulerFormula6_SourceHansfont[4: 8]),
            FadeIn(EulerFormula6_SourceHansfont[8]),
            ReplacementTransform(EulerFormula5_SourceHansfont[16: 20].copy(), EulerFormula6_SourceHansfont[9: 13]),
            ReplacementTransform(EulerFormula5_SourceHansfont[29: 33].copy(), EulerFormula6_SourceHansfont[13: 17]),
            AnimationGroup(
                ReplacementTransform(EulerFormula5_SourceHansfont[14: 16], EulerFormula6_SourceHansfont[17: 19]),
                ReplacementTransform(EulerFormula5_SourceHansfont[27: 29], EulerFormula6_SourceHansfont[17: 19]),
            ),
            Write(EulerFormula6_SourceHansfont[19]),
            ReplacementTransform(EulerFormula5_SourceHansfont[16: 20], EulerFormula6_SourceHansfont[20: 24]),
            ReplacementTransform(EulerFormula5_SourceHansfont[23: 27], EulerFormula6_SourceHansfont[24: 28]),
            ReplacementTransform(EulerFormula6_SourceHansfont[8].copy(), EulerFormula6_SourceHansfont[28]),
            ReplacementTransform(EulerFormula5_SourceHansfont[10: 14], EulerFormula6_SourceHansfont[29: 33]),
            ReplacementTransform(EulerFormula5_SourceHansfont[29: 33], EulerFormula6_SourceHansfont[33: 37]),
            VFadeOut(VGroup(EulerFormula5_SourceHansfont[9], EulerFormula5_SourceHansfont[20: 23],
                            EulerFormula5_SourceHansfont[33])),
            Write(EulerFormula6_SourceHansfont[37]),
            lag_ratio=.5
        )
        self.play(Euler5_to_6)
        self.wait(3.)
        EulerFormula7 = MyText("\\cos", "(", "\\alpha", "+", "\\beta", ")", "+", "i",
                               "\\sin", "(", "\\alpha", "+", "\\beta", ")", "=",
                               default_font="思源黑体", color=BLACK)
        EulerFormula7_SourceHansfont = EulerFormula7.set_color(BLACK).set_color_by_tex_to_color_map(color_dict1) \
            .get_new_font_texs(font_dict1).align_to(EulerFormula6_SourceHansfont, direction=LEFT)

        Euler5_to_7 = AnimationGroup(
            ReplacementTransform(EulerFormula5_SourceHansfont[8], EulerFormula7_SourceHansfont[14]),
            ReplacementTransform(EulerFormula5_SourceHansfont[3: 6].copy(), EulerFormula7_SourceHansfont[2: 5]),
            ReplacementTransform(EulerFormula5_SourceHansfont[3: 6], EulerFormula7_SourceHansfont[10: 13]),
            ReplacementTransform(EulerFormula5_SourceHansfont[7], EulerFormula7_SourceHansfont[7]),
            to_draw.Every_FadeOut(Group(*EulerFormula5_SourceHansfont[0: 3], *EulerFormula5_SourceHansfont[6])),
            to_draw.Every_Write(VGroup(*EulerFormula7_SourceHansfont[:2], *EulerFormula7_SourceHansfont[5: 7],
                                       *EulerFormula7_SourceHansfont[8: 10], *EulerFormula7_SourceHansfont[13]),
                                run_time=2.),
            lag_ratio=.5
        )

        self.play(Euler5_to_7)
        self.wait(3.)
        EulerFormula8 = MyText("\\cos", "(", "\\alpha", "+", "\\beta", ")", "=", "\\cos", "(", "\\alpha", ")", "\\cos",
                               "(", "\\beta", ")", "-", "\\sin", "(", "\\alpha", ")", "\\sin", "(", "\\beta", ")",
                               default_font="思源黑体", color=BLACK)
        EulerFormula9 = MyText("\\sin", "(", "\\alpha", "+", "\\beta", ")", "=", "\\sin", "(", "\\alpha", ")", "\\cos",
                               "(", "\\beta", ")", "+", "\\cos", "(", "\\alpha", ")", "\\sin", "(", "\\beta", ")",
                               default_font="思源黑体", color=BLACK)

        EulerFormula8_SourceHansfont = EulerFormula8.set_color(BLACK).set_color_by_tex_to_color_map(color_dict1) \
            .get_new_font_texs(font_dict1).align_to(EulerFormula6_SourceHansfont, direction=LEFT).shift(UP * 2)

        EulerFormula9_SourceHansfont = EulerFormula9.set_color(BLACK).set_color_by_tex_to_color_map(color_dict1) \
            .get_new_font_texs(font_dict1).align_to(EulerFormula6_SourceHansfont, direction=LEFT).shift(DOWN * 3)

        Euler67to8 = AnimationGroup(
            ReplacementTransform(EulerFormula7_SourceHansfont[0: 6], EulerFormula8_SourceHansfont[0: 6]),
            ReplacementTransform(EulerFormula7_SourceHansfont[6], EulerFormula8_SourceHansfont[6]),
            ReplacementTransform(EulerFormula6_SourceHansfont[0: 17], EulerFormula8_SourceHansfont[7: 24]),
            lag_ratio=.5
        )

        Euler67to9 = AnimationGroup(
            ReplacementTransform(EulerFormula7_SourceHansfont[8: 14], EulerFormula9_SourceHansfont[0: 6]),
            ReplacementTransform(EulerFormula7_SourceHansfont[14], EulerFormula9_SourceHansfont[6]),
            ReplacementTransform(EulerFormula6_SourceHansfont[20: 37], EulerFormula9_SourceHansfont[7: 24]),
            to_draw.UnWrite(Group(*EulerFormula6_SourceHansfont[17: 20], *EulerFormula6_SourceHansfont[37],
                                  *EulerFormula7_SourceHansfont[7])),
            lag_ratio=.5
        )

        self.play(Euler67to8)
        self.play(Euler67to9)
        self.wait(3.)

        self.play(EulerFormula8_SourceHansfont.shift, DOWN * 2 + RIGHT * 2,
                  EulerFormula9_SourceHansfont.shift, UP * 2 + RIGHT * 2)
        self.wait(2.)
        self.play(ShowPassingFlashAround(Group(*EulerFormula8_SourceHansfont,
                                               *EulerFormula9_SourceHansfont),
                                         surrounding_rectangle_config=dict(color=BLUE_D)))
        self.wait(2.)


class last(TripleScene2):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def setup(self):
        self.wait()
        text = SourceHansfont("bgm: Pacific,\n 制作: by bilibili.洛洛洛-洛洛洛_dx,\n 剪辑: by bilibili.zhengyang051119,\n马上开新坑~")\
            .set_color_by_gradient("#42C5FF", "#54FDFF")

        self.play(Write(text))
        self.wait(3.)
        self.play(to_draw.SpinOutToNothing(text=text))


class T(Scene):
    def construct(self):
        color_dict1 = {"e^": "#71D9DD", "{\\theta": "#729DDD", "\\theta": "#729DDD", "\\cos": BLUE_B, "i}": GREEN,
                       "i": GREEN,
                       "\\sin": BLUE_D, "{\\alpha": "#729DDD", "\\alpha": "#729DDD", "{\\beta": "#729DDD",
                       "\\beta": "#729DDD",
                       "+": "#84DDC8", "-": "#84DDC8"}
        font_dict1 = {"e^": "e", "{\\theta": "θ", "i}": "i", "\\theta": "θ", "\\cos": "cos", "\\sin": "sin",
                      "{\\alpha": "α",
                      "\\alpha": "α", "{\\beta": "β", "\\beta": "β", "\\cdot": "·", "\\\\": "\n"}
        EulerFormula6 = MyText("\\cos", "(", "\\alpha", ")", "\\cos", "(", "\\beta", ")", "-", "\\sin", "(", "\\alpha",
                               ")", "\\sin", "(", "\\beta", ")",
                               "+", "i}", "(",
                               "\\sin", "(", "\\alpha", ")", "\\cos", "(", "\\beta", ")", "+", "\\cos", "(", "\\alpha",
                               ")", "\\sin", "(", "\\beta", ")",
                               ")",
                               default_font="思源黑体", color=WHITE)
        EulerFormula6_SourceHansfont = EulerFormula6.set_color_by_tex_to_color_map(color_dict1) \
            .get_new_font_texs(font_dict1)
        self.add(EulerFormula6_SourceHansfont)



