import numpy as np
from math import pow
import os

def clear():
    os.system('clear')

def quick_matpow(matrix: np.ndarray, power: int) -> np.ndarray:
    matrices_buffer = [matrix]
    i = 1

    while pow(2, i) <= power:
        print(pow(2, i), power)
        matrices_buffer.append(np.matmul(matrices_buffer[-1], matrices_buffer[-1]))
        i += 1

    power -= pow(2, i-1)

    result = matrices_buffer[-1]

    while power != 0:
        print(pow(2, i), power, pow(2, i) + power)
        i -= 1
        if pow(2, i) > power:
            continue
        else:
            result = np.matmul(result, matrices_buffer[i])
            power -= pow(2, i)

    return result


def edit_matrix(matrix: np.ndarray) -> np.ndarray:
    finished = False
    cursor_x = 0
    cursor_y = 0

    clear()

    while not finished:
        print(f"Current cursor position (x-axis and y-axis, starting from the top left corner): {cursor_x, cursor_y}")
        print(f"Current matrix cell values: \n{matrix}")
        responce = input("Input the cell value, use the WASD keys to move the cursor, and type 'q' to finish inputting values: ")
        clear()
        match responce.lower():
            case "q":
                finished = True

            case "w":
                cursor_y -= 1

            case "a":
                cursor_x -= 1

            case "s":
                cursor_y += 1

            case "d":
                cursor_x += 1

            case _:
                try:
                    matrix[cursor_y][cursor_x] = float(responce)
                except:
                    print("Please enter a float, 0 or 1\n")

        if cursor_x > len(matrix):
            cursor_x = len(matrix)

        if cursor_x < 0:
            cursor_x = 0

        if cursor_y > len(matrix):
            cursor_y = len(matrix)

        if cursor_y < 0:
            cursor_y = 0


    return matrix

def edit_vector(vector: np.ndarray) -> np.ndarray:
    finished = False
    cursor = 0
    
    clear()

    while not finished:
        print(f"Current cursor position (starting from the left): {cursor}")
        print(f"Current vector cell values: \n{np.array(vector)}")
        responce = input("Input the cell value, use the A and D keys to move the cursor or type 'q' to finish inputting values: ")
        clear()
        match responce.lower():
            case "q":
                finished = True

            case "a":
                cursor -= 1

            case "d":
                cursor += 1

            case _:
                try:
                    vector[cursor] = np.float64(responce)
                except:
                    print("Please enter a float, 0 or 1\n")
        
        if cursor > len(vector):
            cursor = len(vector)

        if cursor < 0:
            cursor = 0
            
    return vector

def extract_vector_to_list(vector: np.matrix) -> list:
    return [i for i in vector.tolist()]

def main():
    finished = False
    
    clear()
    size = int(input("Enter the transition matrix size: "))

    transition_matrix = np.zeros((size, size), dtype=np.float64)
    base_state_vector = np.zeros((size), dtype=np.float64)

    while not finished:

        transition_matrix = edit_matrix(transition_matrix)
        base_state_vector = edit_vector(base_state_vector)

        iterations = int(input("Enter the iteration amount: "))

        state_vector = base_state_vector

        quick_trans = quick_matpow(transition_matrix, iterations)

        state_vector = np.dot(quick_trans, state_vector)

        print(state_vector)

        if input("Do you wish to reenter some values? (Y/n): ").lower() == "n":
            finished = True
        
        clear()

if __name__ == "__main__":
    main()