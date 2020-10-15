#sphere.py
#Craig Maitner

import math
#Defines a new user created class called Sphere.
class Sphere:
    
    def __init__(self , radius):
        self.radius = radius
        self.surfaceArea = (4/3) * math.pi * self.radius ** 3
        self.volume = 4 * math.pi * self.radius ** 2
        
    def getRadius(self):
        return self.radius
        
    def getSurfaceArea(self):
        return self.surfaceArea
        
    def getVolume(self):
        return self.volume

print("This program demonstrates the use of a user created Sphere class.")

#Begin main function.
def main():
    #Try the following code block with the provided input.
    try:
        #Gets the sphere radius from the user as input.
        radius = float(input("\nWhat is the radius of your sphere: "))

        #Invokes the Sphere class, using the given radius as input.
        newSphere = Sphere(radius)

        #Formats the surface area and volume of the sphere to one decimal place.
        print("\nSurface Area: ","{0:.1f}".format(newSphere.getSurfaceArea()))
        print("Volume: ","{0:.1f}".format(newSphere.getVolume()))
    
    #Catch a thrown ValueError expection upon improper user input.
    except ValueError:
            print("You must enter a numeric value.")
    
    #Checks if the user would like to generate a new sphere.
    new = input("\nWould you like a new sphere? (y/n): ")
    
    if new == 'y':
        print("Generating new sphere...")
        main()
    elif new == 'n':
        print("Run again to generate a new sphere.")
    else:
        print("Invalid respone.")

if __name__ == '__main__':
    main()