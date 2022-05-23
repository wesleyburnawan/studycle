#A function to check whether the input has the right format
def check_input(points):
    points = points.split(" ")
    for num in points:
        if num == "":
            print("Invalid input. Too many space between numbers")
            return False
    if(len(points) < 8):
        print("Less than 4 (x,y) coordinates given. No rectangle can be created")
        return False
    elif(len(points) % 2 == 1):
        print("Invalid input. Odd number of points given")
        return False
    return True

#A function to modify points to a list of list containing (x, y) coordinates to coordinates
def modify_input(points, coordinates):
    size = 0
    points = points.split(" ")
    for num in points:
        if(len(coordinates[size]) < 2):
            coordinates[size].append(int(num))
        else:
            coordinates.append([])
            size += 1
            coordinates[size].append(int(num))

#A function to check whether rectangle can be made from coordinates
def form_rectangle(coordinates):
    for p1 in range(len(coordinates)-3):
        for p2 in range(p1+1, len(coordinates)-2):
            for p3 in range(p2+1, len(coordinates)-1):
                for p4 in range(p3+1, len(coordinates)):
                    if is_rectangle(coordinates, p1, p2, p3, p4) == True:
                        if points_on_rectangle(coordinates, p1, p2, p3, p4) == True:
                            return True
    return False


#A helper function for form_rectangle to determine whether the 4 points create a rectangle
def is_rectangle(coordinates, p1, p2, p3, p4):
    #Check whether there is duplicate points
    if(coordinates[p1] == coordinates[p2] or coordinates[p1] == coordinates[p3] or
    coordinates[p1] == coordinates[p4] or coordinates[p2] == coordinates[p3] or
    coordinates[p2] == coordinates[p4] or coordinates[p3] == coordinates[p4]):
        return False

    #Check whether the points can create a rectangle or square using center of mass
    center_of_x = (coordinates[p1][0] + coordinates[p2][0] + coordinates[p3][0] + coordinates[p4][0])/4
    center_of_y = (coordinates[p1][1] + coordinates[p2][1] + coordinates[p3][1] + coordinates[p4][1])/4
    p1_to_center_distance = (center_of_x - coordinates[p1][0])**2 + (center_of_y - coordinates[p1][1])**2
    p2_to_center_distance = (center_of_x - coordinates[p2][0])**2 + (center_of_y - coordinates[p2][1])**2
    p3_to_center_distance = (center_of_x - coordinates[p3][0])**2 + (center_of_y - coordinates[p3][1])**2
    p4_to_center_distance = (center_of_x - coordinates[p4][0])**2 + (center_of_y - coordinates[p4][1])**2
    
    if(p1_to_center_distance != p2_to_center_distance or p1_to_center_distance != p3_to_center_distance or
    p1_to_center_distance != p4_to_center_distance):
        return False

    #Check whether the shape is rectangle or square
    p1_to_p2_distance = (coordinates[p1][0] - coordinates[p2][0])**2 + (coordinates[p1][1] - coordinates[p2][1])**2
    p1_to_p3_distance = (coordinates[p1][0] - coordinates[p3][0])**2 + (coordinates[p1][1] - coordinates[p3][1])**2
    p1_to_p4_distance = (coordinates[p1][0] - coordinates[p4][0])**2 + (coordinates[p1][1] - coordinates[p4][1])**2
    if(p1_to_p2_distance == p1_to_p3_distance or p1_to_p2_distance == p1_to_p4_distance or p1_to_p3_distance == p1_to_p4_distance):
        return False #When there is a similar distance between p1 to 2 other points (square has the same length of sides)
    return True

#A helper function for form_rectangle to determine if all points in coordinates is contained on the rectangle
def points_on_rectangle(coordinates, p1, p2, p3, p4):
    p1_to_p2_distance = (coordinates[p1][0] - coordinates[p2][0])**2 + (coordinates[p1][1] - coordinates[p2][1])**2
    p1_to_p3_distance = (coordinates[p1][0] - coordinates[p3][0])**2 + (coordinates[p1][1] - coordinates[p3][1])**2
    p1_to_p4_distance = (coordinates[p1][0] - coordinates[p4][0])**2 + (coordinates[p1][1] - coordinates[p4][1])**2
    for point in range(len(coordinates)):
        if coordinates[point] == coordinates[p1] or coordinates[point] == coordinates[p2] or coordinates[point] == coordinates[p3] or coordinates[point] == coordinates[p4]:
            continue
        #Get the coordinate not connected to p1 through a line
        if(max(p1_to_p2_distance, p1_to_p3_distance, p1_to_p4_distance) == p1_to_p2_distance):
            if(is_between(coordinates, p1, p3, point) == False and is_between(coordinates, p1, p4, point) == False and
            is_between(coordinates, p2, p3, point) == False and is_between(coordinates, p2, p4, point) == False):
                return False
        elif(max(p1_to_p2_distance, p1_to_p3_distance, p1_to_p4_distance) == p1_to_p3_distance):
            if(is_between(coordinates, p1, p2, point) == False and is_between(coordinates, p1, p4, point) == False and
            is_between(coordinates, p3, p2, point) == False and is_between(coordinates, p3, p4, point) == False):
                return False
        else:
            if(is_between(coordinates, p1, p3, point) == False and is_between(coordinates, p1, p2, point) == False and
            is_between(coordinates, p4, p3, point) == False and is_between(coordinates, p4, p2, point) == False):
                return False
    return True

#A helper function for points_on_rectangle to determine whether p3 is between p1 and p2
def is_between(coordinates, p1, p2, p3):
    cross_product = (coordinates[p3][1] - coordinates[p1][1]) * (coordinates[p2][0] - coordinates[p1][0]) - (coordinates[p3][0] - coordinates[p1][0]) * (coordinates[p2][1] - coordinates[p1][1])
    if cross_product != 0:
        return False

    dot_product = (coordinates[p3][0] - coordinates[p1][0]) * (coordinates[p2][0] - coordinates[p1][0]) + (coordinates[p3][1] - coordinates[p1][1]) * (coordinates[p2][1] - coordinates[p1][1])
    if dot_product < 0:
        return False

    squared_length_p1_p2 = (coordinates[p2][0] - coordinates[p1][0])**2 + (coordinates[p2][1] - coordinates[p1][1])**2
    if dot_product > squared_length_p1_p2:
        return False
    return True

#A tester method to check on the functionality of check_input method
def test_check_input():
    input_1 = " " #input with only space
    input_2 = "2 3 4 5 6 7 8 9 10" #input with odd number of inputs
    input_3 = "2 4 5 6" #input with less than 4 (x, y) coordinates
    input_4 = "2    4     5 6 7  8   9    10" #input with too many space
    input_5 = "1 2 3 4 5 6 7 8" #correct input with only 4 (x, y) coordinates
    input_6 = "1 2 3 4 5 6 7 8 1 2 3 4" #correct input with more than 4 (x, y) coordinates
    if(check_input(input_1) == True or check_input(input_2) == True or check_input(input_3) == True or check_input(input_4) == True or check_input(input_5) == False or check_input(input_6) == False):
        return False
    return True

#A tester method to check on the functionality of is_rectangle method
def test_is_rectangle():
    #Test 1 - Given coordinates have duplicates
    coordinates = [[]]
    points = "2 4 1 2 3 5 2 4"
    modify_input(points, coordinates)
    if(is_rectangle(coordinates, 0, 1 , 2 ,3) == True):
        return False

    #Test 2 - Given coordinates can't create a square or rectangle
    coordinates = [[]]
    points = "2 4 1 2 3 5 2 6"
    modify_input(points, coordinates)
    if(is_rectangle(coordinates, 0, 1 , 2 ,3) == True):
        return False

    #Test 3 - Given coordinates can create a square
    coordinates = [[]]
    points = "0 0 1 0 0 1 1 1"
    modify_input(points, coordinates)
    if(is_rectangle(coordinates, 0, 1 , 2 ,3) == True):
        return False

    #Test 4 - Given coordinates can create a rectangle that has sides parallel to axis
    coordinates = [[]]
    points = "0 0 2 0 0 1 2 1"
    modify_input(points, coordinates)
    if(is_rectangle(coordinates, 0, 1 , 2 ,3) == False):
        return False

    #Test 5 - Given coordinates can create a rectangle that has negative coordinates
    coordinates = [[]]
    points = "-5 -5 -5 10 5 10 5 -5"
    modify_input(points, coordinates)
    if(is_rectangle(coordinates, 0, 1 , 2 ,3) == False):
        return False

    #Test 6 - Given coordinates can create a rectangle that has sides that are not parallel to axis
    coordinates = [[]]
    points = "0 0 5 5 15 -5 10 -10"
    modify_input(points, coordinates)
    if(is_rectangle(coordinates, 0, 1 , 2 ,3) == False):
        return False
    return True

#A tester method to check on the functionality of is_between method
def test_is_between():
    #Test 1 - point is not on the line
    coordinates = [[]]
    points = "0 0 1 0 3 0 2 1"
    modify_input(points, coordinates)
    if(is_between(coordinates, 0, 2, 3) == True):
        return False

    #Test 2 - point is on the line if the line is lengthened
    if(is_between(coordinates, 0, 1, 2) == True):
        return False

    #Test 3 - point is on the line
    if(is_between(coordinates, 0, 2, 1) == False):
        return False
    return True

#A tester method to check on the functionality of points_on_rectangle method
def test_points_on_rectangle():
    #Test 1 - More than 1 point in coordinates not on the rectangle
    coordinates = [[]]
    points = "0 0 3 0 3 2 0 2 1 1 2 1"
    modify_input(points, coordinates)
    if(points_on_rectangle(coordinates, 0, 1, 2, 3) == True):
        return False

    #Test 2 - 1 point in coordinates not on the rectangle
    coordinates = [[]]
    points = "0 0 3 0 3 2 0 2 1 1"
    modify_input(points, coordinates)
    if(points_on_rectangle(coordinates, 0, 1, 2, 3) == True):
        return False

    #Test 3 - Points at the edge of the rectangle
    coordinates = [[]]
    points = "0 0 3 0 3 2 0 2 0 0"
    modify_input(points, coordinates)
    if(points_on_rectangle(coordinates, 0, 1, 2, 3) == False):
        return False

    #Test 4 - All points can be connected to create the rectangle
    coordinates = [[]]
    points = "0 0 3 0 3 2 0 2 2 0 1 0 0 1"
    modify_input(points, coordinates)
    if(points_on_rectangle(coordinates, 0, 1, 2, 3) == False):
        return False
    return True

#A tester method to check on the functionality of form_rectangle method
def test_form_rectangle():
    #Test 1 - A rectangle can't be formed from all the coordinates
    coordinates = [[]]
    points = "0 0 -1 0 3 2 0 2 1 1 2 1"
    modify_input(points, coordinates)
    if(form_rectangle(coordinates) == True):
        return False
    #Test 2 - A rectangle can be formed with the coordinates
    coordinates = [[]]
    points = "0 0 3 2 0 2 2 0 1 0 3 0 0 1"
    modify_input(points, coordinates)
    if(form_rectangle(coordinates) == False):
        return False
    return True

#A function to call all the tester method
def tester():
    print(f'test_check_input: {test_check_input()}')
    print(f'test_is_rectangle: {test_is_rectangle()}')
    print(f'test_is_between: {test_is_between()}')
    print(f'test_points_on_rectangle: {test_points_on_rectangle()}')
    print(f'test_form_rectangle: {test_form_rectangle()}')

#main function
def main():
    tester()
    print('\n*********************************************************************************************')
    coordinates = [[]]
    print('Input your (x, y) coordinates separated with space (Integers Only).\nExample: suppose ' + 
    'your coordinates are [(2,4), (3,5), (4,6), (5,7)], enter 2 4 3 5 4 6 5 7')
    
    points = input()
    if check_input(points) == False:
        return
    modify_input(points, coordinates)
    if form_rectangle(coordinates) == True:
        print('Rectangle can be made from the coordinates given')
    else:
        print('Rectangle can\'t be made from the coordinates given')
    

if __name__=='__main__':
    main()