import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self, courses):
        marks_list = []
        credits_list = []
        
        for course in courses:
            if course.id in self.marks:
                marks_list.append(self.marks[course.id])
                credits_list.append(course.credits)
                
        if len(credits_list) > 0 and sum(credits_list) > 0:
            marks_arr = np.array(marks_list)
            credits_arr = np.array(credits_list)
            self.gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
        else:
            self.gpa = 0.0
        return self.gpa


class Course:
    def init(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits


class SchoolManagement:
    def init(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num = int(input("Enter number of students: "))
        for i in range(num):
            print(f"\nStudent {i+1}:")
            s_id = input("ID: ").strip()
            name = input("Name: ").strip()
            dob = input("DoB (DD/MM/YYYY): ").strip()
            self.students.append(Student(s_id, name, dob))

    def input_courses(self):
        num = int(input("Enter number of courses: "))
        for i in range(num):
            print(f"\nCourse {i+1}:")
            c_id = input("ID: ").strip()
            name = input("Name: ").strip()
            credits = int(input("Credits: ").strip())
            self.courses.append(Course(c_id, name, credits))

    def input_marks(self):
        if not self.courses or not self.students:
            print("Please input students and courses first!")
            return

        print("\nSelect a course:")
        for idx, c in enumerate(self.courses):
            print(f"{idx+1}. {c.name} ({c.id}) - Credits: {c.credits}")
            
        c_id = input("Course ID: ").strip()
        course = next((c for c in self.courses if c.id == c_id), None)
        if not course:
            print("Invalid Course ID!")
            return

        for s in self.students:
            raw_mark = float(input(f"Mark for {s.name} ({s.id}): "))
            floored_mark = math.floor(raw_mark * 10) / 10
            s.marks[course.id] = floored_mark

    def calculate_all_gpa(self):
        for s in self.students:
            s.calculate_gpa(self.courses)

    def sort_students_by_gpa(self):
        self.calculate_all_gpa()
        self.students.sort(key=lambda s: s.gpa, reverse=True)

    def display_students(self):
        self.sort_students_by_gpa()
        print("\n" + "="*50)
        print(f"{'ID':<10} | {'Name':<20} | {'DoB':<12} | {'GPA':<5}")
        print("="*50)
        for s in self.students:
            print(f"{s.id:<10} | {s.name:<20} | {s.dob:<12} | {s.gpa:.2f}")
        print("="*50)


def main():
    system = SchoolManagement()
    while True:
        print("\nSTUDENT MARK MANAGEMENT SYSTEM")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Show Student List sorted by GPA")
        print("0. Exit")
        
        choice = input("Your choice: ").strip()
        if choice == '1':
            system.input_students()
        elif choice == '2':
            system.input_courses()
        elif choice == '3':
            system.input_marks()
        elif choice == '4':
            system.display_students()
        elif choice == '0':
            break
        else:
            print("Invalid choice!")

if name == "main":
    main()