# Enter the marks of 6 students and sort them

marks = []

for x in range(6):
  mark = eval(input("Enter the mark : "))
  marks.append(mark)

print ("Original marks : ", marks)

# sorting marks
marks.sort()
print ("Sorted marks : ", marks)
