# ============================================================
#   Student Record Management System
#   Console-Based Application
# ============================================================

students = []   # Global list that holds all student dictionaries


# ─────────────────────────────────────────────
# HELPER: assign grade from average mark
# ─────────────────────────────────────────────
def get_grade(average):
    """Return letter grade based on average marks."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# ─────────────────────────────────────────────
# FUNCTION 1 – Add a student
# ─────────────────────────────────────────────
def add_student():
    """Collect student info, build a dictionary, and append to students list."""
    print("\n" + "=" * 45)
    print("         ADD NEW STUDENT")
    print("=" * 45)

    name = input("Enter Student Name      : ").strip()
    if not name:
        print("  [!] Name cannot be empty.")
        return

    roll = input("Enter Roll Number        : ").strip()
    if not roll:
        print("  [!] Roll number cannot be empty.")
        return

    # BONUS: Prevent duplicate roll numbers
    for s in students:
        if s["roll"].lower() == roll.lower():
            print(f"  [!] Roll Number '{roll}' already exists. Duplicates not allowed.")
            return

    subjects = ["Math", "English", "Science", "History", "Computer"]
    marks = []

    print(f"\n  Enter marks (0–100) for {name}:")
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"    {subject:<10}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("      [!] Please enter a value between 0 and 100.")
            except ValueError:
                print("      [!] Invalid input. Enter a numeric value.")

    total   = sum(marks)
    average = total / len(marks)
    grade   = get_grade(average)

    student = {
        "name"   : name,
        "roll"   : roll,
        "marks"  : marks,
        "total"  : total,
        "average": round(average, 2),
        "grade"  : grade,
    }

    students.append(student)
    print(f"\n  ✔  Student '{name}' added successfully! | Grade: {grade}")


# ─────────────────────────────────────────────
# FUNCTION 2 – View all students
# ─────────────────────────────────────────────
def view_all_students():
    """Display complete details of every student in a formatted table."""
    print("\n" + "=" * 75)
    print("                        ALL STUDENT RECORDS")
    print("=" * 75)

    if not students:
        print("  No students found. Please add students first.")
        return

    subjects = ["Math", "Eng", "Sci", "His", "Comp"]
    header   = f"  {'Roll':<10} {'Name':<20} " + " ".join(f"{s:<6}" for s in subjects) + \
               f"  {'Total':<8} {'Avg':<8} {'Grade'}"
    print(header)
    print("  " + "-" * 71)

    for s in students:          # for loop – display all students
        marks_str = " ".join(f"{m:<6.1f}" for m in s["marks"])
        print(f"  {s['roll']:<10} {s['name']:<20} {marks_str}  {s['total']:<8.1f} {s['average']:<8.2f} {s['grade']}")

    print("=" * 75)
    print(f"  Total students: {len(students)}")


# ─────────────────────────────────────────────
# FUNCTION 3 – Search student by Roll Number
# ─────────────────────────────────────────────
def search_student():
    """Search for a student by roll number and display their details."""
    print("\n" + "=" * 45)
    print("         SEARCH STUDENT")
    print("=" * 45)

    if not students:
        print("  No students found. Please add students first.")
        return

    roll = input("  Enter Roll Number to search: ").strip()
    subjects = ["Math", "English", "Science", "History", "Computer"]

    for s in students:          # for loop – searching
        if s["roll"].lower() == roll.lower():
            print("\n  ── Student Found ─────────────────────────")
            print(f"  Name        : {s['name']}")
            print(f"  Roll Number : {s['roll']}")
            print(f"  Marks       :")
            for subject, mark in zip(subjects, s["marks"]):
                print(f"    {subject:<12}: {mark:.1f}")
            print(f"  Total       : {s['total']:.1f}")
            print(f"  Average     : {s['average']:.2f}")
            print(f"  Grade       : {s['grade']}")
            print("  ──────────────────────────────────────────")
            return

    print(f"  [!] No student found with Roll Number '{roll}'.")


# ─────────────────────────────────────────────
# FUNCTION 4 – Class statistics
# ─────────────────────────────────────────────
def class_statistics():
    """Show total students, class average, highest & lowest scorer, and grade distribution."""
    print("\n" + "=" * 45)
    print("         CLASS STATISTICS")
    print("=" * 45)

    if not students:
        print("  No students found. Please add students first.")
        return

    total_students  = len(students)
    class_avg       = sum(s["average"] for s in students) / total_students
    highest_scorer  = max(students, key=lambda s: s["total"])
    lowest_scorer   = min(students, key=lambda s: s["total"])

    print(f"  Total Students   : {total_students}")
    print(f"  Class Average    : {class_avg:.2f}")
    print(f"  Highest Scorer   : {highest_scorer['name']} ({highest_scorer['total']:.1f})")
    print(f"  Lowest Scorer    : {lowest_scorer['name']} ({lowest_scorer['total']:.1f})")

    # BONUS: Grade distribution
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in students:          # for loop
        grade_counts[s["grade"]] += 1

    print("\n  ── Grade Distribution ────────────────────")
    for grade, count in grade_counts.items():
        bar = "█" * count
        print(f"    {grade} : {bar} ({count})")
    print("  ──────────────────────────────────────────")


# ─────────────────────────────────────────────
# BONUS FUNCTION – Update marks of a student
# ─────────────────────────────────────────────
def update_student():
    """Allow user to update marks for an existing student."""
    print("\n" + "=" * 45)
    print("         UPDATE STUDENT MARKS")
    print("=" * 45)

    if not students:
        print("  No students found. Please add students first.")
        return

    roll = input("  Enter Roll Number to update: ").strip()
    subjects = ["Math", "English", "Science", "History", "Computer"]

    for s in students:          # for loop – searching to update
        if s["roll"].lower() == roll.lower():
            print(f"\n  Updating marks for {s['name']}. Enter new marks (0–100):")
            new_marks = []
            for subject in subjects:
                while True:
                    try:
                        mark = float(input(f"    {subject:<12}: "))
                        if 0 <= mark <= 100:
                            new_marks.append(mark)
                            break
                        else:
                            print("      [!] Please enter a value between 0 and 100.")
                    except ValueError:
                        print("      [!] Invalid input.")

            s["marks"]   = new_marks
            s["total"]   = sum(new_marks)
            s["average"] = round(s["total"] / len(new_marks), 2)
            s["grade"]   = get_grade(s["average"])
            print(f"\n  ✔  Marks updated! New Average: {s['average']} | Grade: {s['grade']}")
            return

    print(f"  [!] No student found with Roll Number '{roll}'.")


# ─────────────────────────────────────────────
# BONUS FUNCTION – Sort students by total marks
# ─────────────────────────────────────────────
def sort_students():
    """Display students sorted by total marks (descending)."""
    print("\n" + "=" * 55)
    print("      STUDENTS RANKED BY TOTAL MARKS (High → Low)")
    print("=" * 55)

    if not students:
        print("  No students found.")
        return

    sorted_list = sorted(students, key=lambda s: s["total"], reverse=True)

    print(f"  {'Rank':<6} {'Roll':<12} {'Name':<22} {'Total':<10} {'Grade'}")
    print("  " + "-" * 51)
    for rank, s in enumerate(sorted_list, start=1):
        print(f"  {rank:<6} {s['roll']:<12} {s['name']:<22} {s['total']:<10.1f} {s['grade']}")
    print("=" * 55)


# ─────────────────────────────────────────────
# MAIN MENU – while loop keeps program running
# ─────────────────────────────────────────────
def main():
    print("\n  ╔══════════════════════════════════════════╗")
    print("  ║   STUDENT RECORD MANAGEMENT SYSTEM      ║")
    print("  ╚══════════════════════════════════════════╝")

    while True:         # while loop – runs until Exit
        print("\n  ┌─────────────────────────────────┐")
        print("  │           MAIN MENU             │")
        print("  ├─────────────────────────────────┤")
        print("  │  1. Add Student                 │")
        print("  │  2. View All Students           │")
        print("  │  3. Search Student by Roll No.  │")
        print("  │  4. Class Statistics            │")
        print("  │  5. Update Student Marks        │")
        print("  │  6. Sort Students by Total Marks│")
        print("  │  7. Exit                        │")
        print("  └─────────────────────────────────┘")

        choice = input("\n  Enter your choice (1–7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_statistics()
        elif choice == "5":
            update_student()
        elif choice == "6":
            sort_students()
        elif choice == "7":
            print("\n  Goodbye! Exiting the program.\n")
            break
        else:
            print("  [!] Invalid choice. Please enter a number between 1 and 7.")


# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
