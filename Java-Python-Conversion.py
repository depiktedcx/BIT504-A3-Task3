import sys
#constant storing PI
PI = 3.14159
#return the square of any number
def square(number):
    return number * number
#return the area of any circle
def circle(size):
    return PI * square(size)
#return whether the parsed number is a palindrome
def palindrome(number):
    #turn number into a string and then into an array
    strList = list(str(number))
    #reverse the array
    strList.reverse()
    #blank string to store the reversed string
    revString = ""
    #loop through the elements of the array and add to the blank string
    for j in range(0, len(strList)):
        revString += strList[j]
    #turn the reversed string to an integer
    revString = int(revString)
    #compare the value of the reversed string to the original number
    if(number != revString):
        return False
    else:
        return True
#loop forever until broken
while(True):
    try:
        #output a prompt and store the user's input into selection removing any blank spaces
        selection = int(input("""Calculations
1. Calculate area of a square
2. Calculate area of a circle
3. Display palindromes up to 1,000
4. Exit program
>""").replace(' ',''))
        #python equivalent of switch case
        match selection:
            #get user input for square size
            case 1:
                size = int(input("""Area of a square
Enter width of square (cm): """).replace(' ',''))
                print("The area of a square of", size, "cm =", square(size), "cm squared")
            #get user input for circle size
            case 2:
                size = int(input("""Area of a circle
Enter radius of circle (cm): """).replace(' ',''))
                print("The area of a circle of", size, "cm =", circle(size), "cm squared")
            #return all palindromes from 0-1000
            case 3:
                for i in range(0,1000):
                    if(palindrome(i)):
                        print(i)
            #exit the program
            case 4:
                print("Exiting...")
                sys.exit()
            #catch any other inputs and display this error message
            case _:
                print("Invalid option")
    #if anything execpt a number is entered, display this error message
    except ValueError:
        print("Invalid option")
