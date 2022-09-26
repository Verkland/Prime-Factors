from tkinter import *
from primefactors import *
from randomfact import randomFact

# Configure window
root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title('Prime Factors')

# Create a label for the title
titleLabel = Label(root, text="Prime Factors", font=("Helvetica", 24))
titleLabel.pack(pady=20)

# Create a label for the random fact
factLabel = Label(root, text="", font=("Helvetica", 12))
factLabel.pack(pady=10)

# Initialize and pack label with instructional text
info = Label(root, text="Please enter a number", font=("Helvetica", 12))
info.pack()

# Initialize, pack and focus keyboard on the input box
inputBox = Entry()
inputBox.pack()
inputBox.focus()

# Initialize image index
imageIndex = 0

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
            output = "The prime factors are: " + factors
    
    except ValueError:
        # if not an int, print message and ask for input again
        output = "Please only enter a positive integer"
        
    # After we have either loaded prime factors, a warning or an exception
    # into the output variable, we output it to the result label    
    finally:
        result.config(text = output, font=("Helvetica", 14))


# Bind the enter key to the submit, nextImage, hideQuestionMark and randomFact function
root.bind('<Return>', lambda event: [submit(), nextImage(), hideQuestionMark(), factLabel.config(text="Fun fact: " + randomFact())])

# Bind the numpad enter key to the submit, nextImage, hideQuestionMark and randomFact function
root.bind('<KP_Enter>', lambda event: [submit(), nextImage(), hideQuestionMark(), factLabel.config(text="Fun fact: " + randomFact())])
        
# Initialize and pack a button called submitButton that executes both the submit function and the nextImage function
submitButton = Button(root, text="Find Prime Factors", command=lambda: [submit(), nextImage(), hideQuestionMark(), factLabel.config(text="Fun fact: " + randomFact())])
submitButton.pack(pady=10)

# Initialize and pack result label
result = Label(root, text='', pady=20)
result.pack()

# Display imageLabel and pack it
imageLabel = Label(root)
imageLabel.pack()

# Initialize function to display the next image in the image directory of the project
def nextImage():
    # Load images from directory
    import os
    images = os.listdir("images")
    
    # Pick the next image
    global imageIndex
    imageIndex += 1
    if imageIndex >= len(images):
        imageIndex = 0
    image = images[imageIndex]
    
    # Display the image
    image = PhotoImage(file="images/" + image)
    image = image.subsample(2, 2)
    imageLabel.config(image=image)
    imageLabel.image = image

# Display and pack an image of a question mark from the images directory
questionMark = PhotoImage(file="question.png")
questionMark = questionMark.subsample(2, 2)
questionMarkLabel = Label(root, image=questionMark)
questionMarkLabel.pack()

# Initialize function that hides question mark label
def hideQuestionMark():
    questionMarkLabel.pack_forget()

# Display a random fact at startup
factLabel.config(text="Fun fact: " + randomFact())

# Run the app loop
root.mainloop()