# Student Marks Calculator & Report Card Generator

A Python application that calculates student marks, generates grades, and produces a comprehensive report card.

## Features ✅

- ✅ Enter marks for each subject
- ✅ Calculate Total Marks
- ✅ Calculate Average Marks
- ✅ Find Highest Marks
- ✅ Find Lowest Marks
- ✅ Assign Grades (A/B/C/D/F)
- ✅ Check Pass/Fail Status
- ✅ Print a Report Card

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/kamiltirkey/student_marks_calculator.git
cd student_marks_calculator
```

2. Run the script:
```bash
python calculator/student_marks_calculator_v3.py
```

3. Enter marks for each subject when prompted

## Grading System

| Marks Range | Grade |
|------------|-------|
| 90 - 100  | A     |
| 75 - 89   | B     |
| 60 - 74   | C     |
| 40 - 59   | D     |
| Below 40  | F     |

**Pass/Fail**: 40+ marks = Pass, Below 40 = Fail

## Sample Output

```
Enter marks for English: 85
=========================
STUDENT REPORT CARD
=========================

Subject      Marks    Grade    Status

English      85       B        Pass

Enter marks for Math: 92
=========================
STUDENT REPORT CARD
=========================

Subject      Marks    Grade    Status

English      85       B        Pass
Math         92       A        Pass

Enter marks for Science: 78
=========================
STUDENT REPORT CARD
=========================

Subject      Marks    Grade    Status

English      85       B        Pass
Math         92       A        Pass
Science      78       B        Pass

Report Card
=========================
Total Marks    :  255
Average Marks  :  85.00
Highest Marks  :  92 (Math)
Lowest Marks   :  78 (Science)
Result         :  Pass
=========================
```

## File Structure

```
student_marks_calculator/
├── calculator/
│   └── student_marks_calculator_v3.py
└── README.md
```

## Requirements

- Python 3.x

## License

This project is open source and available for educational purposes.
