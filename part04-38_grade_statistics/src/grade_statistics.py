ex_completed = []
exam_points = []
total_points = []
grades = []

def inputs():

    global exam_points # to store all the exam points from inputs
    global ex_completed # to store all the exercises completed from inputs

    while True:
        input1 = input("Exam points and exercises completed: ")
        if input1 == "":
            break
        input_split = input1.split() # create a temporary list "input_split" to save the 2 numbers from input1
        
        exam_points.append(int(input_split[0])) # first number goes to "exam_points" list
        ex_completed.append(int(input_split[1])) # second and last number goes to "ex_completed" list
    
    # At this point there are 2 lists with all the input numbers (as integers).
    # exam_points = [15, 10, 11, 4]
    # ex_completed = [87, 55, 40, 17]
    
    return exam_points
    return ex_completed
    '''
    print(exam_points)
    print(ex_completed)
    '''

def points():
    
    #--------------------------- to convert exercises completed to exercises points ------------------
    global ex_completed
    global exam_points
    global grades

    ex_points = []
    
    for i in range (len(ex_completed)):
        points = ex_completed[i] // 10
        ex_points.append(points)
    # ex_points [8, 5, 4, 1]

    #--------------------------- sum ex_points with exam_points to get total_points -------------------
    global total_points

    for i in range (len(ex_points)):
        sum = ex_points[i] + exam_points[i]
        total_points.append(sum)

    for i in range (len(total_points)):
        if exam_points[i] < 10 or total_points[i] <= 14:
            grade = 0
            grades.append(grade)
            continue
        elif 15 <= total_points[i] <= 17:
            grade = 1
            grades.append(grade)
        elif 18 <= total_points[i] <= 20:
            grade = 2
            grades.append(grade)
        elif 21 <= total_points[i] <= 23:
            grade = 3
            grades.append(grade)
        elif 24 <= total_points[i] <= 27:
            grade = 4
            grades.append(grade)
        elif 28 <= total_points[i] <= 30:
            grade = 5
            grades.append(grade)

    


def statistics():
    global total_points
    global grades

    print("Statistics:")

    # average points calculation
    pts_sum = 0

    for num in total_points:
        pts_sum += num
    nums = len(total_points)
    avg_pts = pts_sum / nums

    # pass percentage calculation
    count = 0

    for i in range (len(grades)):
        if grades[i] >= 1:
            count += 1
    
    percen = (count * 100) / (len(total_points))

    print("Points average:", avg_pts)
    print("Pass percentage:", "{:.1f}".format(percen))
    

    # Grade Distribution
    print("Grade distribution:")

    print("5:", end= " ")
    for n in grades:
        if n == 5:
            print("*", end = "")
    print()
    print("4:", end= " ")
    for n in grades:
        if n == 4:
            print("*", end = "")
    print()
    print("3:", end= " ")
    for n in grades:
        if n == 3:
            print("*", end = "")
    print()
    print("2:", end= " ")
    for n in grades:
        if n == 2:
            print("*", end = "")
    print()
    print("1:", end= " ")
    for n in grades:
        if n == 1:
            print("*", end = "")
    print()
    print("0:", end= " ")
    for n in grades:
        if n == 0:
            print("*", end = "")



'''
    #for num in total_points:
     #   i = 0
      #  for n in [15, 18, 21, 24, 28, 30]:
       #     
       #     if num <= n:
        #        print(f"{i}:", end = "")
       #         print("*", end = "")
        #        i += 1
       #         print()
       #         continue
'''   


inputs()
points()
statistics()