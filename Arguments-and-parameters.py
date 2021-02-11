#This program will output a song "Old McDonald" 
#and with functions that change the animal and the sound

#This function will print out the Title. 
def title():
    print("Old McDonald")
    print("")

#This function will print out the verse of the song. 
def verse(animal, sound):
    print("Old McDonald had a farm, E-I-E-I-O")
    print("And on that farm he had a " + animal + ", E-I-E-I-O.")
    print("With a " + sound + "-" + sound + " here, and a " + sound + "-" + sound + " there.")
    print("Here a " + sound + ", there a " + sound + ", everywhere a " + sound + "-" + sound + ".")
    print("Old McDonald had a farm, E-I-E-I-O")
    print("")

#This function will prompt the user what animal in the song and what sound. 
def newVerse():
    animal = str(input("Enter an animal: "))
    sound = str(input("Enter the sound the horse makes: "))
    #This will print out the information gathered.
    print("Old McDonald had a farm, E-I-E-I-O")
    print("And on that farm he had a " + animal + ", E-I-E-I-O.")
    print("With a " + sound + "-" + sound + " here, and a " + sound + "-" + sound + " there.")
    print("Here a " + sound + ", there a " + sound + ", everywhere a " + sound + "-" + sound + ".")
    print("Old McDonald had a farm, E-I-E-I-O")
    print("")

#This is the main  function
def main():
    title()
    verse("chicken", "cluck")
    verse("cow", "moo")
    verse("duck", "quack")
    newVerse()

    #This is the "Doit again" part. 
    #This will ask the user if he/she want a fifth verse.
    yes = "yes"
    no = "no"
    answer = str(input("Do you want to have a fifth verse (yes/no)? "))
    if answer == yes:
        newVerse()
    elif answer == no:
        print("")
    else:
        newVerse()
main()