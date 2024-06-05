from student import Student
from subject import PreSubject, PostSubject
from inscription import Inscription

def register_student(students):
    levels = {
        "1": "Pregrado",
        "2": "Postgrado"
    }
    name = input("Please enter the student name: ")
    dni = input("Please enter the student dni: ")
    level_option = input("Please enter a level - 1 - Pregrado - 2 - Postgrado: ")
    students.append(
        Student(name,dni,levels.get(level_option, levels["1"]))
    )

def register_subjects(subjects):
    option = input("Please enter a level - 1 - Pregrado - 2 - Postgrado: ")
    name = input("Please enter the subject name: ")
    credits = int(input("Please enter the subject credits: "))
    if option == "1":
        subjects.append(PreSubject(name,credits,input("Please enter the subject department: ")))
    elif option == "2":
        subjects.append(PostSubject(name,credits,input("Please enter the subject diploma: ")))
    else:
        print("Invalid option")

def register_inscriptions(inscriptions, students, subjects):
    dni = input("Please enter the student dni: ")
    student_selected = None
    subject_student_list = []
    for student in students:
        if student.dni == dni:
            student_selected = student
            break
    if student_selected:
        for index, subject in enumerate(subjects): 
            print(index, subject.name, subject.credits, sep= " - ")
        while True:
            subject_index = int(input("Please enter the number of subject you want or -1 if you want to exit:"))
            if subject_index != -1:
                subject_student_list.append(subjects[subject_index])
            else: break
        if len(subject_student_list) > 0:
            total_amount = 0
            total_credits = 0
            for subject in subject_student_list:
                if isinstance(subject, PreSubject):
                    total_amount += subject.credits * 65
                else:
                    total_amount += subject.credits * 75
                total_credits += subject.credits
            inscriptions.append(Inscription(student_selected,total_credits,total_amount,subject_student_list))
            print("**** RECEIPT ****")
            print("Name:",student_selected.name)
            print("Dni:",student_selected.dni)
            print("Level:",student_selected.level)
            print("Subjects:")
            for index, subject in enumerate(subject_student_list): 
                print(index, subject.name, subject.credits, sep= " - ")
            print("Total: ", total_amount)
        else: 
            print("No inscrito")
def main():
    students = []
    subjects = []
    inscriptions = []

main()