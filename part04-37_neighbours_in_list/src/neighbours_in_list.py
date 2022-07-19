# Write your solution here

def longest_series_of_neighbours(list):
    
    list_count = []
    count = 1

    for i in range (len(list)-1):
        
        if list[i] - list[i+1] == 1 or list[i] - list[i+1] == -1:
            count += 1
            list_count.append(count)
        else:
            count = 1
            continue
                
    return max(list_count)



if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))