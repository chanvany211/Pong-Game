import turtle as tl

class PONG:
    def __init__(self):
        self.create_window()
        self.create_paddles()
        self.create_ball()
        self.create_score()
        self.keys()

    def create_window(self):
        self.root = tl.Screen()
        self.root.title("PONG GAME")
        self.root.bgcolor("yellow")
        self.root.setup(width=600, height=400)
        self.root.tracer(0)

    def create_paddles(self):
        # Left paddle
        self.left_paddle = tl.Turtle()
        self.left_paddle.speed(0)
        self.left_paddle.shape("square")
        self.left_paddle.color("red")
        self.left_paddle.shapesize(stretch_wid=7, stretch_len=1.2)
        self.left_paddle.penup()
        self.left_paddle.goto(-260, 0)

        # Right paddle
        self.right_paddle = tl.Turtle()
        self.right_paddle.speed(0)
        self.right_paddle.shape("square")
        self.right_paddle.color("white")
        self.right_paddle.shapesize(stretch_wid=7, stretch_len=1.2)
        self.right_paddle.penup()
        self.right_paddle.goto(260, 0)

    def create_ball(self):
        self.ball = tl.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("green")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 0.10
        self.ball.dy = 0.10

    def create_score(self):
        self.left_score = 0
        self.right_score = 0

        self.score_display = tl.Turtle()
        self.score_display.speed(0)
        self.score_display.color("black")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 160)
        self.update_score()

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(
            f"{self.left_score}    |    {self.right_score}",
            align="center",
            font=("Arial", 20, "bold")
        )

    # Paddle movement
    def left_paddle_up(self):
        y = self.left_paddle.ycor()
        if y < 150:
            self.left_paddle.sety(y + 100)

    def left_paddle_down(self):
        y = self.left_paddle.ycor()
        if y > -150:
            self.left_paddle.sety(y - 100)

    def right_paddle_up(self):
        y = self.right_paddle.ycor()
        if y < 150:
            self.right_paddle.sety(y + 100)

    def right_paddle_down(self):
        y = self.right_paddle.ycor()
        if y > -150:
            self.right_paddle.sety(y - 100)

    def keys(self):
        self.root.listen()
        self.root.onkeypress(self.left_paddle_up, "w")
        self.root.onkeypress(self.left_paddle_down, "s")
        self.root.onkeypress(self.right_paddle_up, "Up")
        self.root.onkeypress(self.right_paddle_down, "Down")

    def game(self):
        while True:
            self.root.update()

            # Move ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # Top/bottom bounce
            if self.ball.ycor() > 180:
                self.ball.sety(180)
                self.ball.dy *= -1

            if self.ball.ycor() < -180:
                self.ball.sety(-180)
                self.ball.dy *= -1

            # Right wall → left scores
            if self.ball.xcor() > 290:
                self.left_score += 1
                self.update_score()
                self.ball.goto(0, 0)
                self.ball.dx *= -1

            # Left wall → right scores
            if self.ball.xcor() < -290:
                self.right_score += 1
                self.update_score()
                self.ball.goto(0, 0)
                self.ball.dx *= -1

            # Paddle collision (right)
            if (250 < self.ball.xcor() < 270 and
                self.right_paddle.ycor() - 70 < self.ball.ycor() < self.right_paddle.ycor() + 70):
                self.ball.setx(250)
                self.ball.dx *= -1

            # Paddle collision (left)
            if (-270 < self.ball.xcor() < -250 and
                self.left_paddle.ycor() - 70 < self.ball.ycor() < self.left_paddle.ycor() + 70):
                self.ball.setx(-250)
                self.ball.dx *= -1


# Run game
pong = PONG()
pong.game()