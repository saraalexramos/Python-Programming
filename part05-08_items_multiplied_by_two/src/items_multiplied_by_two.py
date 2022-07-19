# Please write a function named double_items(numbers: list), which takes a list of integers as its argument.

#The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.

def double_items(numbers:list):
    doubled_numbers = [] # a new list to stored the doubled numbers
    
    for number in numbers: # for each number of the list
        doubled_numbers.append(number*2) # Append to new list the doubled numbers (number*2)
    
    return doubled_numbers


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)