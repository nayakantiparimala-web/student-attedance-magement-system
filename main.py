# Student Attendance Management System

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    with open("attendance.txt", "a") as file:
        file.write(f"{roll_no},{name},0,0\n")

    print("Student added successfully!")


def mark_attendance():
    roll_no = input("Enter Roll Number: ")
    status = input("Enter Attendance (P/A): ").upper()

    with open("attendance.txt", "r") as file:
        records = file.readlines()

    found = False
    updated_records = []

    for record in records:
        data = record.strip().split(",")

        if data[0] == roll_no:
            found = True

            name = data[1]
            present = int(data[2])
            total = int(data[3])

            total += 1

            if status == "P":
                present += 1
                print("Attendance marked as Present.")
            elif status == "A":
                print("Attendance marked as Absent.")
            else:
                print("Invalid input! Enter P or A.")
                return

            updated_records.append(f"{roll_no},{name},{present},{total}\n")
        else:
            updated_records.append(record)

    if found:
        with open("attendance.txt", "w") as file:
            file.writelines(updated_records)
    else:
        print("Student not found.")


def view_attendance():
    print("\n----- Attendance Details -----")

    with open("attendance.txt", "r") as file:
        records = file.readlines()

    if not records:
        print("No student records available.")
        return

    for record in records:
        data = record.strip().split(",")

        roll_no = data[0]
        name = data[1]
        present = int(data[2])
        total = int(data[3])

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print("Roll Number:", roll_no)
        print("Name:", name)
        print("Present:", present)
        print("Total Classes:", total)
        print("Attendance Percentage:", round(percentage, 2), "%")

        if percentage < 75:
            print("Status: Low Attendance")
        else:
            print("Status: Satisfactory")

        print("-----------------------------")


def main():
    while True:
        print("\n===== Student Attendance Management System =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")


main()