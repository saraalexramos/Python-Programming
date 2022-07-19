
def range_of_list(list):
    sma = min(list)
    lar = max(list)
    dif = lar - sma
    return dif

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)