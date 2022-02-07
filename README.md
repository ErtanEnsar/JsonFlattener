### Usage
- Download the neccesary files and cd to folder, if you do not have python download it from https://www.python.org/downloads/.
- To flatten nested Json object in given file, use the general form: **cat File.json | python3  Flatten.py**
- There is 3 test files included for your convenience, all called Input you can use them as such: **cat TestFiles/Input[1-3].json | python3  Flatten.py**
- The program will not run if the given Json is not valid, try and see if you can break it :)
------------
### Testing
- To run the given tests use the command: ** python -m unittest JsonFlattenerTest **

------------
### Interesting but not neccesary info
- Total Time spent on the code is 4 hours.
- JsonFlattener.py works as a module for Flatten.py
