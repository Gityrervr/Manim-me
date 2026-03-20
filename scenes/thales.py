from manim import *

class ThalesTheorem(Scene):
    def construct(self):

        # ── Title ────────────────────────────────────
        title = Text("Thales' Theorem", font_size=56, color=BLUE)
        subtitle = Text(
            "The angle in a semicircle is always 90°",
            font_size=28, color=GRAY
        ).next_to(title, DOWN)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP*0.3))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── Setup circle and diameter ─────────────────
        circle = Circle(radius=2.5, color=BLUE, stroke_width=3)

        A = circle.point_at_angle(PI)
        B = circle.point_at_angle(0)
        O = ORIGIN

        diameter  = Line(A, B, color=YELLOW, stroke_width=4)
        label_A   = MathTex("A", color=YELLOW, font_size=36).next_to(A, LEFT*0.8)
        label_B   = MathTex("B", color=YELLOW, font_size=36).next_to(B, RIGHT*0.8)
        label_O   = MathTex("O", color=WHITE,  font_size=28).next_to(O, DOWN*0.4)
        center_dot = Dot(O, color=WHITE, radius=0.07)

        self.play(Create(circle), run_time=1.5)
        self.play(
            Create(diameter),
            Write(label_A), Write(label_B),
            FadeIn(center_dot), Write(label_O),
            run_time=1.2
        )
        self.wait(0.5)

        # ── Introduce point P ─────────────────────────
        P_tracker = ValueTracker(PI / 2)

        def get_P():
            return circle.point_at_angle(P_tracker.get_value())

        P_dot = always_redraw(lambda:
            Dot(get_P(), color=GREEN, radius=0.12))
        label_P = always_redraw(lambda:
            MathTex("P", color=GREEN, font_size=36)
            .next_to(get_P(), normalize(get_P()) * 0.6))

        AP = always_redraw(lambda:
            Line(A, get_P(), color=GREEN, stroke_width=3))
        BP = always_redraw(lambda:
            Line(B, get_P(), color=ORANGE, stroke_width=3))

        self.play(FadeIn(P_dot), Write(label_P), run_time=0.8)
        self.play(Create(AP), Create(BP), run_time=1)
        self.wait(0.5)

        # ── Right angle marker at P ───────────────────
        angle_mark = always_redraw(lambda:
            RightAngle(
                Line(get_P(), A),
                Line(get_P(), B),
                length=0.22,
                color=RED,
                stroke_width=2
            )
        )
        angle_label = always_redraw(lambda:
            MathTex(r"90^\circ", color=RED, font_size=28)
            .move_to(get_P() + normalize(O - get_P()) * 0.55)
        )

        self.play(Create(angle_mark), Write(angle_label), run_time=1)
        self.wait(0.5)

        # ── Show equation ─────────────────────────────
        eq = MathTex(
            r"\angle APB = 90^\circ",
            font_size=42, color=WHITE
        ).to_edge(UP, buff=0.3)
        self.play(Write(eq), run_time=1)
        self.wait(0.5)

        # ── Move P around the circle ──────────────────
        note = Text(
            "Watch — P moves but the angle stays 90°!",
            font_size=24, color=GRAY
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note, shift=UP*0.2))

        self.play(
            P_tracker.animate.set_value(PI * 0.15),
            run_time=5, rate_func=smooth
        )
        self.play(
            P_tracker.animate.set_value(PI * 1.85),
            run_time=6, rate_func=smooth
        )
        self.play(
            P_tracker.animate.set_value(PI / 2),
            run_time=3, rate_func=smooth
        )
        self.wait(0.5)

        # ── Proof sketch ──────────────────────────────
        self.play(FadeOut(note))
        proof_title = Text("Why?  (Proof)", font_size=32, color=YELLOW)\
            .to_corner(DR, buff=0.4).shift(UP*3)

        # Draw radii OA OP OB
        OA = Line(O, A, color=YELLOW, stroke_width=2, stroke_opacity=0.6)
        OP = always_redraw(lambda:
            Line(O, get_P(), color=WHITE, stroke_width=2, stroke_opacity=0.6))
        OB = Line(O, B, color=YELLOW, stroke_width=2, stroke_opacity=0.6)

        self.play(
            Create(OA), Create(OP), Create(OB),
            Write(proof_title),
            run_time=1
        )

        steps = VGroup(
            MathTex(r"\bullet\ OA = OB = OP\ (\text{radii})",
                    font_size=24, color=WHITE),
            MathTex(r"\bullet\ \triangle OAP\ \text{isosceles}\ \Rightarrow \angle OAP = \angle OPA = \alpha",
                    font_size=24, color=GREEN),
            MathTex(r"\bullet\ \triangle OBP\ \text{isosceles}\ \Rightarrow \angle OBP = \angle OPB = \beta",
                    font_size=24, color=ORANGE),
            MathTex(r"\bullet\ \text{Angles in }\ \triangle APB:\ 2\alpha + 2\beta = 180^\circ",
                    font_size=24, color=WHITE),
            MathTex(r"\therefore\ \angle APB = \alpha + \beta = 90^\circ \quad \blacksquare",
                    font_size=28, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)\
         .to_corner(DR, buff=0.4)

        for step in steps:
            self.play(Write(step), run_time=0.8)
            self.wait(0.3)

        self.wait(1)

        # ── Final highlight ───────────────────────────
        box = SurroundingRectangle(eq, color=YELLOW, buff=0.15)
        self.play(Create(box))
        self.play(Flash(box, color=YELLOW, flash_radius=0.6))
        self.wait(2)
