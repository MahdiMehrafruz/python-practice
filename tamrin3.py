students_list = [
    {
         "id" : 1 ,
        "name" : "Amir" ,
        "grades" : [ 19, 12.5, 16  ]
    },

    {
        "id" : 2,
        "name" : "Setayesh",
        "grades" : [20,11.5,17]
    },
    {

        "id" : 3,
        "name" : "Taha",
        "grades" : [7,16,18.5]
    }
]


def calculate_studens_gpa (grades) :
    gpa = sum(grades) / len(grades)
    return gpa 


for student in students_list :
    avg = calculate_studens_gpa (student["grades"])
    print (f" Student name : {student['name']} ")
    print (f" GPA : {avg:.2f} \n")