

#Student Marks calulator cum report card.
'''
✅ Enter marks for each subject
✅ Calculate Total Marks
✅ Calculate Average Marks
✅ Find Highest Marks
✅ Find Lowest Marks
✅ Assign Grades (A/B/C/D/F)
✅ Check Pass/Fail
✅ Print a Report Card

'''
#subjects = 3
subject_name = ['English', 'Math', 'Science']

total = 0

max = 0
max_subject = ''

min = 100
min_subject = ''

overall_result = "Pass"

report_card =[]

for subject in (subject_name):
    #subject_name = input(f"Enter Subject {i} Name : ")
    marks = int(input(f'Enter marks for {subject}: '))
    total += marks
  
   
   #Max number:
    if marks > max:
        max = marks
        max_subject = subject

    #Min number
    if marks < min:
        min = marks
        min_subject = subject

    #Grade assignment

    if marks >= 90:
        grade = 'A' 
    elif marks >= 75:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    elif marks >= 40:
        grade = 'D'
    else:
        grade = 'F'                


    #Result Status-Pass/Fail  
    if marks >= 40:
        status = 'Pass'
    else:
        status = 'Fail'
        overall_result = "Fail"   

    #store data in  report card
    report_card.append([subject, marks, grade, status])
    
    #Print Report card
    print('='*25)
    print("STUDENT REPORT CARD")
    print('='*25)

    print(f"\n{'Subject':<12} {'Marks':<8} {'Grade':<8} {'Status'}")

    #Loop through each row stored in report_card
    for row in report_card:

        #row[0] = Subject
        #row[1] = Marks
        #row[2] = Grade
        #row[3] = Status

        print(f"\n{row[0]:<12} {row[1]:<8} {row[2]:<8} {row[3]}")



    '''print(f'Subject :{subject_name[i]} ')
    print(f'Marks: {marks}')
    print(f'Grade: {grade}')
    print(f'Result: {status}')
    print('-'*25)
   
    '''




average = total/len(subject_name)

print(f'\nReport Card')
print('='*25)
print(f'Total Marks    :  {total}')
print(f'Average Marks  :  {average:.2f}')
print(f'Higesht Marks  :  {max} ({max_subject})')
print(f'Lowest Marks   :  {min} ({min_subject})')
print(f'Result         :  {overall_result}')
print('='*25)
print(f'\n')




