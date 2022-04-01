import turtle
import random
import operator

jenik = turtle
screen = jenik.Screen()
screen.screensize(800, 800)

canvas_size_x = 20
canvas_size_y = canvas_size_x
screen.setworldcoordinates(0, 0, canvas_size_x, canvas_size_y)
size_of_play_field = 15
jenik.speed(0)
jenik.hideturtle()

# draw grid
for i in range(16):
    jenik.penup()
    jenik.goto((canvas_size_x-size_of_play_field)/2 + i, (canvas_size_y-size_of_play_field)/2)
    jenik.pendown()
    jenik.goto((canvas_size_x-size_of_play_field)/2 + i, (canvas_size_y-size_of_play_field)/2 + size_of_play_field)
for i in range(16):
    jenik.penup()
    jenik.goto((canvas_size_x-size_of_play_field)/2, (canvas_size_x-size_of_play_field)/2 + i)
    jenik.pendown()
    jenik.goto((canvas_size_y-size_of_play_field)/2 + size_of_play_field, (canvas_size_x-size_of_play_field)/2 + i)

# draw labels
font_size = 10
for i in range(15):
    jenik.penup()
    jenik.goto(
        (canvas_size_x-size_of_play_field - 1)/2,
        (canvas_size_y-size_of_play_field)/2 + i + 0.5 - font_size/2/10/2)
    jenik.write(i+1, move=False, align="center", font=("Arial", font_size, "normal"))
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(15):
    jenik.penup()
    jenik.goto(
        (canvas_size_x-size_of_play_field)/2 + i + 0.5,
        (canvas_size_y-size_of_play_field - 1.5)/2)
    jenik.write(alphabet[i].upper(), move=False, align="center", font=("Arial", font_size, "normal"))

# onclick draw shapes


def round_number_to_middle(num):
    if round(num) < num:
        num = round(num)+0.5
    else:
        num = round(num) - 0.5
    return num


padding = 0.2


def draw_cicrcle(x, y):
    circle_radius = (1-padding*2)/2
    y = y - 0.5 + (1-circle_radius*2)/2
    fill_color = "blue"
    jenik.pencolor(fill_color)
    jenik.pensize(3.5)

    jenik.penup()
    jenik.goto(x, y)
    jenik.pendown()
    jenik.circle(circle_radius)


def draw_x_shape(x, y):
    x_shape_radius = (1-padding*2)/2
    fill_color = "red"
    jenik.pencolor(fill_color)
    jenik.pensize(3.5)

    jenik.penup()
    jenik.goto(x-x_shape_radius, y-x_shape_radius)
    jenik.pendown()
    jenik.goto(x+x_shape_radius, y+x_shape_radius)
    jenik.penup()
    jenik.goto(x-x_shape_radius, y+x_shape_radius)
    jenik.pendown()
    jenik.goto(x+x_shape_radius, y-x_shape_radius)


list_of_op_for_columns = [
    operator.add,
    operator.add,
    operator.add,
    0,
    operator.sub,
    operator.sub(),
    operator.sub
    0,
]


def check_columns(list_, symbol: int = 0, y: int = 0, x: int = 0, count=0):
    curr_x = x+1
    curr_y = y+1
    column_count = 0
    operation = list_of_op_for_columns[count]
    # check if on edge
    if count == 2 or count == 6:
        curr_y = operation(curr_y, 1)
    elif count == 0 or count == 4:
        curr_x = operation(curr_x, 1)



    for i in range(len(field)):
        print(field[len(field)-i-1])
    print(operation, curr_x, curr_y, field[curr_y - 1][curr_x - 1])
    # circle = 1
    # x = 2
    print(field[curr_y-1][curr_x-1], symbol)
    print(field[curr_y-1][curr_x-1] == symbol)
    while field[curr_y-1][curr_x-1] == symbol:
        if count % 2 == 0:
            curr_y = operation(curr_y, 1)
        else:
            curr_x = operation(curr_x, 1)
        column_count += 1
    if column_count == 4:
        if symbol == 1:
            symbol_string = "circles"
        else:
            symbol_string = "crosses"
        print("!!!!!!!!!!!!!!!!!!!!           {} won                  !!!!!!!!!!!!!!!!!!!!!!!!!!!!".format(symbol_string))
        return 0
    if count < 7:
        count += 1
        check_columns(list_, symbol, y, x, count)

    print("\n\n")


start = 1
turn = 0
field = []
for i in range(15):
    field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def play(x, y):
    global start, turn, field
    if start:
        start = 0
        turn = random.randint(0, 1)

    if round_number_to_middle(x) < x:
        x = round_number_to_middle(x) + 0.5
    else:
        x = round_number_to_middle(x) - 0.5
    if round_number_to_middle(y) < y:
        y = round_number_to_middle(y) + 0.5
    else:
        y = round_number_to_middle(y) - 0.5

    x = int(x)
    y = int(y)

    x_on_field = x-3
    y_on_field = y-3

    if field[y_on_field][x_on_field] == 0:
        if turn:
            # x_shapes
            # is represented by 2 in field

            draw_x_shape(x, y)

            field[y_on_field][x_on_field] = 2

            if check_columns(field, 2, y_on_field, x_on_field):
                print("x won")
            turn = 0

        else:
            # circle
            # is represented by 1 in field

            draw_cicrcle(x, y)

            field[y_on_field][x_on_field] = 1

            if check_columns(field, 1, y_on_field, x_on_field):
                print("circles won")
            turn = 1

        # print(x, y, x_on_field, y_on_field, "\n")
        # for i in range(len(field)):
        #     print(field[len(field)-i-1])


screen.onclick(play)

screen.mainloop()

# TODO SWAP, 2, without - optional

turtle.done()
