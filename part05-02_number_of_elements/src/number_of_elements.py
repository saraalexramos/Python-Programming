# A function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer value as its arguments. 
# The function then counts how many elements within the matrix match the argument value.

def count_matching_elements(matrix: list, element:int):
    count = 0
    for row in matrix:
        for number in row:
            if number == element:
                count += 1
    return count





if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))