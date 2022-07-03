from manimlib.imports import *
from luoluoluo_useful.imports import *
from luoluoluo_useful.MyFontLuoluoluo.MyFontSourceHansfont import SourceHansfont, SourceHansfontDot, WildlyArrogantPixelFont
from luoluoluo_useful.MySceneLuoluoluo.MyScenes import LuoScene
from luoluoluo_useful.imports import LuoVLast
from manim_sandbox.utils.imports import PassingRectangle, debugTeX

VG = VGroup
MT2P = MTwoPointLine
WAIT_TIME = 3.
WAIT_SMALL_TIME = 1.
COLOR = ["#5D9CB9", "#4CB95C", "#B9AE5D", "#417BB9", "#9179B9", "#5D87B9"]

class Begin(LuoVBegin):
    CONFIG = {
        "TextAbout": "“另类”的加速度 \n 明溪一中   高一(1)班    李依闰"
    }

def click(self, *mob: Mobject, Wait=True, remove=False):
    """使物品闪烁
    - Wait 是否闪烁后停顿
    """
    self.remove(*mob)
    self.add_sound("click.mp4")
    self.wait(0.075)
    if not remove:
        self.add(*mob)

    if Wait: self.wait(0.075)


# class ForReLi(FourierOfPiSymbol):
#     CONFIG = {
#         "camera_config": {
#             "background_color": WHITE,  # 背景为白色
#         },
#         "colors": [
#             BLUE_D,
#             BLUE_C,
#             BLUE_E,
#             GREY_BROWN,
#             "#EEB984",
#         ],
#         "vector_config": {
#             "buff": 0,
#             "max_tip_length_to_length_ratio": 0.35,
#             "tip_length": 0.15,
#             "max_stroke_width_to_length_ratio": 10,
#             "stroke_width": 2,
#             "stroke_color": ["#EEA8E6", "#A1ECEE", "B1EE76", "93A6EE"],
#         },
#         "n_vectors": 100,
#         "drawn_path_color": GREY,#"#EEABE7"
#         "slow_factor": .2
#     }
#
#     def construct(self):
#         self.add_vectors_circles_path()
#         for n in range(self.n_cycles):
#             self.run_one_cycle()
#
#     def get_drawn_path(self, vectors, stroke_width=None, **kwargs):
#         if stroke_width is None:
#             stroke_width = self.drawn_path_stroke_width
#         path = self.get_vector_sum_path(vectors, **kwargs)
#         broken_path = CurvesAsSubmobjects(path)
#         broken_path.curr_time = 0
#
#         def update_path(path, dt):
#             # alpha = path.curr_time * self.get_slow_factor()
#             alpha = self.get_drawn_path_alpha()
#             n_curves = len(path)
#             for a, sp in zip(np.linspace(0, 1, n_curves), path):
#                 b = alpha - a
#                 if b < 0:
#                     width = 0
#                 else:
#                     width = stroke_width
#                 sp.set_stroke(width=width)
#             path.curr_time += dt
#             return path
#
#         broken_path.set_color(self.drawn_path_color)
#         broken_path.add_updater(update_path)
#         return broken_path
#
#     def add_vectors_circles_path(self):
#         path = self.get_path()
#         coefs = self.get_coefficients_of_path(path)
#         vectors = self.get_rotating_vectors(coefficients=coefs)
#         circles = self.get_circles(vectors)
#         self.set_decreasing_stroke_widths(circles)
#         # approx_path = self.get_vector_sum_path(circles)
#         drawn_path = self.get_drawn_path(vectors, stroke_width=path.get_stroke_width())
#         if self.start_drawn:
#             self.vector_clock.increment_value(1)
#
#         path_copy = path.copy()
#         self.add(path_copy.set_stroke(width=.0))
#         self.add(vectors)
#         self.add(circles)
#         self.add(drawn_path)
#
#         self.vectors = vectors
#         self.circles = circles
#         self.path = path
#         self.drawn_path = drawn_path
#
#     def run_one_cycle(self):
#         time = 1 / self.slow_factor
#         self.wait(time)
#
#     def set_decreasing_stroke_widths(self, circles):
#         mcsw = self.max_circle_stroke_width
#         for k, circle in zip(it.count(1), circles):
#             circle.set_stroke(width=max(
#                 # mcsw / np.sqrt(k),
#                 mcsw / k,
#                 mcsw,
#             ))
#         return circles
#
#     def get_path(self):
#         sq1 = SVGMobject("PiCreatures_plain")[4].scale(3.)
#         # tex_mob.set_height(6)
#         path = sq1.family_members_with_points()[0]
#         path.set_style(fill_opacity=.1, stroke_opacity=.9, stroke_color="#7CBDE2", ).set_color(["#54ABE0", "#E08DC2", "#E0825B", "#A7E071"])
#         # path.set_stroke(WHITE, 1).set_color(["#54ABE0", "#E08DC2", "#E0825B", "#A7E071"])
#         return path






# class beginning(LuoScene):
#     def construct(self):
#         # """NH_3 \\cdot H_2O + CO_2 == NH_4HCO_3"""
#
#         sq1 = Square(side_length=4).set_style(fill_opacity=.1, stroke_opacity=.9, stroke_color="#7CBDE2", ).set_color(["#54ABE0", "#E08DC2", "#E0825B", "#A7E071"])
#         '''获取方形坐标'''
#         sq1.P_UL = np.array([sq1.get_left()[0], sq1.get_top()[1], 0.])
#         sq1.P_UR = np.array([sq1.get_right()[0], sq1.get_top()[1], 0.])
#         sq1.P_DL = np.array([sq1.get_left()[0], sq1.get_bottom()[1], 0.])
#         sq1.P_DR = np.array([sq1.get_right()[0], sq1.get_bottom()[1], 0.])
#         P_UL = sq1.P_UL.copy()
#         P_UR = sq1.P_UR.copy()
#         P_DL = sq1.P_DL.copy()
#         P_DR = sq1.P_DR.copy()
#         sq_Group = VG()
#         line1GrLeft = VG()
#         line2GrDown = VG()
#         point_Group = list([P_UR, P_DL, (P_UR + P_DL) / 2.])
#         Up_Group = list([P_UR, P_UL, (P_UR + P_UL) / 2.])
#         Right_Group = list([P_UR, P_DR, (P_UR + P_DR) / 2.])
#         getList = lambda listGroup: listGroup.append((listGroup[0] + listGroup[-1]) / 2.)
#         self.play(ShowCreation(sq1))
#         for x in range(7):
#             sq_Group.add(
#                 Square(side_length=sq1.side_length / (2 ** (x + 1)) if sq1.side_length / (2 ** (x + 1)) < 4. else sq1.side_length / (2 ** (x + 1)) - .05).move_to((point_Group[-2] + point_Group[-1]) / 2).
#                 set_style(fill_color="#54CAFF", fill_opacity=.9, stroke_opacity=0.)
#                 .round_corners(sq1.side_length / (2 ** (x + 1)) / 20.)
#                 .set_color(["#54ABE0", "#E08DC2", "#E0825B", "#A7E071"])
#             )
#
#
#
#             line1GrLeft.add(Line(point_Group[-1], Up_Group[-1]).set_stroke(color=YELLOW, width=2))
#             line2GrDown.add(Line(point_Group[-1], Right_Group[-1]).set_stroke(color=YELLOW, width=2))
#
#             getList(point_Group)
#             getList(Up_Group)
#             getList(Right_Group)
#             if x == 7:
#                 self.play(FadeIn(sq_Group[-1]), run_time=.25)
#                 break
#             self.play(FadeIn(sq_Group[-1]), Write(line1GrLeft[-1]), Write(line2GrDown[-1]), run_time=.5)
#         text = TexMobject("\\sum_{n=1}^{\\infty} \\frac{1}{4^{n}}=\\frac{1}{4}+\\frac{1}{16}+\\frac{1}{64}+\\frac{1}{256}+\\cdots=\\frac{1}{3}").next_to(sq1, DOWN, buff=SMALL_BUFF)[0]
#         NaOH(text)
#         self.play(to_draw.WriteRandom(text), run_time=.7)
#         self.play(
#             AnimationGroup(*[
#                 ReplacementTransform(sq_Group[i].copy(), text[j: z])
#                 for i, j, z in zip(range(4), [10, 14, 19, 24], [13, 18, 23, 29])],
#                 ReplacementTransform(sq_Group[4:].copy(), text[30: 33]),
#                 ReplacementTransform(sq_Group.copy(), text[34: 37]), lag_ratio=.3)
#         )
#
#         for x in range(7):
#             click(self, sq_Group[len(sq_Group) - 1 - x])
#
#         for _ in range(4):
#             click(self, *VG(*[sq_Group[len(sq_Group) - 2 * x] for x in range(1, 4)]))
#             click(self, *VG(*[sq_Group[len(sq_Group) - 2 * x - 1] for x in range(1, 4)]))
#
#         for x in range(7):  # TODO 用更聪明的办法解决
#             click(self, sq_Group[len(sq_Group) - 1 - x], remove=True)
#
#         # debugTeX(self, text)
#         print(Up_Group)
#
#         SquareLeft = VG(sq1, line1GrLeft, line2GrDown)
#
#         self.play(SquareLeft.rotate, dict(angle=PI / 4.), SquareLeft.scale, .5)
#
#         self.wait()
#
#         self.play(SquareLeft.next_to, dict(mobject_or_point=text, direction=LEFT, buff=- LARGE_BUFF + 3 * SMALL_BUFF), SquareLeft.scale, dict(scale_factor=.4))
#
#         self.wait()
#         """
#         # 规定光泽角度
#         sheenAngle = 75 * DEGREES
#         #
#         sq_Group.set_sheen(
#             0.5,
#             np.array([np.sin(sheenAngle),
#                       np.cos(sheenAngle),
#                       0.]))"""
#
#
#         EulerFormula_SourceHansfont = VG(*Text("NH₃∙H₂O + CO₂ == NH₄HCO₃", font="Consolas"))
#         te = Text("NH₄HCO₃ + HCl == NH₄Cl + H₂O + CO₂↑", font="Consolas").next_to(EulerFormula_SourceHansfont, DOWN, buff=SMALL_BUFF)\
#             .align_to(EulerFormula_SourceHansfont, LEFT)
#         EulerFormula_SourceHansfont.add(*te)
#         EulerFormula_SourceHansfont = NaOH(EulerFormula_SourceHansfont, 0, "#29ABCA", "#58C4DD", "#C59978")
#         XyClouded = ImageMobject("XyClouded").move_to(np.array([2., 1., 0.]))
#         rect_xy = PassingRectangle(XyClouded).mobject.set_style(fill_color=WHITE, fill_opacity=1.)
#
#         lineMi = Line(UP, DOWN, stroke_width=8, color=BLACK).move_to(XyClouded.get_right())
#
#         self.add(rect_xy)
#         self.add(XyClouded.add_updater(lambda t: t.set_plot_depth(-1)))
#         EulerFormula_SourceHansfont.next_to(XyClouded.copy().shift(RIGHT * 2), LEFT)
#         turn_animation_into_updater(ApplyMethod(XyClouded.shift, RIGHT * 2))
#         self.play(to_draw.WriteRandom(EulerFormula_SourceHansfont), Write(lineMi))
#         line2 = Line(LEFT * 6., RIGHT * 6., stroke_width=8, color=BLACK).next_to(VG(EulerFormula_SourceHansfont, BackgroundRectangle(XyClouded)), DOWN, buff=MED_SMALL_BUFF)
#         text1 = NaOH(Text("碳酸氢铵   ×   芸星班", color=BLACK, font="千图纤墨体").next_to(line2, DOWN, buff=MED_LARGE_BUFF).scale(1.7), 0, colors=[BLACK, GREY]).set_opacity(.7)
#         self.play(Write(line2))
#         self.play(DrawBorderThenFill(text1))
#
#
#
#         self.wait(2.)


class First(LuoScene):

    def construct(self):
        axes = Axes()
        self.play(Write(axes))

        self.wait()

        self.play(Write(self.text))

        self.wait()

        func1 = axes.get_graph(lambda x: 2 * x ** 2 - 8 * x + 6).set_color("#96DDFF")
        func2 = axes.get_graph(lambda x: x ** 2 - 2 * x - 3).set_color("#FFD6F6")
        func3 = axes.get_graph(lambda x: 4 * x - 12).scale(.5).set_color("#7EFFD1")
        self.play(ShowCreation(func1))

        self.play(ShowCreation(func2))

        self.play(ShowCreation(func3))
        self.wait()

    def set_other1(self):
        self.text = TexMobject(r"4 x-12 \leqslant a x^{2}+b x+c \leqslant 2 x^{2}-8 x+6").scale(.5).set_color(BLACK).to_edge(UR, .5)


class Second(LuoScene):

    CONFIG = {
        "": ""
    }

    def construct(self):
        self.wait()
        self.add(self.captions_mob[0][0])
        self.play(to_draw.WriteRandom((NaOH(self.captions_mob[0])[1:])))

        self.wait()
        self.play(FadeInFromDown(self.obj1))
        self.play(ShowCreation(self.vec))

        self.wait()
        self.add(self.obj1_copy.set_plot_depth(-1))
        self.add(self.disten)
        self.play(self.obj1.shift, RIGHT * 3)
        self.play(DrawBorderThenFill(self.s.next_to(self.disten, DOWN)))
        self.disten.clear_updaters()

        self.play(Write(VG(self.formulaV[:2], self.formulaV[3:])), ReplacementTransform(self.s, self.formulaV[2]))
        self.play(FadeOut(VG(self.obj1, self.vec, self.obj1_copy, self.disten)), self.formulaV.move_to, ORIGIN)

        self.wait()

        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))

        self.wait()

        self.play(FadeOut(self.formulaV[1:]))
        self.wait()
        self.play(Write(VG(self.formulaA[:3], self.formulaA[4:])), ReplacementTransform(self.formulaV[0], self.formulaA[3]))

        self.wait()
        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))
        self.wait()

        self.play(AnimationGroup(ApplyMethod(self.formulaA.shift, UP * 1.5), AnimationGroup(Write(self.formulaA1), Write(self.formulaA2)), lag_ratio = .7))

        self.wait(8.)

        self.play(ReplacementTransform(self.captions_mob[2], NaOH(self.captions_mob[3])))

        self.wait(2.)

        self.play(ReplacementTransform(self.formulaA, self.formulaA_), FadeOut(VG(self.formulaA1, self.formulaA2)))

        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[3], NaOH(self.captions_mob[4])))

        Countdown = TexMobject(r"(2 \phi - 1)^2").to_corner(DR, buff=LARGE_BUFF)
        for x in range(5):
            if x == 0:
                self.play(Write(Countdown.set_color(["#85D0EC", "#F77D6B", "#C56CB3", "#FA9E5A", "#5FC2C0"][x])))
                self.wait()

            else:
                self.play(Countdown.become,
                          TexMobject([r"(2 \phi - 1)^2", r"{\pi \over \arctan{1}}", r"[\ln(21)]",
                                      r"\sum_{i=0}^{+ \infty}{1 \over 2^i}", r"-e^{\pi i}"][x])
                          .set_color(["#85D0EC", "#F77D6B", "#C56CB3", "#FA9E5A", "#5FC2C0"][x]).to_corner(DR, buff=LARGE_BUFF))
            self.play(ShowCreationThenFadeAround(Countdown, surrounding_rectangle_config={"color": ["#85D0EC", "#F77D6B", "#C56CB3", "#FA9E5A", "#5FC2C0"][x]}))
        self.play(FadeOut(Countdown), self.formulaA_.to_corner, UR, dict(buff=LARGE_BUFF))
        self.wait()

        self.play(ReplacementTransform(self.captions_mob[4], NaOH(self.captions_mob[5])))

        self.wait(5.)

        self.play(ReplacementTransform(self.captions_mob[5], NaOH(self.captions_mob[6])))

        self.wait(5.)

        self.play(Write(self.formula1))

        self.wait()

        self.play(ReplacementTransform(self.captions_mob[6], NaOH(self.captions_mob[7])))
        self.wait(2.)

        self.play(Write(self.formula2))
        self.wait()

        self.play(ShowCreationThenFadeAround(self.formulaA_, surrounding_rectangle_config=dict(color="#7BBDD2")))
        self.wait(3.)

        self.play(Write(self.formula3))
        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[7], NaOH(self.captions_mob[8])))
        self.wait(3.)

        self.play(Write(self.formula4))
        self.wait(3.)
        self.play(ReplacementTransform(self.captions_mob[8], NaOH(self.captions_mob[9])))
        self.wait(3.)
        self.play(ShowCreation(self.formula5))
        self.wait(3.)
        self.play(ReplacementTransform(self.captions_mob[9], NaOH(self.captions_mob[10])))
        self.wait()
        self.play(Indicate(self.formula5, color="#B76497"))
        self.wait(3.)
        self.play(to_draw.WriteRandom(self.formula6))
        self.wait(3.)

        self.play(to_draw.UnWrite(VG(self.formula1, self.formula2, self.formula3, self.formula4, self.formula5, self.formulaA_)),
                  self.formula6.move_to, ORIGIN, self.formula6.scale, 1.5, self.formula6[0].set_opacity, 0.)

        self.wait()

        sur = SurroundingRectangle(self.formula6[1:]).set_color(RED)

        self.play(ReplacementTransform(self.captions_mob[10], NaOH(self.captions_mob[11])))

        self.wait()

        self.play(ShowCreation(sur))

        self.wait(3.)

        self.play(Uncreate(sur))

        self.play(self.formula6.scale, 1 / 1.5, self.formula6.to_corner, dict(corner=UR, buff=LARGE_BUFF))

        self.wait(2.)

        self.play(ReplacementTransform(self.captions_mob[11], NaOH(self.captions_mob[12])))  # 既然已知了v(t), 我们就可以对其简单操作求出s(t)

        self.wait(1. + .5)

        self.play(Write(self.formula7))  # 显示s(t)的推导

        self.wait(3.)
        formula7_copy = self.formula7[21:].copy().scale(1 / 1.5).next_to(self.formula6[1:], DOWN, buff=MED_SMALL_BUFF).align_to(self.formula6[1:], LEFT)

        self.play(to_draw.UnWrite(self.formula7[:21]),
                  self.formula7[21:].become, formula7_copy)

        self.wait(2.)

        self.wait()

    def change_cap(self):
        self.caps = [
            "我们在初中时就知道：速度v = s / t",
            "而在高中, 我们将会学另一个物理量——加速度a=Δv / t",
            "如若加速度a恒定, 那么我们对以上公式很熟悉",
            "但是如果加速度并不是这样定义的, 而是a=Δv / s, 那么这两条公式还成立吗?",
            "让我们简单分析一下......",
            "如果我们将这种加速度称为\"另类加速度\", 并将正常加速度记为\'a原\'",
            "设物体速度随时间变化的函数为 v(t);\n物体加速度随时间变化的函数为 a原(t)。\n由速度和加速度定义知:",
            "这里我们用一些技巧, 把式子改写成这样",
            "当另类加速度保持不变, 即物体做匀另类变速加速度时, 设a另=M",
            "将a原(t)用其定义式替换",
            "这是我们小学二年级学过的简单方程, 相信大家闭着眼睛都知道v(t)是什么了",
            "(这里M为常量)",
            "既然已知了v(t), 我们就可以对其简单操作求出s(t)"
        ]

    def setupPic(self):
        self.obj1 = Square().set_style(fill_color=BLUE, stroke_color=BLUE_B, fill_opacity=.7).shift(LEFT * 1.5)
        self.obj1_copy = self.obj1.copy().set_opacity(.3)
        self.vec = Vector(RIGHT * 2, color=GREEN).add_updater(lambda obj: obj.next_to(self.obj1.get_center(), RIGHT, buff=0.))
        self.disten = DoubleArrow(color=BLUE).add_updater(lambda obj: obj.become(DoubleArrow(start=self.obj1_copy.get_left(), end=self.obj1.get_left(), color = PINK)))
        self.formulaV = TexMobject("v", "=", "{s", " \\over", "t}").set_color(BLACK).move_to(np.array([3., 3., 0.]))
        self.s = SourceHansfont("s").set_color(ORANGE)
        self.formulaV[0].set_color("#94D4A9")
        self.formulaV[2].set_color(ORANGE)

        self.formulaA = TexMobject("a", "=", "{\\Delta",  "v", "\\over", "t}").set_color(BLACK)
        self.formulaA[2: 4].set_color("#94D4A9")
        self.formulaA[0].set_color(RED)

        self.formulaA_ = TexMobject("a", "=", "{\\Delta", "v", "\\over", "s}").set_color(BLACK)
        self.formulaA_[2: 4].set_color("#94D4A9")
        self.formulaA_[0].set_color(RED)
        self.formulaA_[-1].set_color("#B9B348")

        self.formulaA1 = NaOH(TexMobject(r"\overline{v} = v_{t \over 2}={v_t + v_0 \over2}")[0], 0, *COLOR).align_to(self.formulaA, LEFT)
        self.formulaA2 = NaOH(TexMobject(r"v_{s \over 2} = \sqrt{v_{t}^2+v_0^2\over 2}")[0], 0, *COLOR).next_to(self.formulaA1, DOWN).align_to(self.formulaA1, LEFT)

        self.formula1 = NaOH(TexMobject("v(t) = \\frac{\\mathrm{d}}{\\mathrm{d}t}s(t), \\ \\ \\ a_\\text{原}(t) = \\frac{\\mathrm{d}}{\\mathrm{d}t}v(t)")[0], 0, *COLOR).to_corner(UL, buff = SMALL_BUFF).shift(LEFT * 1.0).scale(.7)
        self.formula2 = NaOH(TexMobject("v(t) = \\frac{\\mathrm{ds}}{\\mathrm{d}t}(t), \\ \\ \\ a_\\text{原}(t) = \\frac{\\mathrm{dv}}{\\mathrm{d}t}(t)")[0], 0, *COLOR).scale(.7).next_to(self.formula1, DOWN, buff=SMALL_BUFF).align_to(self.formula1, LEFT)
        self.formula3 = NaOH(TexMobject("a_{\\text{另}}= \\frac{\\mathrm{dv}}{\\mathrm{d}s}=\\frac{\\frac{\\mathrm{d} v}{\\mathrm{d} t}}{\\frac{\\mathrm{d} s}{\\mathrm{d} t}} = \\frac{\\frac{\\mathrm{d} v}{\\mathrm{d} t} (t)}{\\frac{\\mathrm{d} s}{\\mathrm{d} t}(t)} = \\frac{a_\\text{原}(t)}{v(t)}")[0], 0, *COLOR).scale(.7).next_to(self.formula2, DOWN, buff=SMALL_BUFF).align_to(self.formula2, LEFT)
        self.formula4 = NaOH(TexMobject("\\frac{a_\\text{原}(t)}{v(t)}  =a_{\\text{另}}=M\\Rightarrow a_\\text{原}(t)=M \\cdot v(t)")[0], 0, *COLOR).scale(.7).next_to(self.formula3, DOWN, buff=SMALL_BUFF).align_to(self.formula3, LEFT)
        self.formula5 = NaOH(TexMobject("\\frac{\\mathrm{d} }{\\mathrm{d} t}v(t) = M\\cdot v(t) ")[0], 0, *COLOR).scale(.7).next_to(self.formula4, DOWN, buff=SMALL_BUFF).align_to(self.formula4, LEFT)
        self.formula6 = NaOH(TexMobject("\\Rightarrow v(t)=e^{M\\cdot t}")[0], 0, *COLOR).scale(.7).next_to(self.formula5, DOWN, buff=SMALL_BUFF).align_to(self.formula5, LEFT)
        self.formula7 = NaOH(TexMobject("s(t) = \\int v(t)\\mathrm{d}x = \\frac{e^{Mt}}{M}+C \\Rightarrow s(t) = \\frac{e^{Mt}}{M}+C")[0], 0, *COLOR).scale(.7 * 1.5)


class Third(Second):

    def change_cap(self):
        self.caps = [
            "既然已知了v(t), 我们就可以对其简单操作求出s(t)",
            "如此, 我们可以求匀另类变速度运动的中点时刻速度和中点位移速度",
            "我们先求其中点位移速度",
            "我们先用t0表示出初速v0、末速vt、初位置s0、末位置st",
            "再解一个简单的公式",
            "这个式子很明显了吧",
            "匀另类变速度运动的中点位移速度就是初速与末速的算数平均数"


        ]

    def construct(self):
        self.add(self.formula6[1:].to_corner(UR, LARGE_BUFF), self.formula7[21:].scale(1 / 1.5).next_to(self.formula6[1:], DOWN, buff=MED_SMALL_BUFF).align_to(self.formula6[1:], LEFT), NaOH(self.captions_mob[0]))

        self.play(self.formula7[21:].become, NaOH(self.formula7[21:].copy(), 0, *COLOR))

        self.wait(2.)

        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))  # 如此, 我们可以求匀另类变速度运动的中点时刻速度和中点位移速度

        self.wait(5.)

        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))  # 我们先求其中点位移速度

        heading = NaOH(Text("中点位移速度", color=BLACK, font="千图纤墨体").scale(1.3), 0, colors=[BLACK, GREY]).set_opacity(.7).to_corner(UP, buff=SMALL_BUFF)

        self.wait(2.)

        self.play(DrawBorderThenFill(heading))

        text_1 = self.text_1
        self.wait()

        self.play(to_draw.RandomGrowFromNothing(*text_1))

        self.wait(2.)

        self.play(ReplacementTransform(self.captions_mob[2], NaOH(self.captions_mob[3])))  # 我们先用t0表示出初速v0、末速vt、初位置s0、末位置st

        self.wait()

        self.play(Write(self.formula2_1), Write(self.formula2_2), Write(self.formula2_3), Write(self.formula2_4))

        vg1 = VG(self.formula2_1, self.formula2_2, self.formula2_3, self.formula2_4)
        vg1_copy = vg1.copy().next_to(self.formula7[21:], DOWN, buff=MED_SMALL_BUFF).next_to(RIGHT_SIDE, LEFT, buff=SMALL_BUFF)

        self.play(VG(self.formula6[1:], self.formula7[21:]).align_to, dict(mobject_or_point=vg1_copy, direction=LEFT),
                  vg1.become, vg1_copy)

        self.wait(2.)

        self.play(ReplacementTransform(self.captions_mob[3], NaOH(self.captions_mob[4])))  # 再解一个简单的公式

        self.wait(2.)

        self.formula2_5[34:].next_to(self.formula2_5[11: 34], DOWN, buff=SMALL_BUFF).align_to(self.formula2_5[11: 34], LEFT)
        self.play(Write(self.formula2_5))

        self.wait()

        formula2_5_34_to_copy = self.formula2_5[34:].copy().align_to(self.formula2_5[11: 34], DL)
        self.play(self.formula2_5[34:].become, formula2_5_34_to_copy,
                  FadeOutAndShift(self.formula2_5[11: 34], UP))

        vgc = NaOH(VG(self.formula2_5[:12], self.formula2_5[34:]).copy(), 0, *COLOR)

        self.play(VG(self.formula2_5[:12], self.formula2_5[34:]).become, vgc, run_time=1.5)

        self.wait()

        self.play(ShowCreation(self.formula2_6))

        self.wait(4.)

        self.play(FadeOutAndShift(self.formula2_6, UP), FadeInFromDown(self.formula2_7))

        self.wait(2.)

        self.play()
        self.formula2_7_copy.next_to(self.formula2_7, RIGHT, coor_mask=UP).align_to(self.formula2_7, LEFT)
        self.play(FadeOut(self.formula2_7[1:9]), self.formula2_7[9:].next_to, dict(mobject_or_point=self.formula2_7[0], direction=RIGHT, buff=SMALL_BUFF, coor_mask=RIGHT))
        self.formula2_7_copy[9:].next_to(self.formula2_7[0], RIGHT, buff=SMALL_BUFF, coor_mask=RIGHT)
        self.wait(.5)
        self.play(FadeOutAndShiftDown(VG(self.formula2_7[18: 20], self.formula2_7[36: 38])), self.formula2_7[20: 36].next_to, dict(mobject_or_point=self.formula2_7[17], direction=RIGHT, buff=SMALL_BUFF))
        self.wait(.5)
        self_formula2_7_copy = self.formula2_7.copy()
        self_formula2_7_copy[12: 18].next_to(self.formula2_7_copy[9], RIGHT, buff=SMALL_BUFF, coor_mask=RIGHT)
        self_formula2_7_copy[26: 35].next_to(self.formula2_7[20], RIGHT, buff=SMALL_BUFF, coor_mask=RIGHT)
        self.play(ReplacementTransform(self.formula2_7[9: 12], self.formula2_7_copy[9]), ReplacementTransform(VG(self.formula2_7[21: 26], self.formula2_7[35]), self.formula2_7_copy[9]),
                  self.formula2_7[12: 18].become, dict(mobject=self_formula2_7_copy[12: 18]), self.formula2_7[26: 35].become, dict(mobject=self_formula2_7_copy[26: 35]))

        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[4], NaOH(self.captions_mob[5])))  # 这个式子很明显了吧
        self.wait(2.)

        self.formula2_7_last.next_to(self.formula2_7, RIGHT, buff=SMALL_BUFF, coor_mask=UP).align_to(self.formula2_7[0], LEFT)
        self.play(ReplacementTransform(VG(self.formula2_7[0], self.formula2_7_copy[9], self.formula2_7[12: 18], self.formula2_7[20], self.formula2_7[26: 35]), self.formula2_7_last))

        self.wait(3.)

        self.play(Write(self.formula2_8))
        self.wait()
        # self.add(self.formula2_8_last.shift(DOWN))

        self.play(
            *[
                ReplacementTransform(self.formula2_8[x1: y1], self.formula2_8_last[x2: y2])
                #                       x1 y1 x2 y2
                for x1, y1, x2, y2 in ([0, 1, 0, 1],
                                       [1, 2, 12, 13],
                                       [2, 7, 1, 6],
                                       [7, 12, 6, 11],)
            ],
            Write(self.formula2_8_last[11: 12]))
        self.play(
            ApplyMethod(self.formula2_8_last[1:].move_to, ORIGIN),
            FadeOut(VG(self.text_1, self.formula2_1, self.formula2_2, self.formula2_3, self.formula2_4, self.formula2_5[0: 12], self.formula2_5[34: 52],
                       self.formula2_7_last, self.formula6[1: 10], self.formula7[21: 33], self.formula2_8_last[0]))
        )
        self.play(ReplacementTransform(self.captions_mob[5], NaOH(self.captions_mob[6])))  # 匀另类变速度运动的中点位移速度就是初速与末速的算数平均数
        self.formula2_8_last = self.formula2_8_last[1:]
        self.suring = SurroundingRectangle(self.formula2_8_last, buff=MED_SMALL_BUFF).set_color(["#66CCFF", "#BB6611"])
        self.play(ShowCreation(self.suring))
        self.wait(1.5)
        self.play(to_draw.UnBorderThenFade(self.suring))
        self.wait()
        self.play(self.formula2_8_last.to_corner, dict(corner=UR, buff=LARGE_BUFF))

        # from manim_sandbox.utils.imports import debugTeX
        # debugTeX(self, self.formula2_5)

        self.wait()

    def set_other1(self):
        self.addNumberOfOthers()
        self.text_1 = NaOH(TextMobject("如果我们设初速度为${v_0}$, 末速度为$v_t$, 初时刻为$t_0$, 末时刻为$t_1$"), 0, colors=[BLACK, GREY]).scale(.5).move_to(np.array([-2.7, 2.3, 0.]))
        self.formula2_1 = NaOH(TexMobject("v_0=v(t_0)=e^{Mt_0}")[0], 0, *COLOR).scale(.7).next_to(self.text_1, DOWN, buff=SMALL_BUFF).align_to(self.text_1, LEFT)
        self.formula2_2 = NaOH(TexMobject("v_t=v(t_1)=e^{Mt_1}")[0], 0, *COLOR).scale(.7).next_to(self.formula2_1, DOWN, buff=SMALL_BUFF).align_to(self.formula2_1, LEFT)
        self.formula2_3 = NaOH(TexMobject("s_0=s(t_0)=\\frac{e^{Mt_0}}{M}+C")[0], 0, *COLOR).scale(.7).next_to(self.formula2_2, DOWN, buff=SMALL_BUFF).align_to(self.formula2_2, LEFT)
        self.formula2_4 = NaOH(TexMobject("s_t=s(t_1)=\\frac{e^{Mt_1}}{M}+C")[0], 0, *COLOR).scale(.7).next_to(self.formula2_3, DOWN, buff=SMALL_BUFF).align_to(self.formula2_3, LEFT)
        self.formula2_5 = NaOH(TexMobject("s_{\\text{中点}}=\\frac{s_0+s_t}{2}=\\frac{1}{2}(\\frac{e^{Mt_0}}{M}+C+\\frac{e^{Mt_1}}{M}+C)=\\frac{1}{2M}(e^{Mt_0}+e^{Mt_1})+C")[0], 0, *COLOR).scale(.7).next_to(self.text_1, DOWN, buff=SMALL_BUFF).align_to(self.text_1, LEFT)
        self.formula2_6 = NaOH(TexMobject("\\text{设}s(t_{\\frac{s}{2}})=s_\\text{中点}=\\frac{1}{2M}(e^{Mt_0}+e^{Mt_1})+C")[0], 0, *COLOR).scale(.7).next_to(self.formula2_5, DOWN, buff=SMALL_BUFF).align_to(self.formula2_5, LEFT)
        self.formula2_7 = NaOH(TexMobject("\\therefore s(t_{\\frac{s}{2}})=\\frac{1}{M}e^{Mt_\\frac{s}{2}}+C=\\frac{1}{2M}(e^{Mt_0}+e^{Mt_1})+C")[0], 0, *COLOR).scale(.7).next_to(self.formula2_5, DOWN, buff=SMALL_BUFF).align_to(self.formula2_5, LEFT)
        self.formula2_7_copy = NaOH(TexMobject("\\therefore s(t_{\\frac{s}{2}})=2e^{Mt_\\frac{s}{2}}+C=\\frac{1}{2M}(e^{Mt_0}+e^{Mt_1})+C")[0], 0, *COLOR).scale(.7).next_to(self.formula2_5, DOWN, buff=SMALL_BUFF).align_to(self.formula2_5, LEFT)
        self.formula2_7_last = NaOH(TexMobject("\\therefore 2 e^{M t \\frac{s}{2}}=e^{M t_{0}}+e^{M t_{1}}")[0], 0, *COLOR).scale(.7).next_to(self.formula2_5, DOWN, buff=SMALL_BUFF).align_to(self.formula2_5, LEFT)
        self.formula2_8 = NaOH(TexMobject("\\therefore 2v_{\\frac{s}{2}}=v_0+v_t")[0], 0, *COLOR).scale(.7).next_to(self.formula2_7_last, DOWN, buff=SMALL_BUFF).align_to(self.formula2_7_last, LEFT).shift(.5 * DOWN)
        self.formula2_8_last = NaOH(TexMobject("\\therefore v_{\\frac{s}{2}}=\\frac{v_0+v_t}{2}")[0], 0, *COLOR).scale(.7).next_to(self.formula2_7_last, DOWN, buff=SMALL_BUFF).align_to(self.formula2_7_last, LEFT).move_to(self.formula2_8)  # real TODO delete some useless codes
        self.set_other2()

    def set_other2(self):
        pass


class Forth(Third):

    def change_cap(self):
        self.caps = [
            "匀另类变速度运动的中点时刻速度就是初速与末速的算数平均数",
            "匀另类变速度运动的中点时刻速度就更简单了",
            "用幼儿园学过的的知识一下就看出来了",
            "发现了吗？",
            "我们将匀加速直线运动的中点时刻速度和中点位移速度列出",
            "amazing!",
            "这两种运动的中点位移速度总是大于中点时刻速度"
            

        ]

    def construct(self):
        self.add(self.formula2_8_last.to_corner(corner=UR, buff=LARGE_BUFF))
        self.add(NaOH(self.captions_mob[0]))  # 匀另类变速度运动的中点位移速度就是初速与末速的算数平均数
        self.add(self.heading)
        heading = NaOH(Text("中点时刻速度", color=BLACK, font="千图纤墨体").scale(1.3), 0, colors=[BLACK, GREY]).set_opacity(.7).to_corner(UP, buff=SMALL_BUFF)
        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])),  # 匀另类变速度运动的中点时刻速度就更简单了
                  self.heading.become, heading)
        self.wait(2.)
        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))  # 用幼儿园学过的的知识一下就看出来了
        self.play(Write(self.formula9))
        self.play(self.formula9[0: 5].move_to, LEFT,
                  self.formula9[40: 46].next_to, dict(mobject_or_point=self.formula9[1: 5].copy().move_to(LEFT), direction=RIGHT, buff=SMALL_BUFF),
                  FadeOut(self.formula9[5: 40]))
        self.formula9 = VG(*self.formula9[0: 5], *self.formula9[40: 46])  # TODO redefine formula9
        self.play(Transform(self.formula9, NaOH(self.formula9.copy(), 0, *COLOR)))  # TODO this also
        self.suring = SurroundingRectangle(self.formula9, buff=MED_SMALL_BUFF).set_color(["#65E2FF", "#5DFF77", "#FFF470", "#50B2FF", "#D6BAFF", "#66ccff"])
        self.play(ShowCreation(self.suring))
        self.wait(1.5)
        self.play(Indicate(self.suring, scale_factor=1.5, color=self.suring.get_color()))
        self.wait(2.)
        self.play(to_draw.UnBorderThenFade(self.suring))
        self.wait()
        self.play(self.formula9.scale, dict(scale_factor=.7),
                  self.formula9.next_to, dict(mobject_or_point=self.formula2_8_last, direction=DOWN, buff=SMALL_BUFF),
                  self.formula9.align_to, dict(mobject_or_point=self.formula2_8_last, direction=LEFT))
        self.wait(.5)
        self.play(self.heading.become, NaOH(Text("比较", color=BLACK, font="千图纤墨体").scale(1.3), 0, colors=[BLACK, GREY]).set_opacity(.7).to_corner(UP, buff=SMALL_BUFF))
        self.wait(2.)
        self.play(ReplacementTransform(self.captions_mob[2], NaOH(self.captions_mob[3])))  # 发现了吗？
        self.wait(3.)
        self.play(ReplacementTransform(self.captions_mob[3], NaOH(self.captions_mob[4])))  # 我们将匀加速直线运动的中点时刻速度和中点位移速度列出
        self.wait(2.)
        self.play(VG(self.formula9, self.formula2_8_last).shift, [UP * .7 + LEFT * .5])
        self.play(to_draw.WriteRandom(self.formula9_in1.scale(.7).next_to(self.formula9, DOWN, buff=SMALL_BUFF).align_to(self.formula9, LEFT)),
                  Write(self.formula9_in2.scale(.7).next_to(self.formula9_in1, DOWN, buff=SMALL_BUFF).align_to(self.formula9_in1, LEFT))) # real TODO add some flash(surrounding)
        self.wait(2.)
        self.play(Write(self.formula10))
        self.wait(2.)
        self.play(ReplacementTransform(self.formula10, self.formula11))
        self.play(ShowCreationThenFadeAround(self.formula11, surrounding_rectangle_config=dict(color=BLUE_E)))
        self.wait(1.)
        self.play(ReplacementTransform(self.captions_mob[4], NaOH(self.captions_mob[5])))  # amazing
        self.wait(2.)
        self.play(ReplacementTransform(self.captions_mob[5], NaOH(self.captions_mob[6])))  # 这两种运动的中点位移速度总是大于中点时刻速度

    def set_other2(self):
        self.addNumberOfOthers()

        self.set_other3()
        self.formula2_8_last = self.formula2_8_last[1:]
        self.heading = NaOH(Text("中点位移速度", color=BLACK, font="千图纤墨体").scale(1.3), 0, colors=[BLACK, GREY]).set_opacity(.7).to_corner(UP, buff=SMALL_BUFF)
        self.formula9 = NaOH(TexMobject("v_{\\frac{t}{2} }=v(\\frac{t_0+t_1}{2})=e^{\\frac{M(t_0+t_1)}{2}}=\\sqrt{e^{Mt_0} \\cdot e^{Mt_1}}=\\sqrt{v_0v_t}  ")[0], 0, *COLOR)
        self.formula9_in1 = NaOH(TexMobject("v_{\\frac{s}{2}\\text{(匀加)}} = \\sqrt{\\frac{v_0^2+v_t^2}{2}}")[0], 0, *COLOR)
        self.formula9_in2 = NaOH(TexMobject("v_{\\frac{t}{2}\\text{(匀加)}} = \\frac{v_0+v_t}{2}")[0], 0, *COLOR)
        self.formula10 = NaOH(TexMobject("\\sqrt{\\frac{a^2+b^2}{2}}\\ge \\frac{a+b}{2}\\ge \\sqrt{ab}\\ge \\frac{2}{\\frac{1}{a}+\\frac{1}{b}}")[0], 0, *COLOR)
        self.formula11 = NaOH(TexMobject("v_{\\frac{s}{2}\\text{(匀加)}}\\ge v_{\\frac{t}{2}\\text{(匀加)}}\\\\"
                                         "v_{\\frac{s}{2}}\\ge v_{\\frac{t}{2}}\\qquad")[0], 0, *COLOR)



    def set_other3(self):
        pass


class Finally_Scene(LuoVLast):

    CONFIG = {
        "word": ["bgm: Fragmented Truce、 Shine",
                 "music time"],
        "camera_config": {
            "background_color": "#B0B0B0",
        },
        "WAIT_TIME": 2.5

    }

    def prepare(self):
        ThankingWords = SourceHansfont("3 Q for watching ^—^").scale(1.5).set_color(BLUE_D).shift(UP * 3.).set_opacity(.7)
        self.add(ThankingWords)

    def then(self):
        WAIT_TIME = self.WAIT_TIME
        that = []
        for word in self.word:
            that.append(NaOH(SourceHansfont("{}".format(word)), 0))
            self.play(PiCreatureSays(self.pi_creature, that[-1].scale(1.), target_mode="thinking"))
            self.wait(WAIT_TIME)
            self.play(RemovePiCreatureBubble(self.pi_creature))

