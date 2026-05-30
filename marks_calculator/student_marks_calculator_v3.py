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
# List containing all subject names
subject_name = ['English', 'Math', 'Science']

# Variable to store the total marks of all subjects
total = 0

# Starting with 100 assuming maximum marks are 100
max = 0
max_subject = ''

# Starting with 100 assuming maximum marks are 100
min = 100
min_subject = ''

# If any subject is failed, this will change to FAIL
overall_result = "Pass"  

# Loop through each subject in the subjects list
report_card =[]  


# Loop through each subject in the subjects list
for subject in (subject_name):
     # Ask user to enter marks for the current subject
    marks = int(input(f'Enter marks for {subject}: '))  
    # Add current subject marks to the running total
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

## Print column headings
# <12 means left align within 12 spaces
# <8 means left align within 8 spaces

print(f"\n{'Subject':<12} {'Marks':<8} {'Grade':<8} {'Status'}")

#Loop through each row stored in report_card
for row in report_card:

        #row[0] = Subject
        #row[1] = Marks
        #row[2] = Grade
        #row[3] = Status

    print(f"\n{row[0]:<12} {row[1]:<8} {row[2]:<8} {row[3]}")


# Calculate Average Marks
average = total/len(subject_name)

print(f'\nReport Card')
print('='*25)
print(f'Total Marks    :  {total}')                 # Display total marks
print(f'Average Marks  :  {average:.2f}')           # Average Marks, with 2 decimal point
print(f'Higesht Marks  :  {max} ({max_subject})')   # Display highest marks with subject name
print(f'Lowest Marks   :  {min} ({min_subject})')   # Display lowest marks with subject name
print(f'Result         :  {overall_result}')        # Display overall pass/fail result
print('='*25)                                       #formate
print(f'\n')




