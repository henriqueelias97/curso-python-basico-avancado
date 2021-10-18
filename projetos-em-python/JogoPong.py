import turtle

janela = turtle.Screen()
janela.title("Jogo Pong")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

#Pontuação

pont_a = 0
pont_b = 0

# Barra 1
Barra1 = turtle.Turtle()
Barra1.speed(0)
Barra1.shape("square")
Barra1.color("white")
Barra1.shapesize(stretch_wid=5, stretch_len=1)
Barra1.penup()
Barra1.goto(-350, 0)

# Barra 2
Barra2 = turtle.Turtle()
Barra2.speed(0)
Barra2.shape("square")
Barra2.color("white")
Barra2.shapesize(stretch_wid=5, stretch_len=1)
Barra2.penup()
Barra2.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 2
bola.dy = -2


#Funções
def Barra1_cima():
    y = Barra1.ycor()
    y += 20
    Barra1.sety(y)

def Barra1_baixo():
    y = Barra1.ycor()
    y -= 20
    Barra1.sety(y)

def Barra2_cima():
    y = Barra2.ycor()
    y += 20
    Barra2.sety(y)

def Barra2_baixo():
    y = Barra2.ycor()
    y -= 20
    Barra2.sety(y)

# Pontuação

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Jogador A: 0 Jogador B: 0", align ="center", font =("Courier", 24, "normal"))

#Operações do Telcado
janela.listen()
janela.onkeypress(Barra1_cima, "w")
janela.onkeypress(Barra1_baixo, "s")
janela.onkeypress(Barra2_cima, "Up")
janela.onkeypress(Barra2_baixo, "Down")

#loop para o jogo
while True:
    janela.update()

#Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

#Limites para bola
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        pont_a += 1
        pen.clear()
        pen.write(f"Jogador A: {pont_a} Jogador B: {pont_b}", align="center", font=("Courier", 24, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        pont_b += 1
        pen.clear()
        pen.write(f"Jogador A: {pont_a} Jogador B: {pont_a}", align="center", font=("Courier", 24, "normal"))


#Relação bola e direcionais
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < Barra2.ycor() + 40 and bola.ycor() > Barra2.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() < -350) and (bola.ycor() < Barra1.ycor() + 40 and bola.ycor() > Barra1.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1



