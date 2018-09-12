# Function that parses line and returns DRE, name and grade
def __parseLine (text):
    data_list = text.split("-")
    return data_list[0], data_list[1], int(data_list[2])

# Function that parses all lines in a file and returns a dictionary where keys=DREs and values=tuple(name, grade)
def generateDict (text_file):
    f = open(text_file, 'r')
    lines = f.readlines()
    gradeDict = {}
    for line in lines:
        dre, name, grade = __parseLine(line)
        gradeDict [dre] = (name, grade)
    return gradeDict