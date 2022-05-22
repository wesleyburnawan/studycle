#Check whether the input has the right format
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

#Modify points to a list of list containing x, y coordinates to coordinates
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

"""
Check whether rectangle can be made from coordinates
"""
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
        return False
    return True

#A helper function for form_rectangle to determine if all points in coordinates is contained on the rectangle
def points_on_rectangle(coordinates, p1, p2, p3, p4):
    pass

#main function
def main():
    coordinates = [[]]
    points = input('Input your x, y coordinates separated with space (Integers Only).\nExample: suppose ' + 
    'your coordinates are [(2,4), (3,5), (4,6), (5,7)], enter 2 4 3 5 4 6 5 7.\n')
    if check_input(points) == False:
        return
    modify_input(points, coordinates)
    print(is_rectangle(coordinates, 0, 1, 2 ,3))
    # if form_rectangle(coordinates) == True:
    #     print('Rectangle can be made from the coordinates given')
    # else:
    #     print('Rectangle can\'t be made from the coordinates given')
    

if __name__=='__main__':
    main()