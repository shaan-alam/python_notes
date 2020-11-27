# Theory class

# strongly typed and loosely typed
# Python is loosely typed language unlinke C++, JAVA

# Control Structure
# if statement

# if condition: # it will result either True or False 
#   <statement>


marks = eval(input("Enter your marks: "))
grade= ''

if marks >= 90:
    grade = 'A'
    print ("Grade = ", grade)
elif  marks >= 70:
    grade = 'B'
    print ("Grade = ", grade)
elif marks >= 50:
    grade = 'C'
    print ('Grade = ', grade)
elif marks >= 40:
    grade = 'D'
    print ("Grade = ", grade)
else:
    grade = 'E'
    print ('Grade = ', grade)
