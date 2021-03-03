
def avgMarks(marksList, passMarks):
  totalMarks = 0

  for mark in marksList:
    if mark < passMarks:
      raise Exception("Essential Repeat")

    totalMarks += mark

  return totalMarks / 3

marks = []

for x in range(3):
  mark = eval(input("Input marks : "))
  assert mark >=1 and mark <= 100, "Marks should be between 1-100"

  marks.append(mark)

passMarks = eval(input("Enter passing marks : "))
assert passMarks >=1 and passMarks <= 100, "Passing marks should be between 1-100"

print ("Average Marks = ", avgMarks(marks, passMarks))
