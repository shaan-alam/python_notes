
# percent function to calculate the percentage of the marks
def percent(marks):
  return (sum(marks) / 400) * 100

marks = [45, 78, 86, 77]
percentage1 = percent(marks) # function call here

marks = [25, 72, 16, 73]
percentage2 = percent(marks) # function call here


print (percentage1, percentage2)