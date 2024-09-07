  #!/usr/bin/env python3

class Dog:
    # Instance method definition
    def bark(self):
        # Print "Woof!" with correct capitalization
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

# Creating an instance of the Dog class
fido = Dog()
fido.bark()
fido.sit()

# Creating a second instance of the Dog class
snoopy = Dog()
snoopy.bark()
snoopy.sit()