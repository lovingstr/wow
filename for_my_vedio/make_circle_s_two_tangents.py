from manimlib.imports import *
from manim_sandbox.utils.imports import *
from luoluoluo_useful.imports import *
from manim_sandbox.Logo import Logo as ManimKindergarten

mkvg = MKVG = mkVG = VGroup

buff = 3.5

my_dict = {}

NONE = Square().scale(.5).set_opacity(.0)

def KCl(start, end):
    return Line(start.get_center(), end.get_center())


class SourceHansfont(Text):
    CONFIG = {
        "font": "思源黑体",
    }


class begin_backgroundBlack(Scene):

    @staticmethod
    def work_for_the_2ks_and_2bs_about_unit_circlesTangentLine(r, p, q):
        if abs(p) - abs(r) != 0.:
            k1 = ((p * q) + (r * np.sqrt(p ** 2 + q ** 2 - r ** 2))) / (p ** 2 - r ** 2)
            k2 = ((p * q) - (r * np.sqrt(p ** 2 + q ** 2 - r ** 2))) / (p ** 2 - r ** 2)

        else:
            k1 = k2 = (q ** 2 - r ** 2) / 2 * p * q

        b1 = q - k1 * p
        b2 = q - k2 * p

        def return_message():

            if b1 > 0:
                b1m = '+'
            elif b1 < 0:
                b1m = '-'
            else:
                b1m = ''

            if b2 > 0:
                b2m = '+'
            elif b2 < 0:
                b2m = '-'
            else:
                b2m = ''

            return b1m, b2m

        b1m, b2m = return_message()
        if k1 != k2:
            print("y1: y = {}x ".format(k1) + b1m + " {}".format(abs(b1)))
            print("y2: y = {}x ".format(k2) + b2m + " {}".format(abs(b2)))

        elif k1 == k2:
            print("y1 & y2: y = {}x ".format(k1) + b1m + " {}".format(abs(b1)))
        return k1, k2, b1, b2

    @staticmethod
    def return_two_point(k, b, x1, x2):
        b1 = k * x1 + b
        b2 = k * x2 + b

        return np.array([x1, b1, 0.]), np.array([x2, b2, 0.])

    @staticmethod
    def return_the_2ks_and_2bs_about_unit_circlesTangentLine(circle, A):
        assert isinstance(circle, Circle) and isinstance(A, np.ndarray), "the first must be Circle and the second " \
                                                                         "must be ndarray"

        r = circle.radius
        print("circle's radius = {}".format(r))

        p, q = A[0], A[1]
        print("P's coord is ({}, {})".format(p, q))

        return work_for_the_2ks_and_2bs_about_unit_circlesTangentLine(r, p, q)

    def setup(self):
        self.set_cap()
        self.set_caption_on()

    def construct(self):
        captions_mob = VGroup(
            *[
                TextMobject(cap, tex_to_color_map={}).to_edge(DOWN * 1.2)
                .add_background_rectangle(color=BLACK, buff=0.1, opacity=0.85)
                for cap in ["我们在初中就知道, 过圆外一点可以作圆的切线",
                            "而且是两条切线",
                            "但是, 你知道怎样用尺规作这两条切线吗?"]
            ]
        )
        self.play(Write(captions_mob[0]))
        cir = Circle(radius=2)
        p1 = np.array([4, 1., 0])
        k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir, p1)
        line1 = Line(*return_two_point(k1, b1, -.5, 5), color="#FF7D83")
        line2 = Line(*return_two_point(k2, b2, -2, 5), color="#87F8FF")
        dot = Dot(p1)

        self.play(ShowCreation(cir))
        self.play(Write(dot))
        self.play(ShowCreation(line2))

        self.play(ShowCreation(line1))

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))

        self.wait()

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]))

        self.wait()

        self.play(VFadeOut(VGroup(cir, dot, line1, line2)))

        self.wait()

        self.play(ReplacementTransform(captions_mob[2], self.captions_mob[0]))

        self.wait()

        one_and_one_is_tex = TexMobject("1+1=2").move_to(LEFT + UP * 2)
        three_times_three_times_three = TexMobject("3^3=27").move_to(.5 * RIGHT + DOWN)

        self.play(*[Write(tex) for tex in [one_and_one_is_tex, three_times_three_times_three]])

        self.wait()

        self.play(ReplacementTransform(self.captions_mob[0], self.captions_mob[1]))

        self.play(*[to_draw.UnWrite(tex) for tex in [one_and_one_is_tex, three_times_three_times_three]])

        self.wait(2.)

        self.play(ReplacementTransform(self.captions_mob[1], self.captions_mob[2]))

        self.wait()

        self.play(to_draw.UnWrite(self.captions_mob[2]))

        self.wait(.1)

    def set_caption_on(self, t2c={}):
        self.captions_mob = VGroup(
            *[
                SourceHansfont(cap, tex_to_color_map=t2c).to_edge(DOWN * 1.2)
                .add_background_rectangle(color=BLACK, buff=0.1, opacity=0.85)
                for cap in self.caps
            ]
        )

    def change_cap(self):
        pass

    def set_cap(self):
        self.caps = ["如果使用初中的数学知识, 应该是很轻松可以计算出来的",
                     "但是, 对于我这个懒人来说, 我才不愿意去思考呢",
                     "所以今天, 我们就来研究如何暴力且优雅的尺规作图"]
        self.change_cap()


class begin_backgroundWhite(begin_backgroundBlack):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def get_l_lths(self, line):
        return length_of_two_point(line.get_start(), line.get_end())

    def construct(self):
        get_l = self.get_l_lths
        line1 = Line(UP * 3, (RIGHT + UP) * 2 + UP).set_color(BLACK)
        line2 = Line(UP, UR).set_color(BLACK)
        line3 = Line(ORIGIN - UP, 4 * RIGHT - UP).set_color(BLACK)

        arc1, arc2, arc3, arc4 = [Arc(arc_center=lin.get_start(), radius=get_l(lin), color=color,
                                      start_angle=start_angle, angle=angle)
                                  for lin, color, start_angle, angle in
                                  zip([line1, line2, Line(DOWN, 2 * RIGHT + DOWN),
                                       Line(2 * RIGHT + DOWN, 3 * RIGHT + DOWN)],
                                      ["#90FFFC", "#A2FF90"] * 2,
                                      [- PI / 15.5, - PI / 12] * 2,
                                      [TAU / 15.5, TAU / 12] * 2)]

        tex1 = TexMobject("a").next_to(line1, DOWN).set_color(BLACK)
        tex2 = TexMobject("b").next_to(line2, DOWN).set_color(BLACK)
        # tex3 = TexMobject("c").next_to(line3, DOWN).set_color(BLACK)

        tex1_copy = TexMobject("a").next_to(Line(DOWN, 2 * RIGHT + DOWN), DOWN).set_color(arc1.get_color())
        tex2_copy = TexMobject("b").next_to(Line(2 * RIGHT + DOWN, 3 * RIGHT + DOWN), DOWN).set_color(arc2.get_color())

        line_copy_1 = Line(DOWN, 2 * RIGHT + DOWN).set_color(BLACK)
        line_copy_2 = Line(2 * RIGHT + DOWN, 3 * RIGHT + DOWN).set_color(BLACK)

        self.play(*[ShowCreation(line) for line in [line1, line2, line3]],
                  *[Write(tex) for tex in [tex1, tex2]])

        self.play(ShowCreation(arc1))
        self.wait()

        vg1 = VGroup(line1, arc1, tex1)
        vg2 = VGroup(line_copy_1, arc3, tex1_copy)
        vg3 = VGroup(line2, arc2, tex2)
        vg4 = VGroup(line_copy_2, arc4, tex2_copy)

        self.play(*[ReplacementTransform(vg1.copy()[num], vg2[num]) for num in range(3)])
        self.wait()
        self.play(ShowCreation(arc2))
        self.wait()
        self.play(*[ReplacementTransform(vg3.copy()[num], vg4[num]) for num in range(3)])
        self.wait()
        vg2.remove(arc3, tex1_copy)
        vg4.remove(arc4, tex1_copy)
        l_f = Line(np.array([.0, -1., 0.]), np.array([3., -1., 0.])).set_color("#58C4CA").set_plot_depth(-1)
        tex_fff = TexMobject("a+b").set_color(["#90FFFC", "#A2FF90"]).scale(.7).next_to(l_f, DOWN)
        self.add(l_f)
        self.play(*[to_draw.UnBorderThenFade(ar) for ar in [vg1, vg2, vg3, vg4]], Uncreate(line3),
                  ReplacementTransform(VGroup(tex2_copy, tex1_copy), tex_fff))
        self.play(*[Uncreate(tex) for tex in Group(arc3, arc4)])
        self.wait(2.)
        self.play(*[to_draw.UnWrite(mob) for mob in Group(l_f, tex_fff)])
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
        pass

    def set_cap(self):
        self.caps = [""]
        self.change_cap()


class BacB(begin_backgroundBlack):
    def construct(self):
        raise Exception("can\'t draw this")


class BacW(begin_backgroundWhite):
    def construct(self):
        raise Exception("can\'t draw this")


class SceneW2(BacW):

    def construct(self):
        get_l = self.get_l_lths
        line1 = Line(UP, RIGHT + UR).set_color(BLACK)
        line2 = Line(DOWN, RIGHT * 3 - UP).set_color(BLACK)
        line3 = Line(DOWN + RIGHT * 2, RIGHT * 3 - UP).set_color(BLACK).set_plot_depth(0)

        line_copy = Line(DOWN, RIGHT + DR).set_color(BLACK)

        arc1, arc2 = [Arc(arc_center=lin.get_start(), radius=get_l(lin), color=color,
                          start_angle=start_angle, angle=angle)
                      for lin, color, start_angle, angle in
                      zip([line1, line_copy], ["#90FFFC"] * 2, [- PI / 15.5] * 2, [TAU / 15.5] * 2)]

        tex1 = TexMobject("a").next_to(line1, DOWN).set_color(BLACK)
        tex2 = TexMobject("b").next_to(line2, DOWN).set_color(BLACK)
        tex3 = TexMobject("b-a").next_to(line3, DOWN).set_color_by_gradient("#E5B4FF", arc1.get_color())

        tex_copy = TexMobject("a").next_to(line_copy, DOWN).set_color(arc1.get_color())

        self.play(*[ShowCreation(line) for line in [line1, line2]],
                  *[Write(tex) for tex in [tex1, tex2]])

        self.play(ShowCreation(arc1))
        self.wait()

        vg1 = VGroup(line1, arc1, tex1)
        vg2 = VGroup(line_copy, arc2, tex_copy)
        vg3 = VGroup(line3, tex3)

        self.play(ReplacementTransform(vg1.copy(), vg2))
        self.wait()

        self.remove(line2)
        self.add(line3)

        self.play(VFadeOut(vg2), ReplacementTransform(tex1, tex3[0][2]), ReplacementTransform(tex2, tex3[0][0]),
                  FadeIn(tex3[0][1]))

        self.wait()

        self.play(ApplyMethod(vg3.shift, LEFT * 2), *[FadeOut(v) for v in (line1, arc1)])
        self.wait()


class SceneW3(SceneW2):

    def setup(self):
        self.set_cap()
        self.set_caption_on()
        self.O = ORIGIN

    def set_caption_on(self, t2c={}):
        self.captions_mob = VGroup(
            *[
                TextMobject(cap, tex_to_color_map=t2c).set_color(BLACK).to_edge(DOWN * 1.2).scale(.7)
                .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in self.caps
            ]
        )

    def construct(self):
        caption_mob = self.captions_mob.copy()
        O = self.O
        line1 = Line(DOWN * 2 + LEFT * 4, DOWN * 2 + RIGHT * 6).set_color(BLACK)
        line2 = Line(LEFT * 2, RIGHT * 4).set_color(BLACK)
        line2_1 = Line(LEFT * 2, LEFT).set_color("#5BFFBD")
        line2_2 = Line(LEFT, O).set_color("#5BFFBD")
        line2_3 = Line(O, RIGHT).set_color("#5BFFBD")
        line2_4 = DashedLine(RIGHT, RIGHT * 2).set_color("#5BFFBD")
        line2_5 = Line(RIGHT * 2, RIGHT * 3).set_color("#5BFFBD")
        line_list = [line2_1, line2_2, line2_3, line2_4, line2_5]

        times_num = len(line_list)
        t = times_num

        tex_VGroup = VGroup()
        A_tex = TexMobject("A").set_color(BLACK).next_to(line1.get_start(), DOWN).scale(.7)
        B_tex = TexMobject("B").set_color(BLACK).next_to(line1.get_end(), DOWN).scale(.7)
        tex_VGroup.add(A_tex, B_tex)

        self.play(ShowCreation(line1), *[Write(tex) for tex in tex_VGroup])
        self.play(Write(caption_mob[0]))
        self.wait()

        point = Dot(UP * 2).set_color("#8DE4FF").set_plot_depth(4)
        rcli = [Arc(arc_center=lin.get_start(), radius=length_of_two_point(lin.get_start(), lin.get_end()), color=color,
                    start_angle=start_angle, angle=angle)
                for lin, color, start_angle, angle in
                zip(line_list, ["#90FFFC"] * t, [- PI / 15.5] * t, [TAU / 15.5] * t)]

        del t

        for x in range(-1, times_num):
            x2 = x1 = np.nan

            self.wait(.1)
            if x == -1:
                self.play(ReplacementTransform(caption_mob[0], caption_mob[1]))

                self.wait()

                self.play(ShowCreation(line_list[x + 1]))

                self.play(ReplacementTransform(caption_mob[1], caption_mob[2]))

                self.wait()

                self.play(ShowCreation(rcli[x + 1]))

                self.wait()

                print("(0, 1)")
                continue
            if x in range(1, times_num) and x is not times_num - 2:
                self.play(ShowCreation(line_list[x]))
                x1 = x
            elif x is times_num - 2:
                self.play(Write(line_list[x]))
                x1 = x

            self.wait()
            if x + 1 in range(times_num):
                self.play(ShowCreation(rcli[x + 1]))
                x2 = x + 1
            print("({}, {})".format(x1, x2))
            self.wait()

        self.wait()
        dot_list = list()
        for x in range(6):
            dot_list.append(Dot(np.array([x - 2, 0., 0.])).set_color("#5DCCFF"))

        for x in range(6):
            if x > 3:
                if x == 4:
                    tex_VGroup.add(TexMobject("Q_{n-1}").set_color("#5DCCFF").scale(.7).next_to(dot_list[x], DOWN, buff=SMALL_BUFF))
                if x == 5:
                    tex_VGroup.add(TexMobject("Q_n").set_color("#5DCCFF").scale(.7).next_to(dot_list[x], DOWN, buff=SMALL_BUFF))
                continue
            tex_VGroup.add(TexMobject("Q_{}".format(x)).set_color("#5DCCFF").scale(.7).next_to(dot_list[x], DOWN, buff=SMALL_BUFF))

        tex_VGroup[-6].next_to(dot_list[0], UL, buff=SMALL_BUFF)
        tex_VGroup[-1].next_to(dot_list[5], UR, buff=SMALL_BUFF)

        self.play(ReplacementTransform(caption_mob[2], caption_mob[3]))
        self.wait()

        self.play(AnimationGroup(*[Write(dot) for dot in dot_list], lag_ratio=.3),
                  AnimationGroup(*[Write(tex) for tex in tex_VGroup[2: 8]], lag_ratio=.3))
        self.play(*[to_draw.UnWrite(arc) for arc in rcli])

        line_side1 = Line(DOWN * 2 + LEFT * 4, point.get_center()).set_color("#A8BEFF")
        line_side2 = Line(DOWN * 2 + RIGHT * 6, point.get_center()).set_color("#A8BEFF")

        self.wait()

        self.play(ReplacementTransform(caption_mob[3], caption_mob[4].shift(DOWN * .5)))

        self.play(*[ShowCreation(line_side) for line_side in [line_side1, line_side2]])

        tex_C = TexMobject("C").set_color(BLACK).scale(.7).next_to(point, UP, SMALL_BUFF)

        self.play(*[Write(mobject=mobject) for mobject in [point, tex_C]])

        self.wait(2.)

        self.play(ReplacementTransform(caption_mob[4], caption_mob[5]))

        p_list = [Dot(np.array([-4 + (10 / 5) * x, -2, 0.])).set_color("#35C0FF", "#40FFE9") for x in range(6)]

        p = [P_P.get_center() for P_P in p_list]

        for x in range(4):
            if x == 3:
                tex_VGroup.add(TexMobject("P_{n-1}").set_color("#35C0FF", "#40FFE9").scale(.7).next_to(p_list[x + 1], DOWN, buff=SMALL_BUFF))
                continue
            tex_VGroup.add(TexMobject("P_{}".format(x + 1)).set_color("#35C0FF", "#40FFE9").scale(.7).next_to(p_list[x + 1], DOWN, buff=SMALL_BUFF))

        # q = [Q_Q.get_center() for Q_Q in dot_list]

        to_line_list = VGroup(*[Line(C, P) for C, P in zip([point] * len(p), p)])[1: len(p) - 1]
        to_line_list.set_colors_by_radial_gradient(center=to_line_list[3].get_center(), radius=2.5, inner_color="#E2FF92", outer_color="#8CCEFF")

        self.play(ShowCreation(to_line_list))

        self.wait(.5)

        self.play(AnimationGroup(AnimationGroup(*[Write(dot) for dot in p_list], lag_ratio=.3),
                  AnimationGroup(*[Write(tex) for tex in tex_VGroup[- 4: len(tex_VGroup)]], lag_ratio=.3), lag_ratio=.2))

        self.wait()

        self.wait()

        self.play(ReplacementTransform(caption_mob[5], caption_mob[6]))

        self.wait()

        self.play(ReplacementTransform(caption_mob[6], caption_mob[7]))

        random_list = [*[to_draw.UnWrite(line) for line in Group(*line_list, line_side1, line_side2, *to_line_list)],
                       *[to_draw.UnBorderThenFade(tex) for tex in Group(tex_VGroup[2: -4], tex_C)],
                       *[to_draw.UnGrowFromCenter(dot) for dot in Group(*dot_list, point)]]

        random.shuffle(random_list)

        self.play(AnimationGroup(*random_list, lag_ratio=.1))

        self.wait()

        self.play(*[to_draw.UnBorderThenFade(m) for m in Group(*p_list, line1, *tex_VGroup[0: 2], *tex_VGroup[-4: len(tex_VGroup)])])

        self.wait()

        self.add(self.captions_mob[7])
        self.remove(caption_mob[7])

    def change_cap(self):
        self.caps = ["$\\underset{\\text{(这只是一个例子, 真正尺规做乘除法运算不是这样)}}{\\text{如图, 我们想将AB平均分成n段($n \\in N_+$)}}$",
                     "首先, 作这条线段的平行线",
                     "然后, 如下操作进行n遍",
                     "这也演示了如何用尺规将一条线段伸长n倍",
                     "然后, 连接并延长$AQ_0$, $BQ_n$, 交于点C (如果没有交点, 则说明$Q_0Q_1=Q_1Q_2=...=Q_{n-1}Q_n={AB \\over n}$)",
                     "连接并延长$CQ_1, CQ_2, CQ_3...CQ_{n-1}$, 分别交$AB\\text{于点}P_1, P_2, P_3...P_{n-1}$",
                     "则$AP_1 = P_1P_2 = P_2P_3=...=P_{n-1}P_n=P_nB$",
                     "这样, 我们就成功地将一条线段等分成n段。",
                     "这说明, 我们可以用尺规做乘除整数运算, 当然, 真正用尺规作图作乘除法不是这样",
                     "只要如图就可以了, 不过方法都差不多, 我就不演示了"]


class SceneW3_1(SceneW3):

    def setup(self):
        self.set_cap()
        self.set_caption_on()

    def construct(self):
        caption_mob = self.captions_mob.copy()
        self.add(self.captions_mob[7])
        self.wait()
        self.play(ReplacementTransform(self.captions_mob[7], self.captions_mob[8]))
        self.add(caption_mob[8])
        self.remove(self.captions_mob[8])
        self.captions_mob = caption_mob

        self.wait(5.)

        self.play(ReplacementTransform(caption_mob[8], caption_mob[9]))

        dot_A = Dot(UL * 3).set_color("#99FFAB").set_plot_depth(20)
        dot_B = Dot(LEFT * (3 + (1 / 3)) + 2 * UP).set_color("#AAFFF7").set_plot_depth(20)
        dot_C = Dot(LEFT * 2.5 + 2 * UP).set_color("#5AC6FF").set_plot_depth(20)
        dot_D = Dot((4 + (1 / 3)) * LEFT - UP).set_color("#FFCB5C").set_plot_depth(20)
        dot_E = Dot(- UR).set_color("#CA9EFF").set_plot_depth(20)
        vg1 = VGroup(dot_A, dot_B, dot_C, dot_D, dot_E)

        line_AC = Line(dot_A.get_center(), dot_C.get_center()).set_color_by_gradient(dot_A.get_color(), dot_C.get_color())
        line_CB = Line(dot_C.get_center(), dot_B.get_center()).set_color_by_gradient(dot_C.get_color(), dot_B.get_color())
        line_BA = Line(dot_B.get_center(), dot_A.get_center()).set_color_by_gradient(dot_B.get_color(), dot_A.get_color())
        line_CE = Line(dot_C.get_center(), dot_E.get_center()).set_color_by_gradient(dot_C.get_color(), dot_E.get_color())
        line_BD = Line(dot_B.get_center(), dot_D.get_center()).set_color_by_gradient(dot_B.get_color(), dot_D.get_color())
        line_ED = Line(dot_E.get_center(), dot_D.get_center()).set_color_by_gradient(dot_E.get_color(), dot_D.get_color())
        vg2 = VGroup(line_AC, line_CB, line_BA, line_CE, line_BD, line_ED)

        tex_a_1 = TexMobject("a").scale(.7).next_to(line_BA, LEFT, buff=-SMALL_BUFF).set_color(line_BA.get_color())
        tex_1_1 = TexMobject("1").scale(.7).next_to(line_AC, RIGHT, buff=-SMALL_BUFF).set_color(line_AC.get_color())
        tex_b_1 = TexMobject("b").scale(.7).next_to(line_CE, RIGHT, buff=-SMALL_BUFF).set_color(line_CE.get_color())
        tex_ab_1 = TexMobject("ab").scale(.7).next_to(line_BD, LEFT, buff=-SMALL_BUFF).set_color(line_BD.get_color())
        vg3 = VGroup(tex_a_1, tex_1_1, tex_b_1, tex_ab_1)

        self.play(*[ShowCreation(line) for line in Group(line_AC, line_CB, line_BA)],
                  *[Write(i) for i in Group(dot_A, tex_a_1, tex_1_1)])

        self.wait()
        self.play(to_draw.UnWrite(caption_mob[9]))
        self.wait()

        self.play(ShowCreation(line_CE))
        self.wait()
        self.play(Write(dot_C))
        self.wait()
        self.play(Write(tex_b_1))
        self.wait()

        self.play(ShowCreation(line_ED))
        self.wait()
        self.play(Write(dot_E))
        self.wait()

        self.play(ShowCreation(line_BD))
        self.wait()
        self.play(Write(dot_D), Write(dot_B))
        self.wait()
        self.play(Write(tex_ab_1))

        self.wait()

        text_times = TextMobject("相乘").scale(.7).set_color_by_gradient(dot_A.get_color(),
                                                                       dot_B.get_color(), dot_C.get_color(),
                                                                       dot_D.get_color(), dot_E.get_color(),).\
            next_to(VGroup(vg1, vg2, vg3), DOWN)

        self.play(Write(text_times))

        vg4 = VGroup(vg1, vg2, vg3, text_times)

        POINT1 = vg4.get_center()
        VG_PAT = POINT2 = - POINT1

        self.play(vg4.move_to, ORIGIN)

        self.wait(3.)

        for x in [tex_a_1, tex_1_1, tex_b_1, tex_ab_1]:
            x.save_state()

        self.play(AnimationGroup(Flash(vg4, flash_radius=4, color=random_bright_color(), line_length=random.randint(5, 10)/10),
            AnimationGroup(ApplyMethod(text_times.become, TextMobject("相除").scale(.7).set_color_by_gradient(
            dot_A.get_color(), dot_B.get_color(), dot_C.get_color(), dot_D.get_color(), dot_E.get_color(),).
            next_to(VGroup(vg1, vg2, vg3), DOWN)),
            ApplyMethod(tex_b_1.become, TexMobject("{a \\over b}").scale(.7).next_to(line_CE, RIGHT, buff=-SMALL_BUFF).set_color(
                      line_CE.get_color())),
            ApplyMethod(tex_ab_1.become,
            TexMobject("a").scale(.7).next_to(line_BD, LEFT, buff=SMALL_BUFF).set_color(line_BD.get_color())),
            ApplyMethod(tex_a_1.become, TexMobject("b").scale(.7).next_to(line_BA, LEFT, buff=-SMALL_BUFF).set_color(
                      line_BA.get_color())), lag_ratio=.2))
        )
        self.wait(5.)
        self.play(tex_a_1.restore, tex_b_1.restore, tex_ab_1.restore)

        tex_b_1.add_updater(lambda _: tex_b_1.next_to(line_CE, RIGHT, buff=-SMALL_BUFF))
        tex_ab_1.add_updater(lambda _: tex_ab_1.next_to(line_BD, LEFT, buff=-SMALL_BUFF))

        line_CE.add_updater(lambda _: line_CE.become(
            Line(dot_C.get_center(), dot_E.get_center()).set_color_by_gradient(dot_C.get_color(),
                                                                               dot_E.get_color())))
        line_BD.add_updater(lambda _: line_BD.become(
            Line(dot_B.get_center(), dot_D.get_center()).set_color_by_gradient(dot_B.get_color(),
                                                                               dot_D.get_color())))

        line_ED.add_updater(lambda _: line_ED.become(
            Line(dot_E.get_center(), dot_D.get_center()).set_color_by_gradient(dot_E.get_color(),
                                                                               dot_D.get_color())))

        dec = ValueTracker(-1.)

        dot_E.add_updater(lambda _: dot_E.move_to(np.array([(dec.get_value() + 3) / (- 2), dec.get_value(), 0.]) + VG_PAT))
        dot_D.add_updater(lambda _: dot_D.move_to(np.array([(dec.get_value() - 12) / 3, dec.get_value(), 0.]) + VG_PAT))
        text_times.add_updater(lambda _: text_times.next_to(VGroup(vg1, vg2, vg3), DOWN))

        self.play(ApplyMethod(tex_b_1.become, TexMobject("a").scale(.7).next_to(line_CE, RIGHT, buff=-SMALL_BUFF)
                              .set_color(line_CE.get_color())),
                  ApplyMethod(tex_ab_1.become,
                              TexMobject("a^{2}").scale(.7).next_to(line_BD, LEFT, buff=-SMALL_BUFF).set_color(
                                  line_BD.get_color())),
                  AnimationGroup(
                ApplyMethod(text_times.become, TexMobject("\\underset{(\\text{就是$a \\times a$})}{\\text{平方}}").scale(.7)
                            .set_color_by_gradient(
                    dot_A.get_color(), dot_B.get_color(), dot_C.get_color(), dot_D.get_color(), dot_E.get_color(), ).
                            next_to(VGroup(vg1, vg2, vg3), DOWN)),
                ), lag_ratio=.5)

        self.play(AnimationGroup(
            Flash(vg4, flash_radius=4, color=random_bright_color(), line_length=random.randint(5, 10) / 10),
            ApplyMethod(dec.set_value, 1)),
            )

        self.wait(5.)

        self.play(to_draw.UnWrite(vg4))

        tex_b_1.clear_updaters()
        tex_ab_1.clear_updaters()
        line_CE.clear_updaters()
        line_BD.clear_updaters()
        line_ED.clear_updaters()
        dot_E.clear_updaters()
        dot_D.clear_updaters()
        text_times.clear_updaters()


class SceneW4(SceneW3):
    def setup(self):
        self.set_cap()
        self.set_caption_on()
        self.add_set()

    def add_set(self):
        pass

    def construct(self):
        line_1 = Line(LEFT * 3, RIGHT * 1).set_color("#29ABCA")
        line_2 = Line(RIGHT * 1, RIGHT * 3).set_color("#46CA87")
        line_3 = Line(RIGHT, np.array([1, 2 * np.sqrt(2.), 0])).set_color("#7485CA")
        cir = Circle(radius=3.).set_color(BLUE_B)
        dot_1 = Dot(RIGHT).set_color("37BAA8")

        a = SourceHansfont("a").next_to(line_1, DOWN).set_color("#29ABCA")
        a1 = SourceHansfont("1").next_to(line_2, DOWN).set_color("#46CA87")
        sqa = SourceHansfont("√a").next_to(line_3).set_color("#7485CA")
        sqa[1].shift(LEFT * .25)

        self.play(ShowCreation(line_1))
        self.wait()

        self.play(ShowCreation(line_2))
        self.wait()

        self.play(ShowCreation(cir))

        self.play(Write(dot_1))
        self.wait()

        self.play(ShowCreation(line_3))
        self.wait()

        self.play(*[Write(tex) for tex in [a, a1]])
        self.wait(2.)

        self.play(ReplacementTransform(Group(a.copy(), a1.copy()), sqa))
        self.wait(2.)

        self.wait()

        self.play(to_draw.UnWriteRandom(VGroup(line_1, line_2, line_3, cir, dot_1, a, a1, sqa)))
        self.wait(1)





class SceneB_1(BacB):
    def setup(self):
        self.set_cap()
        self.set_tex_cap()
        self.set_caption_tex_on()
        self.set_caption_on()
        self.set_up_1()

    def set_up_1(self):
        self.set_scene_captions()

    def construct(self):
        SceneCaption = self.SceneCaption.copy().scale(.7)
        cir = Circle(radius=2.).set_color("#89F3FF")
        Dot_P = Dot(np.array([3., 0., 0.]))
        Dot_O = Dot().set_color("#89F3FF")
        line_OP = Line(Dot_O.get_center(), Dot_P.get_center())
        Dot_A = Dot(RIGHT * 2)
        k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir, Dot_P.get_center())
        point_B, point_P = return_two_point(k2, b2, 4. / 3., 3.)
        point_D, o = return_two_point(k1, b1, 4. / 3., 3.)
        Dot_B = Dot(point_B).set_color("#88D0FF")
        Dot_D = Dot(point_D).set_color(Dot_B.get_color())

        line_OB = Line(Dot_O.get_center(), Dot_B.get_center()).set_plot_depth(2)
        line_PB = Line(Dot_P.get_center(), Dot_B.get_center()).set_plot_depth(3)
        line_PD = Line(Dot_P.get_center(), Dot_D.get_center()).set_plot_depth(2)

        tex_O = TexMobject("O").set_color(Dot_O.get_color()).scale(.7).next_to(Dot_O, DL, buff=SMALL_BUFF)
        tex_A = TexMobject("A").set_color(Dot_A.get_color()).scale(.7).next_to(Dot_A, DR, buff=SMALL_BUFF)
        tex_P = TexMobject("P").set_color(Dot_P.get_color()).scale(.7).next_to(Dot_P, RIGHT, buff=SMALL_BUFF)
        tex_B = TexMobject("B").set_color(Dot_B.get_color()).scale(.7).next_to(Dot_B, UR, buff=SMALL_BUFF)
        tex_D = TexMobject("D").set_color(Dot_D.get_color()).scale(.7).next_to(Dot_D, DR, buff=SMALL_BUFF)

        self.wait()
        self.play(*[FadeIn(mob) for mob in Group(cir, Dot_O, tex_O, Dot_P, tex_P)])
        self.wait()

        self.play(ShowCreation(line_OP))
        self.wait()

        self.play(*[FadeIn(m) for m in Group(Dot_B, tex_B)])
        self.wait()
        self.play(*[ShowCreation(line) for line in Group(line_OB, line_PB)])
        self.wait()

        self.play(Write(NaOH(self.captions_mob[0])))

        self.wait(4.)

        self.play(Write(Dot_A.set_color("#DD6D76")), Write(tex_A.set_color("#DD6D76")))

        tex_1 = SourceHansfont("1").scale(.7).set_color("#8CD3DD").next_to(KCl(Dot_O, Dot_B), UL, buff=-LARGE_BUFF)
        tex_2 = SourceHansfont("1").scale(.7).set_color("#8CD3DD").next_to(KCl(Dot_O, Dot_A), DOWN, buff=SMALL_BUFF)
        tex_3 = SourceHansfont("a").scale(.7).set_color("#DDCC95").next_to(KCl(Dot_A, Dot_P), DOWN, buff=SMALL_BUFF)

        self.wait()
        self.play(FadeIn(VGroup(tex_1, tex_2, tex_3)))

        self.wait()
        self.play(ReplacementTransform(self.captions_mob[0], NaOH(self.captions_tex_mob[0])))

        self.wait()

        NaOH(SceneCaption, s=0)

        for ind in range(3):
            self.play(Write(SceneCaption[ind]))
            self.wait()

        self.wait(2.)
        self.play(ReplacementTransform(self.captions_tex_mob[0], NaOH(self.captions_mob[1])))

        self.SceneCaption_n1_0_3 = SceneCaption_n1_0_3 = SceneCaption[-1][0][3:].copy()

        self.play(SceneCaption_n1_0_3.next_to, KCl(Dot_P, Dot_B), UR, {"buff": -MED_LARGE_BUFF})
        self.wait()

        cir_BP = Circle(arc_center=Dot_P.get_center(), radius=length_of_two_point(Dot_B.get_center(), Dot_P.get_center())).set_color(["#58C4DD", "#9EDDB0"])
        self.play(ShowCreation(cir_BP))

        self.wait()

        self.play(Write(VGroup(Dot_D, tex_D)))

        self.wait()

        self.play(ShowCreation(line_PD))

        self.wait()

        self.play(ShowCreation(KCl(Dot_O, Dot_D)))

        self.wait()

        self.play(ReplacementTransform(self.captions_mob[1], NaOH(self.captions_mob[2])))

    def change_cap(self):
        self.caps = ["既然∠OBP=90°, 我们不妨设OA=OB=1, AP=a",
                     "这样, 只知道OA和AP就可以用尺规作图作出PB了...",
                     "所以?简单吗"
                     ]

    def set_tex_cap(self):
        self.tex_caps = ["$OB^2+PB^2=OP^2$",]

    def set_caption_tex_on(self, t2c={}):
        self.captions_tex_mob = VGroup(
            *[
                TextMobject(cap, tex_to_color_map=t2c).set_color(WHITE).to_edge(DOWN * 1.2).scale(.7)
                .add_background_rectangle(color=BLACK, buff=0.1, opacity=0.85)
                for cap in self.tex_caps
            ]
        )

    def set_scene_captions(self):
        scececap = [r"1^2+BP^2=(1+a)^2",
                    r"1+BP^2=a^2+2a+1",
                    r"BP=\sqrt{a^2+2a}"]

        self.SceneCaption = VGroup(
            *[
                TexMobject(cap)
                for cap in scececap
            ]
        )
        self.set_cap_pos(self.SceneCaption, direction=DOWN, buff=MED_LARGE_BUFF)
        self.SceneCaption.move_to(LEFT * 4 + UP)

    @staticmethod
    def set_cap_pos(captions, **kwargs):
        for x in range(0, len(captions) - 1):
            captions[x + 1].next_to(captions[x], **kwargs)
        return captions[:].copy()


class it_Is_Not_Easy(SceneB_1):
    def construct(self):
        physics = ImageMobject("physics").scale(3.).shift(UP).rotate(90 * DEGREES)
        self.play(FadeIn(physics))
        self.wait(2.)
        physics_angry = NaOH(TextMobject("物理: WDNMB").next_to(physics, DOWN), 0, "#29ABCA", "#8D5630", "#58C4DD", "#C59978", "#ACE2EE", "#E2CCBC")
        self.play(Write(physics_angry))
        self.wait(3.)

        self.play(to_draw.UnWrite(physics_angry), FadeOut(physics))
        self.wait(2.)


class SceneC_1(SceneB_1):

    CONFIG = {
        "TrackPath": Circle(radius=3.),
        "config": None
    }

    def construct(self):

        cir = Circle(radius=2.).set_color("#89F3FF")
        Dot_P = Dot(np.array([3., 0., 0.]))
        Dot_O = Dot().set_color("#89F3FF")

        Dot_A = Dot(RIGHT * 2).set_color("#DD6D76")
        k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir, Dot_P.get_center())
        point_B, point_P = return_two_point(k2, b2, 4. / 3., 3.)
        point_D, o = return_two_point(k1, b1, 4. / 3., 3.)
        Dot_B = Dot(point_B).set_color("#88D0FF")
        Dot_D = Dot(point_D).set_color(Dot_B.get_color())
        all_dot = VGroup(Dot_A, Dot_B, Dot_P, Dot_O, Dot_D,)

        line_OP = Line(Dot_O.get_center(), Dot_P.get_center()).add_updater(lambda line: line.become(Line(Dot_O.get_center(), Dot_P.get_center())))
        line_OB = Line(Dot_O.get_center(), Dot_B.get_center()).add_updater(lambda line: line.become(Line(Dot_O.get_center(), Dot_B.get_center())))
        line_OD = Line(Dot_O.get_center(), Dot_D.get_center()).add_updater(lambda line: line.become(Line(Dot_O.get_center(), Dot_D.get_center())))
        line_PB = Line(Dot_P.get_center(), Dot_B.get_center()).add_updater(lambda line: line.become(Line(Dot_P.get_center(), Dot_B.get_center(), color="#5CDDC7")))
        line_PD = Line(Dot_P.get_center(), Dot_D.get_center()).add_updater(lambda line: line.become(Line(Dot_P.get_center(), Dot_D.get_center(), color="#58C4DD")))
        line_all = VGroup(line_OP, line_OB, line_PB, line_PD, line_OD)

        tex_O = TexMobject("O").set_color(Dot_O.get_color()).scale(.7).add_updater(lambda tex: tex.next_to(Dot_O, DL, buff=SMALL_BUFF))
        tex_A = TexMobject("A").set_color(Dot_A.get_color()).scale(.7).add_updater(lambda tex: tex.next_to(Dot_A, DR, buff=SMALL_BUFF))
        tex_P = TexMobject("P").set_color(Dot_P.get_color()).scale(.7).add_updater(lambda tex: tex.next_to(Dot_P, RIGHT, buff=SMALL_BUFF))
        tex_B = TexMobject("B").set_color(Dot_B.get_color()).scale(.7).add_updater(lambda tex: tex.next_to(Dot_B, UR, buff=SMALL_BUFF))
        tex_D = TexMobject("D").set_color(Dot_D.get_color()).scale(.7).add_updater(lambda tex: tex.next_to(Dot_D, DR, buff=SMALL_BUFF))
        tex_all = VGroup(tex_O, tex_A, tex_P, tex_B, tex_D)

        vg = VGroup()

        self.i = 1
        def anim(dot_p, alpha):
            Dot_P.move_to(self.TrackPath.point_from_proportion(alpha))

            angle = arg_angle(ORIGIN, Dot_P.get_center())
            Dot_A.move_to(2 * UP * np.sin(angle) + 2 * RIGHT * np.cos(angle))
            k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir, Dot_P.get_center(), clear=True)
            Dot_D.become(Dot(return_point(k1, b1, return_r_and_line(2, k1, b1, float64=1e-5)[0][0])).set_color("#88D0FF"))
            Dot_B.become(Dot(return_point(k2, b2, return_r_and_line(2, k2, b2, float64=1e-5)[0][0])).set_color("#88D0FF"))

            if self.i % 3 == 0:
                vg.add(line_PD.copy().clear_updaters().set_stroke(width=1)).add(line_PB.copy().clear_updaters().set_stroke(width=1))
            self.i += 1

        self.add(Dot_P, Dot_A.set_plot_depth(100), Dot_B, Dot_D, line_all, cir, tex_all, vg)

        if self.config:
            self.play(UpdateFromAlphaFunc(Dot_P, anim), **self.config)

        else:
            self.play(UpdateFromAlphaFunc(Dot_P, anim), run_time=6., rate_func=linear)
            self.wait()
        self.ad()

    def ad(self):
        pass


class SceneC_1_1(SceneC_1):
    CONFIG = {
        "TrackPath": Square(side_length=5.),
        # "config": None
    }


class SceneC_1_2(SceneC_1):
    CONFIG = {
        "TrackPath": FunctionGraph(lambda p: np.cos(p / 2) * 2),
        "config": {"run_time": 6., "rate_func": smooth}
    }

    def set_up_1(self):
        self.add(NaOH(TexMobject(r"y=\cos(x)").to_corner(UR, 0.5).shift(DOWN * .5), s=0))


class SceneC_1_3(SceneC_1):
    CONFIG = {
        "TrackPath": SVGMobject("coin")[0].scale(5.5),
        "config": {"run_time": 25, "rate_func": linear}
    }


class SceneC_1_3_1(SceneC_1):
    CONFIG = {
        "TrackPath": SVGMobject("coin")[0].scale(5.5),
        "config": {"run_time": 25, "rate_func": linear}
    }

    def set_up_1(self):
        self.add(SVGMobject("coin")[0].scale(5.5).set_color("#67C0DD").set_opacity(.7))


class unComfortable(SceneW4):
    def construct(self):
        SceneCap = self.SceneCaption
        captions_mob = self.captions_mob.copy()
        captions_tex_mob = self.captions_tex_mob.copy()

        self.play(Write(NaOH(captions_tex_mob[0], 1, BLACK, WHITE)))
        self.wait(3.)

        self.play(ReplacementTransform(captions_tex_mob[0], NaOH(captions_mob[0])))
        self.wait(4.)

        self.play(Write(NaOH(SceneCap[0], s=0)), to_draw.WriteRandom(*NaOH(SceneCap[1], s=0)))
        self.wait()
        self.play(ReplacementTransform(captions_mob[0], NaOH(captions_mob[1].shift(LEFT * 1.5))))
        self.wait(5.)
        self.play(to_draw.RandomSpinToNothing(Group(*SceneCap[0][0], *SceneCap[1][0])), run_time=5.)
        self.wait()

    def change_cap(self):
        self.caps = ["如果你想纯粹用代数去解, 我提前把答案算出来了",
                     "                我想, 这些公式告诉我们, 在指针飞转, 技巧快速更替的今天,\n 我们还能坐下来, 用丑陋的公式维持秩序, 何尝不是一种满足?"
                     ]

    def set_tex_cap(self):
        self.tex_caps = ["这里还有更美的!", ]

    def set_caption_tex_on(self, t2c={}):
        self.captions_tex_mob = VGroup(
            *[
                TextMobject(cap, tex_to_color_map=t2c).set_color(BLACK).to_edge(DOWN * 1.2).scale(.7)
                    .add_background_rectangle(color=Color("#fff"), buff=0.1, opacity=0.85)
                for cap in self.tex_caps
            ]
        )

    @staticmethod
    def set_cap_pos(captions, **kwargs):
        for x in range(0, len(captions) - 1):
            captions[x + 1].next_to(captions[x], **kwargs)
        return captions[:].copy()

    def set_caption_on(self, t2c={}):
        self.captions_mob = VGroup(
            *[
                SourceHansfont(cap, tex_to_color_map=t2c).to_edge(DOWN * 1.2)
                .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85).scale(.7)
                for cap in self.caps
            ]
        )

    def set_scene_captions(self):
        scececap = [r"\text{过圆}x^2+y^2=r^2\text{和圆外一点}(p, q)\text{与圆相切的直线}l\text{的解析式为:}",
                    r"\begin{cases}y = {pq \pm r\sqrt{p^2+q^2-r^2} \over p^2 - r^2}x-{pq \pm r\sqrt{p^2+q^2-r^2}"
                    r" \over p^2 - r^2}p+q \qquad \qquad (p \ne \pm r) \\ \quad \\ y = {q^2-r^2 \over 2pq}x-{q^2-r^2 \over 2q}"
                    r" + q \qquad \qquad \qquad \qquad \qquad \qquad (p^2 -r^2 = 0)\end{cases}"]

        self.SceneCaption = VGroup(
            *[
                TexMobject(cap)
                for cap in scececap
            ]
        )

        self.set_cap_pos(self.SceneCaption, direction=DOWN, buff=MED_LARGE_BUFF)
        self.SceneCaption.move_to(LEFT * 1 - UP * -.5).scale(.7)

    def add_con_before(self):
        pass

    def add_const_after(self):
        pass

    def add_set(self):
        self.add_con_before()
        self.set_scene_captions()
        self.set_tex_cap()
        self.set_caption_tex_on()
        self.add_const_after()


class some_others(BacB):
    def construct(self):

        cir = Circle(radius=2.).set_color("#89F3FF")
        Dot_P = Dot(np.array([3., 0., 0.]))
        Dot_O = Dot().set_color("#89F3FF")
        Dot_middle = Dot(RIGHT * 1.5)
        line_OP = Line(Dot_O.get_center(), Dot_P.get_center())
        Dot_A = Dot(RIGHT * 2)
        k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir, Dot_P.get_center())
        point_B, point_P = return_two_point(k2, b2, 4. / 3., 3.)
        point_D, o = return_two_point(k1, b1, 4. / 3., 3.)
        Dot_B = Dot(point_B).set_color("#88D0FF")
        Dot_D = Dot(point_D).set_color(Dot_B.get_color())

        cir_middle = Circle(arc_center=RIGHT * 1.5, radius=1.5).set_color([BLACK, WHITE])

        line_OB = Line(Dot_O.get_center(), Dot_B.get_center()).set_plot_depth(2)
        line_OD = Line(Dot_O.get_center(), Dot_D.get_center())
        line_PB = Line(Dot_P.get_center(), Dot_B.get_center(), color="#5CDDC7").set_plot_depth(3)
        line_PD = Line(Dot_P.get_center(), Dot_D.get_center(), color="#58C4DD").set_plot_depth(2)

        tex_O = TexMobject("O").set_color(Dot_O.get_color()).scale(.7).next_to(Dot_O, DL, buff=SMALL_BUFF)
        tex_H = TexMobject("H").set_color(Dot_A.get_color()).scale(.7).next_to(Dot_middle, DOWN, buff=SMALL_BUFF)
        tex_P = TexMobject("P").set_color(Dot_P.get_color()).scale(.7).next_to(Dot_P, RIGHT, buff=SMALL_BUFF)
        tex_B = TexMobject("B").set_color(Dot_B.get_color()).scale(.7).next_to(Dot_B, UR, buff=SMALL_BUFF)
        tex_D = TexMobject("D").set_color(Dot_D.get_color()).scale(.7).next_to(Dot_D, DR, buff=SMALL_BUFF)
        self.add(cir, Dot_P, Dot_O, tex_O, tex_P)
        self.wait()

        self.play(ShowCreation(line_OP))
        self.wait()

        self.play(*[Write(obtex) for obtex in Group(Dot_middle, tex_H)])
        self.wait()

        self.play(ShowCreation(cir_middle))
        self.wait()

        self.play(*[Write(obtex) for obtex in Group(Dot_B.set_opacity(0.6), tex_B, Dot_D.set_opacity(0.6), tex_D)])
        self.wait()

        self.play(*[ShowCreation(line) for line in Group(line_PB, line_PD)])
        self.wait()

        self.play(*[ShowCreation(line) for line in Group(line_OD, line_OB)])
        self.wait(2.)

        self.play(Uncreate(cir_middle))
        self.wait()


# class SceneC_1_4(SceneC_1):
#     CONFIG = {
#         "TrackPath": PiCreature[0].scale(5.5),
#         "config": {"run_time": 25, "rate_func": linear}
#     }
#
#     def set_up_1(self):
#         self.add(SVGMobject("coin")[0].scale(5.5).set_color("#67C0DD").set_opacity(.7))

class that_MK(BacW):
    def construct(self):
        logo = ManimKindergarten.Logo(size=4.5, add_bg_square=True, black_bg=False)

        self.add(logo[0].set_opacity(0.))
        for x in range(4):
            for y in range(3):
                self.add(logo[x + 1][y])
                self.wait(.5)
        self.wait()


class make_tangent_of_mk(BacW):

    def construct(self):

        logo = ManimKindergarten.Logo(size=4.5, add_bg_square=True, black_bg=False)

        self.add(logo[0].set_opacity(0.))
        cir = Circle(radius=2.).shift(DOWN * buff).set_color("#89F3FF")
        Dot_P = Dot(np.array([3., 0., 0.]), color=BLACK)
        Dot_O = Dot().move_to(cir.get_center()).set_color("#89F3FF")

        Dot_A = Dot(RIGHT * 2).set_color("#DD6D76")
        k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir, Dot_P.get_center())
        point_B, point_P = return_two_point(k2, b2, 4. / 3., 3.)
        point_D, o = return_two_point(k1, b1, 4. / 3., 3.)
        Dot_B = Dot(point_B).set_color("#88D0FF")
        Dot_D = Dot(point_D).set_color(Dot_B.get_color())
        all_dot = VGroup(Dot_A, Dot_B, Dot_P, Dot_O, Dot_D, )

        line_OP = Line(Dot_O.get_center(), Dot_P.get_center()).add_updater(
            lambda line: line.become(Line(Dot_O.get_center(), Dot_P.get_center()).set_color(BLACK)))
        line_PB = Line(Dot_P.get_center(), Dot_B.get_center()).add_updater(
            lambda line: line.become(Line(Dot_P.get_center(), Dot_B.get_center(), color="#5CDDC7")))
        line_PD = Line(Dot_P.get_center(), Dot_D.get_center()).add_updater(
            lambda line: line.become(Line(Dot_P.get_center(), Dot_D.get_center(), color="#58C4DD")))
        line_all = VGroup(line_OP, line_PB, line_PD)

        tex_O = TexMobject("O").set_color(Dot_O.get_color()).scale(.7).add_updater(
            lambda tex: tex.next_to(Dot_O, DL, buff=SMALL_BUFF))
        tex_A = TexMobject("A").set_color(Dot_A.get_color()).scale(.7).add_updater(
            lambda tex: tex.next_to(Dot_A, DR, buff=SMALL_BUFF))
        tex_P = TexMobject("P").set_color(Dot_P.get_color()).scale(.7).add_updater(
            lambda tex: tex.next_to(Dot_P, RIGHT, buff=SMALL_BUFF))
        tex_B = TexMobject("B").set_color(Dot_B.get_color()).scale(.7).add_updater(
            lambda tex: tex.next_to(Dot_B, UR, buff=SMALL_BUFF))
        tex_D = TexMobject("D").set_color(Dot_D.get_color()).scale(.7).add_updater(
            lambda tex: tex.next_to(Dot_D, DR, buff=SMALL_BUFF))
        tex_all = VGroup(tex_O, tex_A, tex_P, tex_B, tex_D)

        vg = VGroup()

        mk = mkVG()

        self.i = 1

        def anim(dot_p, alpha):
            Dot_P.move_to(self.TrackPath.point_from_proportion(alpha))

            angle = arg_angle(ORIGIN + cir.get_center(), Dot_P.get_center())
            Dot_A.move_to(2 * UP * np.sin(angle) + 2 * RIGHT * np.cos(angle) + cir.get_center())
            k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir.copy().move_to(ORIGIN), Dot_P.get_center() - cir.get_center(), clear=True)
            Dot_D.become(
                Dot(return_point(k1, b1, return_r_and_line(2, k1, b1, float64=1e-5)[0][0])).set_color("#88D0FF")).shift(cir.get_center())
            Dot_B.become(
                Dot(return_point(k2, b2, return_r_and_line(2, k2, b2, float64=1e-5)[0][0])).set_color("#88D0FF")).shift(cir.get_center())

            if self.i % 6 == 0:
                vg.add(line_PD.copy().clear_updaters().set_stroke(width=1)).add(
                    line_PB.copy().clear_updaters().set_stroke(width=1))
            self.i += 1
            self.add(vg)

        self.add(Dot_P, Dot_A.set_plot_depth(100), Dot_B, Dot_D, line_all, cir, tex_all, vg)

        def for_up_anim(dot):
            angle = arg_angle(ORIGIN + cir.get_center(), Dot_P.get_center())
            Dot_A.move_to(2 * UP * np.sin(angle) + 2 * RIGHT * np.cos(angle) + cir.get_center())
            k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir.copy().move_to(ORIGIN),
                                                                                  Dot_P.get_center() - cir.get_center(),
                                                                                  clear=True)
            Dot_D.become(
                Dot(return_point(k1, b1, return_r_and_line(2, k1, b1, float64=1e-5)[0][0])).set_color("#88D0FF")).shift(
                cir.get_center())
            Dot_B.become(
                Dot(return_point(k2, b2, return_r_and_line(2, k2, b2, float64=1e-5)[0][0])).set_color("#88D0FF")).shift(
                cir.get_center())

        for x in range(4):
            for y in range(3):
                self.TrackPath = logo[x + 1][y]
                mk.add(self.TrackPath.copy().set_opacity(.0))
                self.add(mk[-1])
                self.play(UpdateFromAlphaFunc(Dot_P, anim), run_time=1.2)
                self.play(mk[-1].set_opacity, 1.)
                if (x, y) != (3, 2):
                    if y < 2:
                        Dot_P.add_updater(for_up_anim)
                        self.nextOne = logo[x + 1][y + 1]
                        self.play(Dot_P.move_to, self.nextOne.point_from_proportion(0), rate_func=smooth)
                        Dot_P.clear_updaters()
            circ = mkVG(Dot_P, Dot_A, Dot_B, Dot_D, line_all, cir, tex_all, Dot_O)
            if x == 0:
                Dot_P.add_updater(for_up_anim)
                self.play(circ.move_to, (LEFT * buff), run_time=2)

            elif x == 1:
                Dot_P.add_updater(for_up_anim)
                self.play(circ.move_to, (UP * buff), run_time=2)

            elif x == 2:
                Dot_P.add_updater(for_up_anim)
                self.play(circ.move_to, (RIGHT * buff), run_time=2)

            else:
                break
            self.nextOne = logo[x + 2][0]
            self.play(Dot_P.move_to, self.nextOne.point_from_proportion(0), rate_func=smooth)
            Dot_P.clear_updaters()


        self.wait()


class WHITEBOARD(BacW):
    def construct(self):
        pass


class BLACKBOARD(BacB):
    def construct(self):
        pass


class how_to_work(TeacherStudentsScene):
    CONFIG = {

    }

    def construct(self):
        self.student_says(SourceHansfont("所以,\n 那又有什么用呢"), student_index=1)
        self.wait()
        tex_1 = TexMobject(r"\sqrt{x^2+2x}")
        tex_2 = TexMobject(r"\frac{2}{3}a")
        tex_3 = TexMobject(r"{\sqrt{5} - 1 \over 2}")

        self.student_thinks(tex_1, student_index=2)
        self.student_thinks(tex_2, student_index=1)
        self.student_thinks(tex_3, student_index=0)
        self.wait()

        self.teacher_says(SourceHansfont("尺规作图可以作\n加法、减法、乘法、除法、开平方和平方运算！"))
        self.wait()

        self.student_thinks(NONE, student_index=1)
        compass = ImageMobject("compass").move_to(NONE).scale(.7)
        self.play(FadeIn(compass))
        self.wait(2.)


class blackgroundBLUE(Scene):
    def construct(self):
        rect = Rectangle(height=FRAME_HEIGHT, width=FRAME_WIDTH, color=BLUE_B, fill_color=WHITE, fill_opacity=1.).\
            set_stroke(width=34.)
        self.add(rect)
        self.pl(rect, GREEN)
        self.pl(rect, ["#C09575", BLUE])
        self.pl(rect, ["#29ABCA", PURPLE])
        self.pl(rect, ["#C59978", "#58C4DD", "#ACE2EE", "#29ABCA"], run_time=2.)
        self.pl(rect, BLUE_B, rate_func=smooth)

    def pl(self, rect, color, **kwargs):
        self.play(rect.set_stroke, color, **kwargs)


class Why_This(TeacherStudentsScene):
    def construct(self):
        self.student_says(NaOH(SourceHansfont("既然有简单的方法尺规作图, 为什么要用这种方法呢"), 0, "#29ABCA", "#58C4DD", "#ACE2EE"), student_index=0)
        self.wait(2.5)

        self.teacher_says(NaOH(SourceHansfont("因为它们有特别的意义...."), 0, "#8D5630", "#C59978", "#E2CCBC"))
        self.wait()


class The_17_cos(Scene):
    def construct(self):
        thecos = NaOH(TexMobject(r"\cos \left(\frac{2 \pi}{17}\right)=-\frac{1}{16}+\frac{1}{16} \sqrt{17}+\frac{1}{16} \sqrt{2 \cdot 17-2 \sqrt{17}}+\frac{1}{8} \sqrt{17+3 \sqrt{17}-\sqrt{2 \cdot 17-2 \sqrt{17}}-2 \sqrt{2 \cdot 17+2 \sqrt{17}}}").scale(.5).shift(UP), 0, "#29ABCA", "#8D5630", "#58C4DD", "#C59978", "#ACE2EE", "#E2CCBC")
        RegularPolygonOf17 = RegularPolygon(17, fill_color=BLUE).set_opacity(.7).next_to(thecos, DOWN)
        self.play(Write(thecos))
        self.wait(3.)

        self.play(ShowCreation(RegularPolygonOf17))

        self.wait(2.)

        self.play(Uncreate(RegularPolygonOf17, run_time=3.), to_draw.UnWrite(thecos))
        self.wait()


class End(BacB):

    def construct(self):
        end = SourceHansfont("视频制作&解说 ———— bilibili.洛洛洛-洛洛洛_dx\n"
                             "视频剪辑  ———— bilibili.zhengyang051119\n"
                             "bgm     ———— Alexis Ffrench - Close Reality、 I'll Fly Away、 \nKindred Spirit、 Redemption")

        end = NaOH(end.move_to(ORIGIN).shift(UP), s=0)

        cir = Circle(radius=2.).shift(DOWN * buff).set_color("#89F3FF")
        Dot_P = Dot(np.array([3., 0., 0.]))
        Dot_O = Dot().move_to(cir.get_center()).set_color("#89F3FF")

        Dot_A = Dot(RIGHT * 2).set_color("#DD6D76")
        k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir, Dot_P.get_center())
        point_B, point_P = return_two_point(k2, b2, 4. / 3., 3.)
        point_D, o = return_two_point(k1, b1, 4. / 3., 3.)
        Dot_B = Dot(point_B).set_color("#88D0FF")
        Dot_D = Dot(point_D).set_color(Dot_B.get_color())
        all_dot = VGroup(Dot_A, Dot_B, Dot_P, Dot_O, Dot_D, )

        line_OP = Line(Dot_O.get_center(), Dot_P.get_center()).add_updater(
            lambda line: line.become(Line(Dot_O.get_center(), Dot_P.get_center())))
        line_PB = Line(Dot_P.get_center(), Dot_B.get_center()).add_updater(
            lambda line: line.become(Line(Dot_P.get_center(), Dot_B.get_center(), color="#5CDDC7")))
        line_PD = Line(Dot_P.get_center(), Dot_D.get_center()).add_updater(
            lambda line: line.become(Line(Dot_P.get_center(), Dot_D.get_center(), color="#58C4DD")))
        line_all = VGroup(line_OP, line_PB, line_PD)

        tex_O = TexMobject("O").set_color(Dot_O.get_color()).scale(.7).add_updater(
            lambda tex: tex.next_to(Dot_O, DL, buff=SMALL_BUFF))
        tex_A = TexMobject("A").set_color(Dot_A.get_color()).scale(.7).add_updater(
            lambda tex: tex.next_to(Dot_A, DR, buff=SMALL_BUFF))
        tex_P = TexMobject("P").set_color(Dot_P.get_color()).scale(.7).add_updater(
            lambda tex: tex.next_to(Dot_P, RIGHT, buff=SMALL_BUFF))
        tex_B = TexMobject("B").set_color(Dot_B.get_color()).scale(.7).add_updater(
            lambda tex: tex.next_to(Dot_B, UR, buff=SMALL_BUFF))
        tex_D = TexMobject("D").set_color(Dot_D.get_color()).scale(.7).add_updater(
            lambda tex: tex.next_to(Dot_D, DR, buff=SMALL_BUFF))
        tex_all = VGroup(tex_O, tex_A, tex_P, tex_B, tex_D)

        vg = VGroup()

        mk = mkVG()

        self.i = 1

        def anim(dot_p, alpha):
            Dot_P.move_to(self.TrackPath.point_from_proportion(alpha))

            angle = arg_angle(ORIGIN + cir.get_center(), Dot_P.get_center())
            Dot_A.move_to(2 * UP * np.sin(angle) + 2 * RIGHT * np.cos(angle) + cir.get_center())
            k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir.copy().move_to(ORIGIN), Dot_P.get_center() - cir.get_center(), clear=True)
            Dot_D.become(
                Dot(return_point(k1, b1, return_r_and_line(2, k1, b1, float64=1e-5)[0][0])).set_color("#88D0FF")).shift(cir.get_center())
            Dot_B.become(
                Dot(return_point(k2, b2, return_r_and_line(2, k2, b2, float64=1e-5)[0][0])).set_color("#88D0FF")).shift(cir.get_center())

            if self.i % 6 == 0:
                vg.add(line_PD.copy().clear_updaters().set_stroke(width=1)).add(
                    line_PB.copy().clear_updaters().set_stroke(width=1))
            self.i += 1
            self.add(vg)

        self.add(Dot_P, Dot_A.set_plot_depth(100), Dot_B, Dot_D, line_all, cir, tex_all, vg)

        def for_up_anim(dot, dt):
            angle = arg_angle(ORIGIN + cir.get_center(), Dot_P.get_center())
            Dot_A.move_to(2 * UP * np.sin(angle) + 2 * RIGHT * np.cos(angle) + cir.get_center())
            k1, k2, b1, b2 = return_the_2ks_and_2bs_about_unit_circlesTangentLine(cir.copy().move_to(ORIGIN),
                                                                                  Dot_P.get_center() - cir.get_center(),
                                                                                  clear=True)
            Dot_D.become(
                Dot(return_point(k1, b1, return_r_and_line(2, k1, b1, float64=1e-5)[0][0])).set_color("#88D0FF")).shift(
                cir.get_center())
            Dot_B.become(
                Dot(return_point(k2, b2, return_r_and_line(2, k2, b2, float64=1e-5)[0][0])).set_color("#88D0FF")).shift(
                cir.get_center())

        for x in range(len(end)):
            self.TrackPath = end[x]
            mk.add(self.TrackPath.copy().set_opacity(.0))
            self.add(mk[-1])
            self.play(UpdateFromAlphaFunc(Dot_P, anim), run_time=.2)
            self.play(mk[-1].set_opacity, 1., run_time=.2)
            if x < 2:
                Dot_P.add_updater(for_up_anim)
                self.nextOne = end[x + 1]
                self.play(Dot_P.move_to, self.nextOne.point_from_proportion(0), rate_func=smooth, run_time=.1)
                Dot_P.clear_updaters()

        # end
