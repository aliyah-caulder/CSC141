# Code stores the meanings of five python terms and prints them with their definitions using a loop

glossary = {
    'print' : 'A function that prints strings or numerals.' , 
    'variable' : 'A way to store strings or values.' , 
    'list' : 'Stores multiple strings or values into a variable.' , 
    'for loop' : 'Loops the same code for each variable in a list or range.' , 
    'if statement' : 'Executes code based on whether a conditional statement is true or not.' ,
    'while loop' : 'Executes code repeatedly until the conditional value is no longer true or until there is a break in the code.' ,
    'boolean value' : 'A value that has two possible values, true or false' , 
    'input' : 'Data entered by the user' , 
    'tuple' : 'A set of values that cannot be changed, unlike a list.' ,
    'syntax' : 'The format of characters which must be entered into code to make it work.'
    }

for key, value in glossary.items():
    print(f"\n{key.title()}: {value}")