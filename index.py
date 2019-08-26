# Create a function that will ask the user for a number. Use the function to get two numbers from the user, then pass the two numbers to a function. Add, subtract, multiple, and divide the numbers.

def main(begin):
    problem1(begin)


def problem1(add):
    question1 = int(input("Enter a number- "))
    question2 = int(input("Enter another number- "))
    print(question1, question2)
    print(question1 + question2)
    problem2(add)
def problem2(sub):
    question1 = int(input("Enter a number- "))
    question2 = int(input("Enter another number- "))
    print(question1, question2)
    print(question1 - question2)
    problem3(sub)
def problem3(mul):
    question1 = int(input("Enter a number- "))
    question2 = int(input("Enter another number- "))
    print(question1, question2)
    print(question1 * question2)
    problem4(mul)
def problem4(div):
    question1 = int(input("Enter a number- "))
    question2 = int(input("Enter another number- "))
    print(question1, question2)
    print(question1 / question2)


main("hello")
