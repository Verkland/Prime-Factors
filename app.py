from tkinter import *
from primefactors import *

# Configure window
root = Tk()
root.geometry("500x200")
root.resizable(False, False)
root.title('Prime Factors')

# Initialize and pack label with instructional text
info = Label(root, text="Please enter a number that you would like to break down into its primes")
info.pack()

# Initialize, pack and focus keyboard on the input box
inputBox = Entry()
inputBox.pack()
inputBox.focus()

# Function to submit input and call function
# to find prime factors if the input passes the checks
def submit():
    number = 0
    
    try:
        # We want an int ...
        number = int(inputBox.get())
        
        # ... but if it is not greater than 1, we output a warning
        if number < 2:  
            output = "Please only enter a number that is greater than 1"
            
        # If the int IS greater than 1, we find the prime factors
        # and load the result in a variable
        else:
            factors = str(find_prime_factors(number))
            output = "Prime factors are: " + factors
    
    except ValueError:
        # if not an int, print message and ask for input again
        output = "Please only enter a positive integer"
        
    # After we have either loaded prime factors, a warning or an exception
    # into the output variable, we output it to the result label    
    finally:
        result.config(text = output)
    
# Initialize and pack submit button    
submitButton = Button(root, text="Calculate and celebrate", command=submit)
submitButton.pack()

# Initialize and pack result label
result = Label(root, text='')
result.pack()

# Run the app loop
root.mainloop()