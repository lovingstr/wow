from manimlib.imports import *
from luoluoluo_useful.imports import *
from manim_sandbox.utils.scenes.bilibili import *


class VarThetaCreatureScene(PiCreatureScene):
    CONFIG = {"file_name_prefix": "VarThetaCreature"}


class SourceHansfont(Text):
    CONFIG = {
        "font": "思源黑体",
    }


class coord_and_functions(GraphScene):
    CONFIG = {
        "x_min": -8,
        "y_min": -5,
        "x_max": 8,
        "y_max": 5,
        "graph_origin": ORIGIN
    }

    def construct(self):
        self.setupBeforevideo()
        caption_mob = self.captions_mob
        self.play(Write(caption_mob[0]))
        self.play(Write(self.Tex1))

        self.play(Write(self.SceneCaption[0]))

        self.wait(3.)

        self.play(to_draw.RandomSpinFromNothing(*self.SceneCaption[1]))

        self.wait(3.)

        self.play(to_draw.RandomGrowFromNothing(*self.SceneCaption[2]))
        self.wait(3.)

        self.play(to_draw.WriteRandom(*self.SceneCaption[3]))
        self.wait(5.)

        self.play(to_draw.UnWriteRandom(VGroup(*[self.SceneCaption[index][0][indexx]
                                               for index in range(4)
                                               for indexx in range(len(self.SceneCaption[index][0]))]
                                               )
                                        ))

        self.wait(3.)

        self.play(ReplacementTransform(caption_mob[0], caption_mob[1]))

        self.play(ApplyMethod(self.Tex1.restore))

        self.setup_axes(animate=1)

        self.wait()

        func_1 = self.get_graph(lambda x: np.exp(x), color="#76DDBC")
        func_10 = self.get_graph(lambda x: x + 1, color="#ACE2EE")

        self.play(ShowCreation(func_1))

        self.wait(3.)

        self.play(ShowCreation(func_10))

        self.wait()

        label_1 = self.get_graph_label(func_1, label="e^x", direction=LEFT)
        label_10 = self.get_graph_label(func_10, label="x+1", direction=DR, x_val=3.)
        TEXT1_for = self.instead_next_toTrans(TexMobject("e^x"), self.Tex1[0][0: 2][:])
        TEXT2_for = self.instead_next_toTrans(TexMobject("x+1"), self.Tex1[0][3: 6][:])
        self.play(
            *[ReplacementTransform(be, af)
              for be, af in zip((TEXT1_for, TEXT2_for), (label_1, label_10))]
        )

        self.wait()

        line_to_moke_t = Line().set_style(stroke_color="#ACE2EE")
        x_vau_num = ValueTracker(-3)

        line_to_moke_t.add_updater(self.return_func_t(func_1, x_vau_num))
        self.play(Write(line_to_moke_t))
        self.wait(2.)

        self.play(x_vau_num.set_value, 0, run_time=8., rate_func=lambda t: 1 - rush_into(1 - rush_from(t)))
        line_to_moke_t.clear_updaters()
        self.play(ReplacementTransform(caption_mob[1], caption_mob[2]))
        self.wait(3.)

        so_ = TexMobject(r"\frac{\mathrm{d}}{\mathrm{d}x}e^x(0)=0+1").set_color_by_gradient("#44F5D0", "#82F58E", "#F5AEDB").to_edge(DOWN, 2.)
        self.play(Write(so_))
        self.wait()

        self.play(Flash(so_))
        self.wait(4.)

        self.play(to_draw.UnWrite(so_))

        func_20 = self.get_graph(lambda x: x-1).set_color("#F585B4")
        func_21 = self.get_graph(lambda x: np.log(x), x_min=.03, x_max=16).set_color("#98F5ED")
        label_20 = self.get_graph_label(func_20, "x-1")
        label_21 = self.get_graph_label(func_21, "\\ln(x)")

        self.wait(2.)

        self.play(ReplacementTransform(func_10.copy(), func_20), ReplacementTransform(label_1.copy(), label_20))
        self.wait(2.)

        self.play(ShowCreation(func_21), ReplacementTransform(label_10.copy(), label_21))
        self.wait(2.)

        self.play(ReplacementTransform(caption_mob[2], caption_mob[3]))
        self.wait(2.)

        at_same = TexMobject("\\ln(x)\\ge x-1").set_color_by_gradient("#98F5ED", "#F5ABDC").next_to(so_)

        self.play(Write(at_same))

        self.play(ReplacementTransform(caption_mob[3], caption_mob[4]))

        self.wait(3.)

        self.play(at_same.move_to, self.Tex1, self.Tex1.set_opacity, 0.)
        line_to_moke_t__ = Line().set_style(stroke_color="#F585B4")
        x_vau_num = ValueTracker(3.)
        line_to_moke_t__.add_updater(self.return_func_t(func_21, x_vau_num))
        self.play(Write(line_to_moke_t__))

        self.wait(2.)
        sc_value = self.space_unit_to_x
        self.play(x_vau_num.set_value, 1. * sc_value, run_time=8., rate_func=lambda t: 1 - rush_into(1 - rush_from(t)))
        print(at_same.get_center())
        line_to_moke_t__.clear_updaters()
        self.remove(line_to_moke_t__)

    def set_constant(self):
        pass

    def return_func_t(self, func, x_vau_num, dx=.01):
        dx = dx
        ptc = self.point_to_coords

        def animation1(mob):
            k = (self.input_to_graph_point(ptc(np.array([x_vau_num.get_value() + dx, 0., 0.]))[0], func)[1]
                 - self.input_to_graph_point(ptc(np.array([x_vau_num.get_value(), 0, 0.]))[0], func)[1]) / dx
            p1, p2 = return_two_point(k, - k * x_vau_num.get_value() +
                                      self.input_to_graph_point(ptc(np.array([x_vau_num.get_value(), 0., 0.]))[0],
                                                                func)[1],
                                      x_vau_num.get_value() - 3, x_vau_num.get_value() + 3)
            print(p1, p2, k)
            mob.put_start_and_end_on(p1, p2)

        return animation1

    @staticmethod
    def instead_next_toTrans(mob, to_instead):
        mob.match_style(to_instead).match_width(to_instead).move_to(to_instead)
        return mob

    def setupBeforevideo(self):
        self.set_constant()
        self.set_cap()

        self.change_cap()
        self.Tex1 = TexMobject(r"e^x\ge x+1").to_edge(UL, buff=LARGE_BUFF)
        self.Tex2 = TexMobject(r"\ln(x)\le x-1")
        self.Tex1[0][0:2].set_color("#76DDBC")
        self.Tex1[0][3:6].set_color("#ACE2EE")
        self.Tex1.save_state().move_to(UP * 2)
        self.set_scene_captions()
        self.set_caption_on()

    def change_cap(self):
        self.data = (
                     [[0, 3], "#B7C2EE"], [[0, 4], "#B7C2EE"], [[0, 5], "#B7C2EE"], [[0, 6], "#B7C2EE"],
                     [[0, 8], "#76DDBC"], [[0, 9], "#76DDBC"], [[0, 10], "#ACE2EE"], [[0, 11], "#ACE2EE"],
                     [[0, 12], "#ACE2EE"], [[0, 13], "#ACE2EE"], [[0, 15], "#8670F5"], [[0, 16], "#8670F5"],
                     [[0, 17], "#8670F5"], [[0, 18], "#8670F5"], [[0, 19], "#8670F5"], [[0, 21], "#76DDBC"],
                     [[0, 22], "#76DDBC"], [[0, 23], "#ACE2EE"], [[0, 24], "#ACE2EE"],

                     [[1, 0], "#8670F5"], [[1, 1], "#8670F5"], [[1, 2], "#8670F5"], [[1, 3], "#8670F5"],
                     [[1, 4], "#8670F5"], [[1, 6], "#9DF5A9"], [[1, 7], "#9DF5A9"], [[1, 8], "#9DF5A9"],
                     [[1, 10], "#9DF5A9"], [[1, 11], "#9DF5A9"], [[1, 12], "#9DF5A9"], [[1, 15], "#9DF5A9"],
                     [[1, 16], "#9DF5A9"], [[1, 17], "#9DF5A9"], [[1, 19], "#9DF5A9"], [[1, 20], "#9DF5A9"],
                     [[1, 21], "#9DF5A9"],

                     [[2, 1], "#B7C2EE"], [[2, 2], "#B7C2EE"], [[2, 3], "#F59ED4"], [[2, 4], "#B7C2EE"],
                     [[2, 5], "#B7E3F5"], [[2, 6], "#B7E3F5"], [[2, 7], "#B7E3F5"], [[2, 9], "#B7C2EE"],
                     [[2, 10], "#B7C2EE"], [[2, 11], "#F59ED4"], [[2, 12], "#B7C2EE"], [[2, 14], "#F59ED4"],

                     [[3, 1], "#B7C2EE"], [[3, 2], "#B7C2EE"], [[3, 3], "#F59ED4"], [[3, 4], "#B7C2EE"],
                     [[3, 6], "#F59ED4"], [[3, 9], "#B7C2EE"], [[3, 10], "#B7C2EE"], [[3, 12], "#ACE2EE"],
                     [[3, 13], "#ACE2EE"], [[3, 14], "#ACE2EE"],
                     )

    def set_cap(self):
        self.caps = ["首先, 我们先把这个简单的不等式证明一遍",
                     "我们可以尝试用直观图像理解",
                     "显然, 函数y=x+1是y=exp(x)在x=0处的切线, 即",
                     "同理, 我们也可以得到:",
                     "请你尝试证明它吧"]
        self.change_cap()

    def set_caption_on(self):
        self.captions_mob = VGroup(
            *[
                SourceHansfont(cap).to_edge(DOWN * 1.2).scale(.7)
                .set_color_by_gradient("#65E2FF", "#5DFF77", "#FFF470", "#50B2FF", "#D6BAFF", "#66ccff")
                .add_background_rectangle(color="", buff=0.1, opacity=0.85)
                for cap in self.caps
            ]
        )

    def set_scene_captions(self):
        scececap = [r"\text{设函数}f(x)=e^x -x-1 ,f'(x)=e^x -1",
                    r" f'(x)\text{在$x<0$处小于$0$},\text{在$x>0$处大于$0$}  ",
                    r"\therefore f(x)_{\min}=f(0)=0",
                    r"\therefore f(x) \ge 0, \text{即}e^x \ge x+1 ",
                    r""]

        self.SceneCaption = VGroup(
            *[
                TexMobject(cap)
                for cap in scececap
            ]
        )
        self.set_cap_pos(self.SceneCaption, direction=DOWN, buff=MED_LARGE_BUFF)
        self.SceneCaption.next_to(self.Tex1, DOWN)

        self.set_color(self.SceneCaption, self.data)

    def set_cap_pos(self, captions, **kwargs):
        for x in range(0, len(captions) - 1):
            captions[x + 1].next_to(captions[x], **kwargs)
        return captions[:].copy()

    def set_color(self, mob, data):
        for item in data:
            mob[item[0][0]][0][item[0][1]].set_color(item[1])


class The_next_Scene(coord_and_functions):
    CONFIG = {}

    def setupBeforevideo(self):
        self.set_constant()
        self.set_cap()

        self.change_cap()
        self.set_caption_on()
        self.mob()

    def mob(self):
        tex = TexMobject("\\ln(x)\\ge x-1").set_color_by_gradient("#98F5ED", "#F5ABDC").move_to(self.be_coords_array)
        self.mobjects.insert(0, tex)

    def set_constant(self):
        self.be_coords_array = [-4.94471791,  2.7787667,   0.]

    def construct(self):

        V = VG = VGroup

        self.setupBeforevideo()
        captions_mob = self.captions_mob.copy()

        self.play(Write(captions_mob[0]))

        self.wait()
        forTex = self.mobjects[0]
        self.play(forTex.move_to, ORIGIN)
        self.wait()

        self.funcG = FunctionGraph(lambda x: np.log(x), x_min=.5). \
            set_color(["#65E2FF", "#5DFF77", "#FFF470", "#50B2FF", "#D6BAFF", "#66ccff"])
        label = TexMobject("\\ln(x)").set_color(["#98F5ED", "#F5ABDC"]).next_to(self.funcG, UL).shift(DR * 5.)

        self.play(ReplacementTransform(captions_mob[0], self.captions_mob[1]))

        self.funcG1 = FunctionGraph(lambda x: x-1, x_min=-2.5, x_max=3.5). \
            set_color(["#65E2FF", "#5DFF77", "#FFF470", "#50B2FF", "#D6BAFF", "#66ccff"])
        label2 = TexMobject("x-1").set_color(["#98F5ED", "#F5ABDC"]).next_to(self.funcG1, UL).shift(DR * 5.)

        self.wait(2.)

        self.play(ReplacementTransform(VG(self.captions_mob[1], forTex),
                                       V(self.funcG, label, self.funcG1, label2)))
        t = random.randint(3, 5)
        self.wait(t)
        self.wait()

        self.play(to_draw.RandomUnGrowFromCenter(V(*self.funcG, *label[0], *self.funcG1, *label2[0])))

    def set_cap(self):
        self.caps = [
            "显然, 直观的图像有利于理解",
            "这就是所谓的\'数形结合\'"
        ]


class VarTheta_Saying(VarThetaCreatureScene):
    CONFIG = {

    }

    def set_color(self, mob, colors=None, *color):
        if colors in [None]:
            mob.set_color_by_gradient(*["#65E2FF", "#5DFF77", "#FFF470", "#50B2FF", "#D6BAFF", "#66ccff"])
            return mob
        mob.set_color_by_gradient(colors, *color)
        return mob

    def construct(self):
        V = VGroup
        tex = TexMobject("\\ln(x)\\ge x-1").set_color_by_gradient("#98F5ED", "#F5ABDC")
        text = self.set_color(SourceHansfont("我们是可以用求导简单证明出来, 但是总是感觉少了什么...").next_to(tex, DOWN))
        text2 = self.set_color(SourceHansfont("数学直觉!"), "#1BD7DD", "#95DD71", "#8ADD16", "#84D1DD", "#CFDD7C")
        self.blink()
        self.wait()
        self.say(V(tex, text))
        self.say(text2)
        self.funcG = FunctionGraph(lambda x: np.log(x), x_min=.5).\
            set_color(["#65E2FF", "#5DFF77", "#FFF470", "#50B2FF", "#D6BAFF", "#66ccff"])
        label = TexMobject("\\ln(x)").set_color(["#98F5ED", "#F5ABDC"]).next_to(self.funcG, UL).shift(DR * 5.)

        fun = V(self.funcG, label)

        self.wait()

        self.play(Write(fun.shift(LEFT * 2)))

        self.wait()

        Mob = Square().move_to(UR*6).set_opacity(0.)
        self.add(Mob)

        self.pi_creature.add_updater(lambda pi: pi.look_at(Mob))

        self.play(Rotating(Mob, about_point=self.pi_creature.get_center()), run_time=8, radians=15, rate_func=smooth)

        self.wait(2.)


class end(TripleScene2):
    def setup(self):
        self.wait()
        text = SourceHansfont("视频作者: 洛洛洛-洛洛洛_dx     \n\n\nbgm:Alexis Ffrench - Subtract & Verde")\
            .set_color_by_gradient("#42C5FF", "#54FDFF")

        self.play(Write(text))
        self.wait(3.)
        self.play(to_draw.SpinOutToNothing(text=text))
