# PRIME FACTORS
#### Video Demo:  <https://youtu.be/D5T5igAyrfE>
#### Description: CS50 Final Project

Prime Factors is a small app for calculating the prime factors of a given number. The user is presented with an input box and a submit button. The user must input a positive integer. Other types of input will be rejected with a warning. Icons and emojis are used to make the app a little cuter, but this project is evidently not an exercise in beautiful user interface design. It is, however, my first Python app using Tkinter as a framework for creating a GUI. Learning to use Tkinter was my main goal of making the app as a final project for the CS50 course.

The app contains three Python files:

1) app.py handles user input and the design of the GUI. It is by far the largest of the three files, with its 111 lines of code. It imports the other two Python files, in addition to the Tkinter library. It configures the app's window and then goes on to create what Tkinter calls "labels", which are text boxes. It also creates the input box, which in Tkinter is called an Entry. If the user submits the input, using either the submit button or the enter/return key, the app goes on to check if the input is valid with try-except. It also has code to display an image, and to change it when hitting submit. Initially, I wanted to refactor that part out to its own Python file, so that app.py would consist mostly of abstract GUI building blocks. But I didn't get around to it within the time-restraints I had put on the project.

2) randomfact.py reads individual lines of fun facts from a txt-file within the project folder and returns a random one upon app startup and when the user calculates a number.

3) primefactors.py calculates and returns the prime factors of the input.

Lastly, there are a few non-code files in the project folder. There are images: one of a question mark and three happy emojis that symbolizes success. Though the happy emojis are also displayed when the user inputs the wrong kind of data, such as strings or negative numbers. I would have fixed this if I had more time. There is also a text-file with fun facts about primes and a license file that tells you that you can use the project however you would like.

To run the app, you need to run "python app.py" within the project directory.

If your goal is, like mine was, to learn a little bit about making GUIs in Python using Tkinter, you're in the perfect place. Fork the code and have fun with it. Then hit me up on Twitter @john_verkland