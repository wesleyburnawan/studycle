"""
Modify points to a list of list containing x, y coordinates to coordinates
Return number of x, y coordinates in coordinates
"""
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
    return size

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


#main function
def main():
    coordinates = [[]]
    points = input('Input your x, y coordinates separated with space.\nExample: suppose ' + 
    'your coordinates are [(2,4), (3,5), (4,6), (5,7)], enter 2 4 3 5 4 6 5 7.\n')
    if check_input(points) == False:
        return
    size = modify_input(points, coordinates)

if __name__=='__main__':
    main()