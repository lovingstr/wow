from manimlib.imports import *
from luoluoluo_useful.imports import *
from luoluoluo_useful.MyFontLuoluoluo.MyFontSourceHansfont import SourceHansfont, SourceHansfontDot
from luoluoluo_useful.MySceneLuoluoluo.MyScenes import LuoScene


WAIT_TIME = 3.


class Begin(LuoVBegin):
    CONFIG = {
        "TextAbout": "bilibili.洛洛洛-洛洛洛_dx -- 无“尺”之徒"
    }


class BeginningVideoAboutCode(LuoScene):
    def setupPic(self):
        self.cir = Circle(radius=2.).set_color(BLACK)
        self.tex_why = MyText("?", "_?", "^?", default_font="思源黑体").get_new_font_texs({"_?": "?", "^?": "?"}).set_color("#96F0FC").shift(UR * 1.2)

    def set_other1(self):
        pass

    def construct(self):
        self.wait()

        self.play(Write(NaOH(self.captions_mob[0])))
        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))
        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))
        self.wait(3.)

        self.play(Write(self.tex_why))

        self.play(ShowPassingFlashAround(self.captions_mob[2], surrounding_rectangle_config={"color": "#9CDEFF"}), run_time=2.)
        self.wait()

        Countdown = TexMobject(r"(2 \phi - 1)^2")
        for x in range(5):
            if x == 0:
                self.play(Write(Countdown.set_color(["#85D0EC", "#F77D6B", "#C56CB3", "#FA9E5A", "#5FC2C0"][x])))
                self.wait()

            else:
                self.play(Countdown.become,
                          TexMobject([r"(2 \phi - 1)^2", r"{\pi \over \arctan{1}}", r"[\ln(21)]",
                                      r"\sum_{i=0}^{+ \infty}{1 \over 2^i}", r"-e^{\pi i}"][x])
                          .set_color(["#85D0EC", "#F77D6B", "#C56CB3", "#FA9E5A", "#5FC2C0"][x]))
            self.play(ShowCreationThenFadeAround(Countdown,
                                                 surrounding_rectangle_config=
                                                 {"color": ["#85D0EC", "#F77D6B", "#C56CB3", "#FA9E5A", "#5FC2C0"][
                                                     x
                                                 ]}),
                      FadeIn(self.cir.set_color(["#85D0EC", "#F77D6B", "#C56CB3", "#FA9E5A", "#5FC2C0"][x])),
                      run_time=1.5, rate_func=smooth,
                      )
        self.play(FadeOut(Group(Countdown, self.tex_why)), self.cir.set_color, BLACK)

    def change_cap(self):
        self.caps = ["相信大家已经知道如何用只用圆规四等分已知圆心的圆了",
                     "但是怎么只用圆规找到一个圆的圆心呢?",
                     "Four divide the circumference"]

    def setPictureToScreen(self):
        self.play(ShowCreation(self.cir))


class FourDivTheCirCum(BeginningVideoAboutCode):

    def construct(self):
        self.wait()
        self.play(FadeIn(self.cir))
        self.wait(2.)

        self.play(Write(self.A))
        self.wait(2.)

        self.play(GrowFromCenter(self.cirAtoC), run_time=2.)
        self.wait(2.)

        self.play(FadeInFromDown(self.tex_A), run_time=2.)
        self.wait(2.)

        self.play(Write(VGroup(self.B, self.C)), run_time=2.)
        self.play(FadeInFromDown(VGroup(self.tex_B, self.tex_C)), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(GrowFromCenter(self.cirBtoD1), run_time=2.)
        self.play(Write(self.D1), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(VGroup(self.cirBtoD1, self.B.copy()), VGroup(self.cirD1toD2, self.D1)), run_time=2.)
        self.play(Write(self.D2), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(VGroup(self.cirD1toD2, self.D1.copy()), VGroup(self.cirD2toD, self.D2)), run_time=2.)
        self.play(Write(self.D), FadeInFromDown(self.tex_D), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(VGroup(self.cirD2toD, self.D2.copy()), VGroup(self.cirDtoD2, self.D)), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(VGroup(self.cirDtoD2, self.D.copy()), VGroup(self.cirDtoC, self.D)), run_time=2.)  # for passing
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(VGroup(self.cirDtoC.copy(), self.D.copy()), VGroup(self.cirAtoE, self.A)), run_time=2.)
        self.wait(WAIT_TIME)

        self.add(self.tex_A)
        self.play(Write(self.E, run_time=2.), FadeInFromDown(self.tex_E), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(VGroup(self.cirAtoE.copy(), self.A.copy()), VGroup(self.cirEtoF, self.E)), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(Write(self.F), FadeInFromDown(self.tex_F), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(to_draw.UnWrite(VGroup(self.cirDtoC, self.cirAtoE, self.cirEtoF, self.D1, self.D2, self.D, self.E,
                                         self.tex_D, self.tex_E)), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(GrowFromCenter(self.cirBtoF), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(VGroup(self.cirBtoF.copy(), self.B.copy()), VGroup(self.cirAtoF, self.A)), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(Write(self.O), FadeInFromDown(self.tex_O), run_time=2.)
        self.wait(WAIT_TIME)

        self.play(to_draw.UnWrite(VGroup(self.A, self.F, self.B, self.C,
                                         self.tex_A, self.tex_B, self.tex_C, self.tex_F,
                                         self.cirAtoF, self.cirBtoF, self.cirAtoC)))
        self.wait(WAIT_TIME)

        self.play(Write(self.tex_CheckMark))
        self.wait()

    def setupPic(self):
        self.O = Dot(np.array([0., 0., 0.])).set_color("#606050")
        self.A = Dot(2 * DOWN).set_color("#99CCFF")
        self.B = Dot(np.array([-1.602958, -1.1960458395212, 0.])).set_color("#1565C0")
        self.C = Dot(np.array([1.602958, -1.1960458395212, 0.])).set_color("#1565C0")
        self.D1 = Dot(np.array([-0.1052342735472, -0.2098205705611, 0.])).set_color("#808080")
        self.D2 = Dot(np.array([1.4977237264528, -1.0137747310399, 0.])).set_color("#808080")
        self.D = Dot(np.array([1.602958, -2.8039541604788, 0.])).set_color("#FF99CC")
        self.E = Dot(np.array([1.3998467814108, -1.2089259470958, 0.])).set_color("#8FB481")  # TODO set new color
        self.F = Dot(np.array([0.1382442354324, -0.2120667872415, 0.])).set_color("#0099CC")

        AC = length_of_two_point(self.A.get_center(), self.C.get_center())
        D2D = D1D2 = BD1 = length_of_two_point(self.B.get_center(), self.D1.get_center())
        CD = length_of_two_point(self.C.get_center(), self.D.get_center())
        AE = EF = length_of_two_point(self.A.get_center(), self.E.get_center())
        BO = length_of_two_point(self.B.get_center(), ORIGIN)
        self.cir = Circle(radius=2.).set_color(BLACK)
        self.cirAtoC = Circle(arc_center=self.A.get_center(), radius=AC).set_color("#66CCFF")
        self.cirBtoD1 = Circle(arc_center=self.B.get_center(), radius=BD1).set_color("#C0C0C0")
        self.cirD1toD2 = Circle(arc_center=self.D1.get_center(), radius=D1D2).set_color("#C0C0C0")
        self.cirD2toD = Circle(arc_center=self.D2.get_center(), radius=D2D).set_color("#C0C0C0")
        self.cirDtoD2 = Circle(arc_center=self.D.get_center(), radius=D2D).set_color("#C0C0C0")
        self.cirDtoC = Circle(arc_center=self.D.get_center(), radius=CD).set_color("#C0C0C0")
        self.cirAtoE = Circle(arc_center=self.A.get_center(), radius=AE).set_color("#C0C0C0")
        self.cirEtoF = Circle(arc_center=self.E.get_center(), radius=EF).set_color("#00CDF7")
        self.cirBtoF = Circle(arc_center=self.B.get_center(), radius=BO).set_color("#0a7fc6")
        self.cirAtoF = Circle(arc_center=self.A.get_center(), radius=BO).set_color("#4cb2e5")

        self.tex_O = SourceHansfontDot(self.O, text="O").scale(.7).next_to(self.O, UR, buff=SMALL_BUFF)
        self.tex_A = SourceHansfontDot(self.A, text="A").scale(.7).next_to(self.A, UR, buff=SMALL_BUFF)
        self.tex_B = SourceHansfontDot(self.B, text="B").scale(.7).next_to(self.B, UR, buff=SMALL_BUFF)
        self.tex_C = SourceHansfontDot(self.C, text="C").scale(.7).next_to(self.C, UR, buff=SMALL_BUFF)
        self.tex_D = SourceHansfontDot(self.D, text="D").scale(.7).next_to(self.D, UR, buff=SMALL_BUFF)
        self.tex_E = SourceHansfontDot(self.E, text="E").scale(.7).next_to(self.E, UR, buff=SMALL_BUFF)
        self.tex_F = SourceHansfontDot(self.F, text="F").scale(.7).next_to(self.F, UR, buff=SMALL_BUFF)

        self.tex_CheckMark = TexMobject(r"\checkmark").set_color("#8ABB6D").set_opacity(.7).scale(2.5)\
            .next_to(self.tex_O, RIGHT, buff=SMALL_BUFF)


class Last(LuoVLast):
    CONFIG = {
        "words": "制作: by bilibili.洛洛洛-洛洛洛_dx,\n\n 剪辑: by bilibili.zhengyang051119Alexis \n\nbgm: MEGALOVANIA"
    }


class Wchi(LuoScene):
    def construct(self):
        self.add(SourceHansfont("无尺 -- 圆规找圆心").set_color_by_gradient("#6EFFE7", "#C2C46A"))






