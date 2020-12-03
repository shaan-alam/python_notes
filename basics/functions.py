# Functions

def sum (start, end):
    result = 0

    for i in range(start, end):
        result += i
    
    return result

def main():
    print ("Sum from 10 to 100 : ", sum(10, 100))
    print ("Sum from 20 to 200 : ", sum(20, 200))
    print ("Sum from 30 to 300 : ", sum(30, 300))

main()



