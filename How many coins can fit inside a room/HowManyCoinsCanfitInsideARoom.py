from os import system

def main():
    system("cls")
    
    container = input("What do you want to fill the room with?\n: ")
    length = float(input(f"How long is the {container}?\n: "))
    width = float(input(f"How wide is it?\n: "))
    height = float(input(f"What is the height of {container}?: "))
    container_volume = length * width * height
    
    filler = input("Shape of the {container}:\n 1.Square-Box\n 2.Rectangle-Box\n 3.Cylinder\n 4.Sphere\nEnter the number: ") 
    if filler == '1':
        length = float(input("Enter length of the room: "))
        height = float(input("Enter height of the room: "))
        filler_volume = (length*2) * height
        unit = "Square-Boxes"

    elif filler == '2':
        width = float(input("Enter width of the room: "))
        length = float(input("Enter length of the room: "))
        height = float(input("Enter height of the room: "))
        filler_volume = width * length * height
        unit = "Rectangle-Boxes"

    elif filler == '3':
        Pi = 3.141592653589793
        R_squared = float(input("Enter the diameter: "))**2
        height = float(input("Enter the height: "))
        filler_volume = (Pi*R_squared) * height
        unit = "Cylinders"

    elif filler == '4':
        Pi = 3.141592653589793
        R_cube = float(input("Enter the diameter: "))**3
        filler_volume = 4/3 * (Pi*R_cube)
        unit = "Spheres"

    total_fillers = container_volume/filler_volume
    return total_fillers, container, unit


total_fillers, container, unit = main()
print(f"\n\n{round(total_fillers):,} {unit} can fit inside {container}.\n")