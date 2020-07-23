
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
        font='Consolas', size=0.5, color=DARK_GRAY, plot_depth=2)

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
        choise4_1 = TexMobject("D\\text{. }{-}\\frac{x}{2}+{y}").set_color(YELLOW_D).shift(DR + RIGHT * 3.5).scale(.5)
        choice_true_1 = TexMobject("C").set_color(GREEN_C).next_to(text1, RIGHT, buff=-.37).scale(0.5)
        all_1 = VGroup(text1, choise1_1, choise2_1, choise3_1, choise4_1, choice_true_1)

        self.play(Write(text1))
        self.play(Write(choise1_1), Write(choise2_1), Write(choise3_1), Write(choise4_1))
        self.play(Write(captions_mob[0]))
        self.play(FadeInFromDown(choice_true_1))
        self.wait()

        text2 = CodeLine("2.若m>n，则下列不等式错误的是~~~~~~~~~~~~~~~~~~~~~~~~(  )", font='思源黑体 CN Bold', ).shift(UP)
        choise1_2 = TexMobject("A\\text{. }m+2>n+2").set_color(BLUE_D).shift(DL + LEFT * 3.5).scale(.5)
        choise2_2 = TexMobject("B\\text{. }2m>2n").set_color(TEAL_C).shift(DL + LEFT * .5).scale(.5)
        choise3_2 = TexMobject("C\\text{. }\\frac{m}{2}{>}\\frac{n}{2}").set_color(GREEN_B).shift(
            DR + RIGHT * .5).scale(.5)
        choise4_2 = TexMobject("D\\text{. }{-m>-n}").set_color(YELLOW_D).shift(DR + RIGHT * 3.5).scale(.5)
        choice_true_2 = TexMobject("D").set_color(YELLOW_D).next_to(text2, RIGHT, buff=-.37).scale(.5)
        all_2_title = VGroup(text2, choise1_2, choise2_2, choise3_2, choise4_2)
        all_2 = VGroup(text2, choise1_2, choise2_2, choise3_2, choise4_2, choice_true_2)

        self.play(ReplacementTransform(all_1, all_2_title))

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
                rum_time=2.5
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
        choice_true_3 = TexMobject("C").set_color(GREEN_B).next_to(text3, RIGHT, buff=-.37).scale(.5)
        all_3_title = VGroup(text3, choise1_3, choise2_3, choise3_3, choise4_3)
        all_3 = VGroup(text3, choise1_3, choise2_3, choise3_3, choise4_3, choice_true_3)
        self.play(ReplacementTransform(all_2, all_3_title))

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
        choice_true_4 = TexMobject("A").set_color(BLUE_D).next_to(text4, RIGHT, buff=-.37, aligned_edge=DOWN) \
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

        choice_true_5 = TexMobject("D").set_color("#32CB7D").next_to(text5, RIGHT, buff=-.37).scale(.5)

        choise1_5 = TexMobject("A").set_color("#2EEEF4").next_to(chestnut_1, DOWN, buff=.25).scale(.5)
        choise2_5 = TexMobject("B").set_color("#37ECD3").next_to(chestnut_2, DOWN, buff=.25).scale(.5)
        choise3_5 = TexMobject("C").set_color("#36D59F").next_to(chestnut_3, DOWN, buff=.25).scale(.5)
        choise4_5 = TexMobject("D").set_color("#32CB7D").next_to(chestnut_4, DOWN, buff=.25).scale(.5)

        self.play(ReplacementTransform(captions_mob[11], captions_mob[12]))
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

        line1 = Line(chestnut.get_center(), np.array([chestnut.get_x(RIGHT), chestnut.get_y(ORIGIN), 0.])
                     , color=BLUE_B, stroke_width=2.
                     )
        line2 = Line(chestnut_copy.get_center(), np.array([chestnut_copy.get_x(RIGHT), chestnut_copy.get_y(ORIGIN), 0.])
                     , color=BLUE_B, stroke_width=2.)

        arc = Arc(color=BLACK)

        # number_angle = Integer(0, fill_color=BLACK).scale(.24)
        # number_angle.add_updater(lambda x: number_angle.set_value(line2.get_angle() / PI * 180))
        left_value = TexMobject('').add_updater(lambda t:
                                                t.become(TexMobject('%.1f^{\\circ}' % (line2.get_angle() * 180 / PI),
                                                                    fill_color=BLACK).next_to(arc, UR, buff=.05).
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
            scale(.7).set_sheen(.6).set_sheen_direction(UP)
        self.play(Write(title))
        self.play(title.scale, .5)
        self.play(title.move_to, np.array([-4., 3., 0.]))
        self.play(Write(CodeLine("@_2,~0_.making", t2c={"0_.making": "#AE5F92"})))

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
        captions_mob = VGroup(
            *[
                CodeLine(cap, font='思源黑体 CN Bold', size=.5).to_edge(DOWN * 1.2)
                .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in captions
            ]
        )

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

        title_list = self.set_text_type(title_list, title_color, [Write] * 6, choice=3)  # [Write] * 6
        self.wait()

        self.play(FadeInFromDown(all_to_solve[0]))

        self.play(Write(captions_mob[0]))

        self.play(ReplacementTransform(all_to_solve[0], all_to_solve[1]))

        self.play(FadeInFromDown(all_to_solve[2]), Write(all_to_solve[5][0]), FadeOutAndShiftDown(all_to_solve[1]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.play(FadeInFromDown(all_to_solve[4]), Write(all_to_solve[5][2]))

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]))

        self.play(all_to_solve[5][0].next_to, all_to_solve[5][2], RIGHT, .3, DOWN)

        and_to_two_number = TexMobject("-", color="#FA6117", opacity=0.7,
                                       stroke_width=1.5).next_to(all_to_solve[5][2], RIGHT, -.05).\
            scale(.5)

        self.play(FadeInFrom(and_to_two_number, ORIGIN))

        all_to_Trans_VGroup=VGroup(all_to_solve[5][0], and_to_two_number, all_to_solve[5][2])

        self.play(FadeOutAndShiftDown(all_to_solve[2]), FadeOutAndShiftDown(all_to_solve[4]))
        self.play(ReplacementTransform(all_to_Trans_VGroup, all_to_solve[5][1]))
        self.play(Write(all_to_solve[3]))

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))
        all_to_solve.remove(*all_to_solve[0: 3], all_to_solve[4])
        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]))
        self.play(FadeInFromDown(title_list[-1]))
        print(*all_to_solve)
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

    def isinstance_type(self, all_list):
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
            text_list[5].next_to(text_list[0], RIGHT, buff=-.37).scale(0.5)

        elif choice == 1:
            text_list[0].shift(UP)
            text_list[1].shift(DL + LEFT * 3.5).scale(.5)
            text_list[2].shift(DR + RIGHT * 2.).scale(.5)
            text_list[3].shift(DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
            text_list[4].shift(DR + RIGHT * 2. + DOWN * 1.5).scale(.5)
            text_list[5].next_to(text_list[0], RIGHT, buff=-.37).scale(.5)

        elif choice == 2:
            text_list[0].shift(UP)
            text_list[0].shift(DL + LEFT * 3.5).scale(.5)
            text_list[0].shift(DR + RIGHT * 2.).scale(.5)
            text_list[0].shift(DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
            text_list[0].shift(DR + RIGHT * 2. + DOWN * 1.5).scale(.5)
            text_list[0].next_to(text_list[0], RIGHT, buff=-.37).scale(.5)

        elif choice == 3:
            text_list[0].shift(UP)
            text_list[1].shift(DL + LEFT * 3.5).scale(.5)
            text_list[2].shift(DL + LEFT * -1.).scale(.5)
            text_list[3].shift(DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
            text_list[4].shift(DL + LEFT * -1. + DOWN * 1.5).scale(.5)
            text_list[5].next_to(text_list[0], RIGHT, buff=-.37, aligned_edge=DOWN).scale(.5).shift(DOWN * .07)

        elif choice == 4:
            text_list[0].shift(UP)
            text_list[1].scale(.5).move_to(np.array([4.5, -1., 0.])).shift(LEFT * 10.)
            text_list[2].scale(.5).move_to(np.array([4.5, -1., 0.])).shift(LEFT * 8.)
            text_list[3].scale(.5).move_to(np.array([4.5, -1., 0.])).shift(LEFT * 6.)
            text_list[4].scale(.5).move_to(np.array([4.5, -1., 0.])).shift(LEFT * 4.)
            text_list[5].scale(.5).next_to(text_list[0], RIGHT, buff=-.37).scale(.5)

            choise1 = TexMobject("A").set_color(text_list[1].get_color()).next_to(text_list[1], DOWN, buff=.25).scale(.5)
            choise2 = TexMobject("B").set_color(text_list[2].get_color()).next_to(text_list[2], DOWN, buff=.25).scale(.5)
            choise3 = TexMobject("C").set_color(text_list[3].get_color()).next_to(text_list[3], DOWN, buff=.25).scale(.5)
            choise4 = TexMobject("D").set_color(text_list[4].get_color()).next_to(text_list[4], DOWN, buff=.25).scale(.5)
            all_word = VGroup(choise1, choise2, choise3, choise4)
            text_list.insert(5, all_word)
            animation_list.insert(5, Write)

        self.play(*[
                animation_list[x](text_list[x])
                for x in range(len(text_list) - 1)
            ])
        all_choice = VGroup(* text_list)
        return all_choice


class choice_7(choice_6):
    def construct(self):
        title_list = [CodeLine("6.化简~~~~~~~~~的结果是~~~~~~~~~~~~~~~~~~~~~~~~(  )",
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
        title_another.next_to(title_list[0][3], buff=.09)

        self.play(FadeInFromDown(title_another))

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
        self.play(ReplacementTransform(title_to_solve_an[8: 14], title_to_solve_an2[6: 17]))
        self.play(ReplacementTransform(title_to_solve_an[0: 7], title_to_solve_an2[0: 6]))

        self.play(ReplacementTransform(title_to_solve_an2[3].copy(), title_to_solve_an3[0].shift(LEFT * .17)))

        self.wait(.5)

        self.play(ReplacementTransform(title_to_solve_an2, title_to_solve_an3[1:-1]))

        self.play(title_to_solve_an3[0].shift, RIGHT * .17, rum_time=2.)

        self.play(ReplacementTransform(title_to_solve_an3[0: -1], title_to_solve_an4[0: -1]))

        self.play(Transform(title_to_solve_an4[1: -1],
                            (TexMobject("-", "{m}", "\\over", "{m", "+", "3}", color="#60FAB9")
                            .next_to(title_to_solve_an, ORIGIN, buff=0.).scale(.75))[1:].shift(RIGHT * .23)))

        title_to_solve_an4.remove(title_to_solve_an4[6])

        self.play(ReplacementTransform(title_to_solve_an4, title_list[2]))

        self.play(FadeInFromDown(title_list[-1]))

        self.play(FadeOutAndShiftDown(title_list), FadeOut(title_another))

        self.wait(2.)


class choice_8(choice_7):
    def construct(self):
        title_list = [CodeLine("如图， 一次函数₁₁₁~~~~~~~~~~~~~~~~~~~~~~~~(  )",  # 6.y=x+b与y₂=kx+4的图像相交于点p(1,3),x>kx+4
                               font='思源黑体 CN Bold'),
                      TexMobject("1\\text{.}\\frac{m}{m+3}"),
                      TexMobject("2\\text{.}{-}\\frac{m}{m+3}"),
                      TexMobject("3\\text{.}\\frac{m}{m-3}"),
                      TexMobject("4\\text{.}\\frac{m}{3-m}"),
                      TexMobject("B")
                      ]
        title_color = ["7AFAEE", "#57FAAF", "#ECBDFA", "#60FAB9", "#60FAB9"]

        title_list = self.set_text_type(title_list, title_color)




"""text4 = CodeLine(title, font='思源黑体 CN Bold').shift(UP)
        .shift(DL + LEFT * 3.5).scale(.5)
        .shift(DL + LEFT * -1.).scale(.5)
        .shift(DL + LEFT * 3.5 + DOWN * 1.5).scale(.5)
        .shift(DL + LEFT *-1. + DOWN * 1.5).scale(.5)
        .next_to(text4, RIGHT, buff=-.37, aligned_edge=DOWN).scale(.5).shift(DOWN * .07)"""

# TODO#        #####


