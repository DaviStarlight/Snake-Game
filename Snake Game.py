import turtle
import random

# @davi_starlight
WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 10
DELAY = 100

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset():
    global snake, snake_direction, food_pos, pen, score, game_running
    game_running = True  # Controla o estado do jogo
    snake = [[0, 0], [0, 20], [0, 40], [0, 50], [0, 60]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    score = 0  # Reinicia a pontuação
    update_score()  # Atualiza o score na tela
    move_snake()

def move_snake():
    global snake_direction, game_running

    if not game_running:
        return  # Para o movimento se o jogo acabou

    # Próxima posição para cabeça da cobra.
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_direction][0]
    new_head[1] = snake[-1][1] + offsets[snake_direction][1]

    # Checa a colisão própria.
    if new_head in snake[:-1]:
        game_over()
        return
    else:
        snake.append(new_head)
        if not food_collision():
            snake.pop(0)  # Mantém a cobra no mesmo tamanho se não for alimentada.

        # Permitir quebra de tela
        if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
        elif snake[-1][0] < - WIDTH / 2:
            snake[-1][0] += WIDTH
        elif snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
        elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT

        # Limpa as marcas anteriores da cobra
        pen.clearstamps()

        # Desenha a cobra
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        # Atualiza a tela
        screen.update()

        # Enxaguar e repetir
        turtle.ontimer(move_snake, DELAY)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        change_food_color()  # Muda a cor da comida quando ela respawnar
        score += 10  # Incrementa a pontuação
        update_score()  # Atualiza o score na tela
        return True
    return False

def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# Função para mudar a cor da comida
def change_food_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    food.color(r, g, b)

# Atualiza a pontuação na tela
def update_score():
    score_pen.clear()
    score_pen.write(f"Pontuação: {score}", align="center", font=("Arial", 16, "bold"))

# Função para mostrar "Game Over"
def game_over():
    global game_running
    game_running = False  # Interrompe o movimento da cobra
    pen.clearstamps()  # Limpa o desenho da cobra
    pen.goto(0, 0)
    pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
    screen.update()
    turtle.ontimer(reset, 3000)  # Reinicia o jogo após 3 segundos

# Tela
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.colormode(255)  # Modo de cor RGB

# Cor da Cobra
pen = turtle.Turtle("square")
pen.penup()
pen.fillcolor("gold")

# Comida
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Score display
score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.color("white")
score_pen.goto(0, HEIGHT // 2 - 40)
update_score()

# Manipuladores de Eventos
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Bora lá!
reset()
turtle.done()
