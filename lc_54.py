from typing import List


class SpiralOrder:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        height = len(matrix)
        width = len(matrix[0])
        size = height * width
        result = []

        dir_x = [0, 1, 0, -1]
        dir_y = [1, 0, -1, 0]

        x = 0
        y = -1
        direction = 0
        step = 0

        for count in range(size):
            if direction is 0 or direction is 2:
                step = width
                height -= 1
            else:
                step = height
                width -= 1

            print("Step: " + str(step) + " Height: " + str(height) + " Width: " + str(width))

            for i in range(step):
                x += dir_x[direction]
                y += dir_y[direction]
                print(x, y)
                result.append(matrix[x][y])

            direction += 1
            direction %= 4
            if width == 0 or height == 0:
                break

        return result


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
test_case = SpiralOrder()
print(test_case.spiralOrder(matrix))
