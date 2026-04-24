# Esoteric ART Language 
Stack-based esolang with an artistic theme and paint/draw keywords.  
Each command represents a creative action that manipulates data on a stack to create art. The interpreter is in Python and reads a program file line by line, parses, and executes using a stack.  

## How to run programs
------
python interpreter.py programs/helloworld.txt
python interpreter.py programs/cat.txt
python interpreter.py programs/isItEven.txt
python interpreter.py programs/multiply.txt
python interpreter.py programs/repeater.txt
python interpreter.py programs/reverseString.txt
python interpreter.py programs/isItPalindrome.txt


1. Clone the project into your own directory or folder.
```
git clone https://github.com/OC-ComputerScience/tutorial-frontend-vue3-simple.git
```

2. Install the python if you havent.
```
winget install Python.Python.3
restart vs code if needed.
now you should be able to run the programs with the python interpreter.py above.
```


4. Compile and run the project locally.
```
After running a program file: python interpreter.py programs/<programName>.txt
You should be able to give your input depending on what program you run:
Like : isItPalindrome         //takes string input and checks it using esolang custom commands
Not: helloworld              //This only prints the string hello world, not take input.
```

5. Keywords and Operations
```
PAINT - pushes string on stack
BRUSHWEIGHT - pushes int on stack
TRACE - Duplicates top stack slot
FLIP - swaps the top two stack slots
ERASE - removes the top stack slot
SKETCH - takes input and pushes it on stack
SHOWOFF - prints top stack slot
'BLEND' or '+'' - concatenates two strings
'MIX' or '*' - Multiplies two numbers
'Residue' or '%' - Does modulo on two numbers
MERGE - joins two strings together
INVERT - reverses a string
STIPPLE - Repeats a character or string however many times you allow (takes string then int amount)
STEADYHAND - Checks if number is even
MIRROR - Checks if the string is the same forward and backwards(returns true/false)
```





Expand logic to actually make a palindrome checking program file instead of putting built in function

Mirror
Repeater
MIX
BLEND
RESIDUE
MERGE