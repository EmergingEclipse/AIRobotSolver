from roboid import *
import turtle

hamster = HamsterS()

column = 15
row = 15
orientation = 2
position = [13, 3]
wheelspeed = 86
turnspeed = 35
waitvar = 760
map



# creates the global variables used in the program
def instantiate():
    global orientation
    orientation = 1
    global position
    position = [5, 9]
    global map

    map = [[2 for _ in range(15)] for _ in range(15)]
    for i in range(15):
        map[0][i] = 1
        map[14][i] = 1
        map[i][0] = 1
        map[i][14] = 1

    checkWallCurrentNodeUp()
    checkWallCurrentNodeRight()
    map[5][9] = 0


def getOrientation():
    global orientation
    return orientation


def getMap():
    global map
    return map


# updates sensor values
def checker():
    global L
    L = hamster.left_proximity()
    global R
    R = hamster.right_proximity()


def turnCorrecter():
    checker()
    Diff = L - R
    if Diff > 12 or Diff < 12:
        return
    while Diff > 3 or Diff < -3:
        if Diff > 4:
            hamster.turn_right(Diff / 2, 60)
        if Diff < -4:
            hamster.turn_left(-Diff / 2, 60)
        checker()
        Diff = L - R


#scans the walls left and right from the robot by facing right and checking sensor data
#this function will adjust to make the robot face the necisary direction based on its current orientation
def checkWallCurrentNodeUp():
    orientation = getOrientation()
    if orientation == 0:
        checkwallsFacingUp()
    if orientation == 2:
        turnLeft()
        checkwallsFacingUp()
        turnRight()

    if orientation == 3:
        hamster.turn_left(180, 60)
        checkwallsFacingUp()
        hamster.turn_right(180, 60)
    if orientation == 1:
        turnRight()
        checkwallsFacingUp()
        turnLeft()

#scans the walls up and down from the robot by facing right and checking sensor data
#this function will adjust to make the robot face the necisary direction based on its current orientation
def checkWallCurrentNodeRight():
    global L
    checker()
    if True:
        orientation = getOrientation()
        if orientation == 0:
            turnRight()
            checkWallsFacingRight()
            turnLeft()
        if orientation == 2:
            checkWallsFacingRight()
        if orientation == 3:
            turnLeft()
            checkWallsFacingRight()
            turnRight()
        if orientation == 1:
            checker()
            if L > 50:
                hamster.turn_right(180, 60)
                checkWallsFacingRight()
                hamster.turn_left(180, 60)

            hamster.turn_left(180, 60)
            checkWallsFacingRight()
            hamster.turn_right(180, 60)

#this method changes the orientation of the robot
def setOrientation(turn):
    # 0 up, 2 right, 3 down, 1 left
    global orientation
    if turn == "right":
        if orientation == 1:
            orientation = 0
        elif orientation == 2:
            orientation = 3
        elif orientation == 3:
            orientation = 1
        else:
            orientation = 2
    if turn == "left":
        if orientation == 1:
            orientation = 3
        elif orientation == 2:
            orientation = 0
        elif orientation == 3:
            orientation = 2
        else:
            orientation = 1

#plays a victory song when completing the maze
def victory():
    # https://www.irish-folk-songs.com/never-gonna-give-you-up-easy-sheet-music-and-piano-letter-notes.html
    # sheet music for the song I programmed in
    hamster.note(hamster.NOTE_D_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_G_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_B_5)
    wait(325)
    hamster.note(hamster.NOTE_OFF)
    wait(50)
    hamster.note(hamster.NOTE_B_5)
    wait(375)
    hamster.note(hamster.NOTE_A_5)
    wait(700)
    hamster.note(hamster.NOTE_D_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_G_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_A_5)
    wait(200)
    hamster.note(hamster.NOTE_OFF)
    wait(175)
    hamster.note(hamster.NOTE_A_5)
    wait(375)
    hamster.note(hamster.NOTE_G_5)
    wait(375)
    hamster.note(hamster.NOTE_F_SHARP_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(250)
    # DEDEGAF#DDAGDEGEBBA
    hamster.note(hamster.NOTE_D_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_D_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_G_5)
    wait(500)
    hamster.note(hamster.NOTE_A_5)
    wait(250)
    hamster.note(hamster.NOTE_F_SHARP_5)
    wait(375)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_D_5)
    wait(150)
    hamster.note(hamster.NOTE_OFF)
    wait(100)
    hamster.note(hamster.NOTE_D_5)
    wait(150)
    hamster.note(hamster.NOTE_OFF)
    wait(100)
    hamster.note(hamster.NOTE_D_5)
    wait(250)
    hamster.note(hamster.NOTE_A_5)
    wait(500)
    hamster.note(hamster.NOTE_G_5)
    wait(1000)
    hamster.note(hamster.NOTE_D_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_G_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_B_5)
    wait(250)
    hamster.note(hamster.NOTE_OFF)
    wait(100)
    hamster.note(hamster.NOTE_B_5)
    wait(375)
    hamster.note(hamster.NOTE_A_5)
    wait(650)
    hamster.note(hamster.NOTE_OFF)
    wait(100)
    # DEGEdF#GDEGEGAF#DAG
    hamster.note(hamster.NOTE_D_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_G_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_D_6)
    wait(500)
    hamster.note(hamster.NOTE_F_SHARP_5)
    wait(250)
    hamster.note(hamster.NOTE_G_5)
    wait(375)
    hamster.note(hamster.NOTE_F_SHARP_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(250)
    hamster.note(hamster.NOTE_D_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_G_5)
    wait(125)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_G_5)
    wait(400)
    hamster.note(hamster.NOTE_OFF)
    wait(100)
    hamster.note(hamster.NOTE_A_5)
    wait(250)
    hamster.note(hamster.NOTE_F_SHARP_5)
    wait(375)
    hamster.note(hamster.NOTE_E_5)
    wait(125)
    hamster.note(hamster.NOTE_D_5)
    wait(400)
    hamster.note(hamster.NOTE_OFF)
    wait(100)
    hamster.note(hamster.NOTE_D_5)
    wait(250)
    hamster.note(hamster.NOTE_A_5)
    wait(500)
    hamster.note(hamster.NOTE_G_5)
    wait(500)
    hamster.note(hamster.NOTE_OFF)

#calibrates and centers the robot by aligning itself with the wall to the left or right of it based on if its sensors detect a wall 
def calibrate():
    print("calibrating")
    hamster.wheels(-30)
    wait(500)
    checker()
    if L > 43:
        turnRight()
        OrientSelfFromWall()
        turnLeft()
    elif R > 42:
        turnLeft()
        OrientSelfFromWall()
        turnRight()
    checker()
    hamster.wheels(30)
    wait(300)
    hamster.stop()
    print("done calibration")

# updates the map with the new map provided
def setMap(newmap):
    global map
    map = newmap

#scans all the walls left and right and then updates the map
def checkwallsFacingUp():
    hamster.stop()
    checker()
    print("checking left and right walls")
    print("while checking (L,R): " + str(L) + str(R))
    map = getMap()
    position = getPosition()

    hamster.stop()
    checker()
    if L > 24:
        if (map[position[0]][position[1] - 1]) == 2:
            map[position[0]][position[1] - 1] = 1
        if (map[position[0] + 1][position[1] - 1]) == 2:
            map[position[0] + 1][position[1] - 1] = 1
        if (map[position[0] - 1][position[1] - 1]) == 2:
            map[position[0] - 1][position[1] - 1] = 1

    else:
        if (map[position[0]][position[1] - 1]) == 2:
            map[position[0]][position[1] - 1] = 0
    if R > 24:
        if map[position[0]][position[1] + 1] == 2:
            map[position[0]][position[1] + 1] = 1
        if map[position[0] + 1][position[1] + 1] == 2:
            map[position[0] + 1][position[1] + 1] = 1
        if map[position[0] - 1][position[1] + 1] == 2:
            map[position[0] - 1][position[1] + 1] = 1

    else:
        if map[position[0]][position[1] + 1] == 2:
            map[position[0]][position[1] + 1] = 0

    hamster.stop()
    setMap(map)

#scans all the walls up and down and then updates the map
def checkWallsFacingRight():
    hamster.stop()
    print("checking top and bottom wall")

    checker()
    map = getMap()
    position = getPosition()

    checker()
    if L > 24:
        if map[position[0] - 1][position[1] - 1] == 2:
            map[position[0] - 1][position[1] - 1] = 1
        if map[position[0] - 1][position[1]] == 2:
            map[position[0] - 1][position[1]] = 1
        if map[position[0] - 1][position[1] + 1] == 2:
            map[position[0] - 1][position[1] + 1] = 1

    else:
        if map[position[0] - 1][position[1]] == 2:
            map[position[0] - 1][position[1]] = 0
    if R > 24:
        if map[position[0] + 1][position[1] + 1] == 2:
            map[position[0] + 1][position[1] + 1] = 1
        if map[position[0] + 1][position[1]] == 2:
            map[position[0] + 1][position[1]] = 1
        if map[position[0] + 1][position[1] - 1] == 2:
            map[position[0] + 1][position[1] - 1] = 1
    else:
        if map[position[0] + 1][position[1]] == 2:
            map[position[0] + 1][position[1]] = 0

    wait(200)

#returns current position
def getPosition():
    global position
    return (position[0], position[1])

#adjusts the position of the robot based on the movement it has jsut made and based on orientation
def setPositionForward():
    global orientation
    global position
    global map

    position = list(position)
    if orientation == 0:
        position[0] = position[0] - 2
        if map[position[0]][position[1]] == 2:
            map[position[0]][position[1]] = 0
    elif orientation == 1:
        position[1] = position[1] - 2
        if map[position[0]][position[1]] == 2:
            map[position[0]][position[1]] = 0
    elif orientation == 2:
        position[1] = position[1] + 2
        if map[position[0]][position[1]] == 2:
            map[position[0]][position[1]] = 0
    elif orientation == 3:
        position[0] = position[0] + 2
        if map[position[0]][position[1]] == 2:
            map[position[0]][position[1]] = 0
    position = tuple(position)
    print(position)


# turns left and changes orientation
def turnLeft():
    hamster.turn_left(90, 80)
    setOrientation("left")


# turns right and changes orientation
def turnRight():
    hamster.turn_right(90, 80)
    setOrientation("right")


# self correcting movement function, will check both walls and adjust till it is in the center, if the space
def moveForward(wheelspeed=87):
    setPositionForward()
    hamster.stop()
    wait(100)
    print("moving forward")
    checker()
    for i in range(78):
        checker()

        if R >= 38:
            diff = R - 40
            hamster.wheels((wheelspeed) - (diff * 0.6), (wheelspeed) + (diff * 0.6))
            wait(10)
        elif L >= 38:
            diff = L - 40
            hamster.wheels((wheelspeed) + (diff * 0.6), (wheelspeed) - (diff * 0.6))
            wait(10)
        elif R <= 38 and R >= 25:
            diff = R - 40
            hamster.wheels((wheelspeed) - (diff * 0.6), (wheelspeed) + (diff * 0.6))
            wait(10)
        elif L <= 38 and L >= 25:
            diff = L - 40
            hamster.wheels((wheelspeed) + (diff * 0.6), (wheelspeed) - (diff * 0.6))
            wait(10)

        else:
            hamster.wheels(wheelspeed)

            wait(10)


# this function will return possible positions the robot can move to that are adjacent
def check_adjacent_2d_array(arr, row, col):
    rows = len(arr)
    cols = len(arr[0])

    # Check top
    if row > 0 and arr[row - 1][col] == 0:
        if row > 1 and arr[row - 2][col] == 2:
            return "up"

    # Check bottom
    if row < rows - 1 and arr[row + 1][col] == 0:
        if row < rows - 2 and arr[row + 2][col] == 2:
            return "down"

    # Check left
    if col > 0 and arr[row][col - 1] == 0:
        if col > 1 and arr[row][col - 2] == 2:
            return "left"

    # Check right
    if col < cols - 1 and arr[row][col + 1] == 0:
        if col < cols - 2 and arr[row][col + 2] == 2:
            return "right"

    return None


import numpy as np


# this function will find the nearest path to the goal from home or start based on the map that it has mapped so far
def is_valid_move(map, row, col):
    # Check if the row and col are within the bounds of the map
    if row >= 0 and row < len(map) and col >= 0 and col < len(map[0]):
        # Check if the move is allowed (i.e., not hitting a wall)
        if map[row][col] != 1:
            return True
    return False

#this will find the most efficient path to the goal using a breadth first search using recursion
def find_Home():
    start = tuple(position)

    queue = [(start[0], start[1], [])]
    visited = set()

    while queue:
        row, col, path = queue.pop(0)

        if map[row][col] == 4:
            path = [
                tuple(position)
            ] + path  # Update only the cells of the final path and the points in between to value 3
            for i in range(len(path) - 1):
                # Get the current and next point in the path
                curr_point = path[i]
                next_point = path[i + 1]
                # Update the cells in between to value 3
                row_start, row_end = min(curr_point[0], next_point[0]), max(
                    curr_point[0], next_point[0]
                )
                col_start, col_end = min(curr_point[1], next_point[1]), max(
                    curr_point[1], next_point[1]
                )
                for r in range(row_start, row_end + 1):
                    for c in range(col_start, col_end + 1):
                        if map[r][c] == 0:
                            map[r][c] = 3
                map[7][5] = 4
                print(visited)
            return path

        if (row, col) not in visited:
            visited.add((row, col))

            # Generate next possible moves
            moves = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            for move in moves:
                new_row = row + move[0]
                new_col = col + move[1]

                # Check if the move is valid and does not jump over walls
                if (
                    is_valid_move(map, new_row, new_col)
                    and (move[0] == 0 or map[row + int(move[0] / 2)][col] != 1)
                    and (move[1] == 0 or map[row][col + int(move[1] / 2)] != 1)
                ):
                    queue.append((new_row, new_col, path + [(new_row, new_col)]))

    return None


# this function is a breadth first search from the current position to the next unknown space.
#this is a near copy of the find_Home function but this finds a different goal and does not change the map
def find_Path():
    global position
    start = tuple(position)
    queue = [(start[0], start[1], [])]
    visited = set()

    while queue:
        row, col, path = queue.pop(0)

        if map[row][col] == 2:  # Check if the current cell matches the value 2
            path = path
            return path

        if (row, col) not in visited:
            visited.add((row, col))

            # Generate next possible moves
            moves = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            for move in moves:
                new_row = row + move[0]
                new_col = col + move[1]

                # Check if the move is valid and does not jump over walls
                if (
                    is_valid_move(map, new_row, new_col)
                    and (move[0] == 0 or map[row + int(move[0] / 2)][col] != 1)
                    and (move[1] == 0 or map[row][col + int(move[1] / 2)] != 1)
                ):
                    queue.append((new_row, new_col, path + [(new_row, new_col)]))

    return None


import turtle


# draW a map of the maze
def Draw():
    for row in map:
        for element in row:
            if element == 0:  # white square
                turtle.fillcolor("white")
            elif element == 1:  # black square
                turtle.fillcolor("black")
            elif element == 4:  # green target square
                turtle.fillcolor("green")
            elif element == 3:  # path
                turtle.fillcolor("yellow")
            else:  # grey square
                turtle.fillcolor("grey")
            turtle.pendown()
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(square_size)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()
            turtle.setposition(turtle.xcor() + square_size, turtle.ycor())
        turtle.setposition(-200, turtle.ycor() - square_size)

    turtle.done()


# stereo tpyical stack instantiation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()


# this is the main method of the program it drives the program
# it will run consistently repeatedly running until it gets to a state allowing it to solve the maze
def runner():
    s = Stack()

    while True:
        global position
        global map

        hamster.stop()
        path = None
        hamster.leds(Hamster.COLOR_NAME_BLUE)
        direction = check_adjacent_2d_array(map, position[0], position[1])
        if position == (9, 5):
            solver()
        if direction == None:
            hamster.leds(Hamster.COLOR_NAME_RED)
            path = find_Path()

            if path != None:
                for routepoint in path:
                    if routepoint[0] > position[0]:
                        move_func("down")
                    if routepoint[0] < position[0]:
                        move_func("up")
                    if routepoint[1] > position[1]:
                        move_func("right")
                    if routepoint[1] < position[1]:
                        move_func("left")

        else:
            move_func(direction)


# this will return a solved path to the goal from the main starting point and then execute it
def solver():
    hamster.leds(Hamster.COLOR_NAME_GREEN)
    wait(10000)
    global orientation
    orientation = 1
    position = (5, 9)
    solve = find_Home()
    if solve != []:
        print(solve)
    for path in solve:
        if path[0] > position[0]:
            move_func_Solve("down")
        elif path[0] < position[0]:
            move_func_Solve("up")
        elif path[1] > position[1]:
            move_func_Solve("right")
        elif path[1] < position[1]:
            move_func_Solve("left")
    if position == (9, 5):
        victory()
    else:
        solver()


# this is very similar to the orient elf function except this one will center the bot after orienting itself from a wall next to it rather than behind it
def OrientSelfFromWall():
    global orientation
    global position
    if orientation == 0:
        print("fixing down")
        print((map[position[0] + 1][position[1]]))
        if (map[position[0] + 1][position[1]]) == 1:
            hamster.wheels(-70)
            wait(500)
            hamster.wheels(45)
            wait(600)
    if orientation == 1:
        print("fixing left")
        print((map[position[0]][position[1] + 1]))
        if (map[position[0]][position[1] + 1]) == 1:
            hamster.wheels(-70)
            wait(500)
            hamster.wheels(45)
            wait(600)
    if orientation == 2:
        print("fixing right")
        print((map[position[0]][position[1] - 1]))
        if (map[position[0]][position[1] - 1]) == 1:
            hamster.wheels(-70)
            wait(500)
            hamster.wheels(45)
            wait(600)
    if orientation == 3:
        print("fixing up")
        print(map[position[0] - 1][position[1]])
        if (map[position[0] - 1][position[1]]) == 1:
            hamster.wheels(-70)
            wait(500)
            hamster.wheels(45)
            wait(600)


# this will check behind the bot and then ram the bot into it and then move forward to reset distance
def OrientSelf():
    global orientation
    global position
    if orientation == 0:
        print("fixing down")
        print((map[position[0] + 1][position[1]]))
        if (map[position[0] + 1][position[1]]) == 1:
            hamster.wheels(-70)
            wait(500)
            hamster.wheels(30)
            wait(600)
    if orientation == 1:
        print("fixing left")
        print((map[position[0]][position[1] + 1]))
        if (map[position[0]][position[1] + 1]) == 1:
            hamster.wheels(-70)
            wait(500)
            hamster.wheels(30)
            wait(600)
    if orientation == 2:
        print("fixing right")
        print((map[position[0]][position[1] - 1]))
        if (map[position[0]][position[1] - 1]) == 1:
            hamster.wheels(-70)
            wait(500)
            hamster.wheels(30)
            wait(600)
    if orientation == 3:
        print("fixing up")
        print(map[position[0] - 1][position[1]])
        if (map[position[0] - 1][position[1]]) == 1:
            hamster.wheels(-70)
            wait(500)
            hamster.wheels(30)
            wait(600)

def forwardFunc():
    moveForward()
    checkWallCurrentNodeUp()
    checkWallCurrentNodeRight()
    checker()
    if (
        map[position[0]][position[1] + 1] == 1
        and map[position[0]][position[1] - 1] == 1
        and (orientation == 0 or 3)
        or map[position[0] + 1][position[1]] == 1
        and map[position[0] - 1][position[1]] == 1
        and (orientation == 1 or 2)
    ):
        turnCorrecter()
        calibrate()
def RightFunc():
    turnRight()
    OrientSelfFromWall()
    checker()
    if (
        map[position[0]][position[1] + 1] == 1
        and map[position[0]][position[1] - 1] == 1
        and (orientation == 0 or 3)
        or map[position[0] + 1][position[1]] == 1
        and map[position[0] - 1][position[1]] == 1
        and (orientation == 1 or 2)
    ):
        turnCorrecter()
        calibrate()
    moveForward()
    checkWallCurrentNodeUp()
    checkWallCurrentNodeRight()
    
def LeftFunc():
    turnLeft()
    OrientSelfFromWall()
    moveForward()
    checkWallCurrentNodeUp()
    if (
        map[position[0]][position[1] + 1] == 1
        and map[position[0]][position[1] - 1] == 1
        and (orientation == 0 or 3)
        or map[position[0] + 1][position[1]] == 1
        and map[position[0] - 1][position[1]] == 1
        and (orientation == 1 or 2)
    ):
        turnCorrecter()
        calibrate()
    checkWallCurrentNodeRight()

def rotateFunc():
    turnLeft()
    OrientSelfFromWall()
    checker()
    if (
        map[position[0]][position[1] + 1] == 1
        and map[position[0]][position[1] - 1] == 1
        and (orientation == 0 or 3)
        or map[position[0] + 1][position[1]] == 1
        and map[position[0] - 1][position[1]] == 1
        and (orientation == 1 or 2)
    ):
        turnCorrecter()
        calibrate()
    turnLeft()
    OrientSelfFromWall()
    checker()

    if (
        map[position[0]][position[1] + 1] == 1
        and map[position[0]][position[1] - 1] == 1
        and (orientation == 0 or 3)
        or map[position[0] + 1][position[1]] == 1
        and map[position[0] - 1][position[1]] == 1
        and (orientation == 1 or 2)
    ):
        turnCorrecter()
        calibrate()

    moveForward()
    checkWallCurrentNodeUp()
    checkWallCurrentNodeRight()

    checker()


# this function intakes a direction which then will take the orientation of the bot and give it instructions on how to fulfil the order.
#this function is one of the most complicated functions in terms of how long it is i have ever made
# based on the input of the desired direction it will find the easiest way to get to that location and adjust itself accordingly
#it will also scan all the walls and open spaces while doing so
#the exsessive number of lines can be attributed to all the self correcting functions and conditions that i have set to make sure it does not mess up when traveling
#to format nicely on each line there is a condition of the statement making it more readable at the cost of length.
def move_func(direction):
    global orientation
    global position
    print(direction)
    print(position)
    print(orientation)

    OrientSelf()
    # each direction has four orientation options to go off of.
    if direction == "up":
        if orientation == 0:
            forwardFunc()
        elif orientation == 1:
            RightFunc()
        elif orientation == 2:
            LeftFunc()
        elif orientation == 3:
            rotateFunc
    if direction == "down":
        if orientation == 0:
           rotateFunc()
        elif orientation == 1:
            LeftFunc()
        elif orientation == 2:
            RightFunc()   
        elif orientation == 3:
            forwardFunc()
    if direction == "left":
        if orientation == 0:
            LeftFunc()
        elif orientation == 1:
            forwardFunc()
        elif orientation == 2:
            rotateFunc()
        elif orientation == 3:
            RightFunc()
    if direction == "right":
        if orientation == 0:
            RightFunc()
        elif orientation == 1:
            rotateFunc()
        elif orientation == 2:
            forwardFunc()
        elif orientation == 3:
            LeftFunc()

#same as the function above but without any correction or wall checking
def move_func_Solve(direction):
    global orientation
    global position
    if direction == "up":
        if orientation == 0:
            moveForward()
            checker()
        elif orientation == 1:
            turnRight()
            moveForward()
        elif orientation == 2:
            turnLeft()
            moveForward()
        elif orientation == 3:
            turnLeft()
            turnRight()
            moveForward()
            moveForward()
    if direction == "down":
        if orientation == 0:
            turnLeft()
            checker()
            turnLeft()
            checker()
            moveForward()
            checker()
        elif orientation == 1:
            turnLeft()
            checker()
            moveForward()
            checker()
        elif orientation == 2:
            turnRight()
            checker()
            moveForward()
            checker()
        elif orientation == 3:
            moveForward()
            checker()
    if direction == "left":
        if orientation == 0:
            turnLeft()
            checker()
            moveForward()
            checker()
        elif orientation == 1:
            moveForward()
            checker()
        elif orientation == 2:
            turnLeft()
            checker()
            turnLeft()
            checker()
            moveForward()
            checker()
        elif orientation == 3:
            turnRight()
            checker()
            moveForward()
            checker()
    if direction == "right":
        if orientation == 0:
            turnRight()
            checker()
            moveForward()
            checker()
        elif orientation == 1:
            turnLeft()
            checker()
            turnLeft()
            checker()
            moveForward()
            checker()
        elif orientation == 2:
            moveForward()
            checker()
        elif orientation == 3:
            turnLeft()
            checker()
            moveForward()
            checker()


# runner code this is where it is all called
instantiate()
end = (9, 5)
map[9][5] = 4

turtle.speed(0)
turtle.penup()
turtle.tracer(0)
turtle.setposition(-200, 200)


square_size = 35

runner()
Draw()
wait(200000)
