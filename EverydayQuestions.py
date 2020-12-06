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


class MyWiggleOutThenIn(WiggleOutThenIn):
    CONFIG = {
        "scale_value": 1.2,
        "rotation_angle": 0.02 * TAU,
    }

class Begin(Og_Think):
    CONFIG = {
        "num": 1
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


class Question111(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def setup(self):
        self.setupPic()
        self.setPictureToScreen()
        self.change_cap()
        self.set_caption_on()
        self.other1()

    def construct(self):
        self.play(Write(VGroup(self.text_1, self.text_11)))
        self.wait()

        self.play(to_draw.ShowCreationRandom(self.screenPicGroup.shift(RIGHT * 3)))
        self.wait(5.)

        self.play(self.line_BE.set_color, "#DD4D77", self.line_CD.set_color, "#DD4D77")
        self.wait(2.)

        self.play(Write(NaOH(self.captions_mob[0])))
        self.wait(2.)

        self.play(MyWiggleOutThenIn(self.line_BE), MyWiggleOutThenIn(self.line_CD))
        self.wait(3.)

        self.play(ReplacementTransform(NaOH(self.captions_mob[0]), NaOH(self.captions_mob[1])))

        self.play(self.screenPicGroup.shift, LEFT * 3)
        self.play(self.to_big)
        self.wait(3.)

        self.play(Rotating(self.Triangle_ACEpoints, about_point=self.dotA.get_center(), rate_func=smooth, run_time=8.))
        self.wait(2.)

        self.play(*[Uncreate(l) for l in VGroup(self.line_BE, self.line_CD)])
        self.wait()

        self.play(ReplacementTransform(NaOH(self.captions_mob[1]), NaOH(self.captions_mob[2])))
        self.wait()

        self.screenPicGroup.remove(self.line_BE, self.line_CD)

        self.play(self.to_small)
        self.wait()

        self.play(self.screenPicGroup.shift, RIGHT * 3)
        self.wait()

        self.play(to_draw.UnWrite(NaOH(self.captions_mob[2])))
        self.wait()

    def setupPic(self):
        self.dotA = Dot(DOWN).set_color("#77C1DD").save_state()
        self.dotB = Dot(LEFT * 2 + DOWN).set_color("#DDB3CD").save_state()
        self.dotC = Dot(DL + DOWN).set_color("#37DDCB").save_state()
        self.dotD = Dot(UP * 2 + DOWN).set_color("#BCDDA4").save_state()
        self.dotE = Dot(DR + DOWN).set_color("#DD94D4").save_state()
        self.dotM = Dot((self.dotD.get_center() + self.dotE.get_center())/2).set_color(average_color(self.dotD.get_color(), self.dotE.get_color())).add_updater(
            lambda dot: dot.become(Dot((self.dotD.get_center() + self.dotE.get_center())/2).set_color(average_color(self.dotD.get_color(), self.dotE.get_color())))
        )

        self.dotA.generate_target()
        self.dotB.generate_target()
        self.dotC.generate_target()
        self.dotD.generate_target()
        self.dotE.generate_target()

        self.dotA.target.become(Dot(DOWN).set_color("#77C1DD"))
        self.dotB.target.become(Dot(LEFT * 3 + DOWN).set_color("#DDB3CD"))
        self.dotC.target.become(Dot(DL * 3/2 + DOWN).set_color("#37DDCB"))
        self.dotD.target.become(Dot(UP * 3 + DOWN).set_color("#BCDDA4"))
        self.dotE.target.become(Dot(DR * 3/2 + DOWN).set_color("#DD94D4"))

        self.to_big = AnimationGroup(
            MoveToTarget(self.dotA),
            MoveToTarget(self.dotB),
            MoveToTarget(self.dotC),
            MoveToTarget(self.dotD),
            MoveToTarget(self.dotE),
        )

        self.to_small = AnimationGroup(
            ApplyMethod(self.dotA.restore),
            ApplyMethod(self.dotB.restore),
            ApplyMethod(self.dotC.restore),
            ApplyMethod(self.dotD.restore),
            ApplyMethod(self.dotE.restore),
        )

        self.Triangle_ABDpoints = VGroup(self.dotA, self.dotB, self.dotD)
        self.Triangle_ACEpoints = VGroup(self.dotA, self.dotC, self.dotE)

        self.line_AB = KCl(self.dotA, self.dotB).add_updater(lambda line: line.become(KCl(self.dotA, self.dotB)))
        self.line_AD = KCl(self.dotA, self.dotD).add_updater(lambda line: line.become(KCl(self.dotA, self.dotD)))
        self.line_BD = KCl(self.dotB, self.dotD).add_updater(lambda line: line.become(KCl(self.dotB, self.dotD)))
        self.line_AC = KCl(self.dotA, self.dotC).add_updater(lambda line: line.become(KCl(self.dotA, self.dotC)))
        self.line_AE = KCl(self.dotA, self.dotE).add_updater(lambda line: line.become(KCl(self.dotA, self.dotE)))
        self.line_CE = KCl(self.dotC, self.dotE).add_updater(lambda line: line.become(KCl(self.dotC, self.dotE)))
        self.line_AM = KCl(self.dotA, self.dotM).add_updater(lambda line: line.become(KCl(self.dotA, self.dotM)))

        self.line_BC = KCl(self.dotB, self.dotC).add_updater(lambda line: line.become(KCl(self.dotB, self.dotC)))
        self.line_ED = KCl(self.dotE, self.dotD).add_updater(lambda line: line.become(KCl(self.dotE, self.dotD)))
        self.line_BE = KCl(self.dotB, self.dotE).add_updater(lambda line: line.put_start_and_end_on(self.dotB.get_center(), self.dotE.get_center()))
        self.line_CD = KCl(self.dotC, self.dotD).add_updater(lambda line: line.put_start_and_end_on(self.dotC.get_center(), self.dotD.get_center()))

        self.TexA = SourceHansfontDot(self.dotA, text="A").scale(.7).add_updater(lambda tex: tex.next_to(self.dotA, DL))
        self.TexB = SourceHansfontDot(self.dotB, text="B").scale(.7).add_updater(lambda tex: tex.next_to(self.dotB, LEFT))
        self.TexC = SourceHansfontDot(self.dotC, text="C").scale(.7).add_updater(lambda tex: tex.next_to(self.dotC, DOWN))
        self.TexD = SourceHansfontDot(self.dotD, text="D").scale(.7).add_updater(lambda tex: tex.next_to(self.dotD, UP))
        self.TexE = SourceHansfontDot(self.dotE, text="E").scale(.7).add_updater(lambda tex: tex.next_to(self.dotE, DOWN))
        self.TexM = SourceHansfontDot(self.dotM, text="M").scale(.7).add_updater(lambda tex: tex.next_to(self.dotM, RIGHT))
        self.text_1 = SourceHansfont("将Rt△ABD和Rt△ACE按如图所示位置摆放, 其中AB=AD, AC=AE, 连接BC、DE.").scale(.7).shift(UP * 3)
        self.text_11 = SourceHansfont("(1) 如图, 求证: BE=CD") \
            .scale(.7).next_to(self.text_1, DOWN).align_to(self.text_1, direction=LEFT)
        self.text_12 = SourceHansfont("(2) 如图, 若M为DE中点, 连接AM, 求证：BC=2AM")\
            .scale(.7).next_to(self.text_1, DOWN).align_to(self.text_1, direction=LEFT)
        self.text_13 = SourceHansfont("(3) 如图, 在(2)的条件下, 若四边形ABCE是平行四边形, 且AC=2, AB=2√2,\n 求四边形BCED的面积")\
            .scale(.7).next_to(self.text_1, DOWN).align_to(self.text_1, direction=LEFT)
        self.text_13[-15].shift(LEFT * .15)

    def set_caption_on(self, t2c={}):
        self.captions_mob = VGroup(
            *[
                SourceHansfont(cap, tex_to_color_map=t2c).to_edge(DOWN * 1.2).scale(.7)
                .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in self.caps
            ]
        )

    def change_cap(self):
        self.caps = ["先标重点!",
                     "接下来, 可视化动画！",
                     "提示: 证全等",
                     "还是看个可视动画"]

    def setPictureToScreen(self):
        self.screenPicGroup = VGroup(self.line_AB, self.line_AD, self.line_BD, self.line_AC, self.line_AE, self.line_CE,
                                     self.line_BC, self.line_ED, self.line_BE, self.line_CD,
                                     self.TexA, self.TexB, self.TexC, self.TexD, self.TexE,
                                     self.dotA, self.dotB, self.dotC, self.dotD, self.dotE
                                     )

    def other1(self):
        pass


class Question112(Question111):
    def construct(self):
        self.add(self.text_1, self.text_11)
        self.add(self.screenPicGroup.shift(RIGHT * 3))
        self.remove(self.TexM, self.dotM, self.line_AM)
        self.play(to_draw.UnWrite(self.text_11))
        self.wait()
        self.play(to_draw.WriteRandom(self.text_12))
        self.wait()

        self.play(ShowCreation(self.line_AM))
        self.play(Write(self.dotM))
        self.play(Write(self.TexM))
        self.wait(5.)

        self.play(Write(NaOH(self.captions_mob[0])))
        self.wait()

        line_AM_copy = Line(np.array([3., -1., 0.]), np.array([3. + return_two_dot(self.dotA, self.dotM), -1., 0.])).add_updater(
            lambda line: line.become(Line(np.array([3., -1., 0.]), np.array([3. + return_two_dot(self.dotA, self.dotM), -1., 0.])).set_color(
                self.line_AM.get_color()
            ))
        )
        line_BC_copy = Line(np.array([3., 0., 0.]), np.array([3. + return_two_dot(self.dotB, self.dotC), 0., 0.]))\
            .add_updater(
            lambda line: line.become(Line(np.array([3., 0., 0.]), np.array([3. + return_two_dot(self.dotB, self.dotC), 0., 0.])).set_color(
                self.line_BC.get_color()))
        )
        TexAM = SourceHansfontDot(line_AM_copy, text="AM").add_updater(lambda tex: tex.next_to(line_AM_copy, DOWN))
        TexBC = SourceHansfontDot(line_BC_copy, text="BC").add_updater(lambda tex: tex.next_to(line_BC_copy, UP))

        self.play(self.screenPicGroup.shift, LEFT*3)
        self.wait(2.)

        self.play(self.to_big)
        self.wait(2.)

        self.play(ShowCreation(line_AM_copy), ShowCreation(line_BC_copy))
        self.play(Write(TexAM), Write(TexBC))
        self.wait(2.)

        self.play(Rotating(self.Triangle_ACEpoints, about_point=self.dotA.get_center(), rate_func=lambda t: running_start(smooth(t)), run_time=16., radians=2 * TAU))
        self.wait(4.)

        self.play(to_draw.UnWrite(TexAM), to_draw.UnWrite(TexBC))
        self.play(Uncreate(line_AM_copy), Uncreate(line_BC_copy))
        self.wait(3.)

        self.play(self.to_small)
        self.wait(2.)

        self.play(self.screenPicGroup.shift, RIGHT * 3)
        self.wait(2.)

        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))
        self.wait(3.)

        self.play(to_draw.UnWrite(self.captions_mob[1]))
        self.wait()

    def setPictureToScreen(self):
        self.screenPicGroup = VGroup(self.line_AB, self.line_AD, self.line_BD, self.line_AC, self.line_AE, self.line_CE,
                                     self.line_BC, self.line_ED, self.line_AM,
                                     self.TexA, self.TexB, self.TexC, self.TexD, self.TexE, self.TexM,
                                     self.dotA, self.dotB, self.dotC, self.dotD, self.dotE, self.dotM
                                     )

    def change_cap(self):
        self.caps = ["还是看个可视动画",
                     "提示: 构造平行四边形"]

    def other1(self):
        self.other2()

    def other2(self):
        pass


class Question113(Question112):
    def construct(self):
        self.add(self.text_1, self.text_12)
        self.add(self.screenPicGroup.shift(RIGHT * 3))
        self.play(to_draw.UnWrite(self.text_12))
        self.wait()
        self.play(to_draw.WriteRandom(self.text_13))
        self.wait(6.)
        self.dotM.clear_updaters()
        self.screenPicGroup.remove(self.line_AM, self.TexM, self.dotM)
        self.play(to_draw.UnWrite(self.TexM))
        self.play(Uncreate(self.line_AM))
        self.play(to_draw.UnWrite(self.dotM))
        self.wait(2.)
        self.play(Write(NaOH(self.captions_mob[0])))
        self.wait(5.)
        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))
        self.wait(5.)
        self.play(to_draw.UnWrite(self.captions_mob[1]))
        self.wait()

    def change_cap(self):
        self.caps = ["你不觉得第(3)小题比第(2)小题简单吗",
                     "要注意, \"平行四边形\"这个条件会产生误解"]


class Last(TripleScene2):
    CONFIG = {
        "words": "制作: by bilibili.洛洛洛-洛洛洛_dx,\n\n 剪辑: by bilibili.zhengyang051119Alexis \n\nbgm: Ffrench - You Are"
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


