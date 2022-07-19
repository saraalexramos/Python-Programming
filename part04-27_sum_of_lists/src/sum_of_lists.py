#a function named list_sum which takes two lists of integers as arguments. 
# The function returns a new list which contains the sums of the items at each index in the two original lists. 
# You may assume both lists have the same number of items.

def list_sum(list1, list2):
    sumlist=[]
    for i in range (len(list1)):
        sum = list1[i] + list2[i]
        sumlist.append(sum)
    return sumlist
        

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))