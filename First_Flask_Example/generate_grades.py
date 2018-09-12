# Imports
import random
from pathlib import Path

# Macros
FILENAME = 'grades.txt'
NAMES_DICT = {
    'Gabriel' : 123456789,
    'Claudio': 987654321,
    'Madruga' : 362514897
}

# Main
def __main():
    gradeFile = Path("./" + FILENAME)
    if (gradeFile.is_file()):
        print ("Grade file already exists, do you want to overwrite it? (y/N)")
        overwrite = input('-> ')
        if (overwrite == 'Y' or overwrite == 'y'):
            overwrite = True
        elif (overwrite == 'N' or overwrite == 'n'):
            overwrite = False
        else:
            overwrite = None
    else:
        overwrite = True
    if (overwrite == None):
        print ("Sorry, your input is invalid.")
    elif (overwrite == True):
        f = open(gradeFile, 'w')
        print (type(f))
        for name in NAMES_DICT:
            grade = random.randint(0,10)
            f.write("{}-{}-{}\n".format(NAMES_DICT[name], name, grade))
            print ("{} got a {}. Congratulations!".format(name, grade))

# Init
if (__name__ == "__main__"):
    __main()