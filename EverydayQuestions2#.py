from manimlib.imports import *
from luoluoluo_useful.imports import *


def return_two_dot(dot1: Dot, dot2: Dot):
    return length_of_two_point(dot1.get_center(), dot2.get_center())


class KCl(Line):
    def __init__(self, start: Dot, end: Dot, **kwargs):
        Line.__init__(self, start=start.get_center(), end=end.get_center(), color=average_color(start.get_color(), end.get_color()), **kwargs)


class SourceHansfont(Text):
    CONFIG = {
        "font": "思源黑体",
        "color": BLACK
    }


class SourceHansfontDot(SourceHansfont):
    def __init__(self, dot, **kwargs):
        SourceHansfont.__init__(self, color=dot.get_color(), **kwargs)


# class MyWiggleOutThenIn(WiggleOutThenIn):
#     CONFIG = {
#         "scale_value": 1.2,
#         "rotation_angle": 0.02 * TAU,
#     }


class Begin02(Og_Think):
    CONFIG = {
        "num": 2
    }

    def construct(self):

        self.pi_creature[4].set_color(["#29ABCA", "#8D5630", "#58C4DD", "#C59978", "#ACE2EE", "#E2CCBC"])

        self.remove(self.pi_creatures)
        self.play(to_draw.Every_Write(self.pi_creatures.move_to(ORIGIN)))
        EulerFormula = MyText("e^", "{\\pi", "i}", default_font="思源黑体")

        EulerFormula_SourceHansfont = EulerFormula.get_new_font_texs({"e^": "e", "{\\pi": "π", "i}": "i"})

        EulerFormula_SourceHansfont = NaOH(EulerFormula_SourceHansfont, 1, "#29ABCA", "#58C4DD", "#C59978")

        eyes = Eyes(EulerFormula_SourceHansfont[-1]).scale(.4)

        eyes.look_at(UP + np.array([.3, 0., 0.]))

        self.say(VGroup(eyes, EulerFormula_SourceHansfont).shift(3. * RIGHT + UP))
        self.play(eyes.look_at, DR)
        self.look_at(UL)
        self.play(Blink(eyes), Blink(self.pi_creature))
        text = SourceHansfont("每周一题 #{}".format(self.num)).set_color_by_gradient("#37DDD7", "#7ABFDD").next_to(self.pi_creature, DOWN, buff=LARGE_BUFF)
        self.play(Write(text))
        self.play(eyes.look_at, text, self.pi_creature.look_at, text)
        self.play(Blink(eyes), Blink(self.pi_creature))


class Question211(Question112):
    def construct(self):

        self.wait()

        self.play(Write(self.text_1))  # , to_draw.WriteRandom(self.text_11), lag_ratio=.3
        self.wait(3.)
        self.play(Write(NaOH(self.captions_mob[0])))
        self.wait(3.)
        self.play(Write(self.ans1.scale(.7)))
        self.wait(3.)
        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))
        self.wait(3.)
        self.play(to_draw.UnWrite(self.ans1))
        self.wait(3.)
        self.play(Write(self.screenPicGroup))
        self.wait(3.)
        self.play(Write(self.Texa), Write(self.Texb), lag_ratio=.5)
        self.wait(3.)
        self.play(ReplacementTransform(Group(self.Texa, self.Texb).copy(), self.Texsqab))
        self.wait(3.)
        self.play(self.dotD.move_to, self.dotA.get_center(), rate_func=rush_into, run_time=8.)
        self.play(self.dotD.move_to, self.dotB.get_center(), rate_func=rush_from, run_time=8.)
        self.wait(3.)
        self.play(self.dotD.move_to, self.dotA.get_center(), rate_func=rush_into, run_time=8.)
        self.play(self.dotD.move_to, self.dotB.get_center(), rate_func=rush_from, run_time=8.)
        self.wait(3.)
        self.play(self.dotD.move_to, DOWN, rate_func=smooth, run_time=4.)
        self.wait(3.)
        self.play(to_draw.UnWrite(self.captions_mob[1]))
        self.wait(3.)
        self.play(to_draw.UnWriteRandom(VGroup(*self.screenPicGroup, self.Texa, self.Texb, self.Texsqab)))

    def change_cap(self):
        self.caps = ["第一题, 思路是很简单的",
                     "但是, 我想以几何的视角解释第一题"]

    def setupPic(self):
        self.dotO = Dot(DOWN).set_color("#77C1DD").save_state()
        self.dotA = Dot(LEFT * 3 + DOWN).set_color("#DDB3CD").save_state()
        self.dotB = Dot(RIGHT * 3 + DOWN).set_color("#37DDCB").save_state()
        self.dotD = Dot(ORIGIN + DOWN).set_color("#BCDDA4").save_state()
        self.arc = Arc(arc_center=self.dotD.get_center(), angle=-PI, start_angle=PI, radius=length_of_two_point(self.dotO.get_center(), self.dotB.get_center())).set_color(["#97C5C2", "#82C574"])

        def dotE_update(dot):
            dot.move_to(
                np.array([
                    self.dotD.get_center()[0],
                    np.sqrt(length_of_two_point(self.dotA.get_center(), self.dotD.get_center()) *
                            length_of_two_point(self.dotB.get_center(), self.dotD.get_center())) - 1,
                    0.
                ]))

        self.dotE = Dot(DR + DOWN).set_color("#DD94D4").save_state().add_updater(dotE_update)
        self.dotE_update = dotE_update

        self.dotA.generate_target()
        self.dotB.generate_target()
        self.dotD.generate_target()
        # self.dotE.generate_target()

        self.to_big = AnimationGroup(
            ApplyMethod(self.dotA.restore),
            ApplyMethod(self.dotB.restore),
            ApplyMethod(self.dotD.restore),
        )

        self.line_AD = KCl(self.dotA, self.dotD).add_updater(lambda line: line.become(KCl(self.dotA, self.dotD).set_plot_depth(-1)))
        self.line_BD = KCl(self.dotB, self.dotD).add_updater(lambda line: line.become(KCl(self.dotB, self.dotD).set_plot_depth(-1)))
        self.line_DE = KCl(self.dotD, self.dotE).add_updater(lambda line: line.become(KCl(self.dotD, self.dotE).set_plot_depth(-1)))

        self.TexA = SourceHansfontDot(self.dotA, text="A").scale(.7).add_updater(lambda tex: tex.next_to(self.dotA, DL))
        self.TexB = SourceHansfontDot(self.dotB, text="B").scale(.7).add_updater(
            lambda tex: tex.next_to(self.dotB, RIGHT))
        self.TexD = SourceHansfontDot(self.dotD, text="D").scale(.7).add_updater(lambda tex: tex.next_to(self.dotD, DOWN))
        self.TexE = SourceHansfontDot(self.dotE, text="E").scale(.7).add_updater(
            lambda tex: tex.next_to(self.dotE, UP))

        self.Texa = SourceHansfontDot(self.line_AD, text="a").scale(.7).add_updater(
            lambda tex: tex.next_to(self.line_AD, DOWN))

        self.Texb = SourceHansfontDot(self.line_BD, text="b").scale(.7).add_updater(
            lambda tex: tex.next_to(self.line_BD, DOWN))

        self.Texsqab = SourceHansfontDot(self.line_DE, text="√ab").scale(.7).add_updater(
            lambda tex: tex.next_to(self.line_DE, RIGHT))
        self.Texsqab[0].scale(1.7)
        self.Texsqab[1: 3].shift(LEFT * .2)

        self.text_1 = TextMobject(r"如果$a\text{、}b>0$, 证明$a + b \ge 2\sqrt{ab}$").set_color(BLACK)\
            .scale(.7).shift(UP * 3)

        self.text_12 = TextMobject(r"1.如果$x<0$, 求$x+{\pi \over x}$的最大值").set_color(BLACK) \
            .scale(.7).next_to(self.text_1, DOWN).align_to(self.text_1, direction=LEFT)

        self.text_13 = TextMobject(r"2.如果$a\text{、}b$是正数, 求${x+y\over 2x^2 +y^2 + 6}$的最小值").set_color(BLACK) \
            .scale(.7).next_to(self.text_1, DOWN).align_to(self.text_1, direction=LEFT)

        self.text_14 = TextMobject(
            r"3.如果$k$是正整数, 求证${2\over3\sqrt[3]{k+1}}\le\sqrt[3]{(k+1)^2}-\sqrt[3]{{k}^{2}} \le{2\over3\sqrt[3]{k}}$"
        )\
            .set_color(BLACK) \
            .scale(.7).next_to(self.text_1, DOWN).align_to(self.text_1, direction=LEFT)

        self.ans1 = TexMobject(r"(a-b)^2\ge 0\\"
                               r"(a+b)^2\ge 4ab\\"
                               r"a+b \ge 2\sqrt{ab}")
        self.axes2 = Axes(y_max=8, x_max=5.3, y_min=-13, x_min=-5.3, center_point=DOWN * 1,
                          x_axis_config=dict(color="#42C7FF", unit_size=.7),
                          y_axis_config=dict(color="#42C7FF", unit_size=1 / 2, tick_frequency=2)).add_coordinates(
            y_vals=[-6, -4, -2, 2, 4, 6], number_config=dict(color=BLACK, stroke_opacity=.7)
        )
        self.un_ = self.axes2.x_axis_config["unit_size"]
        NaOH(self.ans1, 0, "#C59978", BLUE_B, BLUE_C, BLUE_D)
        self.tex22_for_why_e1 = TexMobject(r"y^+ = x + {\pi \over x}").shift(LEFT * 5).set_color("#FFA7DB")
        self.tex22_for_why_e2 = TexMobject(r"y^- = -x + {\pi \over -x}").shift(LEFT * 5).set_color("#FFA7DB")
        self.tex22_for_why_e3 = TexMobject(r"y^- = -(x + {\pi \over x}) = -y^+").shift(LEFT * 5).set_color("#FFA7DB")
        self.tex33 = NaOH(TexMobject(r"{x+y\over 2x^2+y^2+6}={x+y\over 2x^2+2+y^2+4}\le {x+y \over 2\times 2\sqrt{1 \cdot x} +2\sqrt{4 \cdot y} }"), 0, "#C59978", "#866041", "#5DC2D9", BLUE_D)

    def setPictureToScreen(self):
        self.screenPicGroup = VGroup(self.dotA, self.dotB, self.dotD, self.dotE, self.arc,
                                     self.line_AD, self.line_BD, self.line_DE,
                                     self.TexA, self.TexB, self.TexD, self.TexE
                                     )


class Question212(Question211):
    def construct(self):
        self.add(self.text_1)
        self.wait(3.)
        self.play(Write(self.text_12))
        self.wait(3.)
        self.play(Write(NaOH(self.captions_mob[0])))
        self.wait(3.)
        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))

        self.wait(3.)
        self.play(Write(self.screenPicGroup))

        self.wait(3.)
        fu = FunctionGraph(lambda x: self.axes2.c2p(0., ((x / self.un_) + np.pi / (x / self.un_)))[1], color="#61FFBF",
                           x_min=.3, x_max=self.axes2.c2p(5, 0)[0])
        self.play(ShowCreation(fu))
        self.wait(3.)
        self.captions_mob[2][-1].shift(LEFT * .15)
        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))
        self.wait(3.)

        line = Line(self.axes2.c2p(np.sqrt(np.pi), 0.), self.axes2.c2p(np.sqrt(np.pi), 2 * np.sqrt(np.pi))).set_color("#FFA2D9")
        my_text = MyText(r"y_", r"{\min}", "=", "2", r"\sqrt", r"{\pi", ".}", default_font='思源黑体')\
            .get_new_font_texs({"y_": "y", r"{\min}": "min", r"\sqrt": "√",  r"{\pi": "π"})\
            .scale(.7).next_to(line, RIGHT)
        self.play(ShowCreation(line), Write(my_text.set_color("#FFA2D9")))
        self.wait(3.)

        fun2 = FunctionGraph(lambda x: self.axes2.c2p(0., ((x / self.un_) + np.pi / (x / self.un_)))[1],
                             color="#FFA2D9", x_max=-.3, x_min=-self.axes2.c2p(5, 0)[0])
        f = fu.copy()
        self.play(ReplacementTransform(self.captions_mob[2], NaOH(self.captions_mob[3])))
        self.wait(3.)
        self.play(Rotating(f, about_point=self.axes2.c2p(0., 0.), run_time=8., rate_func=smooth, radians=PI))
        self.wait(3.)

        self.play(f.set_color, fun2.get_color())
        self.add(fun2)
        self.remove(f)
        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[3], NaOH(self.captions_mob[4])))
        self.wait(3.)
        self.play(ApplyWave(VGroup(fu, fun2)))
        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[4], NaOH(self.captions_mob[5])))
        self.wait(3.)

        self.play(Write(self.tex22_for_why_e1))
        self.wait(3.)
        self.play(ReplacementTransform(self.tex22_for_why_e1[0][0], self.tex22_for_why_e2[0][0]),
                  ReplacementTransform(self.tex22_for_why_e1[0][1], self.tex22_for_why_e2[0][1]),
                  ReplacementTransform(self.tex22_for_why_e1[0][2], self.tex22_for_why_e2[0][2]),
                  Write(self.tex22_for_why_e2[0][3]),
                  ReplacementTransform(self.tex22_for_why_e1[0][3], self.tex22_for_why_e2[0][4]),
                  ReplacementTransform(self.tex22_for_why_e1[0][4], self.tex22_for_why_e2[0][5]),
                  ReplacementTransform(self.tex22_for_why_e1[0][5], self.tex22_for_why_e2[0][6]),
                  ReplacementTransform(self.tex22_for_why_e1[0][6], self.tex22_for_why_e2[0][7]),
                  Write(self.tex22_for_why_e2[0][8]),
                  ReplacementTransform(self.tex22_for_why_e1[0][7], self.tex22_for_why_e2[0][9]),)
        self.wait(3.)
        self.tex22_for_why_e3.shift(RIGHT)
        self.play(ReplacementTransform(self.tex22_for_why_e2[0][0: 3], self.tex22_for_why_e3[0][0: 3]),
                  Write(self.tex22_for_why_e3[0][4]),
                  Write(self.tex22_for_why_e3[0][10]),
                  ReplacementTransform(VGroup(self.tex22_for_why_e2[0][3], self.tex22_for_why_e2[0][8]), self.tex22_for_why_e3[0][3]),
                  ReplacementTransform(self.tex22_for_why_e2[0][4], self.tex22_for_why_e3[0][5]),
                  ReplacementTransform(self.tex22_for_why_e2[0][5], self.tex22_for_why_e3[0][6]),
                  ReplacementTransform(self.tex22_for_why_e2[0][6], self.tex22_for_why_e3[0][7]),
                  ReplacementTransform(self.tex22_for_why_e2[0][7], self.tex22_for_why_e3[0][8]),
                  ReplacementTransform(self.tex22_for_why_e2[0][9], self.tex22_for_why_e3[0][9]),
                  Write(self.tex22_for_why_e3[0][11:]),)
        self.wait(3.)
        self.play(ReplacementTransform(self.captions_mob[5], NaOH(self.captions_mob[6])))
        self.wait(3.)
        self.captions_mob[6][0].add_updater(lambda meee: meee.set_plot_depth(fun2.get_plot_depth() + 3))
        anim1 = ApplyMethod(self.captions_mob[6][0].set_opacity, 0.)
        turn_animation_into_updater(anim1)
        self.captions_mob[6][0].clear_updaters()
        self.remove(self.captions_mob[6][0])
        self.wait(3.)

        list1 = [fun2, fu, *self.axes2, self.tex22_for_why_e3, *self.captions_mob[6][1:], *self.text_12[0], line,
                 *my_text]
        random.shuffle(list1)
        self.play(to_draw.UnWrite(VGroup(*list1)))
        self.wait(3.)

    def change_cap(self):
        self.caps = [
            "这题有一点绕弯路, 因为第一题是a、b>0, 求“最小值”, 而这题是x<0, 求“最大值”",
            "那我们就看看当x>0时, y=x+π/x的函数图像吧",
            "x>0时, y有最小值2√π",
            "那当x<0时的图像呢?",
            "看上去, 这个函数关于原点中心对称",
            "事实上, 没错, 当x变为-x时, π/x也变为-π/x, y变为-y",
            "所以当x<0时, y=x+π/x它的最大值是多少呢"
        ]

    def setPictureToScreen(self):
        self.screenPicGroup = VGroup(self.axes2)


class Question213(Question212):
    def construct(self):
        self.add(self.text_1)
        self.wait(3.)
        self.play(Write(self.text_13))
        self.wait(3.)
        self.play(Write(NaOH(self.captions_mob[0]))),
        self.wait(3.)
        self.play(Write(self.tex33))
        self.wait(3.)
        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))
        self.wait(3.)
        self.play(to_draw.UnWrite(self.tex33))
        self.wait(3.)

        tt = MyText(r"{?", r"^?", r"}_?", default_font='思源黑体')\
            .get_new_font_texs({r"{?": "?", r"^?": "?", r"}_?": r"?"}).set_color(BLUE_D)
        self.play(Write(tt))
        self.wait(3.)

        self.play(to_draw.UnWrite(tt))
        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))
        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[2], NaOH(self.captions_mob[3])))
        self.wait(3.)

        self.play(to_draw.UnWrite(self.captions_mob[3]), to_draw.UnWrite(self.text_13))
        self.wait(3.)

    def change_cap(self):
        self.caps = ["这道题其实也不难",
                     "但要直观理解它很难, 我们要找到一种方法",
                     "我们可以把这个曲面在三维中画出来",
                     "其实这道题不是很简单, 对吗"]


class Question2131(Question213, ThreeDScene):
    CONFIG = {

    }

    def construct(self):
        self.add(self.text_1, self.text_13, NaOH(self.captions_mob[2]))
        self.wait(2.)
        self.move_camera(phi=70 * DEGREES, theta=PI / -4)
        threedasex = ThreeDAxes().set_color(BLACK)
        self.play(Write(threedasex))
        self.begin_ambient_camera_rotation(.2)
        p1 = ParametricSurface(lambda u, v: np.array([u, v, (u+v) / (2 * u ** 2 + v ** 2 + 6) * 10]),
                               u_max=5, v_max=5, u_min=-5., v_min=-5., checkerboard_colors=["#5DC2D9", "#866041"], fill_opacity=.7)  #
        self.play(Write(p1))
        self.begin_ambient_camera_rotation(.3)
        self.wait(10.)

        line = Line(np.array([1., 2., 0.]), np.array([1., 2., 2.5])).set_color("#98C8FF")
        Tex = TexMobject(r"{x+y \over 2x^2 + y^2 + 6}_{\max}").set_color(BLACK).rotate(PI / 2, axis=DOWN).rotate(PI / 2, axis=RIGHT).next_to(line, OUT + RIGHT)
        self.begin_ambient_camera_rotation(.2)
        self.play(Write(Tex), FadeIn(line))
        self.wait(40.)
        self.begin_ambient_camera_rotation(.0)

        self.move_camera(phi=0)
        self.begin_ambient_camera_rotation(.2)
        self.wait(10)


class Question214(Question213):
    def construct(self):
        self.add(self.text_1)
        self.wait(3.)
        self.play(Write(self.text_14))
        self.wait(3.)
        self.play(Write(NaOH(self.captions_mob[0]))),
        g = ValueTracker(1.)
        k = Integer(1).set_color(BLACK).add_updater(lambda d: d.set_value(int(np.round(g.get_value())))).scale(.7)
        t = 1 / 3
        k1 = DecimalNumber(0.529, show_ellipsis=True, num_decimal_places=12).add_updater(lambda k_: k_.set_value(2 / (3 * (k.get_value() + 1) ** t))).scale(.7)
        k2 = DecimalNumber(0.666, show_ellipsis=True, num_decimal_places=12).add_updater(lambda k_: k_.set_value(((k.get_value() + 1) ** 2) ** t - ((k.get_value() ** 2) ** t))).scale(.7)
        k3 = DecimalNumber(0.587, show_ellipsis=True, num_decimal_places=12).add_updater(lambda k_: k_.set_value(2 / (3 * k.get_value() ** t))).scale(.7)
        t1 = TexMobject(r"{2\over3\sqrt[3]{k+1}}=").set_color("#9FE4FF").scale(.7)
        t2 = TexMobject(r"\sqrt[3]{(k+1)^2}-\sqrt[3]{{k}^{2}}=").set_color("#89FFD8").scale(.7).shift(DOWN).align_to(t1, LEFT)
        t3 = TexMobject(r"{2\over3\sqrt[3]{k}}=").set_color("#E2ACCF").scale(.7).shift(2 * DOWN).align_to(t1, LEFT)
        tt = TexMobject(r"k=").set_color(BLACK).scale(.7).shift(1.5 * UP).align_to(t1, LEFT)
        k1.set_color(t1.get_color()).next_to(t1, RIGHT, buff=MED_SMALL_BUFF)
        k2.set_color(t2.get_color()).next_to(t2, RIGHT, buff=MED_SMALL_BUFF)
        k3.set_color(t3.get_color()).next_to(t3, RIGHT, buff=MED_SMALL_BUFF)
        k.next_to(tt, RIGHT, buff=MED_SMALL_BUFF)
        self.play(Write(VGroup(t1, t2, t3, k1, k2, k3, tt, k)))
        self.wait(3.)

        self.play(ReplacementTransform(self.captions_mob[0], self.captions_mob[1]))
        self.wait(3.)

        self.play(g.set_value, 2000, run_time=20, rate_func=smooth)
        self.wait(3.)

        self.play(to_draw.UnWrite(VGroup(t1, t2, t3, k1, k2, k3, tt, k)))
        self.wait(3.)
        self.play(to_draw.UnWrite(VGroup(self.text_1, self.text_14, self.captions_mob[1])))
        self.wait(3.)

    def change_cap(self):
        self.caps = ["这题不必思考, 因为这纯粹是我弄出来坑同学的",
                     "(估计也没有同学想去做)"]


class Last02(TripleScene2):
    CONFIG = {
        "words": "制作: by bilibili.洛洛洛-洛洛洛_dx,\n\n 剪辑: by bilibili.zhengyang051119Alexis \n\nbgm: Ffrench - Being Again、I'll Fly Away、Verde"
    }

    def setup(self):
        self.pi_creature = PiCreature().move_to(ORIGIN)
        self.pi_creature[4].set_color(["#29ABCA", "#8D5630", "#58C4DD", "#C59978", "#ACE2EE", "#E2CCBC"])

        self.play(to_draw.Every_Write(self.pi_creature.move_to(ORIGIN)))

        self.play(self.pi_creature.look_at, UL)
        self.play(Blink(self.pi_creature))
        svg = SVGMobject("coin").set_color("#67C0DD")
        that = NaOH(SourceHansfont("{}".format(self.words)), 0)
        self.play(PiCreatureSays(self.pi_creature, that, target_mode="thinking"))
        self.play(RemovePiCreatureBubble(self.pi_creature))
        self.play(PiCreatureSays(self.pi_creature, svg, target_mode="thinking"))
        self.play(Blink(self.pi_creature))
        self.play(RemovePiCreatureBubble(self.pi_creature))





# by luoluoluo
