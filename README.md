# store-student-marks-in-a-python-list
This program is capable of getting user inputs and save in a python list.

program will take the marks (for three assessments Quiz1 (20%), Quiz2(30% and Final(50%)) of all the students of a unit as input and stores all the detail in a list. Your program should have following features and constrains:
• Check the input validity
• Compute the total marks and letter grade. Use the Murdoch university grade conversion table to calculate the letter grade.
• Keep taking the input unless a negative or zero is given as the input for student ID
• Save the data in following format:
[st_ID, Q1_mark, Q2_mark, Final_mark, Total, Letter grade]
• Display the whole list.
A typical input output screenshot might be as follows:
Student ID:1001
Enter Q1: 20
Enter Q2: 25
Enter Final: 40
Student ID:1002
Enter Q1: 12
Enter Q2: 2.5
Enter Final: 45
Student ID:1003
Enter Q1: 20
Enter Q2: 30
Enter Final: 32
Student ID:0
[[1001, 20.0, 25.0, 40.0, 85.0, ‘HD’], [1002, 12.0, 2.5, 45.0, 59.5, ‘P’],
