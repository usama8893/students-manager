students = {}

while True:
    print("\n--- Students Manager Menu ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Edit Student name")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        # Marks input validation
        while True:
            try:
                marks = int(input("Enter marks (0-99): "))
                if 0 <= marks <= 99:
                    break
                else:
                    print("❌ Marks must be between 0 and 99.")
            except ValueError:
                print("❌ Please enter a whole number.")
        students[name] = markscd cd
        print(f"✅ Added {name} with marks {marks}")

    elif choice == "2":
        name = input("Enter the student's name to update marks: ")
        if name in students:
            print(f"Current marks for {name}: {students[name]}")
            while True:
                try:
                    new_marks = int(input("Enter new marks (0-99): "))
                    if 0 <= new_marks <= 99:
                        break
                    else:
                        print("❌ Marks must be between 0 and 99.")
                except ValueError:
                    print("❌ Please enter a whole number.")
            students[name] = new_marks
            print(f"✅ Marks updated for {name}")
        else:
            print("❌ Student not found.")

    elif choice == "3":
        old_name = input("Enter current student name: ")
        if old_name in students:
            print(f"Current name {old_name}, marks: {students[old_name]}")
            new_name = input("Enter new name: ")
            students[new_name] = students.pop(old_name)
            print(f"✅ Name changed from {old_name} to {new_name}")
        else:
            print("❌ Student not found.")

    elif choice == "4":
        if students:
            print("\n--- Student Records ---")
            for name, marks in students.items():
                print(f"{name} → {marks}")
        else:
            print("⚠️ No students available.")

    elif choice == "5":
        with open("students.txt", "w") as f:
            for name, marks in students.items():
                f.write(f"{name}: {marks}\n")
        print("💾 Data saved. Exiting...")
        break
    else:
        print("❌ Invalid choice, please try again.")
