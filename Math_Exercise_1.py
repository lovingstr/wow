# by 李依闰
# Is my own code by a clever boy luo luo luo luo luo luo
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
        left_value = TexMobject('My QQ is 482970284').add_updater(lambda t:
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
            "分式分母不为零,",#
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

    def set_text_type_fill(self, text_list, start, end, text_color=None, animation_list=None, choice=0):
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
        self.play(*[
            animation_list[x](text_list[x])
            for x in range(len(text_list) - 1)
        ])
        all_choice = VGroup(*text_list)
        return all_choice


class fill_2(fill_1):
    def construct(self):
        captions = [
            "分式分母不为零,"
        ]
        captions_tex = ["x \\ne 3"]
        captions_all = self.set_caption(captions, captions_tex_input=captions_tex)

        captions_mob = captions_all[0]
        captions_tex_mob = captions_all[1]

        title_list = [CodeLine("12.分解因式:~~~~~~~~=______________", font='思源黑体 CN Bold'),
                      TexMobject("(", "x", "+", "2", ")", "(", "x", "-", "2", ")")]

        title_list = self.set_text_type_fill(title_list, 17, 30, ["#72C4C5"], [FadeInFromDown], choice=1)

        tex_for_ch = TexMobject("x", "^2", "-", "4"
                                , color="#4ED6E5").\
            scale(.6).\
            next_to(title_list[0][7], RIGHT, buff=.12)

        tex_for_ch1 = TexMobject("x", "^2", "-", "4")

        tex_for_ch2 = TexMobject("x", '^2', "-", "2", "^2")

        tex_for_ch3 = TexMobject("(", "x", "+", "2", ")", "(", "x", "-", "2", ")")

        self.play(ShowCreation(tex_for_ch))

        self.play(FadeInFromDown(title_list[-1]))

        self.wait()


"""text4 = CodeLine(title, font='思源黑体 CN Bold').shift(UP)
        .shift(DL + LEFT * 3.5).scale(.5)
        .shift(DL + LEFT * -1.).scale(.5)
        .shift(DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
        .shift(DL + LEFT *-1. + DOWN * 1.5).scale(.5)
        .next_to(text4, RIGHT, buff=-.37, aligned_edge=DOWN).scale(.5).shift(DOWN * .07)"""
# TODO#        #####

