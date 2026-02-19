# student_grade_manager_commented.py
# Beginner to Intermediate Python Project
# Features: Variables, Loops, Functions, and Intro to OOP
# Project: Student Grade Management System

# -----------------------------
# Step 1: Define OOP Classes
# -----------------------------
class Student:
    """
    Represents a single student with a name and a score.
    """
    def __init__(self, name, score):
        self.name = name          # Student's name
        self.score = score        # Student's numeric score

class Classroom:
    """
    Represents a classroom containing multiple students.
    Contains methods to add students, calculate average, and find top student.
    """
    def __init__(self):
        self.students = []  # List to store Student objects

    def add_student(self, name, score):
        """
        Adds a new Student object to the classroom.
        """
        self.students.append(Student(name, score))

    def average_score(self):
        """
        Calculates the average score of all students.
        Returns 0 if no students are in the classroom.
        """
        total = sum(student.score for student in self.students)
        return total / len(self.students) if self.students else 0

    def top_student(self):
        """
        Finds the student with the highest score.
        Returns a tuple (name, score). If no students, returns (None, None)
        """
        if not self.students:
            return None, None
        top = max(self.students, key=lambda s: s.score)
        return top.name, top.score

# -----------------------------
# Step 2: Helper Functions
# -----------------------------
def letter_grade(score):
    """
    Converts numeric score to letter grade.
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: <60
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def show_menu():
    """
    Displays the main menu to the user.
    """
    print("\n--- Classroom Menu ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Calculate Average Score")
    print("4. Show Top Student")
    print("5. Remove Student")
    print("6. Exit")

# -----------------------------
# Step 3: Main Program
# -----------------------------
def main():
    # Create a Classroom object
    classroom = Classroom()
    choice = 0  # Menu choice variable

    # Main loop: repeats until user chooses to exit
    while choice != 6:
        show_menu()  # Display menu options

        # Get user choice and validate input
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 6.")
            continue  # Skip back to menu if input invalid

        # -----------------------------
        # Menu Option 1: Add Student
        # -----------------------------
        if choice == 1:
            name = input("Enter student name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue  # Skip if name is empty
            try:
                score = int(input("Enter student score (0-100): "))
                if score < 0 or score > 100:
                    print("Score must be between 0 and 100.")
                    continue  # Skip if score out of range
            except ValueError:
                print("Please enter a valid integer score.")
                continue
            classroom.add_student(name, score)
            print(f"{name} added successfully.")

        # -----------------------------
        # Menu Option 2: View All Students
        # -----------------------------
        elif choice == 2:
            if not classroom.students:
                print("No students in the classroom yet.")
            else:
                print("\n--- Student List ---")
                for s in classroom.students:
                    # Show name, score, and letter grade
                    print(f"{s.name} - {s.score} ({letter_grade(s.score)})")

        # -----------------------------
        # Menu Option 3: Calculate Average Score
        # -----------------------------
        elif choice == 3:
            avg = classroom.average_score()
            print(f"Average Score: {avg:.2f}")  # 2 decimal places

        # -----------------------------
        # Menu Option 4: Show Top Student
        # -----------------------------
        elif choice == 4:
            name, score = classroom.top_student()
            if name:
                print(f"Top Student: {name} with score {score} ({letter_grade(score)})")
            else:
                print("No students yet.")

        # -----------------------------
        # Menu Option 5: Remove Student
        # -----------------------------
        elif choice == 5:
            name = input("Enter the name of the student to remove: ").strip()
            removed = False
            # Search for student (case-insensitive)
            for s in classroom.students:
                if s.name.lower() == name.lower():
                    classroom.students.remove(s)
                    removed = True
                    print(f"{name} removed successfully.")
                    break
            if not removed:
                print(f"Student {name} not found.")

        # -----------------------------
        # Menu Option 6: Exit
        # -----------------------------
        elif choice == 6:
            print("Exiting program. Goodbye!")

        # -----------------------------
        # Invalid Menu Choice
        # -----------------------------
        else:
            print("Invalid choice, please try again.")

# Run the main program
if __name__ == "__main__":
    main()
