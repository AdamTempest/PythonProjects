# print out the color of the specific square on the chessboard
# Example; 
# input: e4
# output: white

def whatColor(position):
    # even numbers are white if the column is a c e g
    if position[0].lower() in 'aceg':
        if position[1] in '2468':
            return 'white'
        else:
            return 'black'
    else: # otherwise even numbers are black
        if position[1] in '2468':
            return 'black'
        else:
            return 'white'

def isValid(position):
    if len(position) > 2:
        return False
    
    # check if position is valid
    cond1 = position[0].lower() in 'abcdefgh'
    cond2 = position[1] in '12345678'
    
    if cond1 and cond2:
        return True
    else:
        return False

if __name__ == "__main__":
    pos = input("Please Enter The position of the square: ")
    while not isValid(pos):
        print('Position invalid! Please try again.')
        pos = input("Enter The position of the square: ")
    print(f'The square is {whatColor(pos)}.')