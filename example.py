def main():
    # we are creating our class_b object
    class_b = ClassB()
    # getting the input from the user
    number = input("Please enter your number")
    # passing the number variable into our class_b method
    class_b.print_number(number)


main()

class ClassB:
    # this does not matter
    def __init__(self):
        pass
    # created our method
    def print_number(self, number):
        # creating a method called callC that is allowing us to initalise our number parameter
        # inside of the Class C class
        classC = ClassC(number)
        # because we have now initalised our object we can now print the value that has been passed in
        print(classC.get_number())


class ClassC:
    # here we initalise our classC object
    def __init__(self, number):
        # this turns self.number into our inputted number
        self.number = number
    # this then returns that number
    def get_number(self):
        return self.number
