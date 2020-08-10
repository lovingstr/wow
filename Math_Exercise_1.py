# by a LiYiRun
# Is my own code by a clever boy luo luo luo luo luo luo 

# The animation engine is 3b1b manim

#Use animation outside the engine: WriteRamdon and UnWriteRamdon

# Used a geometry tool

from manimlib.imports import *
# from manim_sandbox.utils.imports import *


class Mytext_1(Text):
    CONFIG = {
        'color': BLACK,
        'fill_opacity': 0.7,
        'stroke_width': 0,
        'font': '思源黑体 CN Bold',
        'gradient': None,
        'size': 1,
        'tab_width': 4,
    }


class CodeLine(Text):
    CONFIG = dict(t2c={
        "~": WHITE
    },
        font='Consolas', size=.6, color=DARK_GRAY, plot_depth=2)

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class Choice_1(Scene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):

        captions = [
            # step 1
            "显然， 只有C选项分母有未知数， 故选C",  # 0

            # step 2
            "由不等式性质3可得：",  # 1
            "-m<-n",  # 2
            "于是选项D错误",  # 3
            "所以答案是D",  # 4

            # step 3
            "选项A不是因式分解",  # 5
            "选项B没分解完",  # 6
            "选项D分解错误",  # 7
            "选项D应该是：",  # 8
            "故选C",  # 9

            # step 4
            "显然，它们的交集是绿色这一部分",  # 10
            "故选A",  # 11

            # step 5
            "~",  # 12
            "将右图旋转180°，得：",  # 13
            "与D图一样",  # 14
            "故选D",  # 15
            ""
        ]
        captions_mob = VGroup(
            *[
                CodeLine(cap, font='思源黑体 CN Bold', size=.5).to_edge(DOWN * 1.2)
                    .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in captions
            ]
        )
        captions_tex = [
            "2x ^ {2} - 4y + 2 = 2{(x^{2} - 2 y + 1)} = 2 {(x+1)}^{2}",
            "",
            ""
        ]

        captions_tex_mob = VGroup(
            *[
                TexMobject(cap).scale(.5).set_color(BLACK).to_edge(DOWN * 1.2)
                .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in captions_tex
            ]
        )

        text1 = CodeLine("1.下列式子是分式的是~~~~~~~~~~~~~~~~~~~~~~~~(  )", font='思源黑体 CN Bold', ).shift(UP)
        choise1_1 = TexMobject("A\\text{. }\\frac{1}{3}{x}").set_color(BLUE_E).shift(DL + LEFT * 3.5).scale(.5)
        choise2_1 = TexMobject("B\\text{. }{-}\\frac{y}{5}").set_color(TEAL_D).shift(DL + LEFT * .5).scale(.5)
        choise3_1 = TexMobject("C\\text{. }\\frac{1}{x+1}").set_color(GREEN_C).shift(DR + RIGHT * .5).scale(.5)
        choise4_1 = TexMobject("D\\text{. }{-}\\frac{x}{2}+{y}").set_color(YELLOW_B).shift(DR + RIGHT * 3.5).scale(.5)
        choice_true_1 = TexMobject("C").set_color(GREEN_B).next_to(text1, RIGHT, buff=-.43).scale(0.5)
        all_1 = VGroup(text1, choise1_1, choise2_1, choise3_1, choise4_1, choice_true_1)

        self.play(Write(text1))
        self.play(Write(choise1_1), Write(choise2_1), Write(choise3_1), Write(choise4_1))

        self.wait(3.)

        self.play(Write(captions_mob[0]))
        self.play(FadeInFromDown(choice_true_1))
        self.wait()

        text2 = CodeLine("2.若m>n，则下列不等式错误的是~~~~~~~~~~~~~~~~~~~~~~~~(  )", font='思源黑体 CN Bold', ).shift(UP)
        choise1_2 = TexMobject("A\\text{. }m+2>n+2").set_color(BLUE_D).shift(DL + LEFT * 3.5).scale(.5)
        choise2_2 = TexMobject("B\\text{. }2m>2n").set_color(TEAL_C).shift(DL + LEFT * .5).scale(.5)
        choise3_2 = TexMobject("C\\text{. }\\frac{m}{2}{>}\\frac{n}{2}").set_color(GREEN_B).shift(
            DR + RIGHT * .5).scale(.5)
        choise4_2 = TexMobject("D\\text{. }{-m>-n}").set_color(YELLOW_D).shift(DR + RIGHT * 3.5).scale(.5)
        choice_true_2 = TexMobject("D").set_color(YELLOW_D).next_to(text2, RIGHT, buff=-.43).scale(.5)
        all_2_title = VGroup(text2, choise1_2, choise2_2, choise3_2, choise4_2)
        all_2 = VGroup(text2, choise1_2, choise2_2, choise3_2, choise4_2, choice_true_2)

        self.play(ReplacementTransform(all_1, all_2_title))

        self.wait(3.)

        list_1 = [
            [[0],
             [1]],
            [[1],
             [2]],
            [[2],
             [3]],
            [[3],
             [4]]
        ]

        for x_x, y_y in list_1:
            self.play(
                *[
                    ReplacementTransform(captions_mob[i], captions_mob[j])
                    for i, j in zip(x_x, y_y)
                ],
                run_time=3.
            )
        self.play(FadeInFromDown(choice_true_2))

        text3 = CodeLine("3.下列各式中，从左到右的变形，属于分解因式的是~~~~~~~~~~~~~~~~~~~~~~~~(  )", font='思源黑体 CN Bold', ).shift(UP)
        choise1_3 = TexMobject("A\\text{. }a(m+n)=am+an").set_color(BLUE_D) \
            .shift(DL + LEFT * 3.5).scale(.5)
        choise2_3 = TexMobject("B\\text{. }a^{2} - b^{2} - c^{2} = (a-b)(a+b) - c^{2}").set_color(TEAL_C) \
            .shift(DR + RIGHT * 2.).scale(.5)
        choise3_3 = TexMobject("C\\text{. }10 x^{2} - 5x = 5x(2x-1)").set_color(GREEN_B) \
            .shift(DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
        choise4_3 = TexMobject("D\\text{. }2 x^2 - 4y + 2 = 2(x^{2} - 2y)").set_color(YELLOW_D) \
            .shift(DR + RIGHT * 2. + DOWN * 1.5).scale(.5)
        choice_true_3 = TexMobject("C").set_color(GREEN_B).next_to(text3, RIGHT, buff=-.43).scale(.5)
        all_3_title = VGroup(text3, choise1_3, choise2_3, choise3_3, choise4_3)
        all_3 = VGroup(text3, choise1_3, choise2_3, choise3_3, choise4_3, choice_true_3)
        self.play(ReplacementTransform(all_2, all_3_title))

        self.wait(3.)

        list_2 = [
            [[4], [5]], [[5], [6]], [[6], [7]], [[7], [8]], [[8], [9]]
        ]
        for x_x, y_y in list_2:
            if (x_x, y_y) != ([8],
                              [9]):
                self.play(
                    *[
                        ReplacementTransform(captions_mob[i], captions_mob[j])
                        for i, j in zip(x_x, y_y)

                    ],
                    rum_time=2.5
                )
            else:
                for i in range(2):
                    captions_tex_mob[0][i].set_color(["#CCFFEE", YELLOW_D][i])
                self.play(ReplacementTransform(captions_mob[y_y[0] - 1], captions_tex_mob[0]))
                self.play(ReplacementTransform(captions_tex_mob[0], captions_mob[y_y[0]]))  # y_y ==
        self.play(FadeInFromDown(choice_true_3))
        title = """4.已知两个不等式的解集在数轴上如图所示，
  则由这两个不等式组成的不等式组的解集为~~~~~~~~~~~~~~~~~~~~~~~~(  )"""
        text4 = CodeLine(title, font='思源黑体 CN Bold').shift(UP)
        choise1_4 = TexMobject("A\\text{. }x>2").set_color(BLUE_D).shift(DL + LEFT * 3.5).scale(.5)
        choise2_4 = TexMobject("B\\text{. }x<2").set_color(TEAL_C).shift(DL + LEFT * -1.).scale(.5)
        choise3_4 = TexMobject("C\\text{. }{x}\\ge{-2}").set_color(GREEN_B).shift(
            DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
        choise4_4 = TexMobject("D\\text{. }{-2}\\le{x}<{2}").set_color(YELLOW_D).shift(
            DL + LEFT * -1. + DOWN * 1.5).scale(.5)  #
        choice_true_4 = TexMobject("A").set_color(BLUE_D).next_to(text4, RIGHT, buff=-.43, aligned_edge=DOWN) \
            .scale(.5).shift(DOWN * .07)
        image_4 = NumberLine(x_max=3.7, x_min=-3.5,
                             color="#8DF6DC",
                             include_tip=True).set_opacity(0.3).add_numbers(number_config={"color": GRAY})

        dot_min = Dot(np.array([-2., 0., 0.])).set_color("#70FEFF").set_opacity(.9)
        line_min_1 = Line(np.array([-2., 0., 0.]), np.array([-2., 1., 0.])).set_color("#70FEFF").set_opacity(.6)
        line_min_2 = Line(np.array([-2., 1., 0.]), np.array([4., 1., 0.])).set_color("#70FEFF").set_opacity(.6)
        dot_bigger_than_dm = Dot(np.array([2., 0., 0.])).set_color(WHITE)\
            .set_stroke(color="#FF8664", width=3, opacity=.9)
        db_than_line_min_1 = Line(np.array([2., 0., 0.]), np.array([2., .7, 0.])).set_color("#FF8664").set_opacity(.6)
        db_than_line_min_2 = Line(np.array([2., .7, 0.]), np.array([4., .7, 0.])).set_color("#FF8664").set_opacity(.6)

        part = Rectangle(height=0.7, width=2., color=GREEN, fill_opacity=.3, stroke_opacity=0.).\
            next_to(db_than_line_min_2, DOWN, buff=0.)
        part.next_to(db_than_line_min_1, RIGHT, buff=0.)

        min_mobject = VGroup(dot_min, line_min_1, line_min_2)
        br_mobject = VGroup(db_than_line_min_1, dot_bigger_than_dm, db_than_line_min_2)
        min_all_mobject = VGroup(image_4, min_mobject, br_mobject)
        min_all_mobject_all = VGroup(min_all_mobject, part)
        min_all_mobject_all_to_save = min_all_mobject_all.copy().scale(.5).move_to(np.array([3.5, -2., 0.]))

        all_4_title = VGroup(text4, choise1_4, choise2_4, choise3_4, choise4_4)
        all_4 = VGroup(text4, choise1_4, choise2_4, choise3_4, choise4_4, choice_true_4, min_all_mobject_all)

        # self.play(ReplacementTransform(all_3, all_4_title))min_all_mobject_all
        self.play(FadeOutAndShiftDown(all_3))
        self.play(Write(min_mobject), Write(image_4))
        self.play(Write(br_mobject))
        self.play(ApplyMethod(min_all_mobject.scale, .5))
        self.play(ApplyMethod(min_all_mobject.move_to, np.array([3.5, -2., 0.])))

        part_at_last = min_all_mobject_all_to_save[1]
        min_all_mobject_all.remove(part)  # Because_that I cannot know the bug
        all_4.add(part_at_last)

        self.play(Write(all_4_title))

        self.wait(3.)

        self.play(ReplacementTransform(captions_mob[9], captions_mob[10]))
        self.play(FadeInFromDown(part_at_last))
        self.play(ReplacementTransform(captions_mob[10], captions_mob[11]))
        self.play(FadeInFromDown(choice_true_4))

        text5 = CodeLine("5.将右边叶片旋转180°后，得到的图形是~~~~~~~~~~~~~~~~~~~~~~~~(  )", font='思源黑体 CN Bold',
                         t2c={"~": WHITE, "右边": "#28F41C"}).shift(UP)
        chestnut = SVGMobject("Exercise_th_choice").set_color(WHITE)\
            .set_stroke(color="#28F41C", width=4.5, opacity=.7).scale(0.5).move_to([4.5, -1., 0.])
        began_svg = VGroup(chestnut, text5)

        chestnut_1 = chestnut.copy().shift(LEFT * 10.).set_color(WHITE).\
            set_stroke(color="#2EEEF4", width=4.5, opacity=.9).flip(axis=RIGHT)
        chestnut_2 = chestnut.copy().shift(LEFT * 8.).set_color(WHITE).\
            set_stroke(color="#37ECD3", width=4.5, opacity=.9).flip()
        chestnut_3 = chestnut.copy().shift(LEFT * 6.).set_color(WHITE).\
            set_stroke(color="#36D59F", width=4.5, opacity=.9)
        chestnut_4 = chestnut.copy().shift(LEFT * 4.).set_color(WHITE).\
            set_stroke(color="#32CB7D", width=4.5, opacity=.9).rotate(180 * DEGREES)

        choice_true_5 = TexMobject("D").set_color("#32CB7D").next_to(text5, RIGHT, buff=-.43).scale(.5)

        choise1_5 = TexMobject("A").set_color("#2EEEF4").next_to(chestnut_1, DOWN, buff=.25).scale(.5)
        choise2_5 = TexMobject("B").set_color("#37ECD3").next_to(chestnut_2, DOWN, buff=.25).scale(.5)
        choise3_5 = TexMobject("C").set_color("#36D59F").next_to(chestnut_3, DOWN, buff=.25).scale(.5)
        choise4_5 = TexMobject("D").set_color("#32CB7D").next_to(chestnut_4, DOWN, buff=.25).scale(.5)

        self.play(ReplacementTransform(captions_mob[11], captions_mob[12]))

        self.wait()

        self.play(ReplacementTransform(all_4, began_svg))
        self.play(ReplacementTransform(chestnut.copy(), chestnut_4))
        self.play(Write(choise4_5))

        self.play(ReplacementTransform(chestnut_4.copy(), chestnut_3))
        self.play(Write(choise3_5))

        self.play(ReplacementTransform(chestnut_3.copy(), chestnut_2))
        self.play(Write(choise2_5))

        self.play(ReplacementTransform(chestnut_2.copy(), chestnut_1))
        self.play(Write(choise1_5))

        chestnut_copy = chestnut.copy().set_fill(opacity=0.)

        line1 = Line(chestnut.get_center(),
                     np.array([chestnut.get_x(RIGHT), chestnut.get_y(ORIGIN), 0.]),
                     color=BLUE_B, stroke_width=2.
                     )
        line2 = Line(chestnut_copy.get_center(),
                     np.array([chestnut_copy.get_x(RIGHT), chestnut_copy.get_y(ORIGIN), 0.]),
                     color=BLUE_B, stroke_width=2.)

        arc = Arc(color=BLACK)

        # number_angle = Integer(0, fill_color=BLACK).scale(.24)
        # number_angle.add_updater(lambda x: number_angle.set_value(line2.get_angle() / PI * 180))
        left_value = TexMobject('My QQ is 3515674727').add_updater(lambda t:
                                                                  t.become(
                                                                      TexMobject('%.1f^{\\circ}' %
                                                                                 (line2.get_angle() * 180 / PI),
                                                                                 fill_color=BLACK)
                                                                      .next_to(arc, UR, buff=.05).
                                                                      scale(0.5)))
        chestnut_copy.add_updater(lambda x: x.set_opacity(1 - (line2.get_angle() / PI) * 0.5))
        chestnut.add_updater(lambda x: x.set_stroke(opacity=(1. - line2.get_angle() / PI)))

        arc.add_updater(
            lambda a: a.become(Arc(color=RED_B, arc_center=[line1.get_x(LEFT), line1.get_y(), 0], radius=0.1,
                                   start_angle=0, angle=(line2.get_angle() * 180 / PI) * DEGREES,
                                   stroke_width=2.)))

        self.play(ReplacementTransform(captions_mob[12], captions_mob[13]))

        self.play(Write(arc))

        self.play(Write(line1), Write(line2))
        self.play(Write(left_value))
        SVG_all = VGroup(chestnut_copy, line2)
        self.play(
            Rotating(SVG_all, axis=OUT, radians=PI, run_time=2), rum_time=5
        )
        # self.wait(0.5)
        # self.play(
        #     Rotating(SVG_all, axis=IN, radians=PI, run_time=2)
        # )
        self.play(ReplacementTransform(captions_mob[13], captions_mob[14]))
        self.wait()

        self.play(ReplacementTransform(chestnut_copy.copy(), chestnut_4))

        self.wait()

        self.play(ReplacementTransform(captions_mob[14], captions_mob[15]))

        self.play(ReplacementTransform(captions_mob[15], captions_mob[16]))

        self.play(FadeInFromDown(choice_true_5))
        self.wait(2.5)


class Title(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": "#79797D",
        },
    }

    def construct(self):
        title = TexMobject(
            r" \ce{\Delta O2^2- + HO^2+ -> JK3^4-v}\oint_L { \mathord"
            r"{\buildrel{ \lower3pt \hbox{$ \scriptscriptstyle \rightharpoonup$}} \over E} }"
            r" \cdot { \rm{d}} \mathord{ \buildrel{"
            r" \lower3pt \hbox{$ \scriptscriptstyle \rightharpoonup$}}  \over l}  = 0 ")
        title.set_color(["#37ECD3", "#CBEC8E", "#EC7E8D", "#AE5F92", "#718BC3", "#47E27A", "#4CFADE"]).set_opacity(.7).\
            scale(2.1).set_sheen(.6).set_sheen_direction(UP)
        self.play(Write(title))
        self.play(title.scale, .5)
        self.play(title.move_to, np.array([0., 3., 0.]))
        self.play(Write(CodeLine("@_2,~0_.making", t2c={"0_.making": "#AE5F92"}).scale(2.)))

        self.wait(1.5)


class choice_6(Scene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):

        captions = [
            # step 6
            "显然， 因为MN垂直平分AB，所以∠A=∠ABN=40°",  # 0
            "又因为在△ABC中，AB=AC，∠A=40°，所以∠ABC=70°",
            "所以",
            "∠NBC=30°",
            "答案选D",
            " "

        ]
        captions_mob = self.set_caption(captions)[0]
        # #VGroup(
        # #     *[
        # #         CodeLine(cap, font='思源黑体 CN Bold', size=.5).to_edge(DOWN * 1.2)
        # #         .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
        # #         for cap in captions
        # #     ]
        #  )

        Write(captions_mob[0])

        point_A_1 = np.array([0., 1. * np.tan(70. * DEGREES) - 1., 0])
        point_B_1 = np.array([-1.,  0. - 1.,   0.])
        point_C_1 = np.array([1.,   0. - 1.,   0.])
        point_M_1 = (point_A_1 + point_B_1) / 2.
        point_N_1 = cross_lines_point(
            MTwoPointLine(point_A_1, point_C_1),
            MBisectOfVertical(MTwoPointLine(point_A_1, point_B_1)))
        line_BC = Line(point_B_1, point_C_1, color=BLUE)
        line_AB = Line(point_A_1, point_B_1, color=BLUE)
        line_AC = Line(point_A_1, point_C_1, color=BLUE)
        line_MN_before_point = Line(point_M_1, point_N_1).scale(1.5).get_end()
        line_MN = Line(point_M_1, line_MN_before_point, color=GREEN_B).set_opacity(.7)
        line_NB = Line(point_N_1, point_B_1, color="#FABB6B")
        line_LI1 = Line(point_M_1, point_M_1 + np.array([.15, 0., 0.]), color="#4CFADE", stroke_width=2.)\
            .rotate(20 * DEGREES, IN, about_point=point_M_1).set_opacity(.6)
        line_LI1.rotate(90 * DEGREES, IN, about_point=line_LI1.get_end())
        line_LI2 = line_LI1.copy().rotate(90 * DEGREES, IN, about_point=line_LI1.get_start())

        # self.add(line_LI1, line_LI2)  # try stroke_width

        Text_1A = TexMobject("A", color=BLACK).scale(0.5).next_to(point_A_1, direction=UP, buff=.1)
        Text_1B = TexMobject("B", color=BLACK).scale(0.5).next_to(point_B_1, direction=DL, buff=.1)
        Text_1C = TexMobject("C", color=BLACK).scale(0.5).next_to(point_C_1, direction=DR, buff=.1)
        Text_1N = TexMobject("N", color=BLACK).scale(0.5).next_to(point_N_1, direction=DR, buff=.1)
        Text_1M = TexMobject("M", color=BLACK).scale(0.5).next_to(point_M_1, direction=DL, buff=.1)
        point_M = Dot(point_N_1, color=BLACK, fill_opacity=0.3)

        all_word = VGroup(Text_1A, Text_1B, Text_1C, Text_1M, Text_1N)
        aline_to_point = VGroup(line_AB, line_BC, line_AC, line_MN, line_NB, point_M)
        all_LI = VGroup(line_LI1, line_LI2)
        all_line = VGroup(aline_to_point, all_LI)
        all_image = VGroup(all_line, all_word)

        title_list = [CodeLine("6.如图,在△ABC中，AB=AC，∠A=40°，MN垂直平分AB，则∠NBC的度数为~~~~~~~~~~~~~~~~~~~~~~~~(  )",
                               font='思源黑体 CN Bold'),
                      TexMobject("A\\text{. }20^{\\circ}"),
                      TexMobject("B\\text{. }30^{\\circ}"),
                      TexMobject("C\\text{. }40^{\\circ}"),
                      TexMobject("D\\text{. }70^{\\circ}"),
                      TexMobject("D")
                      ]
        title_color = ["#5D9DFA", "#81B0FA", "#B5ADFA", "#1BEDEB", "#1BEDEB"]

        triangle_1 = Polygon(point_A_1, point_M_1, point_N_1, fill_color="#83FAD3", fill_opacity=0.7, stroke_opacity=0.)
        triangle_2 = Polygon(point_B_1, point_M_1, point_N_1, fill_color="#FA7E7C", fill_opacity=0.7, stroke_opacity=0.)
        arc1 = Arc(color="#86F8DC", arc_center=point_B_1, start_angle=30 * DEGREES, angle=40 * DEGREES, stroke_angle=2.,
                   radius=.5)

        arc2 = Arc(color="#FA5E88", arc_center=point_B_1, start_angle=0. * DEGREES, angle=30 * DEGREES, stroke_angle=2.,
                   radius=.5)

        arc3 = Arc(color="#FAA894", arc_center=point_B_1, start_angle=0. * DEGREES, angle=70 * DEGREES, stroke_angle=2.,
                   radius=.7)

        number_1_angle = TexMobject("40^{\\circ}", color="#86F8DC").set_opacity(0.7).next_to(arc1, UR, buff=.1)
        number_2_angle = TexMobject("30^{\\circ}", color="#FA5E88").set_opacity(0.7).next_to(arc2, UR, buff=.1)
        number_3_angle = TexMobject("70^{\\circ}", color="#FAA894").set_opacity(0.7).next_to(arc3, UR, buff=.1)

        all_to_solve_number = VGroup(number_1_angle, number_2_angle, number_3_angle)
        all_to_solve = VGroup(triangle_1, triangle_2, arc1, arc2, arc3, all_to_solve_number)
        real_all_image = VGroup(all_image, all_to_solve)

        self.play(Write(line_AB), FadeInFromDown(line_BC), ShowCreation(line_AC))

        self.play(ShowCreation(line_MN))

        self.play(ShowCreation(all_LI), rate_func=smooth)

        self.play(Write(point_M))

        self.play(SpinInFromNothing(line_NB))

        self.play(Write(all_word))

        self.wait()
        real_all_image_copy = real_all_image.copy()
        real_all_image_copy.scale(0.5).shift(np.array([5., -2., 0.]))
        all_to_solve = real_all_image_copy[1]
        self.play_all([all_image.scale, all_image.shift], [[0.5], [np.array([5., -2., 0.])]], function=[smooth] * 2)

        title_list = self.set_text_type(title_list, title_color, [Write] * 5, choice=3)  # [Write] * 6

        self.wait(3.)

        self.play(FadeInFromDown(all_to_solve[0]))

        self.play(Write(captions_mob[0]))

        self.play(ReplacementTransform(all_to_solve[0], all_to_solve[1]))

        self.play(FadeInFromDown(all_to_solve[2]), Write(all_to_solve[5][0]), FadeOutAndShiftDown(all_to_solve[1]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.play(FadeInFromDown(all_to_solve[4]), Write(all_to_solve[5][2]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]))

        self.wait()

        self.play(all_to_solve[5][0].next_to, all_to_solve[5][2], RIGHT, .3, DOWN)

        and_to_two_number = TexMobject("-", color="#FA6117", opacity=0.7,
                                       stroke_width=1.5).next_to(all_to_solve[5][2], RIGHT, -.05).\
            scale(.5)

        self.play(FadeInFrom(and_to_two_number, ORIGIN))

        self.wait()

        all_to_Trans_VGroup = VGroup(all_to_solve[5][0], and_to_two_number, all_to_solve[5][2])

        self.play(FadeOutAndShiftDown(all_to_solve[2]), FadeOutAndShiftDown(all_to_solve[4]))
        self.play(ReplacementTransform(all_to_Trans_VGroup, all_to_solve[5][1]))
        self.play(Write(all_to_solve[3]))

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.wait()

        all_to_solve.remove(*all_to_solve[0: 3], all_to_solve[4])
        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]))

        self.wait()

        self.play(FadeInFromDown(title_list[-1]))
        print(*all_to_solve)
        self.wait()

        self.play(FadeOutAndShiftDown(all_to_solve), FadeOutAndShiftDown(title_list), FadeOut(all_image))
        self.play(ReplacementTransform(captions_mob[4], captions_mob[5]))
        self.wait()

    def play_all(self, mobject, mob_kwarg, function=None, wait_time=1., **kwargs):
        # TODO want to make list about kwarg
        assert isinstance(mobject, list), "mob must be list"
        if function in [None]:
            function = len(mobject) * [linear]
        assert self.isinstance_type(mob_kwarg)
        assert self.isinstance_type([mobject, * mob_kwarg, function]), "The kwarg must be list or tuple"
        assert self.isinstance_len([mobject, mob_kwarg, function]), "The length of the three must be equal"

        for mobject_kwarg, mob_kwarg_kwarg, function_kwarg in zip(mobject, mob_kwarg, function):
            self.play(mobject_kwarg, *mob_kwarg_kwarg, rate_func=function_kwarg, **kwargs)
            self.wait(wait_time)

    @staticmethod
    def isinstance_type(all_list):
        """all_list must have lists"""
        assert not isinstance(all_list, tuple), "all_list must be list, not tuple"
        assert isinstance(all_list, list), "all_list must be list"
        for to_isinstance in all_list:
            for x in [tuple, list]:
                if isinstance(to_isinstance, x):
                    break
            else:
                return False
        return True

    def isinstance_len(self, all_list):
        """all_list must have lists"""
        assert self.isinstance_type(all_list), "The kwarg must be list or tuple"
        for sale in all_list:
            assert self.isinstance_type([sale]), "The %s is not list" % sale
        list_for_sale = [len(kwarg) for kwarg in all_list]
        if max(list_for_sale) == min(list_for_sale):
            return True
        else:
            return False

    def set_text_type(self, text_list, text_color=None, animation_list=None, choice=0):
        all_list_for_check = [text_list]

        if text_color not in [None]:
            assert isinstance(text_color, list), "text_color must be list"
            all_list_for_check.append(text_color + [True])

        if animation_list not in [None]:
            assert isinstance(animation_list, list), "animation_list must be list"
        else:
            animation_list = [Write] * 5
        all_list_for_check.append(animation_list + [Write])
        assert self.isinstance_type(all_list_for_check), "The kwarg must be list or tuple"
        assert self.isinstance_len(all_list_for_check), "this three of all_list_for_check must be equal"
        assert isinstance(text_list[0], Mobject), "hey, you can't use only a list to waste time"

        # I think I don't need to check color
        if text_color not in [None]:
            for x, y in zip(text_color, range(len(text_color))):
                text_list[y + 1].set_color(x)

        if choice == 0:
            text_list[0].shift(UP)
            text_list[1].shift(DL + LEFT * 3.5).scale(.5)
            text_list[2].shift(DL + LEFT * .5).scale(.5)
            text_list[3].shift(DR + RIGHT * .5).scale(.5)
            text_list[4].shift(DR + RIGHT * 3.5).scale(.5)
            text_list[5].next_to(text_list[0][-1], RIGHT, buff=-.43).scale(0.5)

        elif choice == 1:
            text_list[0].shift(UP)
            text_list[1].shift(DL + LEFT * 3.5).scale(.5)
            text_list[2].shift(DR + RIGHT * 2.).scale(.5)
            text_list[3].shift(DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
            text_list[4].shift(DR + RIGHT * 2. + DOWN * 1.5).scale(.5)
            text_list[5].next_to(text_list[0][-1], RIGHT, buff=-.43).scale(.5)

        elif choice == 2:
            text_list[0].shift(UP)
            text_list[0].shift(DL + LEFT * 3.5).scale(.5)
            text_list[0].shift(DR + RIGHT * 2.).scale(.5)
            text_list[0].shift(DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
            text_list[0].shift(DR + RIGHT * 2. + DOWN * 1.5).scale(.5)
            text_list[0].next_to(text_list[0][-1], RIGHT, buff=-.43).scale(.5)

        elif choice == 3:
            text_list[0].shift(UP)
            text_list[1].shift(DL + LEFT * 3.5).scale(.5)
            text_list[2].shift(DL + LEFT * -1.).scale(.5)
            text_list[3].shift(DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
            text_list[4].shift(DL + LEFT * -1. + DOWN * 1.5).scale(.5)
            text_list[5].next_to(text_list[0][-1], RIGHT, buff=-.43, aligned_edge=DOWN).scale(.5).shift(DOWN * .07)

        elif choice == 4:
            text_list[0].shift(UP)
            text_list[1].scale(.5).move_to(np.array([4.5, -1., 0.])).shift(LEFT * 10.)
            text_list[2].scale(.5).move_to(np.array([4.5, -1., 0.])).shift(LEFT * 8.)
            text_list[3].scale(.5).move_to(np.array([4.5, -1., 0.])).shift(LEFT * 6.)
            text_list[4].scale(.5).move_to(np.array([4.5, -1., 0.])).shift(LEFT * 4.)
            text_list[5].scale(.5).next_to(text_list[0][-1], RIGHT, buff=-.43).scale(.5)

            choise1 = TexMobject("A").set_color(text_list[1].get_color()).next_to(text_list[1], DOWN, buff=.25)\
                .scale(.5)

            choise2 = TexMobject("B").set_color(text_list[2].get_color()).next_to(text_list[2], DOWN, buff=.25)\
                .scale(.5)

            choise3 = TexMobject("C").set_color(text_list[3].get_color()).next_to(text_list[3], DOWN, buff=.25)\
                .scale(.5)

            choise4 = TexMobject("D").set_color(text_list[4].get_color()).next_to(text_list[4], DOWN, buff=.25)\
                .scale(.5)

            all_word = VGroup(choise1, choise2, choise3, choise4)
            text_list.insert(5, all_word)
            animation_list.insert(5, Write)

        self.play(*[
                animation_list[x](text_list[x])
                for x in range(len(text_list) - 1)
            ])
        all_choice = VGroup(* text_list)
        return all_choice

    def set_caption(self, captions, captions_tex_input=None, captions_font='思源黑体 CN Bold'):
        assert self.isinstance_type([captions])
        captions = captions
        captions_tex = captions_tex_input

        captions_mob = VGroup(
            *[
                CodeLine(cap, font=captions_font, size=.5).to_edge(DOWN * 1.2)
                .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in captions
            ]
        )
        if captions_tex not in [None]:
            assert self.isinstance_type([captions_tex])
            captions_tex_mob = VGroup(
                *[
                    TexMobject(cap).scale(.5).set_color(BLACK).to_edge(DOWN * 1.2)
                    .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                    for cap in captions_tex
                ]
            )
            return [captions_mob, captions_tex_mob]
        return [captions_mob]


class choice_7(choice_6):
    def construct(self):
        title_list = [CodeLine("7.化简~~~~~~~~的结果是~~~~~~~~~~~~~~~~~~~~~~~~(  )",
                               font='思源黑体 CN Bold'),
                      TexMobject("A\\text{.}\\frac{m}{m+3}"),
                      TexMobject("B\\text{.}{-}\\frac{m}{m+3}"),
                      TexMobject("C\\text{.}\\frac{m}{m-3}"),
                      TexMobject("D\\text{.}\\frac{m}{3-m}"),
                      TexMobject("B")
                      ]
        title_color = ["7AFAEE", "#57FAAF", "#ECBDFA", "#60FAB9", "#60FAB9"]
        title_another = TexMobject("{m", "^", "2", "-", "3", "m",
                                   "}", "\\over{", "9", "-", "m",
                                   "^", "2}", ".", color="#60FAB9").scale(.5)

        title_list = self.set_text_type(title_list, title_color, choice=3)
        title_another.next_to(title_list[0][3], buff=.1)

        self.play(FadeInFromDown(title_another))

        self.wait(3.)

        title_to_solve_an = title_another.copy().move_to(np.array([4., -2., 0.])).scale(1.5)
        title_to_solve_an2 = TexMobject("{m", "(", "m", "-",
                                        "3", ")", "\\over", "(",
                                        "3", "-", "m", ")",
                                        "(", "3", "+", "m", ")}", ".", color="#60FAB9")\
            .next_to(title_to_solve_an, ORIGIN, buff=0.).scale(.75)

        title_to_solve_an3 = TexMobject("{-}", "{m", "(", "3", "-", "m",
                                        ")", "\\over", "(3", "-", "m",
                                        ")", "(", "3", "+", "m", ")}", ".", color="#60FAB9") \
            .next_to(title_to_solve_an, ORIGIN, buff=0.).scale(.75)

        title_to_solve_an4 = TexMobject("{-}", "{{m}", "\\over", "{3", "+", "m}}", ".", color="#60FAB9") \
            .next_to(title_to_solve_an, ORIGIN, buff=0.).scale(.75)

        self.play(ReplacementTransform(title_another.copy(), title_to_solve_an))

        self.wait()

        self.play(ReplacementTransform(title_to_solve_an[8: 14], title_to_solve_an2[6: 17]))

        self.wait()

        self.play(ReplacementTransform(title_to_solve_an[0: 7], title_to_solve_an2[0: 6]))

        self.wait()

        self.play(ReplacementTransform(title_to_solve_an2[3].copy(), title_to_solve_an3[0].shift(LEFT * .17)))

        self.play(ReplacementTransform(title_to_solve_an2, title_to_solve_an3[1:-1]))

        self.play(title_to_solve_an3[0].shift, RIGHT * .17, rum_time=2.)

        self.wait(2.)

        self.play(ReplacementTransform(title_to_solve_an3[0: -1], title_to_solve_an4[0: -1]))

        self.wait()

        self.play(Transform(title_to_solve_an4[1: -1],
                            (TexMobject("-", "{m}", "\\over", "{m", "+", "3}", color="#60FAB9")
                            .next_to(title_to_solve_an, ORIGIN, buff=0.).scale(.75))[1:].shift(RIGHT * .23)))

        title_to_solve_an4.remove(title_to_solve_an4[6])

        self.play(ReplacementTransform(title_to_solve_an4, title_list[2]))

        self.play(FadeInFromDown(title_list[-1]))

        self.wait()

        self.play(FadeOutAndShiftDown(title_list), FadeOut(title_another))

        self.wait(2.)


class choice_8(choice_7):
    def construct(self):
        captions = [
            "显然,绿色这个区域符合题意",
            "解集看x",
            "函数旁边的解析式被挡住看不清了吗?",
            "好吧···^_-",
            "现在看清了吗",
            "故选C",
            ""
        ]
        captions_tex = [
            "x+b>kx+4,\\text{即: }y_{2}>y_{1}",
            "y_{1}=x+b",
            "y_{2}=kx+4",
            "\\text{为可视化}y_{2}>y_{1},\\text{我们需要一个区域使得}x+b>kx+4",
            "\\text{显然，绿色这一部分的满足:}x>1"
        ]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]

        title_list = [CodeLine("8.如图，一次函数~~~~~~~~~与~~~~~~~~~~的图像相交于点P(1,3),"
                               "\n  则关于x的不等式x+b>kx+b的解集是~~~~~~~~~~~(  )", font='思源黑体 CN Bold'),  # ~~~~~~~~~~~~~
                      TexMobject("A\\text{.}\\frac{m}{m+3}"),
                      TexMobject("B\\text{.}{-}\\frac{m}{m+3}"),
                      TexMobject("C\\text{.}\\frac{m}{m-3}"),
                      TexMobject("D\\text{.}\\frac{m}{3-m}"),
                      TexMobject("C")
                      ]
        title_color = ["#7AFAEE", "#57FAAF", "#ECBDFA", "#60FAB9", "#ECBDFA"]

        title_list = self.set_text_type(title_list, title_color, choice=3)

        function_y_1_title = TexMobject("y_1=x+b", color="#67FAB7")\
            .scale(0.5).next_to(title_list[0][8], buff=.09, aligned_edge=DOWN)
        function_y_2_title = TexMobject("y_2=kx+4", color="#FAE160")\
            .scale(0.5).next_to(title_list[0][18], buff=.09, aligned_edge=DOWN)

        title_v_group = VGroup(title_list[0], function_y_1_title, function_y_2_title)

        self.play(FadeInFromDown(function_y_1_title), FadeInFromDown(function_y_2_title))

        self.play(title_v_group.shift, UP, rate_function=smooth, run_time=.5)
        axes_image = Axes(x_max=4.7, x_min=-3.2, y_max=6.7, y_min=-1.2, axis_config={
                          "color": "#000000",
                          "number_scale_val": 1.
                          },
                          ).add_coordinates(number_config={"color": "#FFFFFF"})
        function_y_1 = FunctionGraph(
            lambda x: x + 2,
            x_min=-2.7, x_max=4.19, color="#69FAA8")
        function_y_2 = FunctionGraph(
            lambda x: -x + 4,
            x_min=-3., x_max=4.6, color="#61EBFA")
        point_1_special = function_y_1.get_point_from_function(x=4.)
        point_2_special = function_y_2.get_point_from_function(x=4.)
        function_y_1_label = TexMobject("y_1=x+b", color="#67FAB7").next_to(np.array(point_1_special), DL)
        function_y_2_label = TexMobject("y_2=kx+4", color="#61EBFA").next_to(np.array(point_2_special), UR)

        func_line1 = Line(np.array([1., 0., 0.]), np.array([1., 3., 0.]), color="#FFE994")
        func_line2 = Line(np.array([0., 3., 0.]), np.array([1., 3., 0.]), color="#C5B22D", stroke_opacity=.3450)
        to_fill_polygon = Polygon(np.array([1., 3., 0.]),
                                  np.array([12., 14., 0.]),   np.array([12., -8., 0.]),
                                  color="#98FF88", fill_opacity=.7, stroke_opacity=0.)
        x1_y3 = np.array([1., 3., 0.])
        dot_x1_y3 = Dot(x1_y3, color="#B3F7FF", fill_opacity=.7, radius=.2)

        all_image_tra = VGroup(axes_image, function_y_1, function_y_2,  func_line1, func_line2, dot_x1_y3,
                               function_y_2_label, function_y_1_label, to_fill_polygon).move_to([5.5, -1., 0.])\
            .scale(.5)

        self.play(Write(all_image_tra[0:6]))
        # self.play(ReplacementTransform(function_y_1_title, function_y_1_label),
        #           ReplacementTransform(function_y_2_title, function_y_2_label))
        self.play(
            *[ReplacementTransform(*x)
              for x in [(function_y_1_title.copy(), function_y_1_label),
                        (function_y_2_title.copy(), function_y_2_label)]
              ],
        )
        self.wait(2)

        self.play(GrowFromCenter(captions_tex_mob[0]))

        captions_tex_mob[1][1].set_color(function_y_1.get_color())
        captions_tex_mob[2][1].set_color(function_y_2.get_color())

        self.play()

        self.play(ReplacementTransform(captions_tex_mob[0], captions_tex_mob[1]
                                       .add_background_rectangle(
            color=function_y_2.get_color(), buff=0.1, opacity=0.85)))

        self.play(Flash(function_y_1_label, color=function_y_2_label.get_color(),
                        flash_radius=function_y_1_label.get_width(),
                        line_length=.35),

                  Indicate(function_y_1, scale_factor=2., color=function_y_2_label.get_color())
                  )

        self.wait()

        self.play(ReplacementTransform(captions_tex_mob[1], captions_tex_mob[2]
                                       .add_background_rectangle(
            color=function_y_1.get_color(), buff=0.1, opacity=0.85)))

        self.play(
                 Flash(function_y_2_label, color=function_y_1_label.get_color(),
                       flash_radius=function_y_2_label.get_width(),
                       line_length=.35),

                 Indicate(function_y_2, scale_factor=2., color=function_y_1_label.get_color())
        )
        self.wait()

        self.play(ReplacementTransform(captions_tex_mob[2], captions_tex_mob[3]))

        self.wait()

        self.play(ReplacementTransform(captions_tex_mob[3], captions_mob[0]))

        self.wait()

        self.play(SpinInFromNothing(all_image_tra[-1]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]))

        self.wait(.5)

        def ce():
            self.play(
                Flash(function_y_1_label, color=function_y_2.get_color(),
                      flash_radius=function_y_1_label.get_width(),
                      line_length=.35),
                Flash(function_y_2_label, color=function_y_1.get_color(),
                      flash_radius=function_y_2_label.get_width(),
                      line_length=.35))

        ce()

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.wait()

        self.add(function_y_1_label, function_y_2_label)

        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]))

        ce()

        self.wait(2.5)

        self.play(ReplacementTransform(captions_mob[4], captions_tex_mob[4]))

        self.wait()

        self.play(ReplacementTransform(captions_tex_mob[4], captions_mob[-2]))

        self.next_to_last_title(title_list, aligned_edge=ORIGIN)
        self.play(FadeInFromDown(title_list[-1]))

        self.wait()

        self.play(FadeOut(title_list), FadeOut(function_y_1_title), FadeOutAndShift(function_y_2_title, DOWN))

        self.wait()

        self.play(VFadeOut(all_image_tra))

        self.wait()

        self.play(Transform(captions_mob[-2], captions_mob[-1]))

        self.wait()

    @staticmethod  # TODO give next_to_last_title some functions and delete the func' 's static
    def next_to_last_title(title_list, is_choice=True, scale_to_mob=None, *mob, **kwargs):
        assert isinstance(title_list, VGroup), 'title_list must be VGroup, not %s' % str(type(title_list))
        if is_choice:
            title_list[-1].scale(2.).next_to(title_list[0][-1], RIGHT, buff=-.43, **kwargs)
            title_list[-1].scale(.5)
        else:
            title_list[-1].scale(scale_to_mob).next_to(*mob, **kwargs)
            title_list[-1].scale(1 / scale_to_mob)


class choice_9(choice_8):
    def construct(self):
        captions = [
            "显然,大家可以看出△ACD (于是AC)",
            "全等于△AEC (等于AE)",
            "全等于△BEC (AC等于BE)",
            "而BE...",
            "^P^@#%$z8z7*",
            "故选B",
            "因此啊"
        ]
        captions_tex = [
            "\\text{显然,}\\underset{\\text{不要管“$\\sin$”,其实30度角就能看出来 "  # 1
            "BD=2DE(就是懒得写代码)}}{DE=BD\\sin(\\angle B)=2\\times\\frac{1}{2}=1}",
            "BE=BD\\cos(\\angle B)=\\frac{\\sqrt{3}}{2} \\times 2 = "  # 2
            "\\sqrt{3}"
        ]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]

        title_list = [CodeLine("9.如图,△ABC中,∠C=90°,∠B=30°,点D\n  是BC上一点,AD平分∠CAB,过D作DE⊥AB,\n  "
                               "垂足为点E,若BD=2,则AC的长是~~~~~~~~~~~(  )", font='思源黑体 CN Bold'),
                      TexMobject("A\\text{.}3"),
                      TexMobject("B\\text{.}\\sqrt{3} "),
                      TexMobject("C\\text{.}2"),
                      TexMobject("D\\text{.}1"),
                      TexMobject("B")
                      ]
        title_color = ["#AEADFD", "#9683AE", "#71B5BC", "#60FAB9", "#9683AE"]

        title_list = self.set_text_type(title_list, title_color, choice=3)

        point_A = np.array([-np.sqrt(3.), 0., 0.])
        point_B = np.array([np.sqrt(3.), 0., 0.])
        point_C = np.array([-.5 * np.sqrt(3.), 1.5, 0])

        geometry_triangle = MTriangle(point_A, point_B, point_C)

        point_E = geometry_triangle.bisect_vertical_points[2]

        point_D = cross_lines_point(MTwoPointStraightLine(point_B, point_C),
                                    MBisectOfVertical(MTwoPointStraightLine(point_A, point_B)))

        line_AC = Line(point_A, point_C, color="#58C4DD")
        line_AB = Line(point_A, point_B, color="#49BCFF")
        line_BC = Line(point_B, point_C, color="#63E2FF")
        line_DE = Line(point_D, point_E, color="#28468B", stroke_opacity=.75)
        line_DA = Line(point_A, point_D, color="#C27D41", stroke_opacity=.75)
        line_set = VGroup(line_AC, line_AB, line_BC, line_DE, line_DA)

        point_A_dot = Dot(point_A, color="#FF1E53", fill_opacity=.7)
        point_B_dot = Dot(point_B, color="#54CBD0", fill_opacity=.7)
        point_C_dot = Dot(point_C, color="#3131D0", fill_opacity=.7)
        point_D_dot = Dot(point_D, color="#CA2AD0", fill_opacity=.7)
        point_E_dot = Dot(point_E, color="#D05190", fill_opacity=.7)
        point_dot_set = VGroup(point_A_dot, point_B_dot, point_C_dot, point_D_dot, point_E_dot)

        point_A_tex = TexMobject("A", color="#FF1E53", fill_opacity=.7).next_to(point_A, DL, buff=.1).scale(.67)
        point_B_tex = TexMobject("B", color="#54CBD0", fill_opacity=.7).next_to(point_B, DOWN, buff=.1).scale(.67)
        point_C_tex = TexMobject("C", color="#3131D0", fill_opacity=.7).next_to(point_C, UP, buff=.1).scale(.67)
        point_D_tex = TexMobject("D", color="#CA2AD0", fill_opacity=.7).next_to(point_D, UR, buff=.07).scale(.67)
        point_E_tex = TexMobject("E", color="#D05190", fill_opacity=.7).next_to(point_E, DOWN, buff=.1).scale(.67)
        point_tex_set = VGroup(point_A_tex, point_B_tex, point_C_tex, point_D_tex, point_E_tex)

        triangle_ADE = Polygon(point_A, point_D, point_E, color="#FF4E8C", fill_opacity=.7, stroke_opacity=0.)
        triangle_BED = Polygon(point_B, point_E, point_D, color="#7FFFD2", fill_opacity=.7, stroke_opacity=0.)
        triangle_ACD = Polygon(point_A, point_D, point_C, color="#BC38BA", fill_opacity=.7, stroke_opacity=0.)

        all_fill_triangle = VGroup(triangle_ACD, triangle_ADE, triangle_BED)

        ninety_angle_sign_11 = Line(point_C, np.array([-.5 * np.sqrt(3) + .1, 1.5 - np.sqrt(3) / 3. * .1, 0.]),
                                    color="#F7A1A2", stroke_opacity=.5).\
            rotate(90 * DEGREES, OUT,
                   about_point=np.array([-.5 * np.sqrt(3) + .1, 1.5 - np.sqrt(3) / 3. * .1, 0.]))

        ninety_angle_sign_12 = ninety_angle_sign_11.copy().\
            rotate(90 * DEGREES, OUT,
                   about_point=ninety_angle_sign_11.get_start())

        ninety_angle_sign_21 = Line(point_E, point_E + UP * .2 / np.sqrt(3), color="#F7A1A2", stroke_opacity=.5).\
            rotate(PI / 2, IN, about_point=point_E + UP * .2 / np.sqrt(3))
        ninety_angle_sign_22 = ninety_angle_sign_21.copy().\
            rotate(PI / 2, IN,
                   about_point=ninety_angle_sign_21.get_start())

        ninety_angle_sign_31 = ninety_angle_sign_21.copy().flip(about_point=np.array([0., 0., 0.]), axis=UP)
        ninety_angle_sign_32 = ninety_angle_sign_22.copy().flip(about_point=ORIGIN, axis=UP)

        sign_angle_30_DEGREES = Arc(arc_center=point_B, angle=PI / 6., start_angle=150 * DEGREES, stroke_angle=2.,
                                    radius=.7, color="#F7A1A2")
        sign_angle30 = TexMobject("30^{\\circ}", color="#F7A1A2", fill_opacity=.7).\
            next_to(sign_angle_30_DEGREES, UL, buff=.07).\
            scale(.67)

        sign_angle_group_v = VGroup(sign_angle_30_DEGREES, sign_angle30)

        sign_90time1 = VGroup(ninety_angle_sign_11, ninety_angle_sign_12)
        sign_90time2 = VGroup(ninety_angle_sign_21, ninety_angle_sign_22)
        sign_90time3 = VGroup(ninety_angle_sign_31, ninety_angle_sign_32)
        sign_90time = VGroup(sign_90time1, sign_90time2, sign_90time3, sign_angle_group_v)

        all_image = VGroup(line_set, point_dot_set, point_tex_set, all_fill_triangle, sign_90time)

        all_image.move_to(np.array([3.6, -1.5, 0.]))

        self.play(Write(point_dot_set))

        self.play(
            *[FadeInFromPoint(Mobject_the_VGroup, point_that_dot)
              for Mobject_the_VGroup, point_that_dot in zip(line_set,
                                                            [point_that_dot.get_center()
                                                             for point_that_dot in point_dot_set])]
        )
        self.play(
            *[FadeInFromPoint(tex_to_point, point_that_dot)
              for tex_to_point, point_that_dot in zip(point_tex_set,
                                                      [point_that_dot.get_center()
                                                       for point_that_dot in point_dot_set])]
        )

        self.play(Write(captions_mob[0]))
        self.play(FadeInFromDown(triangle_ACD))

        as_a_label_tex_AC = TexMobject("AC", color="#61EBFA", fill_opacity=.7).\
            scale(.67).move_to(line_AC.copy().shift(UP * .45).get_center())

        self.play(Write(as_a_label_tex_AC))
        self.play(SpinInFromNothing(sign_90time1))
        captions_mob[1][0].set_color(triangle_BED.get_color())
        captions_mob[2][0].set_color(triangle_ADE.get_color())

        captions_mob[2][1:].set_color(triangle_BED.get_color())
        captions_mob[1][1:].set_color(triangle_ADE.get_color())

        self.play(ReplacementTransform(triangle_ACD, triangle_ADE),
                  ReplacementTransform(captions_mob[0], captions_mob[1]),
                  ApplyMethod(as_a_label_tex_AC.move_to, Line(point_A_dot.get_center(), point_E_dot.get_center())
                              .shift(DOWN * .45).get_center()),
                  ReplacementTransform(sign_90time1, sign_90time2))

        captions_tex_mob[1][-1][-3:].set_color("#9683AE")

        self.wait()

        self.play(ReplacementTransform(triangle_ADE, triangle_BED),
                  ReplacementTransform(captions_mob[1], captions_mob[2]),
                  ApplyMethod(as_a_label_tex_AC.move_to, Line(point_B_dot.get_center(), point_E_dot.get_center())
                              .shift(DOWN * .45).get_center()),
                  ReplacementTransform(sign_90time2, sign_90time3))

        self.wait(.7)

        self.play(FadeOutAndShift(triangle_BED, LEFT))

        self.play(Flash(sign_90time3, color=line_BC.get_color()))

        self.play(FadeToColor(sign_90time3, "#FFFFFF"))

        self.remove(sign_90time3)

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.wait(.5)

        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]))

        self.play(ShowCreation(sign_angle_group_v))

        self.play(ReplacementTransform(captions_mob[4], captions_tex_mob[0]))

        self.play(Flash(sign_angle30, color=point_B_dot.get_color(), flash_radius=sign_angle30.get_width()))

        self.wait(2)

        self.play(ReplacementTransform(captions_tex_mob[0], captions_tex_mob[1]))

        self.play(FadeOutAndShiftDown(sign_angle_group_v))

        all_image.remove(sign_90time)
        all_image.remove(all_fill_triangle)
        self.wait(2)

        all_image.add(as_a_label_tex_AC)

        as_a_label_tex_AC_to_copy = as_a_label_tex_AC.copy()

        self.play(ApplyMethod(as_a_label_tex_AC.set_color, "#9683AE"),
                  ReplacementTransform(captions_tex_mob[1][-1][-3:].copy(), as_a_label_tex_AC_to_copy
                                       .set_color("#9683AE")))

        self.remove(as_a_label_tex_AC_to_copy)

        self.wait()

        self.play(ReplacementTransform(as_a_label_tex_AC.copy(), title_list[-1]),
                  ReplacementTransform(captions_tex_mob[1][-1][-3:].copy(), title_list[-1]),
                  ReplacementTransform(title_list[2].copy(), title_list[-1]))

        self.wait()

        self.play(ReplacementTransform(captions_tex_mob[1], captions_mob[5]))

        self.play(*[to_draw.UnGrowRandom(mobject)
                    for mobject in title_list],
                  VFadeOut(all_image))

        self.play(ReplacementTransform(captions_mob[5], captions_mob[6]))

        self.wait()


class choice_10(choice_9):
    def construct(self):
        captions = [
            "因此啊",  # return 伏笔
            "最后一题直接看图",
            "先画出它们的图像",
            "显然,",
            "这是最后的答案吗?",
            "不,这只是x_min的值,我们求的是y_max的值",
            "故选C"

        ]
        captions_tex = [
            "f(x) = \\min{2x-1, -x+3}\\text{中$x_{\\min}$满足}2x_{\\min}-1=3x_{\\min}+3",
            "\\text{即:}",
            "x_{\\min}=\\frac{4}{3}",
            "y_{\\max}=\\underset{(y_{2_{\\max}})}{2 \\times x_{\\min} - 1}=\\underset{(y_{2_{\\max}})}{-x_{\\min} + 3}"
            "=\\frac{5}{3}"
        ]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]

        self.add(captions_mob[0])

        self.wait()
        title_list = [CodeLine("10.对于实数a,b,定义符号min{a,b},其意义为:当a≥b时,min{a,b}=b,当a<b时,\n  min{a,b}=a,例如:min{2,1}=-1,"
                               " 若关于的函数y=min{2x-1,-x+3},则该函数\n  的最大值是~~~~~~~~~~~(  )", font='思源黑体 CN Bold'),
                      TexMobject("A\\text{.}1"),
                      TexMobject("B\\text{.}\\frac{3}{4}"),
                      TexMobject("C\\text{.}\\frac{3}{5}"),
                      TexMobject("D\\text{.}2"),
                      TexMobject("C")
                      ]
        title_color = ["#58C4DD", "#29ABCA", "#ACE2EE", "#D68644", "#ACE2EE"]

        title_list = self.set_text_type(title_list, title_color, [to_draw.WriteRandom] * 5, choice=3)

        axes_image = Axes(x_max=4.7, x_min=-4.2, y_max=6.7, y_min=-3.2, axis_config={
            "color": "#000000",
            "number_scale_val": 1.
        },
                          ).add_coordinates(number_config={"color": "#C59978"})

        function_y_1 = FunctionGraph(
            lambda x: 2. * x - 1,
            x_min=-1.37, x_max=4.19, color="#83CBC3")
        function_y_2 = FunctionGraph(
            lambda x: -x + 3,
            x_min=-3., x_max=3.21, color="#D5648C")

        function_y_3 = FunctionGraph(
            lambda x: min(2 * x - 1, -x + 3),
            x_min=-1.2, x_max=3.12, color="#3B3FC3")

        point_1_special = function_y_1.get_point_from_function(x=-.7)
        point_2_special = function_y_2.get_point_from_function(x=-3.)
        point_3_special = function_y_2.get_point_from_function(x=1.)
        function_y_1_label = TexMobject("y_1=2x-1", color="#D5648C").next_to(np.array(point_1_special), DL)
        function_y_2_label = TexMobject("y_2=-x+3", color="#83CBC3").next_to(np.array(point_2_special), DOWN)
        function_y_3_label = TexMobject("y_3=\\min\\{2x - 1, -x + 3\\}", color="#3B3FC3").next_to(
            np.array(point_3_special), UR)
        dot_1 = Dot(np.array([4 / 3, 5 / 3, 0.]), color="#4A90B8", fill_opacity=.7)
        dot_2 = Dot(np.array([4 / 3, 0., 0.]), color="#904881", fill_opcaity=.7)
        dot_3 = Dot(np.array([0., 5 / 3, 0.]), color="#6DB3B3", fill_opcaity=.7)
        line_1 = Line(np.array([4 / 3, 0., 0.]), dot_1.get_center(), color="#6DB3B3", stroke_opcaity=.7)
        line_2 = Line(np.array([0., 5 / 3, 0.]), dot_1.get_center(), color="#904881", stroke_opcaity=.7)

        label_under_dot2 = TexMobject("x_{\\min}", color="#C5648C").scale(.7).next_to(dot_2, DOWN, buff=.1)
        label_under_dot3 = TexMobject("y_{\\max}", color="#3C8EC5").scale(.7).next_to(dot_3, LEFT, buff=.1)

        function_Group = VGroup(axes_image, function_y_1, function_y_1_label, function_y_2, function_y_2_label,
                                function_y_3, function_y_3_label, dot_1, dot_2, dot_3, line_1, line_2,
                                label_under_dot2, label_under_dot3).scale(.7).shift(2 * DOWN)

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.wait()

        self.play(
            *[
             to_draw.FadeOutFromRandom(title_list_x, anim_type=FadeOutAndShift, kwarg={"direction": UP})
             for title_list_x in title_list[:5]],
            run_time=3.
        )

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]))

        self.play(to_draw.WriteRandom(function_Group[:5]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[3], captions_tex_mob[0]))

        self.wait(4.)

        self.play(ReplacementTransform(captions_tex_mob[0], captions_tex_mob[1]))

        self.wait(1.3)

        self.play(ReplacementTransform(captions_tex_mob[1], captions_tex_mob[2]))

        self.wait(2.7)

        self.play(ReplacementTransform(captions_tex_mob[2], captions_mob[4]))

        self.wait(2.8)

        self.play(ReplacementTransform(captions_mob[4], captions_mob[5]),
                  FadeIn(dot_1), FadeInFromPoint(line_1, dot_1.get_center()),
                  FadeInFromPoint(line_2, dot_1.get_center()))

        self.play(ApplyMethod(function_Group[:5].set_opacity, .3), ShowCreation(function_y_3, rate_func=smooth),
                  FadeInFrom(function_y_3_label, UP), FadeInFromPoint(dot_3, dot_2.get_center()),
                  FadeInFromPoint(dot_2, dot_3.get_center()),
                  Write(label_under_dot2), ShowCreation(label_under_dot3), run_time=2.
                  )

        self.wait()

        self.play(Flash(label_under_dot2,
                        color=label_under_dot3.get_color(), flash_radius=label_under_dot2.get_width(), num_lines=20),
                  Flash(label_under_dot3,
                        color=label_under_dot2.get_color(), flash_radius=label_under_dot3.get_width(), num_lines=20))

        self.wait()

        self.play(ReplacementTransform(captions_mob[5], captions_tex_mob[3]))

        self.play(Flash(label_under_dot3, color="#7E75C5", flash_radius=label_under_dot3.get_width()))

        self.wait(5.)

        self.play(ReplacementTransform(captions_tex_mob[3], captions_mob[6]))

        self.wait()

        self.play(ReplacementTransform(function_Group, title_list[:5]))

        self.wait()

        self.play(Write(title_list[-1]))

        self.wait()

        self.play(*[to_draw.UnWriteRandom(func_list)
                    for func_list in title_list],
                  to_draw.UnGrowRandom(captions_mob[-1]))

        self.wait()


class fill_1(choice_10):
    def construct(self):
        captions = [
            "分式分母不为零,",
            "于是"
        ]
        captions_tex = ["x \\ne 3"]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]

        title_list = [CodeLine("11.当_____时,分式~~~~~~有意义", font='思源黑体 CN Bold'),
                      TexMobject("\\ne 3")]

        title_list = self.set_text_type_fill(title_list, 3, 9, ["#FABBA2"], [to_draw.WriteRandom], choice=0)

        tex_that = TexMobject("{1", "\\over", "3", "-", "x}", color="#3FDCFF").scale(.6).\
            next_to(title_list[0][12], RIGHT, buff=.12)

        self.play(Write(tex_that))

        tex_that_2 = tex_that.copy().shift(3. * DOWN).scale(5 / 3)

        tex_that_3 = TexMobject("{1", "\\over", "3", "-", "x", "\\ne", "0}", color="#3FDCFF")\
            .move_to(tex_that_2, ORIGIN)

        tex_that_4 = TexMobject("3", "-", "x", "\\ne", "0", color="#3FDCFF")\
            .move_to(tex_that_3[2: 5], ORIGIN)

        tex_that_5 = TexMobject("x", "\\ne", "3", color="#3FDCFF")\
            .move_to(tex_that_4[2: 5], ORIGIN)

        self.add(captions_mob[0][0])

        tex_that_3[-2].set_color("#FE3443")
        tex_that_3[-1].set_color("#23B552")
        tex_that_4[-2].set_color("#FE3443")
        tex_that_4[0].set_color("#23B552")
        tex_that_5[-2].set_color("#FE3443")
        tex_that_5[-1].set_color("#23B552")

        self.play(to_draw.Write(captions_mob[0][1:]))

        self.wait()

        self.play(ReplacementTransform(tex_that.copy(), tex_that_2))

        self.wait()

        self.play(ReplacementTransform(tex_that_2[:2], tex_that_3[:2]),
                  ReplacementTransform(tex_that_2[2: 5], tex_that_3[2: 5]))

        self.play(Write(tex_that_3[5:]))

        self.play(FadeOutAndShift(tex_that_3[:2], UP))

        self.wait()

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.wait()

        self.play(ReplacementTransform(tex_that_3[2: 7], tex_that_4))

        self.wait()

        self.play(ReplacementTransform(tex_that_4[2], tex_that_5[0]),
                  FadeOutAndShiftDown(tex_that_4[-1]), FadeOutAndShift(tex_that_4[1], UP),
                  ReplacementTransform(tex_that_4[0], tex_that_5[2]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[1], captions_tex_mob[0]))

        self.play(FadeInFromDown(title_list[1]))

        self.play(FadeOutAndShiftDown(tex_that_4[3]), run_time=.25)

        self.play(FadeOutAndShiftDown(tex_that_5[0]), run_time=.25)
        self.play(FadeOutAndShiftDown(tex_that_5[2]), run_time=.25)

        self.wait()

        self.play(
            *[
                to_draw.UnWriteRandom(text_mobject)
                for text_mobject in title_list
            ],
            to_draw.UnWriteRandom(captions_tex_mob[0][1:]),
            to_draw.UnWrite(tex_that)
        )

        self.remove(captions_tex_mob[0][0])

        self.wait()

    def set_text_type_fill(self, text_list, start, end, text_color=None, animation_list=None, choice=0, ifanima=True):
        all_list_for_check = [text_list]

        if text_color not in [None]:
            assert isinstance(text_color, list), "text_color must be list"
            all_list_for_check.append(text_color + [True])

        if animation_list not in [None]:
            assert isinstance(animation_list, list), "animation_list must be list"
            animation_list += [True]
        else:
            animation_list = [Write] * 2
        all_list_for_check.append(animation_list)
        assert self.isinstance_type(all_list_for_check), "The kwarg must be list or tuple"
        assert self.isinstance_len(all_list_for_check), "this three of all_list_for_check must be equal"
        assert isinstance(text_list[0], Mobject), "hey, you can't use only a list to waste time"

        """I think I don't need to check color"""
        if text_color not in [None]:
            for x, y in zip(text_color, range(len(text_color))):
                text_list[y + 1].set_color(x)

        if choice == 0:
            text_list[0].shift(UP)
            text_list[1].scale(.6).move_to((text_list[0][start].get_center() + text_list[0][end].get_center()) / 2,
                                           ORIGIN,)
        if choice == 1:
            text_list[0].shift(UP)
            text_list[1].scale(.6).move_to((text_list[0][start].get_center() + text_list[0][end].get_center()) / 2,
                                           ORIGIN)

        if ifanima:
            self.play(*[
                animation_list[x](text_list[x])
                for x in range(len(text_list) - 1)
            ])
        all_choice = VGroup(*text_list)
        return all_choice


class fill_2(fill_1):
    def construct(self):
        captions = [
            "先写成平方差形式",
            "于是答案出来了"
        ]
        captions_tex = ["\\underset{a^2-b^2}{(x^2-2^2)} \\underset{\\underset{\\ce{<->}}{\\ce{->}}}{=}"
                        "\\underset{(a+b)(a-b)}{(x+2)(x-2)}"]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]

        title_list = [CodeLine("12.分解因式:~~~~~~~~=______________~", font='思源黑体 CN Bold'),
                      TexMobject("(", "x", "+", "2", ")", "(", "x", "-", "2", ")")]

        title_list = self.set_text_type_fill(title_list, 16, 31, ["#72C4C5"], [FadeInFromDown], choice=1)

        tex_for_ch = TexMobject("x", "^2", "-", "4",
                                color="#4ED6E5")\
            .scale(.6)\
            .next_to(title_list[0][7], RIGHT, buff=.12)

        tex_for_ch1 = TexMobject("x", "^2", "-", "4", color="#4ED6E5").scale(.6).move_to(np.array([0., -2., 0.]))

        tex_for_ch2 = TexMobject("x", '^2', "-", "2", "^2", color="#4ED6E5").scale(.6).\
            next_to(tex_for_ch1, ORIGIN)

        tex_for_ch3 = TexMobject("(", "x", "+", "2", ")", "(", "x", "-", "2", ")", color="#4ED6E5").\
            scale(.6).next_to(tex_for_ch1,
                              ORIGIN)

        tex_for_ch2[1].set_color("#E568DD")
        tex_for_ch2[2].set_color("#1CE50E")
        tex_for_ch2[4].set_color("#E568DD")
        tex_for_ch3[2].set_color("#30E5AC")
        tex_for_ch3[3].set_color("#E568DD")
        tex_for_ch3[7].set_color("#1CE50E")
        tex_for_ch3[8].set_color("#E568DD")
        # index1 = get_submobject_index_labels(tex_for_ch2)
        # self.add(get_submobject_index_labels(tex_for_ch3))
        self.play(ShowCreation(tex_for_ch))

        self.wait()

        self.add(captions_mob[0])

        self.play(to_draw.WriteRandom(captions_mob[0][1:]))

        self.wait()

        self.play(ReplacementTransform(tex_for_ch.copy(), tex_for_ch1))

        self.wait()

        self.play(ReplacementTransform(tex_for_ch1[:2], tex_for_ch2[:2]),
                  ReplacementTransform(tex_for_ch1[3:], tex_for_ch2[3: 5]),
                  ReplacementTransform(tex_for_ch1[2], tex_for_ch2[2]))

        self.play(ReplacementTransform(captions_mob[0], captions_tex_mob[0]))

        self.wait(2.)
        self.play(ReplacementTransform(tex_for_ch2[:3], tex_for_ch3[:5]))

        self.wait()

        self.play(ReplacementTransform(tex_for_ch2[3:], tex_for_ch3[5:]))

        self.wait()

        self.play(ReplacementTransform(captions_tex_mob[0], captions_mob[1]))

        self.wait()

        self.play(Transform(tex_for_ch3, tex_for_ch3.copy().next_to(title_list[1], ORIGIN)))

        self.play(to_draw.UnWrite(title_list[0]),
                  Uncreate(captions_mob[-1]),
                  to_draw.UnWriteRandom(tex_for_ch3),
                  to_draw.UnWrite(tex_for_ch))

        self.wait()


class fill_3(fill_2):
    def construct(self):
        captions = [
            "720°？!",
            "那不就是六边形了吗",
            "我们再看另一种方法",
            "先欣赏一段可视化动画",
            "显然",
            "答案是60°"
        ]
        captions_tex = ["\\text{外角}=180^{\\circ}-\\text{内角}=180^{\\circ}-120^\\circ=60^\\circ",
                        "=\\frac{360^{\\circ}}{\\text{边数}}"
                        "=\\frac{360^{\\circ}}{6}=60^{\\circ}"]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]

        title_list = [CodeLine("13.若正多边形的内角和等于720°,那么它的每一个外角是______°", font='思源黑体 CN Bold'),
                      TexMobject("60^\\circ")]

        title_list = self.set_text_type_fill(title_list, 28, 35, ["#72C4C5"], [FadeInFromLarge], choice=1)

        six_re_polygon = RegularPolygon(color="#6CE4FF").set_fill("#76F7FF", opacity=.7)

        six_re_polygon.move_to(np.array([3., -2., 0.]))

        point_need_0, point_need_1, point_need_2 = (six_re_polygon.get_points_defining_boundary()[0],
                                                    six_re_polygon.get_points_defining_boundary()[-2],
                                                    six_re_polygon.get_points_defining_boundary()[-4])

        line = Line(point_need_1, point_need_2, stroke_color="#4798FF")
        line_1 = line.copy().shift((point_need_1 - point_need_2))
        line1 = Line(point_need_0, point_need_1)

        arc_to_angle1 = Arc(arc_center=point_need_1, start_angle=0, angle=PI / 3., radius=.2, color="#28B623")
        arc_to_angle2 = Arc(arc_center=point_need_1, start_angle=PI / 3., angle=PI * 2. / 3.,
                            radius=.3, color="#28B623")

        arc_to_angle1_label = TexMobject("60^{\\circ}", color="#6E84FF").scale(.5).next_to(arc_to_angle1, UR,
                                                                                           buff=.03)
        arc_to_angle2_label = TexMobject("120^{\\circ}", color="#6E84FF").scale(.5).next_to(arc_to_angle2, UL, buff=.03)

        self.wait(3.)

        self.play(Write(captions_mob[0]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.wait()

        self.play(ReplacementTransform(title_list[0][11: 15].copy(), six_re_polygon), run_time=2.)

        self.wait(1.5)

        self.play(ReplacementTransform(line1.copy(), line_1),
                  ReplacementTransform(line1.copy(), line),
                  ApplyMethod(line1.set_color, "#2CD6FF"))

        self.wait()

        self.play(ShowCreation(arc_to_angle2), Write(arc_to_angle2_label))

        self.wait()

        self.play(ReplacementTransform(captions_mob[1], captions_tex_mob[0]))

        self.wait(2.)

        self.play(ShowCreation(arc_to_angle1), Write(arc_to_angle1_label))

        self.wait()

        self.play(ReplacementTransform(captions_tex_mob[0], captions_mob[2]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.play(FadeOut(arc_to_angle2),
                  FadeOut(arc_to_angle2_label), FadeOut(arc_to_angle1), FadeOut(arc_to_angle1_label),
                  FadeOut(line), FadeOut(line_1), FadeOut(line1))

        las_tex = TexMobject("6", "\\times", "`", "=", "360", "^\\circ", color="#6E84FF").scale(.5)

        point_list1 = []
        for index in range(0, 11, 2):
            point_list1.append(
                six_re_polygon.get_points_defining_boundary()[index])

        line_list1 = []
        line_list2 = []
        line_list3 = []
        angle_vGroup_list = []
        for index in range(6):
            line = Line(point_list1[index], point_list1[index + 1 if index < 5 else 0], color="#4798FF")

            line_list3.append(line.copy())

            line.shift(point_list1[index + 1 if (index + 1) in range(6) else 0] - point_list1[index])

            line2 = line.copy().shift(point_list1[index - 1] - point_list1[index])
            line_list2.append(line2)

            line = Line(point_list1[index - 1], point_list1[index], color="#4798FF")

            line.shift(point_list1[index] - point_list1[index - 1])

            line_list1.append(line)

            arc = Arc(arc_center=point_list1[index], start_angle=line.get_angle(),
                      angle=PI / 3., radius=.2, color="#74FB0D")

            angle_vGroup_list.append(VGroup(line_list3[-1], line, arc))

            print(*angle_vGroup_list[0][:])

        self.__set_to_Rotate(angle_vGroup_list)

        self.__Rotate_IN(angle_vGroup_list, run_time=2., rate_func=smooth)

        self.__Rotate_OUT(angle_vGroup_list, run_time=2., rate_func=there_and_back_with_pause)

        self.__Rotate_IN(angle_vGroup_list, run_time=1., rate_func=there_and_back)

        self.__Rotate_OUT(angle_vGroup_list, run_time=1.5)

        las_tex.next_to(angle_vGroup_list[-1][2], UR, buff=.07)

        labels = get_submobject_index_labels(las_tex[4:])

        self.play(FadeInFromDown(las_tex[0]))

        self.wait()

        self.play(FadeInFrom(las_tex[1], UP))

        self.wait()

        angle_vGroup_list_n1_2_copy = angle_vGroup_list[-1][2].copy()

        self.play(angle_vGroup_list_n1_2_copy.move_to, las_tex[2], ORIGIN)

        self.wait()

        las_tex[2].become(angle_vGroup_list_n1_2_copy.move_to(las_tex[2], ORIGIN))

        self.play(to_draw.WriteRandom(labels))
        self.play(ReplacementTransform(labels, las_tex[3:]))

        angle_vGroup_list[-1].add(las_tex)

        self.remove(angle_vGroup_list_n1_2_copy)

        self.play(
            *[
                ApplyMethod(group.set_opacity, 0.3)
                for group in angle_vGroup_list if group != angle_vGroup_list[-1]
            ],
            run_time=2.
        )

        self.__Rotate_IN(angle_vGroup_list, run_time=2., rate_func=running_start)

        self.__Rotate_OUT(angle_vGroup_list, run_time=2., rate_func=wiggle)

        self.__Rotate_IN(angle_vGroup_list, run_time=1., rate_func=exponential_decay)

        self.__Rotate_OUT(angle_vGroup_list, run_time=.5, rate_func=rush_into)

        self.__Rotate_OUT(angle_vGroup_list, run_time=.5, rate_func=rush_from)

        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[4], captions_tex_mob[1]))

        self.wait()

        self.play(angle_vGroup_list_n1_2_copy.next_to, captions_tex_mob[1], LEFT, {"buff": -.04})

        self.wait(2.)

        self.play(Transform(las_tex, TexMobject("60", "^\\circ", color="#6E84FF").scale(.5).
                            next_to(angle_vGroup_list[-1][2], UR, buff=.07)))

        self.wait()

        self.play(ReplacementTransform(VGroup(captions_tex_mob[1], angle_vGroup_list_n1_2_copy), captions_mob[5]))

        self.play(FadeInFrom(title_list[-1], LEFT))

        self.wait()

        self.play(to_draw.UnWriteRandom(angle_vGroup_list, run_time=2.), to_draw.UnWrite(title_list),
                  Uncreate(captions_mob[5]), Uncreate(six_re_polygon))

        self.wait()

    def __set_to_Rotate(self, angle_vGroup_list):
        """to set VGroup of rotate"""
        self.play(
            *[
                ShowCreation(group, about_point=group[0].get_end(), radians=PI / 3., axis=IN)
                for group in angle_vGroup_list
            ],
            run_time=1.
        )

    def __Rotate_IN(self, angle_vGroup_list, **kwargs):
        """I think the font is beautiful"""
        self.play(
            *[
                Rotating(group, about_point=group[0].get_end(), radians=PI / 3., axis=IN, **kwargs)
                for group in angle_vGroup_list
            ]
        )

    def __Rotate_OUT(self, angle_vGroup_list, **kwargs):
        self.play(
            *[
                Rotating(group, about_point=group[0].get_end(), radians=PI / 3., axis=OUT, **kwargs)
                for group in angle_vGroup_list
            ]
        )


class fill_4(fill_3):
    def construct(self):
        captions = [
            "我们先把它的逆命题写出来",
            "把答案和结论互换",
            "当然是真命题",
            "不过大家要知道, 逆命题和否命题真假性一样, 我们也可以判断该命题的否命题真&假",
            "先写出该命题的否命题",
            "一看就是真命题"
        ]
        captions_all = self.set_caption(captions)

        captions_mob = captions_all[0]

        title_list = [CodeLine("14.命题 \"直角三角形的两个锐角互余\" 的逆命题是__________(填 \"真命题\" 或 \"假命题\" )", font='思源黑体 CN Bold'),
                      TexMobject("\\text{真命题}")]

        title_list = self.set_text_type_fill(title_list, 25, 36, ["#72C4C5"], [FadeInFromLarge], choice=1)

        self.wait(3.)

        Cod_texT = title_list[0][7: 19].copy().move_to(np.array([0., -2.5, 0.])).set_color("#993300")

        Cod_texT2 = CodeLine("两个锐角互余的三角形是直角三角形", font='思源黑体 CN Bold', color="#993300").move_to(Cod_texT, ORIGIN)

        Cod_texT3 = CodeLine("不是直角三角形的三角形两个锐角不互余", font='思源黑体 CN Bold', color="#993300").move_to(Cod_texT, ORIGIN).\
            shift(3. * RIGHT)

        Cod_texT[0: 5] .set_color("#D24550")
        Cod_texT[6: 13].set_color("#D271BF")

        Cod_texT2[0: 6].set_color("#D271BF")
        Cod_texT2[7: 10].set_color("#69D2BD")
        Cod_texT2[11: 16].set_color("#D24550")

        Cod_texT3[0: 2].set_color("#EB4429")
        Cod_texT3[2: 7].set_color("#D24550")
        Cod_texT3[8: 11].set_color("#69D2BD")
        Cod_texT3[11: 15].set_color("#D271BF")
        Cod_texT3[15].set_color("#EB4429")
        Cod_texT3[16: 18].set_color("#D271BF")

        self.add(captions_mob[0][0])

        self.play(to_draw.WriteRandom(captions_mob[0][1:]))

        self.wait()

        self.play(ReplacementTransform(title_list[0][7: 19].copy(), Cod_texT))

        self.wait()

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.wait()

        self.play(ReplacementTransform(Cod_texT[0: 5], Cod_texT2[11: 16]),
                  ReplacementTransform(Cod_texT[6: 13], Cod_texT2[0: 6]),
                  Write(Cod_texT2[6]), Write(Cod_texT2[10]),
                  to_draw.WriteRandom(Cod_texT2[7: 10], run_time=1.), to_draw.UnWrite(Cod_texT[5], run_time=1.))

        self.wait()

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]))

        self.wait(2.)

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.wait(3.)

        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]))

        self.wait()

        self.play(ReplacementTransform(Cod_texT2.copy(), Cod_texT3))

        self.wait()

        self.play(Cod_texT3.shift, 1. * UP)

        self.wait(3.)

        self.play(ReplacementTransform(captions_mob[4], captions_mob[5]))

        self.play(FadeInFromDown(title_list[-1]))

        self.wait()

        self.play(FadeOutAndShiftDown(title_list),
                  *[
                      to_draw.UnWriteRandom(mob_that_y)
                      for x in [Cod_texT2, Cod_texT3, captions_mob[5]]
                      for mob_that_y in x
                  ])
        self.wait()

    def TODO(self):
        # TODO
        self.wait()


class fill_5(fill_4):
    def construct(self):
        captions = [
            "所以答案为6, 不是5",
            "我就这题错了, 没看到是 “非负整数解” , 写了5   (┬_┬)"
        ]
        captions_tex = ["\\text{先写成}3x-6\\le x+4",
                        "\\text{易得:}x\\le5"]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]

        title_list = [CodeLine("15.不等式 3(x-2)≤x+4 的非负整数解有____个", font='思源黑体 CN Bold'),
                      TexMobject("6")]

        title_list = self.set_text_type_fill(title_list, 24, 29, ["#4BC4A5"], [FadeInFromDown], choice=1)

        tex1 = TexMobject("3", "(", "x", "-", "2", ")", "\\le x+4", color="#8ED603")\
            .scale(.5).next_to(title_list[0][7: 16], DOWN, buff=2.)\
            .shift(1 * RIGHT)

        tex2 = TexMobject("3", "x", "-", "6", "\\le", "x", "+", "4", color="#29C48D")\
            .scale(.5).next_to(tex1, ORIGIN)

        tex3 = TexMobject("x", "\\le", "5", color="#29C48D")\
            .scale(.5).next_to(tex1, ORIGIN)

        self.play(Write(tex1))

        self.wait()

        self.play(Write(captions_tex_mob[0]))

        self.wait()

        self.play(ReplacementTransform(tex1[6], tex2[4:]),
                  ReplacementTransform(tex1[0], tex2[0]),
                  FadeOut(tex1[1]), FadeOut(tex1[5]),
                  ReplacementTransform(tex1[2: 4], tex2[1: 3]))

        self.wait()

        self.play(ReplacementTransform(tex1[0].copy(), tex2[3]),
                  ReplacementTransform(tex1[4], tex2[3]))

        self.wait()

        self.play(ReplacementTransform(captions_tex_mob[0], captions_tex_mob[1]))

        self.wait()

        self.play(ReplacementTransform(tex2, tex3))

        self.wait()

        self.play(ReplacementTransform(captions_tex_mob[1], captions_mob[0]))

        self.wait(3.)

        self.play(ReplacementTransform(captions_mob[0].copy(), title_list[-1]))

        self.wait(2.)

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.wait(3.)

        self.play(
            *[
                to_draw.UnWriteRandom(mob)
                for mob in VGroup(captions_mob[-1], *title_list, tex3)
            ]
        )

        self.wait()


class for_Title(fill_4):  # TODO It is the fail of fill_6, but it' good for begin.
    def construct(self):

        point_O = np.array([0., 0., 0.])
        point_A = np.array([3., 0., 0.])
        point_B = np.array([0., 4., 0.])
        point_D = point_B.copy()
        point_B1 = point_B.copy()
        point_A1 = point_A.copy()
        point_for = np.array([1.92, 1.44, 0.])

        dotA = Dot(point_A, color="#72659B")
        dotB = Dot(point_B, color="#537285")
        dotD = Dot(point_D, color="#3D9D98")
        dot_O = Dot(point_O, color="#A578A2")
        dotA1 = Dot(point_A1, color="#60BBAB", fill_opacity=.7)
        dotB1 = Dot(point_B1, color="#A68041", fill_opacity=.7)
        all_point_isdot = VGroup(dotA, dotB, dotD, dot_O, dotA1, dotB1)

        A_tex = TexMobject("A", color=dotA.get_color()).scale(.5).next_to(dotA, DOWN, buff=.1)
        B_tex = TexMobject("B", color=dotB.get_color()).scale(.5).next_to(dotB, LEFT, buff=.1)
        O_tex = TexMobject("O", color=dot_O.get_color()).scale(.5).next_to(dot_O, DL, buff=.1)
        D_tex = TexMobject("D", color=dotD.get_color()).scale(.5).next_to(dotD, DOWN, buff=.1)
        A1_tex = TexMobject("(A_1)", color=dotA1.get_color()).scale(.5).next_to(dotA1, RIGHT, buff=.1)
        B1_tex = TexMobject("(B_1)", color=dotB1.get_color()).scale(.5).next_to(dotB1, UP, buff=.1)
        all_tex_vgroup = VGroup(A_tex, B_tex, D_tex, O_tex, A1_tex, B1_tex)

        triangle1 = Polygon(point_A, point_B, point_O)
        triangle2 = Polygon(point_A1, point_B1, point_O)
        all_triangle = VGroup(triangle1, triangle2)

        def tex_to_point(vgroup):
            vgroup[0].become(TexMobject("A", color=dotA.get_color()).scale(.5).next_to(dotA, DOWN, buff=.1))
            vgroup[1].become(TexMobject("B", color=dotB.get_color()).scale(.5).next_to(dotB, LEFT, buff=.1))
            vgroup[2].become(TexMobject("O", color=dot_O.get_color()).scale(.5).next_to(dot_O, DL, buff=.1))
            vgroup[3].become(TexMobject("D", color=dotD.get_color()).scale(.5).next_to(dotD, DOWN, buff=.1))
            vgroup[4].become(TexMobject("A_1", color=dotA1.get_color()).scale(.5).next_to(dotA1, RIGHT, buff=.1))
            vgroup[5].become(TexMobject("B_1", color=dotB1.get_color()).scale(.5).next_to(dotB1, UP, buff=.1))

        def dot_to_point(vgroup):
            isinstance(vgroup, VGroup)
            for index, color in zip(range(len(vgroup) - 3), ["#A578A2", "#60BBAB", "#A68041"]):
                vgroup[index + 3].become(Dot(triangle2.get_points_defining_boundary()[2 * index - 2], color=color))

        def dot_d_update(dot):
            line_1 = MTwoPointLine(dotA.get_center(), dotB.get_center())
            line_2 = MTwoPointLine(dot_O.get_center(), dotB1.get_center())

            point = cross_lines_point(line_1, line_2)
            color = dot.get_color()
            dot.become(Dot(point, color=color))

        # def point_to_point(point_v):
        #     for x in len(point_v)
        #         point_v[x]

        # print(dotA.get_points())
        # leng_OB = TexMobject("OB\\text{长度是}")

        self.play(Write(all_point_isdot))

        self.play(SpinInFromNothing(triangle2), ShowCreation(triangle1))

        self.play(Write(all_tex_vgroup))

        self.play(
            *[
                to_draw.UnWrite(all_tex_vgroup[index_x][0][index_y])
                for index_x in [4, 5]
                for index_y in [0, -1]
            ]
        )

        all_image = VGroup(all_point_isdot, all_tex_vgroup, all_triangle)
        self.play(all_image.scale, .5, all_image.move_to, np.array([3., -2., 0.]))

        dotD.add_updater(dot_d_update)

        self.add(all_tex_vgroup)

        all_tex_vgroup.add_updater(tex_to_point)

        all_point_isdot.add_updater(dot_to_point)

        self.play(Rotating(triangle2, axis=IN, about_point=point_O), rate_function=smooth)

        self.wait()


class fill_6(fill_4):
    def construct(self):

        title_list = [CodeLine("  16.已知: 如图, 在△AOB中, ∠AOB=90°, AO=3cm, BO=4cm,\n"  # 47
                               "将△AOB绕顶点O, 按顺时针旋转得到~~~~~~~~, 线段~~~~与边AB相交于点D,\n"  # 44
                               "则线段~~~~~的最大值为=____cm.", font='思源黑体 CN Bold'),
                      TexMobject("1.6")]

        captions = [
            "首先, 让我们直观感受下OB_1的长度变换",
            "显然, OD变小则OB_1增大,",
            "那如果OD取最小呢",
            "看到我留的小球了吗"
        ]
        captions_tex = ["\\text{易得}OB_{1 \\min}\\perp AB\\ce{->}OD = {S_{\\triangle ABC} \\over{2AB}} = "
                        "{3 \\times  4 \\over5} = 2.4",
                        "B_1D_{\\max}=1.6"]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]

        point_O = np.array([0., 0., 0.])
        point_A = np.array([3., 0., 0.])
        point_B = np.array([0., 4., 0.])
        point_D = point_B.copy()
        point_B1 = point_B.copy()
        point_A1 = point_A.copy()
        point_for = np.array([1.92, 1.44, 0.])

        dotA = Dot(point_A, color="#72659B")
        dotB = Dot(point_B, color="#537285")
        dotD = Dot(point_D, color="#3D9D98")
        dot_O = Dot(point_O, color="#A578A2")
        dotA1 = Dot(point_A1, color="#60BBAB", fill_opacity=.7)
        dotB1 = Dot(point_B1, color="#A68041", fill_opacity=.7)
        all_point_isdot = VGroup(dotA, dotB, dotD, dot_O, dotA1, dotB1)

        dot_for = Dot(point_for, color="#58C4DD")

        A_tex = TexMobject("A", color=dotA.get_color()).scale(.5).next_to(dotA, DOWN, buff=.1)
        B_tex = TexMobject("B", color=dotB.get_color()).scale(.5).next_to(dotB, LEFT, buff=.1)
        O_tex = TexMobject("O", color=dot_O.get_color()).scale(.5).next_to(dot_O, DOWN, buff=.1)
        D_tex = TexMobject("D", color=dotD.get_color()).scale(.5).next_to(dotD, DOWN, buff=.1)
        A1_tex = TexMobject("(A_1)", color=dotA1.get_color()).scale(.5).next_to(dotA1, RIGHT, buff=.1)
        B1_tex = TexMobject("(B_1)", color=dotB1.get_color()).scale(.5).next_to(dotB1, UP, buff=.1)
        all_tex_vgroup = VGroup(A_tex, B_tex, D_tex, O_tex, A1_tex, B1_tex)

        triangle1 = Polygon(point_A, point_B, point_O)
        triangle2 = Polygon(point_A1, point_B1, point_O)
        all_triangle = VGroup(triangle1, triangle2)

        def tex_to_point(vgroup):
            vgroup[0].become(TexMobject("A", color=dotA.get_color()).scale(.5).next_to(dotA, DOWN, buff=.1))
            vgroup[1].become(TexMobject("B", color=dotB.get_color()).scale(.5).next_to(dotB, LEFT, buff=.1))
            vgroup[2].become(TexMobject("O", color=dot_O.get_color()).scale(.5).next_to(dot_O, DOWN, buff=.1))
            vgroup[3].become(TexMobject("D", color=dotD.get_color()).scale(.5).next_to(dotD, DOWN, buff=.1))
            vgroup[4].become(TexMobject("A_1", color=dotA1.get_color()).scale(.5).next_to(dotA1, RIGHT, buff=.1))
            vgroup[5].become(TexMobject("B_1", color=dotB1.get_color()).scale(.5).next_to(dotB1, UP, buff=.1))

        def dot_to_point(vgroup):
            isinstance(vgroup, VGroup)
            for index, color in zip(range(len(vgroup) - 3), ["#A578A2", "#60BBAB", "#A68041"]):
                vgroup[index + 3].become(Dot(triangle2.get_points_defining_boundary()[2 * index - 2], color=color))
            for index, color in zip(range(len(vgroup)), ["#72659B", "#537285", "#A578A2"]):
                if index != 2:
                    vgroup[index].become(Dot(triangle1.get_points_defining_boundary()[2 * index], color=color))
                else:
                    vgroup[index + 1].become(Dot(triangle1.get_points_defining_boundary()[2 * index], color=color))

        def dot_d_update(dot):
            line_1 = MTwoPointLine(dotA.get_center(), dotB.get_center())
            line_2 = MTwoPointLine(dot_O.get_center(), dotB1.get_center())

            point = cross_lines_point(line_1, line_2)
            color = dot.get_color()
            dot.become(Dot(point, color=color))

        long_fOD = TexMobject("OD\\text{长度:} ", "4.00", color="#83C167").move_to(np.array([0., -1., 0.])).scale(.5)
        long_fDB1 = TexMobject("DB_1\\text{长度:} ", "0.00", color="#3A819A").move_to(np.array([0., -2., 0.])).scale(.5)

        self.add(dot_for)

        self.play(SpinInFromNothing(triangle2), ShowCreation(triangle1))

        self.play(ShowCreation(all_point_isdot))

        self.play(Write(all_tex_vgroup))

        self.play(
            *[
                to_draw.UnWrite(all_tex_vgroup[index_x][0][index_y])
                for index_x in [4, 5]
                for index_y in [0, -1]
            ]
        )
        for index_x, index_y in zip([4, 5], [0, -1]):
            all_tex_vgroup.remove(all_tex_vgroup[index_x][0][index_y])

        self.add(all_tex_vgroup)

        all_tex_vgroup.add_updater(tex_to_point)
        all_point_isdot.add_updater(dot_to_point)
        dotD.add_updater(lambda dot123: dot123.become(dotB))

        all_image = VGroup(all_triangle, dot_for)
        self.play(all_image.scale, .5, all_image.move_to, np.array([3., -2., 0.]))

        dotD.clear_updaters()

        title_list = self.set_text_type_fill(title_list, 106, 111, ["#4BC4A5"], None, choice=1, ifanima=False)

        fill_title1 = TexMobject("\\Delta A_1OB_1", color="#47AB8C").scale(.5)\
            .next_to(title_list[0][65], RIGHT, buff=.1, aligned_edge=DOWN)
        fill_title2 = TexMobject("OB_1", color="#7E6E9A").scale(.5)\
            .next_to(title_list[0][77], RIGHT, buff=.1, aligned_edge=DOWN)
        fill_title3 = TexMobject("B_1D", color="#448494").scale(.5)\
            .next_to(title_list[0][95], RIGHT, buff=.1, aligned_edge=DOWN)

        def set_veOD(tex):
            long_of_OD = length_of_two_point(dot_O.get_center(), dotD.get_center()) * 2
            tex.become(TexMobject("OD\\text{长度:} %.2f" % long_of_OD, color="#83C167"))
            tex.move_to(np.array([0., -1., 0.])).scale(.5)

        def set_veDB1(tex):
            long_of_DB1 = length_of_two_point(dotD.get_center(), dotB1.get_center()) * 2
            tex.become(TexMobject("DB_{1}\\text{长度:} %.2f" % long_of_DB1, color="#3A819A"))
            tex.move_to(np.array([0., -2., 0.])).scale(.5)

        def set_that(tex):
            long_of_DB1 = length_of_two_point(dotD.get_center(), dotB1.get_center()) * 2
            long_of_OD = length_of_two_point(dot_O.get_center(), dotD.get_center()) * 2
            tex.become(TexMobject("%.2f" % long_of_OD, "+", "%.2f" % long_of_DB1, "=4.00", color="#75A0A2"))
            tex.move_to(np.array([0., -1.5, 0.])).scale(.5)
            tex[0].set_color("#83C167")
            tex[2].set_color("#3A819A")

        def set_that_but(tex):
            long_of_DB1 = length_of_two_point(dotD.get_center(), dotB1.get_center()) * 2
            long_of_OD = length_of_two_point(dot_O.get_center(), dotD.get_center()) * 2
            tex.become(TexMobject("%.2f" % long_of_OD, "+", "%.2f" % long_of_DB1, "=4.00", color="#75A0A2"))
            tex.move_to(np.array([0., -1.5, 0.])).scale(.5)
            tex[0].set_color("#83C167")
            tex[2].set_color("#3A819A")
            tex[-1].set_color("#FFFFFF")

        self.play(
            *[
                to_draw.WriteRandom(mob)
                for mob in [title_list[0], fill_title1, fill_title2, fill_title3]
            ]
        )
        tex_that = TexMobject("T_T").add_updater(set_that)

        dotD.add_updater(dot_d_update)

        all_image.add(all_point_isdot, all_tex_vgroup)

        pass  # TODO

        self.play(Rotating(triangle2, axis=IN, about_point=dot_O.get_center(), rate_func=smooth))

        self.play(Write(captions_mob[0]))

        self.wait()

        self.play(Write(long_fOD), Write(long_fDB1))

        long_fOD.add_updater(set_veOD)
        long_fDB1.add_updater(set_veDB1)

        self.play(Rotating(triangle2, axis=IN, about_point=dot_O.get_center(), rate_func=smooth, radians=TAU / 4),
                  run_time=8.)

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.play(Write(tex_that))
        self.play(ReplacementTransform(long_fOD[0][7:].copy(), tex_that[0]),
                  ReplacementTransform(long_fDB1[0][7:].copy(), tex_that[2]))

        self.add(tex_that)

        tex_that.add_updater(set_that)

        self.play(Rotating(triangle2, axis=OUT, about_point=dot_O.get_center(), rate_func=there_and_back,
                           radians=TAU / 4), run_time=8.)

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]))

        self.wait(2.)

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.wait()

        self.play(Flash(dot_for, color="#325370", flash_radius=.5, line_length=.25))

        self.play(Rotating(triangle2, axis=OUT, about_point=dot_O.get_center(), rate_func=smooth,
                           radians=np.arctan(3 / 4)), run_time=8.)

        self.play(ReplacementTransform(captions_mob[3], captions_tex_mob[0]))

        self.wait(3.)

        self.play(ReplacementTransform(captions_tex_mob[0], captions_tex_mob[1]))

        tex_that.clear_updaters()

        self.play(FadeOutAndShiftDown(tex_that[-1]))

        self.wait()

        tex_that.add_updater(set_that_but)

        self.add(tex_that)

        self.play(Rotating(triangle2, axis=OUT, about_point=dot_O.get_center(), rate_func=smooth,
                           radians=TAU - np.arctan(3 / 4)))

        for vg in [all_point_isdot, all_tex_vgroup, dotD, long_fDB1, long_fOD, tex_that]:
            vg.clear_updaters()

        self.play(FadeInFromDown(title_list[-1]))

        self.wait()

        self.play(VFadeOut(all_image), *[
            to_draw.UnWriteRandom(ti_xgnb)
            for ti_xgnb in [title_list, fill_title1, fill_title2, fill_title3]
        ])
        self.play(
            *[
                to_draw.UnWrite(mob)
                for mob in VGroup(long_fDB1, long_fOD, tex_that)
            ]
        )

        self.play(FadeOut(captions_tex_mob))

        self.wait()


class answer_1(fill_5):
    def construct(self):
        title_list = [TexMobject("17.\\text{解不等式 }3(x+1)<x+5,\\text{并将结果表示在数轴上.}", color="#000000").scale(.6)]

        self.set_answer_title(title_list, choice=0, animation_list=[Write])

        answer_for_set = [
            "\\text{解: 去括号得:}\\qquad \\quad 3x + 1 < x + 3",
            "\\text{移项得:}\\qquad \\qquad  3x - x < 3 - 1",
            "\\text{合并同类项得:}\\qquad \\quad 2x < 2",
            "\\text{系数化一得:}\\qquad \\qquad \\text{ } x < 1"
        ]

        answer_str = self.set_answer(answer_for_set, choice=0)[0]

        answer_should = self.should_answer(title_list[0].get_left() + np.array([-1., -.5, 0.]), answer_str, choice=1,
                                           choice_list=[DOWN], choice_dict={"aligned_edge": LEFT,
                                                                            "buff": .0}, word=[DOWN], aligned_edge=LEFT,
                                           buff=.1)

        numberline = NumberLine(
            x_max=3.7, x_min=-4.9,
            tick_frequency=0.5,
            include_tip=True,
            unit_size=1
        ).add_numbers(*range(-4, 4), number_config={"color": "#000000",
                      "size": 1})

        line1 = Line(np.array([1., 0., 0.]), np.array([1., .7, 0.]), stroke_color="#34D7C0", stroke_opacity=.7)
        line2 = Line(np.array([1., .7, 0.]), np.array([-5.3, .7, 0.]), stroke_color="#34D7C0", stroke_opacity=.7)

        all_image = VGroup(numberline, line1, line2).scale(.7).move_to([-1., -3., 0.])

        that = TextMobject("将 $ x < 1 $ 表示在数轴上得:").scale(.5).set_color(["#3D6A9C", "#50ACB1", "#34D7C0"]).\
            next_to(numberline, UP, buff=1.5).add_background_rectangle(color="#FFFFFF", buff=0.1, opacity=0.85)

        self.add(answer_should[0][0])

        self.wait(3.)

        self.play(ShowIncreasingSubsets(answer_should[0][1], run_time=2.))

        self.wait()

        self.play(Write(answer_should[1]))

        self.wait()

        self.play(*[to_draw.WriteRandom(should) for should in answer_should[2]])

        self.wait()

        self.add(answer_should[3][0])
        self.play(to_draw.SpinInFromNothing(answer_should[3][1:]))

        self.play(FadeIn(that))

        self.wait()

        self.play(ShowCreation(line1, run_time=2.), Write(numberline))
        self.play(GrowFromCenter(line2))

        self.wait(2.)

        self.play(*[to_draw.UnWrite(answer) for answer in [answer_should, title_list]])

        self.play(*[to_draw.UnGrowFromRandom(image) for image in all_image],
                  *[Uncreate(that_word) for that_word in that])

        self.wait()

    def set_answer_title(self, text_list, text_color=None, animation_list=None, choice=0, ifanima=True, **kwargs):
        all_list_for_check = [text_list]

        if text_color not in [None]:
            assert isinstance(text_color, list), "text_color must be list"
            all_list_for_check.append(text_color)

        if animation_list not in [None]:
            assert isinstance(animation_list, list), "animation_list must be list"
        else:
            animation_list = [Write] * len(text_list)
        all_list_for_check.append(animation_list)
        assert self.isinstance_type(all_list_for_check), "The kwarg must be list or tuple"
        assert self.isinstance_len(all_list_for_check), "this three of all_list_for_check must be equal"
        assert isinstance(text_list[0], Mobject), "hey, you can't use only a list to waste time"

        """I think I don't need to check color"""
        if text_color not in [None]:
            for x, y in zip(text_color, range(len(text_color))):
                text_list[y].set_color(x)

        if choice == 0:
            text_list[0].move_to(TOP + DOWN)
            for x in range(len(text_list) - 1):
                text_list[x + 1].next_to(text_list[x], DOWN, **kwargs)
        if choice == 1:
            text_list[0].shift(UP)

        if choice == 2:
            pass  # TODO

        if ifanima:
            self.play(*[
                animation_list[x](text_list[x])
                for x in range(len(text_list))
            ])
        all_title = VGroup(*text_list)
        return all_title

    def should_answer(self, np_array, answer, choice, choice_list=[], choice_dict={}, word=[], **kwargs):
        # assert isinstance(np_array)
        assert isinstance(np_array, np.ndarray), "np.array, a point."
        assert isinstance(answer, VGroup)
        assert isinstance(answer[0], Mobject), "hey, you can't use only a list to waste time"

        if choice == 0:
            answer[0].next_to(np_array, *choice_list, **choice_dict)

            for answer_that in range(len(answer) - 1):
                answer[answer_that + 1].next_to(answer[answer_that], *word, **kwargs)
        elif choice == 1:
            answer[0].next_to(np_array, *choice_list, **choice_dict)
            answer[1].next_to(answer[0], *word, **kwargs).shift(RIGHT * .5)
            for answer_that in range(len(answer) - 2):
                answer[answer_that + 2].next_to(answer[answer_that + 1], *word, **kwargs)

        return answer

    def set_answer(self, captions_tex_input, captions_text=None, choice=0, **kwargs):  # TODO
        captions_text = captions_text
        captions_tex = captions_tex_input

        if choice == 0:
            captions_tex_mob = VGroup(
                *[
                    TexMobject(cap, color="#000000").scale(.5)
                    .add_background_rectangle(color="#FFFFFF", buff=0.1, opacity=0.85)
                    for cap in captions_tex
                ]
            )
            if captions_text not in [None]:
                assert self.isinstance_type([captions_text])
                captions_mob = VGroup(
                    *[
                        TexMobject(cap, color="#000000").scale(.5)
                        .add_background_rectangle(color="#FFFFFF", buff=0.1, opacity=0.85)
                        for cap in captions_text
                    ]
                )
                return [captions_tex_mob, captions_mob]

        elif choice == 1:
            captions_tex_mob = VGroup(
                *[
                    TexMobject(cap, color="#000000").scale(.5)
                    for cap in captions_tex
                ]
            )
            if captions_text not in [None]:
                assert self.isinstance_type([captions_text])
                captions_mob = VGroup(
                    *[
                        TexMobject(cap, color="#000000").scale(.5)
                        for cap in captions_text
                    ]
                )
                return [captions_tex_mob, captions_mob]

        return [captions_tex_mob]


class answer_2(answer_1):
    def construct(self):
        captions = [
            "先提公因式",
            "先通分",
            "再去分母",
            "完了吗?",
            "不, 还要检验"
        ]
        captions_tex = ["\\text{再用完全平方公式: }a^2+2ab+b^2=(a+b)^2"]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]
        title_list = [TexMobject("18.(1)\\quad \\text{分解因式} \\quad 3a^3-6a^2+3a}", color="#000000").scale(.6)]

        self.set_answer_title(title_list, choice=0, animation_list=[Write])

        answer_for_set = [
            "\\text{解: 原式}=3a(a^2-2a+1)",
            "=3a(a+1)^2"
        ]

        answer_str = self.set_answer(answer_for_set, choice=0)[0]

        answer_should = self.should_answer(title_list[0].get_left() + np.array([-1., -.5, 0.]), answer_str, choice=1,
                                           choice_list=[LEFT],
                                           choice_dict={"buff": .0}, word=[DOWN], aligned_edge=LEFT,
                                           buff=.1)

        answer_should[0][1:].set_color(["#43D341", "#43D339", "#4F916F"])
        answer_should[1][1:].set_color(["#6F9CA0", "#7C72A0", "#309C9E"])

        answer_should[1].shift(RIGHT * .5)

        self.wait(3.)

        self.play(Write(captions_mob[0]))

        self.wait()

        self.play(Write(answer_should[0]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[0], captions_tex_mob[0]))

        self.wait()

        self.play(Write(answer_should[1]))

        self.wait(5.)

        self.play(to_draw.UnWrite(answer_should), to_draw.UnWrite(*title_list))

        self.wait()

        title_list = [TexMobject("18.(2)\\quad \\text{解分式方程: } \\quad {1-x\\over {x-3}}-{1\\over{3-x}}=-2",
                                 color="#000000").scale(.6)]

        self.set_answer_title(title_list, choice=0, animation_list=[Write], text_color=[["#3D6A9C", "#2C9C8D", "#3FD353"]])

        answer_for_set = [
            "\\text{解: }{x-2 \\over 3-x}=-2",
            "x-2=-2(3-x)",
            "x-2=2x-6",
            "--""x=4",
            "\\text{检验:将}x=4\\text{代入公分母}x-3\\text{得:}x-3=4-3=1\\ne 0",
            "\\text{所以}x=4\\text{是原方程的解}"
        ]

        answer_str = self.set_answer(answer_for_set, choice=0)[0]

        answer_should = self.should_answer(title_list[0].get_left() + np.array([-1., -.5, 0.]), answer_str, choice=1,
                                           choice_list=[DOWN], choice_dict={"aligned_edge": LEFT,
                                                                            "buff": .0}, word=[DOWN], aligned_edge=LEFT,
                                           buff=.1)

        captions_mob[4][-2:].set_color("#E72C45")

        answer_should[3][1][:2].set_color("#FFFFFF")
        answer_should[4][1][:2].set_color("#E72C45")

        self.wait(3.)

        self.play(ReplacementTransform(captions_tex_mob[0], captions_mob[1]))

        self.wait()

        self.play(Write(answer_should[0]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]))

        self.wait()

        self.play(Write(answer_should[1]))

        self.wait()

        self.play(Write(answer_should[2]))

        self.wait()

        self.play(Write(answer_should[3]))

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]))

        self.play(*[Write(answer)
                    for answer in answer_should[4: 6]])

        self.wait(5.)

        self.play(to_draw.UnWrite(answer_should), to_draw.UnWrite(title_list))

        self.remove(captions_mob[4][0])
        self.play(to_draw.UnWriteRandom(captions_mob[4][1:]))

        self.wait()


class answer_3(answer_2):
    def construct(self):
        captions = [
            "这道题很简单, 先化简",
            "不过要注意这个地方",
            "事实上有很多这样的地方(分母不为0)",
            "所以只能选1"
        ]
        captions_tex = ["\\text{显然}x-2 \\ne 0, \\text{所以}x \\ne 2",
                        "\\text{同理}x \\ne 0"]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]
        title_list = [TexMobject("19.\\quad \\text{化简求值:} \\quad {x^2 - 4x + 4 \\over x^2 - 2x }÷"
                                 "(x-{4\\over x}) \\qquad \\text{从}\\text{ }0, \\text{ } 1, \\text{ } 2 \\text{ }"
                                 "\\text{中选出一个你认为合适的} \\text{} x\\text{} \\text{代入求值}", color="#000000").scale(.6)]

        self.set_answer_title(title_list, choice=0, animation_list=[Write])

        answer_for_set = [
            "\\text{解: 原式}={(x-2)^2 \\over x(x-2)} ÷ {x^2 - 4 \\over x}",
            "={(x-2)^2\\over x(x-2)} \\times {x \\over (x+2)(x-2)}",
            "={1 \\over x+2}",
            "\\text{我选}1",
            "\\therefore {1 \\over x+2} = {1 \\over 1+2} = {1 \\over 3}",
        ]

        answer_str = self.set_answer(answer_for_set, choice=0)[0]

        answer_should = self.should_answer(title_list[0].get_center() + np.array([-1., -.5, 0.]), answer_str, choice=1,
                                           choice_list=[DOWN], choice_dict={"aligned_edge": LEFT,
                                                                            "buff": .0}, word=[DOWN], aligned_edge=LEFT,
                                           buff=.1)

        # self.add(get_submobject_index_labels(answer_should[1][1]))

        self.wait(3.)

        self.play(Write(captions_mob[0]))

        self.wait()

        self.play(Write(answer_should[0]))

        self.wait()

        self.play(Write(answer_should[1]))

        self.wait()

        self.play(Write(answer_should[2]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.wait()

        self.play(answer_should[1][1][9: 14].set_color, ["#FF6973", "#902314"])

        self.play(ReplacementTransform(captions_mob[1], captions_tex_mob[0]))

        self.play(answer_should[1][1][9: 14].set_color, "#000000")

        self.wait()

        self.play(answer_should[1][1][8].set_color, ["#1CA924", "#902314"])

        self.play(ReplacementTransform(captions_tex_mob[0], captions_tex_mob[1]))

        self.play(answer_should[1][1][8].set_color, "#000000")

        self.play(ReplacementTransform(captions_tex_mob[1], captions_mob[2]))

        all_tex = [*[answer_should[0][1][5: 10],  answer_should[0][1][11: 18], answer_should[0][1][24]],
                   *[answer_should[1][1][8], answer_should[1][1][9: 14], answer_should[1][1][17: 27]],
                   *[answer_should[2][1][3: 6]]
                   ]

        self.play(*[ShowPassingFlashAround(tex_that, surrounding_rectangle_config=dict(color=color))
                  for tex_that, color in zip(all_tex, color_gradient(["#EA0328", "#118724", "#4BB9E9"], len(all_tex)))],
                  *[ApplyMethod(tex_that.set_color, color)
                  for tex_that, color in zip(all_tex, color_gradient(["#EA0328", "#118724", "#4BB9E9"], len(all_tex)))])

        self.wait(2.)

        self.play(*[ApplyMethod(that.set_color, "#000000") for that in
                  [answer_should[0][1], answer_should[1][1], answer_should[2][1]]])

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.wait()

        answer_should[3].align_to(title_list[0], direction=LEFT)

        self.play(Write(answer_should[3]))

        self.play(Write(answer_should[4]))

        self.wait(5.)

        self.play(*[to_draw.UnWrite(mob_that) for mob_that in [answer_should, captions_mob[-1]]], to_draw.UnWriteRandom(title_list[0]))

        self.wait()


class answer_4(answer_2):
    def construct(self):
        captions = [
            "step1: 弱智题, 直接画图",
            "step2: 弱智题, 直接画图",
            "step3: 连接对应点, 取交点",
            "挺好玩",
            "就以这样的方式结束这题吧"
        ]

        captions_all = self.set_caption(captions)

        captions_mob = captions_all[0]
        title_list = [TexMobject("20.\\text{如图, 每个小方格都是边长为}1\\text{个单位长度的正方形, $\\triangle ABC$的三个顶点都在格点上}"
                                 "\\\\"
                                 "\\text{$($每个小方格的顶点叫格点$)$}", color="#000000").scale(.6)]

        self.set_answer_title(title_list, choice=0, animation_list=[Write])

        self.wait(3.)

        little_title = self.set_little_answer_title(title_list[0].get_left() + np.array([0., -1., 0.]), [
            TextMobject("(1)$\\quad$画出$\\triangle ABC$向下平移$4$个单位长度后得到的"
                        "$\\triangle A_1B_1C_1$", color="#000000").scale(.6),
            TextMobject("(2)$\\quad$画出$\\triangle A_1B_1C_1$关于点"
                        "$O$"
                        "成中心对称的图形$\\triangle A_2B_2C_2$", color="#000000").scale(.6),
            TextMobject("(3)$\\quad$将$\\triangle A_1B_1C_1$绕某点旋转可以得到"
                        "$\\triangle A_2B_2C_2$, 旋转中心的\\\\坐标是$\\rule[-2pt]{1.5cm}{.5pt}$111", color="#000000",
                        tex_to_color_map={"111": "#FFFFFF"}).scale(.6)
        ], choice=0, word=[DOWN], buff=.1, aligned_edge=LEFT)
        little_title[2][0][37:].set_color("#FFFFFF")

        self.play(little_title[2][0][33: 37].align_to, little_title[2][0][3], {"direction": LEFT})

        number_axes1 = NumberPlane(x_max=7.5, x_min=-7.5, y_max=7.5, y_min=-7.5,
                                   background_line_style=dict(
                                       stroke_color="#51F1FB",
                                       stroke_width=2,
                                       stroke_opacity=1),
                                   axis_config={
                                                      "stroke_color": "#9C785C",
                                                      "stroke_width": 3.,
                                                      "include_ticks": True,
                                                      "include_tip": True,
                                                      "line_to_number_buff": .1,
                                                      "label_direction": DR,
                                                      "number_scale_val": 0.5,
                                                  },
                                   ).add_coordinates(number_config=dict(color="#000000"))

        pointA = np.array([-2., 3., 0.])
        pointA1 = np.array([-2., -1., 0.])
        pointA2 = np.array([2., -3., 0.])

        pointB = np.array([-6., 0., 0.])
        pointB1 = np.array([-6., -4., 0.])
        pointB2 = np.array([6., 0., 0.])

        pointC = np.array([-1., 0., 0.])
        pointC1 = np.array([-1., -4., 0.])
        pointC2 = np.array([1., 0., 0.])

        point_all = [pointA, pointA1, pointA2,
                     pointB, pointB1, pointB2,
                     pointC, pointC1, pointC2]
        # other point

        pointO = np.array([0., 0., 0.])  # ORIGIN

        dota = Dot(pointA, color="#41C176").scale(1.5)
        dot_a1 = Dot(pointA1, color="#C13E34").scale(1.5)
        dot_a2 = Dot(pointA2, color="#6995C1").scale(1.5)

        dotb = Dot(pointB, color="#41C176").scale(1.5)
        dot_b1 = Dot(pointB1, color="#C13E34").scale(1.5)
        dot_b2 = Dot(pointB2, color="#6995C1").scale(1.5)

        dotc = Dot(pointC, color="#41C176").scale(1.5)
        dot_c1 = Dot(pointC1, color="#C13E34").scale(1.5)
        dot_c2 = Dot(pointC2, color="#6995C1").scale(1.5)

        dot_o = Dot(pointO)

        dot_that_cross = Dot(np.array([0., -2., 0.]), color="#426FA8").scale(1.5)

        all_dot = VGroup(dota, dot_a1, dot_a2,
                         dotb, dot_b1, dot_b2,
                         dotc, dot_c1, dot_c2, dot_o, dot_that_cross)

        line_AA2 = Line(pointA, pointA2, color=average_color("#41C176", "#6995C1"))
        line_A1A2 = Line(pointA1, pointA2, color=average_color("#C13E34", "#6995C1"))
        line_AA1 = Line(pointA, pointA1, color=average_color("#41C176", "#C13E34"))

        line_BB2 = Line(pointB, pointB2, color=average_color("#41C176", "#6995C1"))
        line_B1B2 = Line(pointB1, pointB2, color=average_color("#C13E34", "#6995C1"))
        line_BB1 = Line(pointB, pointB1, color=average_color("#41C176", "#C13E34"))

        line_CC2 = Line(pointC, pointC2, color=average_color("#41C176", "#6995C1"))
        line_C1C2 = Line(pointC1, pointC2, color=average_color("#C13E34", "#6995C1"))
        line_CC1 = Line(pointC, pointC1, color=average_color("#41C176", "#C13E34"))
        all_line = VGroup(line_AA2, line_A1A2, line_AA1, line_BB2, line_B1B2, line_BB1, line_CC2, line_C1C2, line_CC1)

        polygon = Polygon(pointA, pointB, pointC, color="#41C176")
        polygon1 = Polygon(pointA1, pointB1, pointC1, color="#C13E34")
        polygon2 = Polygon(pointA2, pointB2, pointC2, color="#6995C1")
        polygon_all_is_VGroup = VGroup(polygon, polygon1, polygon2)

        texA = TexMobject("A", color=average_color("#41C176", "#41C176")).scale(.9).next_to(pointA, UR, buff=.1)
        texA1 = TexMobject("A_1", color=average_color("#41C176", "#C13E34")).scale(.9).next_to(pointA1, UP, buff=.1)
        texA2 = TexMobject("A_2", color=average_color("#41C176", "#6995C1")).scale(.9).next_to(pointA2, DR, buff=.1)
        texB = TexMobject("B", color=average_color("#C13E34", "#C13E34")).scale(.9).next_to(pointB, DL, buff=.1)
        texB1 = TexMobject("B_1", color=average_color("#C13E34", "#6995C1")).scale(.9).next_to(pointB1, DL, buff=.1)
        texB2 = TexMobject("B_2", color=average_color("#C13E34", "#41C176")).scale(.9).next_to(pointB2, UP, buff=.1)
        texC = TexMobject("C", color=average_color("#6995C1", "#6995C1")).scale(.9).next_to(pointC, DOWN, buff=.1)
        texC1 = TexMobject("C_1", color=average_color("#6995C1", "#41C176")).scale(.9).next_to(pointC1, DOWN, buff=.1)
        texC2 = TexMobject("C_2", color=average_color("#6995C1", "#C13E34")).scale(.9).next_to(pointC2, UP, buff=.1)

        tex_cross = TexMobject("(0, -2)").scale(1.).next_to(pointC2, UP, buff=.1).set_color(["#6995C1", "#C13E34"])\
            .next_to(np.array(
            [0., -2., 0.]
        ))

        all_tex = VGroup(texA, texA1, texA2, texB1, texB2, texB, texC1, texC2, texC, tex_cross)

        all_image = VGroup(number_axes1, all_line, polygon_all_is_VGroup, all_dot, all_tex)

        all_image.scale(.4).shift(1. * DOWN + 2.5 * RIGHT)

        self.wait(3.)

        self.add(captions_mob[0][0])
        self.play(to_draw.WriteRandom(captions_mob[0][1:]))
        self.play(FadeIn(number_axes1), ShowCreation(polygon), ApplyMethod(little_title[1:].set_opacity, .3))

        self.play(*[FadeInFromPoint(dot1, dot2.get_center())
                    for dot1, dot2 in zip([dota, dotb, dotc], [dotc, dota, dotb])],
                  *[FadeInFromPoint(tex, dot2.get_center())
                    for tex, dot2 in zip([texA, texB, texC], [dotc, dota, dotb])]
                  )

        self.wait()

        self.play(*[ShowCreation(line_that) for line_that in VGroup(all_line[2], all_line[5], all_line[8])])

        self.wait()

        self.play(ReplacementTransform(polygon.copy(), polygon1))

        self.play(*[Uncreate(line_that) for line_that in VGroup(all_line[2], all_line[5], all_line[8])],
                  *[FadeIn(that_mob) for that_mob in VGroup(dot_a1, dot_b1, dot_c1,
                                                            texA1, texB1,
                                                            texC1)])

        self.wait()

        self.play(ApplyMethod(little_title[1].set_opacity, 1.), ApplyMethod(little_title[0].set_opacity, .3),
                  ApplyMethod(little_title[2].set_opacity, .3), run_time=2., rate_function=smooth)

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.wait()

        polygon_copy = polygon.copy()

        self.wait()

        self.play(ShowCreation(line_AA2), ShowCreation(line_CC2))

        self.play(Rotating(polygon_copy, about_point=dot_o.get_center(), axis=IN, radians=180 * DEGREES,
                           rate_func=smooth),
                  run_time=2,
                  )


        self.wait()

        self.play(Uncreate(line_AA2), Uncreate(line_CC2))

        self.play(ApplyMethod(polygon_copy.set_color, polygon2.get_color()))

        self.add(polygon2)

        self.remove(polygon_copy)

        self.wait()

        self.play(*[FadeIn(that_mob) for that_mob in VGroup(dot_a2, dot_b2, dot_c2, texA2, texB2, texC2)])

        self.wait()

        self.play(ApplyMethod(little_title[2].set_opacity, 1.), ApplyMethod(little_title[0].set_opacity, .3),
                  ApplyMethod(little_title[1].set_opacity, .3),
                  run_time=2., rate_function=smooth)

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]))

        self.wait()

        self.play(*[ShowCreation(line) for line in VGroup(line_A1A2, line_B1B2, line_C1C2)])

        self.wait()

        self.play(Write(dot_that_cross), Write(tex_cross)) #  37 UP

        self.wait()

        self.play(*[Uncreate(line) for line in VGroup(line_A1A2, line_B1B2, line_C1C2)])

        self.wait()

        self.play(ApplyMethod(little_title[0].set_opacity, 1.),
                  ApplyMethod(little_title[1].set_opacity, 1.))

        self.wait()

        tex_cross_copy = tex_cross.copy()
        tex_cross_copy.scale(1.5).next_to(little_title[2][0][36], UP, buff=.05)
        self.play(ReplacementTransform(tex_cross.copy(), tex_cross_copy))

        self.wait()

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.wait(3.)

        number_axes1.add(polygon, polygon_all_is_VGroup, all_tex, all_dot)

        number_axes1.prepare_for_nonlinear_transform(num_inserted_curves=20)

        f = lambda array: np.exp(array[0] * 1. + array[1] * 1.j)

        self.play(FadeOut(VGroup(*title_list, *little_title, tex_cross_copy)))

        self.wait()

        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]))

        self.wait()

        self.play(Uncreate(captions_mob[4]))

        self.play(number_axes1.apply_function,
                  lambda array: np.array([f(array).imag * .1, f(array).real * .1, 0.]), run_time=6.
                  )

        self.wait(3.)

        self.play(number_axes1.apply_function,
                  lambda array: array + np.array([np.cos(array[1]), np.sin(array[0]), 0.]), run_time=6.
                  )

        self.wait(3.)

        self.play(FadeIn(number_axes1))

        self.play(to_draw.UnWriteRandom(number_axes1))

        self.wait()

    def set_little_answer_title(self, np_array, text_list, text_color=None, animation_list=None, choice=0, ifanima=True,
                                choice_list=[], choice_dict={}, word=[], **kwargs):
        assert isinstance(np_array, np.ndarray), "np.array, a point."

        all_list_for_check = [text_list]

        if text_color not in [None]:
            assert isinstance(text_color, list), "text_color must be list"
            all_list_for_check.append(text_color)

        if animation_list not in [None]:
            assert isinstance(animation_list, list), "animation_list must be list"
        else:
            animation_list = [Write] * len(text_list)
        all_list_for_check.append(animation_list)
        assert self.isinstance_type(all_list_for_check), "The kwarg must be list or tuple"
        assert self.isinstance_len(all_list_for_check), "this three of all_list_for_check must be equal"
        assert isinstance(text_list[0], Mobject), "hey, you can't use only a list to waste time"

        """I think I don't need to check color"""
        if text_color not in [None]:
            for x, y in zip(text_color, range(len(text_color))):
                text_list[y].set_color(x)

        if choice == 0:
            text_list[0].next_to(np_array, *choice_list, **choice_dict)

            for answer_that in range(len(text_list) - 1):
                text_list[answer_that + 1].next_to(text_list[answer_that], *word, **kwargs)
        elif choice == 1:
            text_list[0].next_to(np_array, *choice_list, **choice_dict)
            text_list[1].next_to(text_list[0], *word, **kwargs).shift(RIGHT * .5)
            for answer_that in range(len(text_list) - 2):
                text_list[answer_that + 2].next_to(text_list[answer_that + 1], *word, **kwargs)

        if choice == 2:
            pass  # TODO

        if ifanima:
            self.play(*[
                animation_list[x](text_list[x])
                for x in range(len(text_list))
            ])

        little_title = VGroup(*text_list)

        return little_title


class answer_5(answer_4):
    def construct(self):
        captions = [
            "这道题没什么好说, 注意HL的判定就行",
        ]

        captions_all = self.set_caption(captions)

        captions_mob = captions_all[0]
        title_list = [TexMobject("21.\\text{如图}, \\text{点}E, F\\text{在线段}AC\\text{上},"
                                 "AE=CF, DE {\\bot AC}, \\text{垂足分别为}E, F, AB = CD", color="#000000").scale(.6)]

        self.set_answer_title(title_list, choice=0, animation_list=[Write])
        little_title = self.set_little_answer_title(title_list[0].get_left() + np.array([0., -1., 0.]), [
            TextMobject("求证: \\quad (1) \\quad $BE=BF$", color="#000000").scale(.6),
            TextMobject("(2) \\quad $AB//CD$", color="#000000").scale(.6)  # \\parallel
        ], choice=0, word=[DOWN], buff=.1, aligned_edge=LEFT)

        self.play(little_title[1].align_to, little_title[0][0][3], dict(direction=LEFT))

        answer_for_set = [
            "\\because DE\\perp AC,\\quad BF \\perp AC \\quad \\therefore \\angle AFB = \\angle DEC = 90 ^ \\circ",
            "\\text{又} \\because AE = CF \\quad \\therefore AE+EF=CF+FE, \\quad \\text{即:} AF = CE",
            "\\begin{array}{l}"
            "\\text{在$Rt\\triangle ABF $和$Rt\\triangle  CDE$}"
            "\\text{中:}\\\\\\text{有}\\begin{cases} AB=CD"
            "\\\\AF=CE\\end{cases}\\end{array}",
            "\\therefore \\triangle ABF \\cong \\triangle CDE \\qquad (HL)",
            "\\therefore DE = BF",
            "\\text{由(1)知:} \\quad  \\triangle ABF \\cong \\triangle CDE",
            "\\therefore \\angle A = \\angle C \\quad  \\therefore AB \\parallel CD"
        ]

        answer_str = self.set_answer(answer_for_set, choice=0)[0]

        answer_should = self.should_answer(little_title[-1].get_center() + np.array([-2., -.5, 0.]), answer_str, choice=0,
                                           choice_list=[DOWN], choice_dict={"aligned_edge": LEFT,
                                                                            "buff": .0}, word=[DOWN], aligned_edge=LEFT,
                                           buff=.1)
        VGroup(*[answer_should[x][1:] for x in range(len(answer_should))]).set_colors_by_radial_gradient(
            radius=4.,
            inner_color="#57AFDA",
            outer_color="#63E157"
        )

        theta = 23 * DEGREES

        pointA = np.array([0., 0., 0.])
        pointB = np.array([3., 0., 0.])
        pointF = np.array([3. * np.cos(theta) ** 2, 3. * np.cos(theta) * np.sin(theta), 0.])

        triangleABF = Polygon(pointA, pointB, pointF, color="#87C9E1")
        triangleEDC = triangleABF.copy().rotate(PI, about_point=(pointA + pointF) * 3. / 4.).set_color(["#709DE1",
                                                                                                        "#948DE1"])

        all_triangle = VGroup(triangleABF, triangleEDC)

        for x in [0, 2, 4]:
            if x == 0:
                pointC = triangleEDC.get_points_defining_boundary()[x]
            elif x == 2:
                pointD = triangleEDC.get_points_defining_boundary()[x]
            else:
                pointE = triangleEDC.get_points_defining_boundary()[x]

        point_all = [pointA, pointB, pointC,
                     pointD, pointE, pointF]

        dotA = Dot(pointA, color="#41B176")
        dotB = Dot(pointB, color="#7FE092")
        dotC = Dot(pointC, color="#8480C4")
        dotD = Dot(pointD, color="#CFA6E0")
        dotE = Dot(pointE, color="#E04782")
        dotF = Dot(pointF, color="#91E04A")

        all_dot = VGroup(dotA, dotB, dotC, dotD, dotE, dotF)

        texA = TexMobject("A", color=dotA.get_color()).scale(.9).next_to(dotA, DL, buff=.1)
        texB = TexMobject("B", color=dotB.get_color()).scale(.9).next_to(dotB, DR, buff=.1)
        texC = TexMobject("C", color=dotC.get_color()).scale(.9).next_to(dotC, UR, buff=.1)
        texD = TexMobject("D", color=dotD.get_color()).scale(.9).next_to(dotD, UL, buff=.1)
        texE = TexMobject("E", color=dotE.get_color()).scale(.9).next_to(dotE, DOWN, buff=.1)
        texF = TexMobject("F", color=dotF.get_color()).scale(.9).next_to(dotF, UP, buff=.1)

        all_tex = VGroup(texA, texB, texC, texD, texE, texF)

        all_image = VGroup(all_triangle, all_dot, all_tex)

        all_image.scale(1.01).move_to(np.array([3., -2., 0.]))

        self.play(Write(all_image))

        self.wait(3.)

        self.wait()

        self.play(Write(captions_mob[0]))

        self.wait()
        self.play(to_draw.UnWrite(captions_mob[0]))

        self.wait()

        for index_x in range(7):
            self.play(Write(answer_should[index_x]))
            if index_x == 6:
                break
            self.wait()

        self.wait(6.)

        for index_x in range(7):
            self.play(to_draw.UnWrite(answer_should[6 - index_x], anim_kwargs=dict(rate_func=lambda t: linear(1-t)),
                                      run_time=.5))

        self.play(to_draw.UnWrite(title_list))

        self.wait()

        self.play(*[to_draw.UnWrite(little_title_that) for little_title_that in little_title],
                  *[to_draw.UnWriteRandom(image)
                    for image in all_image])

        self.wait()


class answer_6(answer_5):
    def construct(self):
        captions = [
            "第一小题: 很简单 (其实依题意有三种作法, 你发现了吗)",
            "这里注意是BC上方, 因为BC下方还有一个交点",
            "我们验证一下",
            "验证完成, 看第二题",
            "注意书上定律证明顺序, 最好用 平行四边形对边平行 这个定律"
        ]

        captions_all = self.set_caption(captions)

        captions_mob = captions_all[0]

        title_list = [TextMobject("22.证明定律:$\\quad$平行四边形对角相等", color="#000000").scale(.6)]

        self.set_answer_title(title_list, choice=0, animation_list=[Write])
        little_title = self.set_little_answer_title(title_list[0].get_left() + np.array([-3., -1., 0.]), [
            TextMobject("(1) \\quad 尺规作图: 已知$\\angle ABC$,求作一个点$D$,"
                        " 使得以$A, B, C, D$为顶点的四边形$ABCD$是平行四边形", color="#000000").scale(.6),
            TextMobject("(2) \\quad 根据已知图形写出已知、求证和证明过程", color="#000000").scale(.6)  # \\parallel
        ], choice=0, word=[DOWN], buff=.1, aligned_edge=LEFT)

        self.play(little_title[0][0][-13:].align_to, little_title[1][0][3], dict(direction=LEFT))

        answer_for_set = [
            "\\bullet \\quad \\text{以}\\text{点}C\\text{为圆心}, AB\\text{为半径作弧}, \\text{再以}\\text{点}C\\text{为圆心}, BC\\text{为半径作弧}",
            "\\bullet \\quad \\text{两弧在}BC\\text{上方交于点D}",
            "\\bullet \\quad \\text{连接}AD, DC",
            "\\bullet \\quad \\text{则四边形}ABCD\\text{为平行四边形}"
        ]

        answer_str = self.set_answer(answer_for_set, choice=0)[0]

        answer_should = self.should_answer(little_title[-1].get_center() + np.array([-2., -.5, 0.]), answer_str,
                                           choice=0,
                                           choice_list=[DOWN], choice_dict={"aligned_edge": LEFT,
                                                                            "buff": .0}, word=[DOWN], aligned_edge=LEFT,
                                           buff=.1)

        VGroup(*[answer_should[index][1] for index in range(len(answer_should))])\
            .set_color_by_gradient("#35D2FA", "#E37183", "#3AE394", "#8A4830")

        answer_should[1][1][6: 8].set_color("#FA3F37")

        captions_mob[1][8: 10].set_color("#FA3F37")

        answer_for_set2 = [
            r"\text{已知:} \quad \text{四边形}ABDF\text{是平行四边形}",
            r"\text{求证:} \quad \angle A = \angle C, \angle B = \angle D",
            r"\text{证明:} \quad \because \text{四边形}ABDF\text{是平行四边形}",
            r"\therefore AB // CD , AD // BC, \\ & \therefore \begin{cases} \angle A + \angle B = 180 ^ \circ"
            r" \\ \angle D + \angle A = 180 ^ \circ \\ \angle B + \angle C = 180 ^ \circ "
            r"\\ \angle B + \angle D = 180 ^ \circ \\ \end{cases}",
            r"\text{整理得:} \angle A = \angle C, \angle B = \angle D"
        ]

        answer_str2 = self.set_answer(answer_for_set2, choice=0)[0]

        answer_should2 = self.should_answer(little_title[-1].get_center() + np.array([-2., -.5, 0.]), answer_str2,
                                            choice=0,
                                            choice_list=[DOWN], choice_dict={"aligned_edge": LEFT,
                                                                             "buff": .0}, word=[DOWN],
                                            aligned_edge=LEFT,
                                            buff=.1)

        VGroup(*[answer_should2[index][1] for index in range(len(answer_should2))]) \
            .set_color_by_gradient("#5292E0", "#7EDDF7", "#E099CF")

        self.wait()

        theta = 67 * DEGREES
        length_of_AB = 2.
        length_of_BC = 3.

        pointA = np.array([length_of_AB * np.cos(theta), length_of_AB * np.sin(theta), 0.])
        pointB = np.array([0., 0., 0.])
        pointC = np.array([length_of_BC, 0., 0.])
        pointD = np.array([length_of_AB * np.cos(theta) + length_of_BC, length_of_AB * np.sin(theta), 0.])

        point_all = [pointA, pointB, pointC, pointD]

        dota = Dot(pointA, color="#83EEA0")
        dotb = Dot(pointB, color="#518ECF")
        dotc = Dot(pointC, color="#E660B6")
        dotd = Dot(pointD, color="#AD504F")

        all_dot = VGroup(dota, dotb, dotc, dotd)

        line_AB = Line(dota.get_center(), dotb.get_center(), color=average_color(dota.get_color(), dotb.get_color()))
        line_AD = Line(dota.get_center(), dotd.get_center(), color=average_color(dota.get_color(), dotd.get_color()))
        line_BC = Line(dotb.get_center(), dotc.get_center(), color=average_color(dotb.get_color(), dotc.get_color()))
        line_CD = Line(dotc.get_center(), dotd.get_center(), color=average_color(dotc.get_color(), dotd.get_color()))

        answer_should[2][1][3: 5].set_color(line_AD.get_color())
        answer_should[2][1][6: 8].set_color(line_CD.get_color())
        answer_should[3][1][5: 9].set_color([dot.get_color() for dot in all_dot])

        all_line = VGroup(line_AB, line_AD, line_BC, line_CD)

        texA = TexMobject("A", color=dota.get_color()).scale(.9).next_to(dota, UL, buff=.1)
        texB = TexMobject("B", color=dotb.get_color()).scale(.9).next_to(dotb, DL, buff=.1)
        texC = TexMobject("C", color=dotc.get_color()).scale(.9).next_to(dotc, DR, buff=.1)
        texD = TexMobject("D", color=dotd.get_color()).scale(.9).next_to(dotd, UR, buff=.1)

        all_tex = VGroup(texA, texB, texC, texD)

        circle1 = Circle(arc_center=pointC, radius=length_of_AB, color=line_AB.get_color())
        circle2 = Circle(arc_center=pointA, radius=length_of_BC, color=line_BC.get_color())
        all_circle = VGroup(circle1, circle2)

        all_image = VGroup(all_circle, all_line, all_dot, all_tex)

        all_image.scale(.7).move_to([3., -1.7, 0.])

        self.wait(3.)

        self.add(captions_mob[0][0])
        self.play(to_draw.WriteRandom(captions_mob[0][1:]))

        self.play(*[FadeIn(image) for image in [line_AB, line_BC, texA, texB, texC, dotb]])

        self.wait()

        self.play(Write(answer_should[0]))

        line_BC_copy = line_BC.copy()
        line_AB_copy = line_AB.copy()
        self.play(line_BC_copy.next_to, dota.get_center(), dict(direction=RIGHT, buff=0.))

        arc1 = Arc().add_updater(lambda arc: arc.become(
                Arc(arc_center=dota.get_center(), radius=line_BC.get_length(),
                    color=line_BC.get_color(), start_angle=0.,
                    angle=abs(line_BC_copy.get_angle()) if line_BC_copy.get_end()[1] >= dota.get_center()[1] else
                    2 * PI - abs(line_BC_copy.get_angle())
                    )
        )
                                 )

        self.play(line_AB_copy.next_to, dotc.get_center(), dict(direction=pointA, buff=0.))

        def that(line_ab_copy):
            if - PI <= line_ab_copy <= line_CD.get_angle():
                if - abs(line_ab_copy - line_CD.get_angle()) + PI >= 0:
                    return - TAU - abs(line_ab_copy - line_CD.get_angle()) + PI
                return - abs(line_ab_copy - line_CD.get_angle()) + PI
            elif 0 < line_ab_copy < PI:
                return - PI + (line_ab_copy - line_CD.get_angle())

        arc2 = Arc().add_updater(lambda arc: arc.become(
                Arc(arc_center=dotc.get_center(), radius=line_AB.get_length(),
                    color=line_AB.get_color(), start_angle=line_CD.get_angle(),
                    angle=that(line_AB_copy.get_angle())
                    )
            )
                                 )

        self.remove(arc1, arc2)

        self.wait()

        self.play(Write(dota), Write(dotc))

        self.wait()

        self.play(AnimationGroup(
            AnimationGroup(Rotating(line_BC_copy, about_point=dota.get_center(), rate_func=smooth),
                           FadeIn(arc1, run_time=2., rate_func=smooth), lag_ratio=.1),
            AnimationGroup(Rotating(line_AB_copy, axis=IN, about_point=dotc.get_center()),
                           ShowCreation(arc2, run_time=2., rate_func=smooth), rate_func=smooth,
                           lag_ratio=.1),

            lag_ratio=.1
            ))

        self.play(AnimationGroup(
            FadeOut(line_BC_copy, run_time=1.5),
            FadeOut(line_AB_copy, run_time=1.5),
            lag_ratio=.3
        ))

        arc1.clear_updaters()
        arc2.clear_updaters()

        self.add(circle1, circle2)

        self.remove(arc1, arc2)

        self.wait()

        self.play(ApplyMethod(little_title[1].set_opacity, .3))

        self.wait()

        self.play(Write(answer_should[1]))

        self.wait()

        self.play(ShowCreation(dotd), FadeIn(texD))

        self.wait()

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.wait()

        dotd_copy = dotd.copy().flip(axis=pointA + LEFT * length_of_BC, about_point=dota.get_center())

        self.play(ShowCreation(dotd_copy))

        self.wait()

        self.play(Flash(dotd_copy, color="35D2FA", flash_radius=dotd_copy.get_width() * 3.
                        , num_lines=18, flash_length=.3,
                        run_time=2.))

        self.wait()

        self.play(to_draw.UnWrite(dotd_copy))

        self.wait()

        self.add(answer_should[2][0])
        self.play(to_draw.WriteRandom(answer_should[2][1:]))

        self.wait()

        self.play(*[ShowCreation(line) for line in VGroup(line_AD, line_CD)])

        self.wait()

        self.add(answer_should[3][0])
        self.play(SpinInFromNothing(answer_should[3][1:]))

        def update_to_dotA(tex_A):
            tex_A.next_to(dota, UL, buff=.1)

        def update_to_dotC(tex_C):
            tex_C.next_to(dotc, DR, buff=.1)

        def update_to_dotD(tex_D):
            tex_D.next_to(dotd, UR, buff=.1)

        def to_that(dot_a, dot_c, dot_b):
            return dot_a.get_center() + dot_c.get_center() - dot_b.get_center()

        def update_point_d(dot_d):
            pointD_1 = to_that(dota, dotc, dotb)
            dot_d.become(Dot(pointD_1, color="#AD504F"))

        def line_of_AB_function_update(line):
            line.become(Line(dota.get_center(), dotb.get_center(), color=average_color(dota.get_color(), dotb.get_color(

            ))))

        def line_of_AD_function_update(line):
            line.become(Line(dota.get_center(), dotd.get_center(), color=average_color(dota.get_color(), dotd.get_color(

            ))))

        def line_of_BC_function_update(line):
            line.become(Line(dotb.get_center(), dotc.get_center(), color=average_color(dotb.get_color(), dotc.get_color(

            ))))

        def line_of_CD_function_update(line):
            line.become(Line(dotc.get_center(), dotd.get_center(), color=average_color(dotc.get_color(), dotd.get_color(

            ))))

        def circle_1(circle):
            circle.become(Circle(arc_center=dotc.get_center(), radius=line_AB.get_length(), color=line_AB.get_color()))

        def circle_2(circle):
            circle.become(Circle(arc_center=dota.get_center(), radius=line_BC.get_length(), color=line_BC.get_color()))

        texA.add_updater(update_to_dotA)
        texC.add_updater(update_to_dotC)
        texD.add_updater(update_to_dotD)

        line_AB.add_updater(line_of_AB_function_update)
        line_BC.add_updater(line_of_BC_function_update)
        line_AD.add_updater(line_of_AD_function_update)
        line_CD.add_updater(line_of_CD_function_update)

        circle1.add_updater(circle_1)
        circle2.add_updater(circle_2)

        # I won't use lambda function

        # add_updater

        dotd.add_updater(update_point_d)

        pointA = dota.get_center()
        pointC = dotc.get_center()

        self.wait()

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]))

        self.wait()

        self.play(dota.shift, UP, rate_func=smooth)
        self.wait()
        self.play(dota.move_to, np.array([0., -1., 0.]), rate_func=smooth)
        self.wait()
        self.play(Rotating(dota, about_point=ORIGIN), ApplyMethod(dotc.shift, 2 * UP),
                  rate_func=there_and_back)

        self.play(dota.move_to, pointA, dotc.move_to, pointC)

        self.play(Rotating(dota, about_point=LEFT), Rotating(dotc, about_point=ORIGIN))

        self.wait(6.)

        texA.clear_updaters()
        texC.clear_updaters()
        texD.clear_updaters()

        line_AB.clear_updaters()
        line_BC.clear_updaters()
        line_AD.clear_updaters()
        line_CD.clear_updaters()

        circle1.clear_updaters()
        circle2.clear_updaters()

        dotd.clear_updaters()

        self.wait()

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))

        self.wait()

        self.play(*[Uncreate(circle) for circle in all_circle])

        self.play(FadeOut(answer_should))

        self.wait()

        self.play(ApplyMethod(little_title[0].set_opacity, .3), ApplyMethod(little_title[1].set_opacity, 1.))

        self.wait()

        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]))

        for index in range(len(answer_should2)):
            if index == 3:
                self.play(FadeIn(answer_should2[index][0]))
                self.play(to_draw.WriteRandom(answer_should2[index][1]))
                ShowPassingFlashAround(answer_should2[index][1], surrounding_rectangle_config=dict(
                    color="#7EDDF7"))
                self.wait()

                # make it more beautiful than before

                continue

            self.play(Write(answer_should2[index]))
            self.wait()

        self.wait(8.)

        for index_x in range(len(answer_should2)):
            self.play(to_draw.UnWrite(answer_should2[len(answer_should2) - index_x - 1],
                                      anim_kwargs=dict(rate_func=lambda t: linear(1-t)),
                                      run_time=.5))

        self.play(ApplyMethod(little_title[0].set_opacity, 1.))

        self.play(Uncreate(all_line), to_draw.UnWrite(all_dot), to_draw.SpinOutToNothing(all_tex),
                  FadeOut(captions_mob[4][0]))

        self.play(*[to_draw.RandomSpinToNothing(title) for title in [tex_is_mob[0] for tex_is_mob in [*little_title,
                                                                                                      title_list[0],
                                                                                                      [captions_mob[4]
                                                                                                       [1:]]]]])

        self.wait()


class answer_7(answer_6):
    def construct(self):
        captions = [
            "请注意, 这道题很多人会去证全等, 但是你写的下吗",
            "先转换条件"
        ]
        captions_tex = ["\\text{注意} AF \\perp AC ,\\text{这就是坑点, 它会让你的证明很难受, 所以我选择证} AB \\parallel FD"]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]
        title_list = [TextMobject("{\\small $23.$已知$:\\quad$如图, 四边形$ABCD$中垂直平分$AC$,"
                                  " 垂足为$E$,$AF\\perp AC$,$AD\\perp FD$}", color="#000000").scale(.7)]

        self.set_answer_title(title_list, choice=0, animation_list=[Write])
        little_title = self.set_little_answer_title(title_list[0].get_left() + np.array([0., -1., 0.]), [
            TextMobject("(1) 求证 :$\\text{}$四边形$ABDF$是平行四边形", color="#000000").scale(.6),
            TextMobject("(2) 如果$AF=10$, $DF=6$求四边形$ABCD$的面积", color="#000000").scale(.6)
        ], choice=0, word=[DOWN], buff=.1, aligned_edge=LEFT)

        answer_for_set = [
            "\\because BD \\text{垂直平分} AC \\quad \\therefore AB = BC, AD = DC \\therefore \\angle BAC "
            "= \\angle BCA, \\angle DAB = \\angle DCB,\\quad \\angle BEA = 90 ^ \\circ",
            "\\because \\angle BAC + \\angle DAB = \\angle BCA + \\angle DCB, \\quad \\text{即}:\\angle BAD"
            "= \\angle BCD \\quad \\therefore \\angle BAD = 90 ^ \\circ",
            "\\because AD \\perp DF \\quad \\therefore \\angle BAD = \\angle ADF \\quad \\therefore AB \\parallel "
            "DF \\quad \\text{又} \\because \\angle BEA = 90 ^ \\circ \\quad \\therefore \\angle BAE = \\angle DAF",
            "\\because AF \\parallel BD \\quad \\therefore \\text{四边形}ABDF\\text{是平行四边形}"
        ]

        answer_str = self.set_answer(answer_for_set, choice=0)[0]

        answer_should = self.should_answer(little_title[-1].get_center() + np.array([-4., -.5, 0.]), answer_str,
                                           choice=0,
                                           choice_list=[DOWN], choice_dict={"aligned_edge": LEFT,
                                                                            "buff": .0}, word=[DOWN], aligned_edge=LEFT,
                                           buff=.1)

        VGroup(*[answer_should[index][1] for index in range(len(answer_should))]).\
            set_colors_by_radial_gradient(radius=3., inner_color="#71CBD6", outer_color="#28AC85")

        captions_mob[0][15: 17].set_color("#BF8080", "#B02020")
        captions_tex_mob[0][1: 3].set_color("#B02020", "#BF8080")

        answer_for_set2 = [
            "\\text{由(1)得:} \\quad AB = BC, AD = DC \\quad \\text{又} \\because BD = BD \\quad"
            " \\therefore \\triangle ABD \\cong \\triangle CBD (SSS)",
            "\\because FD = 6, AF = 10 \\quad \\therefore AD = 8 \\quad \\therefore S_{\\triangle AFD} = {8 \\times 6 "
            "\\over 2} = 24 \\quad \\text{由(1)易得:} S_{\\triangle AFD} = S_{\\triangle ABD} = S_{\\triangle BCD}",
            "\\because S_{ABCD} = S_{\\triangle ABD} + S_{\\triangle BCD} = 48"
        ]

        answer_str2 = self.set_answer(answer_for_set2, choice=0)[0]

        answer_should2 = self.should_answer(little_title[-1].get_center() + np.array([-4., -.5, 0.]), answer_str2,
                                            choice=0,
                                            choice_list=[DOWN], choice_dict={"aligned_edge": LEFT,
                                                                             "buff": .0}, word=[DOWN],
                                            aligned_edge=LEFT,
                                            buff=.1)

        VGroup(*[answer_should2[index][1] for index in range(len(answer_should2))]).\
            set_color_by_gradient("#89EBD0", "#81EB6F", "#6E87BF")

        that_point = np.array([3., 0., 0.])

        pointA = np.array([3., 4., 0.])
        pointB = np.array([6., 4., 0.])
        pointC = Dot(pointA).flip(axis=pointA, about_point=that_point).get_center()
        pointD = that_point
        pointE = cross_lines_point(MTwoPointStraightLine(pointB, pointD), MTwoPointStraightLine(pointA, pointC))
        pointF = ORIGIN

        del that_point

        point_all = [pointA, pointB, pointC, pointD, pointE, pointF]

        dota = Dot(pointA, color="#5CBECF").scale(1.5)
        dotb = Dot(pointB, color="#F77FB7").scale(1.5)
        dotc = Dot(pointC, color="#8AF766").scale(1.5)
        dotd = Dot(pointD, color="#89CF7A").scale(1.5)  # EE83BD
        dote = Dot(pointE, color="#F75C64").scale(1.5)
        dotf = Dot(pointF, color="#6CEEEC").scale(1.5)

        all_dot = VGroup(dota, dotb, dotc, dotd, dote, dotf)

        line_AB = Line(dota.get_center(), dotb.get_center(), color=average_color(dota.get_color(), dotb.get_color()))
        line_AD = Line(dota.get_center(), dotd.get_center(), color=average_color(dota.get_color(), dotd.get_color()))
        line_DB = Line(dotd.get_center(), dotb.get_center(), color=average_color(dotd.get_color(), dotb.get_color()))
        line_DC = Line(dotd.get_center(), dotc.get_center(), color=average_color(dotd.get_color(), dotc.get_color()))
        line_FD = Line(dotf.get_center(), dotd.get_center(), color=average_color(dotf.get_color(), dotd.get_color()))
        line_BC = Line(dotb.get_center(), dotc.get_center(), color=average_color(dotb.get_color(), dotc.get_color()))
        line_AC = Line(dota.get_center(), dotc.get_center(), color=average_color(dota.get_color(), dotc.get_color()))
        line_AF = Line(dota.get_center(), dotf.get_center(), color=average_color(dota.get_color(), dotf.get_color()))

        all_line = VGroup(line_AB, line_AD, line_DC, line_FD, line_BC, line_AC, line_AF, line_DB)

        texA = TexMobject("A", color=dota.get_color()).scale(1.01).next_to(dota, UP, buff=.1)
        texB = TexMobject("B", color=dotb.get_color()).scale(1.01).next_to(dotb, UR, buff=.1)
        texC = TexMobject("C", color=dotc.get_color()).scale(1.01).next_to(dotc, RIGHT, buff=.1)
        texD = TexMobject("D", color=dotd.get_color()).scale(1.01).next_to(dotd, DOWN, buff=.1)
        texE = TexMobject("E", color=dote.get_color()).scale(1.01).next_to(dote, UP, buff=.1)
        texF = TexMobject("F", color=dotf.get_color()).scale(1.01).next_to(dotf, DOWN, buff=.1)

        all_tex = VGroup(texA, texB, texC, texD, texE, texF)

        all_image = VGroup(all_line, all_dot, all_tex).scale(.7).move_to(np.array([3., -2., 0.]))

        self.wait(3.)

        self.wait()

        self.play(Write(all_image))

        self.wait()

        self.play(Write(captions_mob[0]))

        self.wait()

        self.play(Write(captions_mob[0][]))


        self.play(Write(answer_should2))


class all_to_thank(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": "#FFFFFF",
        },
    }

    def construct(self):
        TextMobject("")



"""
\\\\\\\\\\\\\\\\ \\\\\\\\\\\\\\\\ \\\\\\\\\\\\\\\\ stop stop stop \\\\\\\\\\\\\\\\ \\\\\\\\\\\\\\\\ \\\\\\\\\\\\\\\\  
"""


"""text4 = CodeLine(title, font='思源黑体 CN Bold').shift(UP)
        .shift(DL + LEFT * 3.5).scale(.5)
        .shift(DL + LEFT * -1.).scale(.5)
        .shift(DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
        .shift(DL + LEFT *-1. + DOWN * 1.5).scale(.5)
        .next_to(text4, RIGHT, buff=-.37, aligned_edge=DOWN).scale(.5).shift(DOWN * .07)"""
# TODO#        #####

# choice1 - 10 end         cost 17 days
# fill_1 - 6 end           cost 7  days
