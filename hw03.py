"""
Name: (Sophia Bernal)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    """ updates content of grades depending on the user's input

    Updates the values inside the global variable grades (list)
    with each of the user's 5 input ints.
    If the user inputs are not digits, it prints
    "Error in read_five_ints: input string is not for an integer",
    and if the input converted to int is outside of [0,10], prints
    "Error in read_five_ints: input integer outside of range".
    """
    for idx in range ( len(grades) ):
        # for each idx in 0, 1,... 4 do:
        # check if the input is not a digit print error
        # convert to int
        # check if the int is not in the interval [0 to 10] print error
        # add the int to grades at index idx
        #First get user input for the grades 
        in_str = input("Give me the next grade in [0 to 10]:")
        #Check that the user input is only digits
        check_digit = in_str.isdigit()
        #If user input is not only digits, print error and stop
        if check_digit == False:
                print("Error in read_five_ints: input string is not for an integer")
                exit()
        #If user input is only digits, cast to integer and check that the values are between 0 and 10
        else:
            in_int = int(in_str)
            if 0<=in_int<=10:
                    grades[idx] = in_int
        #If the grades provided are not between 0 and 10, print error and stop
            else:
                print("Error in read_five_ints: input integer outside of range")
                exit()

    #Anything with this indentation is NO LONGER inside the loop


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    """
    #Collect input from the user for type of average 
    avg_method = input("Pick 'a' for mean, 'b' for median, 'c' for mode: ")
    # If user picked "a" calculate the mean for the average 
    if avg_method == "a":
        print("picked: Mean")
        average = statistics.mean(grades)
        return average
    # If user picked "b", calculate median for the average 
    if avg_method == "b":
        print("picked: Median")
        average = statistics.median(grades)
        return average
    # If user picked "c", calculate mode for the average  
    if avg_method == "c":
        print("picked: Mode")
        average = statistics.mode(grades)
        return  average
    # If user did not pick a, b, or c, print error prompt 
    else:
        print("Error in pick_averaging_method: incorrect option picked")
        exit()

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    # As user to enter either 1 or 2 
    user_pick = input("Pick '1' for print average, or '2' for plot average: ")
    # If user inputs 1 then just print the list and chosen average 
    if user_pick == "1":
        print_list_and_average(average)
    # If the user inputs 2 print grades and annotate average 
    if user_pick == "2":
        plot_grades(average)
    # If the user does not input 1 or 2 print error and stop 
    if user_pick!= "1" and user_pick!= "2":
        print("Error in pick_visualization: incorrect option picked")
        exit()
        


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
