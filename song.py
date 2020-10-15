#song.py
#Demonstrates user created functions by printing lyrics to a song.

print("This program demonstrates the use of functions by outputing the lyrics to Old MacDonald.")

#Defines a function titled "line".
def line():                                                                   
    print("Old MacDonald had a farm, Ee-igh, Eeigh, Oh!")

#Defines a new function titled "animal".
def animal(animal, sound):                                                    
    line()
    print("And on that farm he had a", animal + ", Eeigh, Eeigh, Oh!")
    print("With a ", sound + ",", sound + " here and a ", sound + ",", sound + " there")
    print("Here a ", sound + ", there a ", sound + ", everywhere a ", sound + ",", sound)
    line()

#Begin "main" function.
def main():                                                                  
    print()
    animal("cow", "moo")                                                         
    print()
    animal("mouse", "squeek")                                                  
    print()
    animal("pig", "oink")                                                       
    print()
    animal("sheep", "ba")                                                      
    print()
    animal("chicken","cluck")                                           
main()
