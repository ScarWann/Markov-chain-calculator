import numpy as np

def matrix_input(size):
    line = [0] * size
    matrix = [line]
    for _ in range(1, size):
        matrix.extend([line.copy()])
    finished = False
    cursor_x = 0
    cursor_y = 0
    while finished != True:
        print(f"Current cursor position (x-axis and y-axis, starting from the top left corner): {cursor_x, cursor_y}")
        print(f"Current matrix cell values: \n{np.matrix(matrix)}")
        responce = input("Input the cell value, use the WASD keys to move the cursor or type either 'quit' or 'exit' to finish inputting values\n")
        match responce.lower():
            case "quit" | "exit":
                break

            case "w":
                cursor_y -= 1

            case "a":
                cursor_x -= 1

            case "s":
                cursor_y += 1

            case "d":
                cursor_x += 1

            case _:
                line = matrix[cursor_y]
                line[cursor_x] = float(responce)
                matrix[cursor_y] = line
    return np.matrix(matrix)

def vector_input(size):
    line = []
    for _ in range(size):
        line.append([0])
    print(line)
    cursor = 0
    while True:
        print(f"Current cursor position (x-axis and y-axis, starting from the top left corner): {cursor}")
        print(f"Current matrix cell values: \n{np.array(line)}")
        responce = input("Input the cell value, use the A and D keys to move the cursor or type either 'quit' or 'exit' to finish inputting values\n")
        match responce.lower():
            case "quit" | "exit":
                break

            case "a":
                cursor -= 1

            case "d":
                cursor += 1

            case _:
                try:
                    line[cursor][0] = float(responce)
                except:
                    print("Whoops! Something went wrong! You wont have to fill out the matrix again though\n")
    return np.matrix(line)


DISCRETE = True
if DISCRETE:
    size = int(input("Enter the transition matrix size\n"))
    matrix = matrix_input(size)
    vector = vector_input(size)
    iterations = int(input("Enter the iteration amount"))
    result = np.dot(np.linalg.matrix_power(matrix, iterations), vector)
    print(result)