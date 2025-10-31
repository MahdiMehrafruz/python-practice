num = int (input ("Enter the number of lessons: "))
if num == 0 :
    print ("Error 0 lessons!!! ")
    exit()

grades = []
for i in range ( num ):
    score = float (input (f"Enter ur grade fo lesson {i + 1} : "))
    grades.append(score)
 

def avg (grades) :
    total = sum( grades )
    count = len( grades )
    avg = total / count 
    return avg

def status (avg) :
    if avg >= 17 :
        return "Perfect"
    elif avg >= 12 :
        return "Passed"
    else : 
        return "Probation"
    

gpa = avg(grades)
print (f"Ur status is : { status (gpa) }")
print (f"Ur avg is:  {gpa:.2f}")