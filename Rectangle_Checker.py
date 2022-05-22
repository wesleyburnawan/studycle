#Check whether the input has the right format
def check_input(points):
    points = points.replace(" ", "")
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
    points = points.replace(" ", "")
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
    pass

#A helper function for form_rectangle to determine if all points in coordinates is contained on the rectangle
def points_on_rectangle(coordinates, p1, p2, p3, p4):
    pass

#main function
def main():
    coordinates = [[]]
    points = input('Input your x, y coordinates separated with space.\nExample: suppose ' + 
    'your coordinates are [(2,4), (3,5), (4,6), (5,7)], enter 2 4 3 5 4 6 5 7.\n')
    if check_input(points) == False:
        return
    modify_input(points, coordinates)
    if form_rectangle(coordinates) == True:
        print('Rectangle can be made from the coordinates given')
    else:
        print('Rectangle can\'t be made from the coordinates given')

if __name__=='__main__':
    main()