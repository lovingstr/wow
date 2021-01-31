from manimlib.imports import *
from luoluoluo_useful.imports import *
from luoluoluo_useful.MySceneLuoluoluo.MyScenes import *
from luoluoluo_useful.MyFontLuoluoluo.MyFontSourceHansfont import WildlyArrogantPixelFont as Sans_font
from luoluoluo_useful.MyFontLuoluoluo.MyFontSourceHansfont import SourceHansfontDot
from manim_sandbox.utils.imports import Angle

WAIT_TIME = 4.

MKnb = VG = VGroup
size21 = 2.
W21, H21 = 0.5 * size21, 0.6339745962156 * size21


class Begin(LuoVBegin):
    CONFIG = {
        "TextAbout": "bilibili.洛洛洛-洛洛洛_dx -- 暂时叫“行列式”吧。"
    }


class WaterMater(LuoScene):
    def construct(self):
        self.text = NaOH(SourceHansfont("bilibili.洛洛洛-洛洛洛_dx"), 0).scale(.7).set_opacity(.7)
        self.add(self.text)


class Trip1(LuoScene):
    def construct(self):
        self.wait()
        self.play(Write(NaOH(self.captions_mob[0])))
        self.wait()
        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))
        self.wait()
        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))
        self.wait()

    def setupPic(self):
        pass
        # DotA = self.DotA = Dot(RIGHT).set_color("#81D3D0")
        # DotB = self.DotB = Dot(2 * UP).set_color("#FFC0FB")
        # DotC = self.DotC = Dot(2 * LEFT).set_color("#D1FF62")
        #
        # tag = self.TriAnGle_MWorker = MTriangle(P(DotA), P(DotB), P(DotC))
        #
        # self.DotD = Dot(tag.bisect_of_angle_points[0]).set_color("#B5D379")
        # self.DotE = Dot(cross_lines_point(MVerticalLine(P(self.DotD), MT2P(P(DotA), P(DotB))), MT2P(P(DotA), P(DotB))))\
        #     .set_color("#47D3BF")
        # self.DotF = Dot(cross_lines_point(MVerticalLine(P(self.DotD), MT2P(P(DotC), P(DotA))), MT2P(P(DotC), P(DotA)))) \
        #     .set_color("#47D3BF")
        # self.DotG = Dot(cross_lines_point(MParallelLine(P(DotB), MT2P(P(DotA), P(DotC))), MT2P(P(self.DotA), P(self.DotD))))\
        #     .set_color("#9DE9FF")
        #
        # self.lineAB = Line(P(self.DotA), P(self.DotB)).set_color("#5EE4F1")
        # self.lineAC = Line(P(self.DotA), P(self.DotC)).set_color("#41F1BD")
        # self.lineBC = Line(P(self.DotB), P(self.DotC)).set_color("#B1EC91")
        # self.lineAD = Line(P(self.DotA), P(self.DotD)).set_color("#5EC2D1")
        # self.lineBG = Line(P(self.DotB), P(self.DotG)).set_color("#5DD394")
        # self.lineDG = Line(P(self.DotD), P(self.DotG)).set_color("#5EC2D1")
        # self.lineCG = Line(P(self.DotC), P(self.DotG)).set_color("#F1A8F0")
        #
        # self.tex_A = SourceHansfontDot(self.DotA, text="A").scale(.7).next_to(self.DotA, UR, buff=SMALL_BUFF)
        # self.tex_B = SourceHansfontDot(self.DotB, text="B").scale(.7).next_to(self.DotB, UR, buff=SMALL_BUFF)
        # self.tex_C = SourceHansfontDot(self.DotC, text="C").scale(.7).next_to(self.DotC, UR, buff=SMALL_BUFF)
        # self.tex_D = SourceHansfontDot(self.DotD, text="D").scale(.7).next_to(self.DotD, UR, buff=SMALL_BUFF)
        # self.tex_E = SourceHansfontDot(self.DotE, text="E").scale(.7).next_to(self.DotE, UR, buff=SMALL_BUFF)
        # self.tex_F = SourceHansfontDot(self.DotF, text="F").scale(.7).next_to(self.DotF, UR, buff=SMALL_BUFF)
        # self.tex_G = SourceHansfontDot(self.DotG, text="G").scale(.7).next_to(self.DotG, UR, buff=SMALL_BUFF)
        #
        # self.text1 = NaOH(WildlyArrogantPixelFont("then, BG = AB"), 0).scale(.7).shift(RIGHT * 3)
        # self.text2 = NaOH(WildlyArrogantPixelFont("BG parallel to AC , then BG : BD = AC : AD"), 0).scale(.7).next_to(self.text1, DOWN, buff=SMALL_BUFF)

    def set_other1(self):
        self.set_other2()

    def set_other2(self):
        pass

    def change_cap(self):
        self.caps = ["在初中阶段, 有许多的数学问题是很难直接解决的",
                     "但用一些小结论, 可以轻松证明",
                     "就让我们来看看吧"]



# class Trip2(FourierOfPiSymbol):
#     CONFIG = {
#         "tex": "\\vartheta",
#         "n_vectors": 51,
#         "run_time": 30,
#     }
class Trip2(Trip1):
    CONFIG = {
        "part_name": "inscribed square problem",
        "solver": "Andrew Lobb & Joshua Greene"
    }
    def construct(self):
        self.wait(WAIT_TIME)
        self.add(self.point_path)
        self.play(UpdateFromAlphaFunc(self.point1, self.anim1, rate_func=smooth), run_time=10.)
        self.wait()
        self.point_path.clear_updaters()
        self.point1.restore()
        self.play(*[ShowCreation(line) for line in self.Square_Group_M])
        # self.wait()
        # self.play(UpdateFromAlphaFunc(self.point1, self.anim1, rate_func=smooth, run_time=2 * 6.),
        #           UpdateFromAlphaFunc(self.point2, self.anim1, rate_func=linear, run_time=2 * 8.),
        #           UpdateFromAlphaFunc(self.point3, self.anim1, rate_func=double_smooth, run_time=2 * 10.),
        #           UpdateFromAlphaFunc(self.point4, self.anim1, rate_func=smooth, run_time=2 * 12.))

    def setupPic(self):
        self.point1 = Dot().set_color("#62A4C3").move_to(SVGMobject("PiCreatures_plain.svg")[4].scale(3.).point_from_proportion(0)).save_state()
        self.point2 = self.point1.copy().set_color("#A490C3").save_state()
        self.point3 = self.point2.copy().set_color("#57C372").save_state()
        self.point4 = self.point3.copy().set_color("#C37049").save_state()

        def anim(dot_p, alpha):
            dot_p.move_to(SVGMobject("PiCreatures_plain.svg").scale(3.)[4].point_from_proportion(alpha))

        self.anim1 = anim
        self.point_path = TracedPath(self.point1.get_center, stroke_width=6., stroke_color="#79DFFF")
        line1 = Line(self.point1.get_center(), self.point2.get_center()).set_color("#96D3FE").add_updater(lambda line: line.become(Line(self.point1.get_center(), self.point2.get_center()).set_color("#96D3FE")))
        line2 = Line(self.point2.get_center(), self.point3.get_center()).set_color("#96D3FE").add_updater(lambda line: line.become(Line(self.point2.get_center(), self.point3.get_center()).set_color("#96D3FE")))
        line3 = Line(self.point3.get_center(), self.point4.get_center()).set_color("#96D3FE").add_updater(lambda line: line.become(Line(self.point3.get_center(), self.point4.get_center()).set_color("#96D3FE")))
        line4 = Line(self.point4.get_center(), self.point1.get_center()).set_color("#96D3FE").add_updater(lambda line: line.become(Line(self.point4.get_center(), self.point1.get_center()).set_color("#96D3FE")))
        self.Square_Group_M = VG(line1, line2, line3, line4)  # MayBe

    def set_other2(self):
        self.set_other3()

    def set_other3(self):
        pass

    def change_cap(self):
        self.caps = []


class Trip21(Trip2):
    CONFIG = {
        "part_name": "inscribed square problem",
        "solver": "Andrew Lobb & Joshua Greene"
    }

    def construct(self):
        self.wait(WAIT_TIME)

        self.play(Write(NaOH(self.captions_mob[0])))
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))
        self.wait(WAIT_TIME)

        self.play(
            AnimationGroup(
                AnimationGroup(*[Write(dot) for dot in self.list_dots]),
                AnimationGroup(*[Write(tex) for tex in self.list_tex]),
                lag_ratio=.3)
        )
        self.wait(WAIT_TIME)

        self.play(*[ShowCreation(line) for line in self.Group_lines])
        self.wait(WAIT_TIME)

        self.play(*[Write(dot) for dot in self.list_dotS])
        self.wait(WAIT_TIME)

        self.play(*[ShowCreation(line) for line in self.Group_lineS])
        self.wait(WAIT_TIME)

        self.play(
            to_draw.RandomSpinToNothing(
                VG(*self.list_dots, *self.list_tex, *self.Group_lines, *self.list_dotS, *self.Group_lineS)
            )
        )
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))
        self.wait(WAIT_TIME)

        self.play(AnimationGroup(
            AnimationGroup(*[FadeInFromDown(image) for image in self.people_images], lag_ratio=.5),
            AnimationGroup(*[Write(name) for name in self.people_names], lag_ratio=.5), lag_ratio=.3))

        self.play(*[FadeOutAndShiftDown(image) for image in self.people_images],
                  *[to_draw.UnWrite(name) for name in self.people_names])
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[2], NaOH(self.captions_mob[3])))
        self.wait(WAIT_TIME)

        self.play(Write(self.necessary))
        self.wait(WAIT_TIME)

        self.play(to_draw.UnWrite(self.necessary))
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[3], NaOH(self.captions_mob[4])))
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[4], NaOH(self.captions_mob[5])))
        self.wait(WAIT_TIME)

        self.play(AnimationGroup(*[Write(word) for word in self.title], lag_ratio=0.3))
        self.wait(WAIT_TIME)

    def setupPic(self):
        # person
        self.people_images = Group(ImageMobject("images1_people/Andrew Lobb.jpg").scale(2.).shift(LEFT * 3.5),
                                   ImageMobject("images1_people/Joshua Greene.jpg").scale(2.).shift(RIGHT * 3.5))

        self.people_names = VG(NaOH(Sans_font("Andrew Lobb"), 0).next_to(self.people_images[0], DOWN, buff=SMALL_BUFF),
                               NaOH(Sans_font("Joshua Greene"), 0).next_to(self.people_images[1], DOWN, buff=SMALL_BUFF)
                               )

        # geometry creating

        self.Dot_A = Dot(np.array((- W21, H21, 0.)), color="#70A7FF")
        self.Dot_B = Dot(np.array((W21, H21, 0.)), color="#9A84FF")
        self.Dot_C = Dot(np.array((W21, - H21, 0.)), color="#87FF9E")
        self.Dot_D = Dot(np.array((- W21, - H21, 0.)), color="#F2B2FF")
        self.list_dots = [self.Dot_A, self.Dot_B, self.Dot_C, self.Dot_D]

        self.Tex_A = SourceHansfontDot(self.Dot_A, text="A").scale(.7).next_to(self.Dot_A, UL)
        self.Tex_B = SourceHansfontDot(self.Dot_B, text="B").scale(.7).next_to(self.Dot_B, UR)
        self.Tex_C = SourceHansfontDot(self.Dot_C, text="C").scale(.7).next_to(self.Dot_C, DR)
        self.Tex_D = SourceHansfontDot(self.Dot_D, text="D").scale(.7).next_to(self.Dot_D, DL)
        self.list_tex = [self.Tex_A, self.Tex_B, self.Tex_C, self.Tex_D]

        line2 = Line(self.Dot_B.get_center(), self.Dot_C.get_center()).set_color("#66CCFF")
        line4 = Line(self.Dot_D.get_center(), self.Dot_A.get_center()).set_color("#66CCFF")

        Circle1Center = Dot(np.array([0., 1.5 * size21, 0.]))
        Circle2Center = Dot(np.array([0., - 1.5 * size21, 0.]))
        self.Arc1 = Angle(self.Dot_A, Circle1Center, self.Dot_B, radius=length_of_two_point(
            Circle1Center.get_center(), self.Dot_B.get_center()), color="#66CCFF")
        self.Arc2 = Angle(self.Dot_C, Circle2Center, self.Dot_D, radius=length_of_two_point(
            Circle2Center.get_center(), self.Dot_D.get_center()), color="#66CCFF")
        self.Group_lines = VG(line2, self.Arc1, line4, self.Arc2)

        self.Dot_1 = Dot(np.array([-0.5 * size21, size21 * 0, 0.])).set_color("#8D5630")
        self.Dot_2 = Dot(np.array([0 * size21, size21 * 0.5, 0.])).set_color("#66CCFF")
        self.Dot_3 = Dot(np.array([0.5 * size21, size21 * 0, 0.])).set_color("#FFCA7B")
        self.Dot_4 = Dot(np.array([0 * size21, size21 * - 0.5, 0.])).set_color("#4CFADE")
        self.list_dotS = [self.Dot_1, self.Dot_2, self.Dot_3, self.Dot_4]

        self.LineS1 = Line(self.Dot_4.get_center(), self.Dot_1.get_center()).set_color("#8D5630")
        self.LineS2 = Line(self.Dot_1.get_center(), self.Dot_2.get_center()).set_color("#66CCFF")
        self.LineS3 = Line(self.Dot_2.get_center(), self.Dot_3.get_center()).set_color("#FFCA7B")
        self.LineS4 = Line(self.Dot_3.get_center(), self.Dot_4.get_center()).set_color("#4CFADE")
        self.Group_lineS = VG(self.LineS1, self.LineS2, self.LineS3, self.LineS4)

        self.necessary = SourceHansfont("① 在一条封闭曲线上, 总存在四点, 使其构成的四边形是菱形\n\n"
                                        "② 在一条封闭曲线上, 总存在四点, 使其构成的四边形是矩形\n\n"
                                        "③ 在一条封闭曲线上, 总存在四点, 使其构成的四边形是平行四边形\n").scale(.5)

        self.necessary = NaOH(self.necessary, 0)

        self.text1 = SourceHansfont("下列说法正确的有                                             (  )").set_color(BLACK).scale(.7).shift(UP)
        self.choise1 = SourceHansfont("① 在菱形上总能找到四个点, 得到以这四个点为顶点的平行四边形").set_color(BLUE_E).shift(np.array([0., 0., 0.])).scale(.5)
        self.choise2 = SourceHansfont("② 在平行四边形上无法总能找到四个点, 得到以这四个点为顶点的菱形").set_color(TEAL_D).shift(np.array(DOWN * .5)).scale(.5).align_to(self.choise1, LEFT)
        self.choise3 = SourceHansfont("③ 在三角形上总能找到四个点, 得到以这四个点为顶点的不是正方形的菱形").set_color(GREEN_C).shift(DOWN * 1.).scale(.5).align_to(self.choise1, LEFT)
        self.choise4 = SourceHansfont("④ 在平行四边形上总能找到四个点, 得到以这四个点为顶点的正方形").set_color(YELLOW_D).shift(DOWN * 1.5).scale(.5).align_to(self.choise1, LEFT)
        self.choiseA = SourceHansfont("A. ①③④").set_color("#8D5630").next_to(self.choise4, DOWN).align_to(self.choise4, LEFT).scale(.7)
        self.choiseB = SourceHansfont("B. ②④").set_color("#66CCFF").next_to(self.choiseA, RIGHT).scale(.7)
        self.choiseC = SourceHansfont("C. ①④").set_color("#FFCA7B").next_to(self.choise4, DOWN).align_to(self.choise4, RIGHT).scale(.7)
        self.choiseD = SourceHansfont("D. ①③").set_color("#4CFADE").next_to(self.choiseC, LEFT).scale(.7)
        self.choice_true_1 = TexMobject("A").set_color("#8D5630").next_to(self.text1, RIGHT, buff=-.43).scale(0.5)
        self.title = VG(self.text1, self.choise1, self.choise2, self.choise3, self.choise4, self.choiseA, self.choiseB,
                        self.choiseC, self.choiseD)

    def set_other2(self):
        self.set_other21()

    def set_other21(self):
        pass

    def change_cap(self):
        self.caps = ["part 1. inscribed square problem",
                     "在一条封闭曲线上, 总存在四点, 使其构成的四边形是正方形",
                     "这个定理是Andrew Lobb和Joshua Greene在疫情期间太闲证明出来的",
                     "它有几个推论(这个命题的必要条件)",
                     "那这个定理有什么用呢",
                     "那就是在选择题的时候有用"]


class Trip3(Trip2):
    CONFIG = {
        "part_name": "determinanteterminant working",
    }

    def construct(self):
        self.play(Write(self.axis))

        self.wait(WAIT_TIME)

        self.play(Write(NaOH(self.captions_mob[0])))
        self.wait(WAIT_TIME)

        self.play(AnimationGroup(AnimationGroup(Write(self.dot_O), Write(self.tex_O), lag_ratio=.3),
                                 AnimationGroup(Write(self.dot_test1), Write(self.tex_A), lag_ratio=.3),
                                 AnimationGroup(Write(self.dot_test2), Write(self.tex_B), lag_ratio=.3), lag_ratio=.5))
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_mob[1])))
        self.wait(WAIT_TIME)

        self.play(AnimationGroup(ShowCreation(self.line1),
                                 ShowCreation(self.line2),
                                 ShowCreation(self.line3),
                                 lag_ratio=.3))
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))
        self.wait(WAIT_TIME)

        self.play(AnimationGroup(FadeIn(self.triangleAB_O), Write(self.StriAB_O), lag_ratio=.7))
        self.wait(WAIT_TIME)

        self.play(to_draw.UnWrite(self.StriAB_O))
        self.wait(WAIT_TIME)

        self.play(
            AnimationGroup(
                *[
                    ReplacementTransform(name, pos)
                    for name, pos in zip([self.tex_A, self.tex_B], [self.tex_PosA, self.tex_PosB])
                ]
            ), ReplacementTransform(self.captions_mob[2], NaOH(self.captions_mob[3]))
        )
        self.wait(WAIT_TIME * 2)

        self.play(ReplacementTransform(self.captions_mob[3], NaOH(self.captions_mob[4])))
        self.wait(WAIT_TIME)

        self.play(AnimationGroup(Write(self.Dot_C), AnimationGroup(ShowCreation(self.line_CD), ShowCreation(self.line_CE), lag_ratio=.5),
                                 AnimationGroup(Write(self.Dot_D), Write(self.Dot_E), lag_ratio=.5),
                                 AnimationGroup(*[FadeInFromDown(triangle)
                                                  for triangle in VG(
                                         self.triangleDO_B, self.triangleOE_A, self.triangleAC_B
                                     )], lag_ratio=.3),
                                 lag_ratio=.7))
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[4], NaOH(self.captions_mob[5])))
        self.wait(WAIT_TIME)

        self.play(AnimationGroup(to_draw.UnWrite(self.Dot_C),
                                 AnimationGroup(*[FadeOutAndShiftDown(triangle)
                                                  for triangle in VG(
                                         self.triangleAC_B, self.triangleOE_A, self.triangleDO_B
                                     )], lag_ratio=.3),
                                 AnimationGroup(to_draw.UnWrite(self.Dot_D), to_draw.UnWrite(self.Dot_E), lag_ratio=.5),
                                 AnimationGroup(Uncreate(self.line_CD), Uncreate(self.line_CE), lag_ratio=.5),

                                 lag_ratio=.7))
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[5], NaOH(self.captions_mob[6])))
        self.wait(WAIT_TIME * 2)

        self.play(ReplacementTransform(self.captions_mob[6], NaOH(self.captions_mob[7])))
        self.wait(WAIT_TIME)

        self.play(AnimationGroup(ReplacementTransform(self.tex_PosA.copy(), self.tex1[0: 6]), Write(self.tex1[6: 9]),
                                 ReplacementTransform(self.tex_PosB.copy(), self.tex1[9: 15]), lag_ratio=.7))
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[7], NaOH(self.captions_mob[8])))
        self.wait(WAIT_TIME)

        self.play(AnimationGroup(ReplacementTransform(self.tex1[1].copy(), self.tex2[1]),
                                 Write(self.tex2[2: 5]),
                                 ReplacementTransform(self.tex1[13].copy(), self.tex2[5]),
                                 Write(self.tex2[6: 9]),
                                 ReplacementTransform(self.tex1[10].copy(), self.tex2[9]),
                                 Write(self.tex2[10: 12]),
                                 ReplacementTransform(self.tex1[4].copy(), self.tex2[13]), lag_ratio=.7))
        self.wait(WAIT_TIME)

        self.play(AnimationGroup(Write(self.tex2[0]), Write(self.tex2[14]), Write(self.tex2[15]), Write(self.tex2[16]),
                                 Write(self.tex2[17]), Write(self.tex2[18]), Write(self.tex2[19]),
                                 Write(self.tex2[20]), Write(self.tex2[21]), Write(self.tex2[22]), lag_ratio=.65))
        self.wait(WAIT_TIME)

        self.play(to_draw.UnWriteRandom(self.tex1),
                  to_draw.UnWriteRandom(self.tex2), lag_ratio=.9)
        self.play(ReplacementTransform(self.captions_mob[8], NaOH(self.captions_mob[9])))

        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(VG(self.line1, self.line2, self.line3), self.line_all),
                  ReplacementTransform(self.triangleAB_O, self.papolygon),
                  ReplacementTransform(VG(self.tex_PosA, self.tex_PosB, self.tex_O), self.texaall),
                  ReplacementTransform(VG(self.dot_test1, self.dot_test2, self.dot_O), self.dotnumall),)
        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[9], NaOH(self.captions_mob[10])))
        self.wait(WAIT_TIME)

        self.play(*[ReplacementTransform(name, pos)
                    for name, pos in zip(self.texaall, self.tessxs)])
        self.wait(WAIT_TIME)

        self.play(Write(self.tex3_copy, run_time=8.),
                  AnimationGroup(*[ReplacementTransform(redp, red) for redp, red in zip(self.red_parp, self.red_tex)], lag_ratio=.7),
                  AnimationGroup(*[ReplacementTransform(greenp, green) for greenp, green in zip(self.green_parp, self.green_tex)], lag_ratio=.7),
                  lag_ratio=.3)

        self.wait(WAIT_TIME)

        self.play(self.tex3_copy[-1].set_color, ("#7FB665", "#707070", "#FF6F4D"),  run_time=4., rate_func=smooth)

        self.wait(WAIT_TIME)

        self.play(ReplacementTransform(self.captions_mob[10], NaOH(self.captions_mob[11])))
        self.wait(WAIT_TIME)

        self.play(to_draw.UnWrite(VG(self.line_all, self.papolygon, self.tessxs, self.dotnumall)),
                  FadeOut(VG(self.tex3_copy, self.red_tex, self.green_tex)))

        self.play(to_draw.UnWrite(self.captions_mob[11][1:]))
        self.wait(WAIT_TIME)

    def setupPic(self):
        self.axis = NumberPlane(
            axis_config=dict(stroke_color=ORANGE, stroke_width=4)
        )
        self.dot_test1 = Dot(np.array([1.5, 1., 0.])).set_color("#7FB665")
        self.dot_test2 = Dot(np.array([.5, 2., 0.])).set_color("#FF6F4D")
        self.dot_O = Dot(ORIGIN).set_color("#909090")
        self.Dot_D = Dot(UP * 2).set_color("#707070")
        self.Dot_E = Dot(RIGHT * 1.5).set_color("#707070")
        self.Dot_C = Dot(UP * 2 + RIGHT * 1.5).set_color("#707070")

        self.line1 = Line(ORIGIN, self.dot_test1.get_center()).set_color("#7FB665")
        self.line2 = Line(ORIGIN, self.dot_test2.get_center()).set_color("#FF6F4D")
        self.line3 = Line(self.dot_test1.get_center(), self.dot_test2.get_center()).set_color("#BF9259")

        # Dashedline
        self.line_CD = DashedLine(self.Dot_C.get_center(), self.Dot_D.get_center()).set_color("#707070")
        self.line_CE = DashedLine(self.Dot_C.get_center(), self.Dot_E.get_center()).set_color("#707070")

        self.tex_A = SourceHansfontDot(self.dot_test1, text="A").scale(.7).next_to(self.dot_test1, DR, buff=SMALL_BUFF)
        self.tex_B = SourceHansfontDot(self.dot_test2, text="B").scale(.7).next_to(self.dot_test2, UR, buff=SMALL_BUFF)
        self.tex_O = SourceHansfontDot(self.dot_O, text="O").scale(.7).next_to(self.dot_O, DL, buff=SMALL_BUFF)
        self.triangleAB_O = Polygon(self.dot_test1.get_center(), self.dot_test2.get_center(), ORIGIN, stroke_opacity=0.,
                                    fill_color="#7FD0E1", fill_opacity=.7)

        # special
        self.dot1 = Dot(np.array(np.array([-1.46, 0.97, 0.]))).set_color("#707070")
        self.dot2 = Dot(np.array(np.array([-1.52, -1.41, 0.]))).set_color("#707070")
        self.dot3 = Dot(np.array(np.array([1.32, -1.83, 0.]))).set_color("#707070")
        self.dot4 = Dot(np.array(np.array([1.78, 0.59, 0.]))).set_color("#707070")
        self.dot5 = Dot(np.array(np.array([0.32, 1.97, 0.]))).set_color("#707070")
        self.dotnumall = VG(self.dot1, self.dot2, self.dot3, self.dot4, self.dot5)

        self.aline1 = Line(self.dot1, self.dot2).set_color("#707070")
        self.aline2 = Line(self.dot2, self.dot3).set_color("#707070")
        self.aline3 = Line(self.dot3, self.dot4).set_color("#707070")
        self.aline4 = Line(self.dot4, self.dot5).set_color("#707070")
        self.aline5 = Line(self.dot5, self.dot1).set_color("#707070")
        self.line_all = VG(self.aline1, self.aline2, self.aline3, self.aline4, self.aline5)

        self.range_polygon = Polygon(self.dot1.get_center(), self.dot2.get_center(), self.dot3.get_center(), self.dot4.get_center(), self.dot5.get_center())
        self.texa1 = self._get_label(self.dot1, direction=UL, buff=SMALL_BUFF)
        self.texa2 = self._get_label(self.dot2, direction=DL, buff=SMALL_BUFF)
        self.texa3 = self._get_label(self.dot3, direction=UR, buff=SMALL_BUFF)
        self.texa4 = self._get_label(self.dot4, direction=UR, buff=SMALL_BUFF)
        self.texa5 = self._get_label(self.dot5, direction=UR, buff=SMALL_BUFF)
        self.texaall = VG(self.texa1, self.texa2, self.texa3, self.texa4, self.texa5)

        self.tessxs1 = self._get_label(self.dot1, words_for="(a1, b1)", direction=UL, buff=SMALL_BUFF)
        self.tessxs2 = self._get_label(self.dot2, words_for="(a2, b2)", direction=DL, buff=SMALL_BUFF)
        self.tessxs3 = self._get_label(self.dot3, words_for="(a3, b3)", direction=UR, buff=SMALL_BUFF)
        self.tessxs4 = self._get_label(self.dot4, words_for="(a4, b4)", direction=UR, buff=SMALL_BUFF)
        self.tessxs5 = self._get_label(self.dot5, words_for="(a5, b5)", direction=UR, buff=SMALL_BUFF)
        self.tessxs = VG(self.tessxs1, self.tessxs2, self.tessxs3, self.tessxs4, self.tessxs5)

        self.papolygon = Polygon(self.dot1.get_center(), self.dot2.get_center(), self.dot3.get_center(), self.dot4.get_center(), self.dot5.get_center(), stroke_opacity=0., fill_color="#707070", fill_opacity=.7)


        # Black triangles
        self.triangleDO_B = Polygon(self.Dot_D.get_center(), ORIGIN, self.dot_test2.get_center(), stroke_opacity=0.,
                                    fill_color="#707070", fill_opacity=.7)
        self.triangleAC_B = Polygon(self.dot_test1.get_center(), self.Dot_C.get_center(), self.dot_test2.get_center(), stroke_opacity=0.,
                                    fill_color="#707070", fill_opacity=.7)
        self.triangleOE_A = Polygon(ORIGIN, self.Dot_E.get_center(), self.dot_test1.get_center(), stroke_opacity=0.,
                                    fill_color="#707070", fill_opacity=.7)

        self.tex_PosA = SourceHansfont("(3, 2)").set_color("#7FB665").scale(.7).next_to(self.dot_test1, DR, buff=SMALL_BUFF)
        self.tex_PosB = SourceHansfont("(1, 4)").set_color("#FF6F4D").scale(.7).next_to(self.dot_test2, UR, buff=SMALL_BUFF)

        # FONT
        self.StriAB_O = NaOH(Sans_font("S=?").scale(.7).move_to(self.triangleAB_O), 0, "#50827B", "#55964B")

        # text
        self.tex1 = SourceHansfont("(3, 2) & (1, 4)").scale(.8).move_to(DOWN).set_color("#636363")
        self.tex2 = SourceHansfont("(3 × 4 - 1 × 2) ÷ 2 = 5").scale(.8)\
            .next_to(self.tex1, DOWN, buff=SMALL_BUFF).set_color("#636363")
        self.tex3 = SourceHansfont("a1b2 + a2b3 + a3b4 + a4b5 + a5b1 - (b1a2 + b2a3 + b3a4 + b4a5 + b5a1) = 2S").scale(.7).set_color("#707070").next_to(self.tex2, DOWN)
        self.tex3_copy = self.tex3.copy()
        # set colors
        self.tex1[0: 6].set_color("#7FB665")
        self.tex1[9: 15].set_color("#FF6F4D")

        self.tex2[1].set_color("#7FB665")
        self.tex2[5].set_color("#FF6F4D")
        self.tex2[9].set_color("#FF6F4D")
        self.tex2[13].set_color("#7FB665")

        self.tessxs1[1: 3].set_color("#FF6F4D")
        self.tessxs2[1: 3].set_color("#FF6F4D")
        self.tessxs3[1: 3].set_color("#FF6F4D")
        self.tessxs4[1: 3].set_color("#FF6F4D")
        self.tessxs5[1: 3].set_color("#FF6F4D")
        self.red_parp = VG(self.tessxs1[1: 3].copy(), self.tessxs2[1: 3].copy(), self.tessxs3[1: 3].copy(), self.tessxs4[1: 3].copy(), self.tessxs5[1: 3].copy(), self.tessxs2[1: 3].copy(), self.tessxs3[1: 3].copy(), self.tessxs4[1: 3].copy(), self.tessxs5[1: 3].copy(), self.tessxs1[1: 3].copy())

        self.tessxs1[5: 7].set_color("#7FB665")
        self.tessxs2[5: 7].set_color("#7FB665")
        self.tessxs3[5: 7].set_color("#7FB665")
        self.tessxs4[5: 7].set_color("#7FB665")
        self.tessxs5[5: 7].set_color("#7FB665")
        self.green_parp = VG(self.tessxs2[5: 7].copy(), self.tessxs3[5: 7].copy(), self.tessxs4[5: 7].copy(), self.tessxs5[5: 7].copy(), self.tessxs1[5: 7].copy(), self.tessxs1[5: 7].copy(), self.tessxs2[5: 7].copy(), self.tessxs3[5: 7].copy(), self.tessxs4[5: 7].copy(), self.tessxs5[5: 7].copy())

        self.tex3[0: 2].set_color("#FF6F4D")
        self.tex3[7: 9].set_color("#FF6F4D")
        self.tex3[14: 16].set_color("#FF6F4D")
        self.tex3[21: 23].set_color("#FF6F4D")
        self.tex3[28: 30].set_color("#FF6F4D")
        self.tex3[38: 40].set_color("#FF6F4D")
        self.tex3[45: 47].set_color("#FF6F4D")
        self.tex3[52: 54].set_color("#FF6F4D")
        self.tex3[59: 61].set_color("#FF6F4D")
        self.tex3[66: 68].set_color("#FF6F4D")
        self.red_tex = VG(self.tex3[0: 2], self.tex3[7: 9], self.tex3[14: 16], self.tex3[21: 23], self.tex3[28: 30], self.tex3[38: 40], self.tex3[45: 47], self.tex3[52: 54], self.tex3[59: 61], self.tex3[66: 68])

        self.tex3[2: 4].set_color("#7FB665")
        self.tex3[9: 11].set_color("#7FB665")
        self.tex3[16: 18].set_color("#7FB665")
        self.tex3[23: 25].set_color("#7FB665")
        self.tex3[30: 32].set_color("#7FB665")
        self.tex3[36: 38].set_color("#7FB665")
        self.tex3[43: 45].set_color("#7FB665")
        self.tex3[50: 52].set_color("#7FB665")
        self.tex3[57: 59].set_color("#7FB665")
        self.tex3[64: 66].set_color("#7FB665")
        self.green_tex = VG(self.tex3[2: 4], self.tex3[9: 11], self.tex3[16: 18], self.tex3[23: 25], self.tex3[30: 32], self.tex3[36: 38], self.tex3[43: 45], self.tex3[50: 52], self.tex3[57: 59], self.tex3[64: 66])

    def _get_label(self, dot:Dot, words_for=False, **kwargs):
        if words_for:
            return SourceHansfont(str(words_for)).scale(.7).next_to(dot, **kwargs).set_color("#707070")
        tup = (a, b) = float("%.2f" % dot.get_center()[0]), float("%.2f" % dot.get_center()[1])
        return SourceHansfont(str(tup)).scale(.7).next_to(dot, **kwargs).set_color("#707070")

    def set_other3(self):
        self.set_other4()

    def set_other4(self):
        pass

    def change_cap(self):
        self.caps = ["part 2. determinanteterminant",
                     "如图, 我们已知三点A、B、O",
                     "我们想求这三点为顶点构成的三角形△ABO的面积。",
                     "比如, 当A是(3,2)、B是(1,4)时, 要怎么求三角形△ABO的面积呢？",
                     "当我们想求一个三角形的面积时, 我们一般会用“割补法”",
                     "这太麻烦了, 不是吗？",
                     "我们需要找到一个简便的方法…",
                     "行列式随之而生！",
                     "（P.s: 此处外项相乘减去内项相乘, 如果为负数, 加个绝对值就好了！）",
                     "同样的, 我们可以推理出…",
                     "这个式子…",
                     "我们在以后的视频再把这个式子证明一遍吧 :  )"]


class for_while_ed(LuoVLast):
    CONFIG = {
        "words": "制作: by bilibili.洛洛洛-洛洛洛_dx,\n\n 剪辑: by bilibili.zhengyang051119Alexis \n\nbgm: Ffrench - My Time"
    }



