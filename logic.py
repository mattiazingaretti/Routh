

def initWithUsage():
    print("Usage: Insert first and second row in comma separated values/params ")
    fr = input("Enter first row of Routh table : ")
    sr = input("Enter second row of Routh table : ")
    first_row = fr.split(',')
    second_row = sr.split(',')

    print("Received : \n", first_row, "\n :", second_row)

    return



