My_dict = {'Alice':85}
try:
    a = input("Enter the student's name:")
    print(f"{a}'s marks: {(My_dict[a])}")
except KeyError:
    print("Student not found")
