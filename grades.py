# Name: Matthew Weeks
# Prog Purpose: This program computes grades for students using a
#   Python LIST of data in Python DICTIONARIES (as student records)
#   Each student has 3 graded items: Homework, Midterm exam, and Final exam.
#   Each item is worth 100 points.
#   The student's final grade is the average of the three graded items.

stu = [
    {'name' : "Anderson, Manuel" ,
     'hw' : 89,
     'mid_exam' : 92,
     'fin_exam' : 94,
     'fin_grade' : 0,
     'ltr_grade' : "X",
     },

    {'name' : "Thompson, Yani",
     'hw' : 63,
     'mid_exam' : 74,
     'fin_exam' : 59,
     'fin_grade' : 0,
     'ltr_grade' : "X",
     },

    {'name' : "Ortiz, Graciela" ,
     'hw' : 81,
     'mid_exam' : 76,
     'fin_exam' : 79,
     'fin_grade' : 0,
     'ltr_grade' : "X",
     },

    {'name' : "Wilson, Danielle" ,
     'hw' : 100,
     'mid_exam' : 89,
     'fin_exam' : 94,
     'fin_grade' : 0,
     'ltr_grade' : "X",
     },
    ]

def main() :
    calculate_grades()
    print_grade_report()

def calculate_grades():
    for i in range (len(stu)):
        sum_grades = stu[i]['hw'] + stu[i]['mid_exam'] + stu[i]['fin_exam']
        stu[i]['fin_grade'] = sum_grades / 3

        finalgr = stu[i]['fin_grade']
        if finalgr >= 90:
            lettergrade = 'A'
        elif finalgr >= 80:
            lettergrade = 'B'
        elif finalgr >= 70:
            lettergrade = 'C'
        elif finalgr >= 60:
            lettergrade = 'D'
        else:
            lettergrade = 'F'
        stu[i]['ltr_grade'] = lettergrade

def print_grade_report() :
    print("*************** CSC 230 Grade Report ************")
    print("Name                    HW\tMID\tFIN\tFINAL GRADE")
    for i in range(len(stu)):
        sname = '{0:<18}'.format(stu[i]['name'])
        hw = str(stu[i]['hw'])
        midex = str(stu[i]['mid_exam'])
        finex = str(stu[i]['fin_exam'])
        fingrade = format(stu[i]['fin_grade'], '6,.2f')
        print (sname + "\t" + hw + "\t" + midex + "\t" +finex + "\t" + fingrade + " "+ stu[i]['ltr_grade'])
                            

main()
