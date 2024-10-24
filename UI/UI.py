from src.repository.DisciplineRepo import DisciplineRepository, DisciplineTextRepo
from src.repository.ErrorRepo import RepositoryError
from src.repository.GradeRepo import GradeRepository, GradeTextRepository
from src.repository.StudentRepo import StudentRepository
from src.services.DisciplineServ import DisciplineService
from src.services.GradeServ import GradeService
from src.services.StudentServ import StudentServ
from src.services.UndoServ import UndoService
from src.repository.StudentRepo import SdudentTextRepo





student_repo=SdudentTextRepo("studenti.txt")
discipline_repo=DisciplineTextRepo("discipline.txt")
grade_repo=GradeTextRepository("grade.txt")
undo_serv=UndoService()
grade_serv=GradeService(grade_repo, student_repo, discipline_repo, undo_serv)
student_serv=StudentServ(student_repo, undo_serv, grade_serv)
discipline_serv=DisciplineService(discipline_repo, undo_serv, grade_serv)


class UI:
    def __init__(self, studentserv, discserv, gradeserv,undoserv):
        self.__studentserv=studentserv
        self.__discserv=discserv
        self.__gradeserv=gradeserv
        self.__undoserv=undoserv

    def print_menu(self):
        print("\n1. Add Student")
        print("2. Add Discipline")
        print("3. Remove Student")
        print("4. Remove Discipline")
        print("5. Update Student")
        print("6. Update Discipline")
        print("7. Display Students")
        print("8. Display Disciplines")
        print("9. Display Grades")
        print("10. Grade Certain Student")
        print("11. Search a Student by Name")
        print("12. Search a Student by ID")
        print("13. Search a Discipline by Name")
        print("14. Search a Discipline by ID")
        print("15. Show the Failing Students")
        print("16. Display Best Students")
        print("17. Display All disciplines at which there is at least one grade")
        print("18. Undo")
        print("19. Redo")

        print("0. Exit")


    def add_student_ui(self):
        try:
            print("Please provide student informations ")
            id = int(input("Please enter the student's id: "))
            name= input("Please enter the student's name: ")

            self.__studentserv.add_student(id, name)
            print("\nThe student was successfully added! ")
        except ValueError:
            print("\n The id must be an integer")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def delete_student_ui(self):

        try:
            id = int(input("Please provide the id of the student you want to remove: "))
            deleted_student=self.__studentserv.delete_student(id)
            print('\nThe student ' + str(deleted_student) + ' was deleted successfully.')
        except ValueError:
            print("\n The id must be an integer")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def update_student_ui(self):

        try:
            id = int(input("Please enter the id of the student you want to modify: "))
            name = input("PLease enter the student's new name: ")
            self.__studentserv.update(id, name)
            print("The student was successfully updated!")
        except ValueError:
            print("\n The id must be an integer")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def add_discipline_ui(self):

        try:
            print("Please provide discipline informations ")
            id = int(input("Please enter the discipline's id: "))
            name = input("Please enter the discipline's name: ")
            self.__discserv.add_discipline(id, name)
            print("\nThe discipline was successfully added! ")
        except ValueError:
            print("\n The id must be an integer")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def delete_discipline_ui(self):

        try:
            id = int(input("Please provide the id of the discipline you want to remove: "))
            deleted_discipline=self.__discserv.delete_discipline(id)
            print('\nThe discipline ' + str(deleted_discipline) + ' was deleted successfully.')
        except ValueError:
            print("\n The id must be an integer")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def update_discipline_ui(self):

        try:
            id = int(input("Please enter the id of the discipline you want to modify: "))
            name = input("Please enter the discipline's new name: ")
            self.__discserv.update(id, name)
            print("The discipline was successfully updated!")
        except ValueError:
            print("\n The id must be an integer")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def grade_student_ui(self):
        try:
            student_id=int(input("Please enter the student's id: "))
            discipline_id=int(input("Please enter the discipline's id: "))
            grade_value= int(input("Please enter the grade that the student will have: "))
            self.__gradeserv.grade_student(student_id, discipline_id, grade_value)
            print("The grade was successfully awarded!")
        except ValueError:
            print("\n The id must be an integer")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def find_student_after_id_ui(self):
        try:
            id=int(input("Plese provide an id for search: "))
            if self.__studentserv.search_student_id(id) is not None:
                print(f"{self.__studentserv.search_student_id(id)}")
            else:
                print("The student couldn't be found")
        except ValueError:
            print("\n The id must be an integer")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def find_student_after_name(self):
        try:
            name=input("Plese provide a name for search: ")
            # if self.__studentserv.search_students_name(name) is not None:
            for student in self.__studentserv.search_students_name(name):
                print(student)

            # else:
            #     print("The student couldn't be found")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def find_discipline_after_id(self):
        try:
            id=int(input("Plese provide an id for search: "))
            if self.__discserv.search_discipline_after_id(id) is not None:
                print(f"{self.__discserv.search_discipline_after_id(id)}")
            else:
                print("The discipline couldn't be found")
        except ValueError:
            print("\n The id must be an integer")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def find_discipline_after_name(self):
        try:
            name=input("Plese provide a name for search: ")
            if self.__discserv.search_discipline_after_name(name) is not None:
                for discipline in self.__discserv.search_discipline_after_name(name):
                    print(discipline)
            else:
                print("The discipline couldn't be found")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def undo_ui(self):
        print("")
        try:
            self.__undoserv.undo()
            print("Undo was successful.")
        except Exception as e:
            print(str(e))
        print("")

    def redo_ui(self):
        print("")
        try:
            self.__undoserv.redo()
            print("Redo was successful.")
        except Exception as e:
            print(str(e))
        print("")

    def print_list_student(self):
        for student in self.__studentserv.display_list_s():
            print(f"Student : {student.id}, Name: {student.name}")

    def print_list_disc(self):
        for discipline in self.__discserv.get_list_serv():
            print(f"Discipline: {discipline.id}, Name: {discipline.name}")


    def print_list_grade(self):
         for grade in self.__gradeserv.display_list():
             print(f"Student ID: {grade.student_id}, Discipline ID: {grade.discipline_id}, Grade: {grade.grade_value}")

    def grade_student_serv(self):
        try:
            id_student=int(input("Please enter the id of the student you want to grade: "))
            id_discipline=input("Please enter the id of the discipline you want to grade the student: ")
            grade_value=int(input("Please enter the grade you want to award: "))
            self.__gradeserv.grade_student(id_student, id_discipline, grade_value)
        except ValueError:
            print("\n The id must be an integer")
        except RepositoryError as e:
            print("\n ERROR" + str(e))

    def fail(self):
        for student in self.__studentserv.get_student_list():
            if student.id in self.__gradeserv.fail_student():
                print(student)

    def sort(self):
        list=[]
        for grade in self.__gradeserv.sort_avg():
            for student in self.__studentserv.get_student_list():
                if grade.student_id==student.id:
                    if student not in list:
                        list.append(student)
                        print(student)

    def sort_di(self):
        list=[]
        for grade in self.__gradeserv.sort_avg_dis():
            for discipline in self.__discserv.get_list_serv():
                if grade.discipline_id == discipline.id:
                    if discipline not in list:
                        list.append(discipline)
                        print(discipline)





    def run_program(self):
        self.__studentserv.sample_list_s()
        self.__discserv.sample_serv()
        self.__gradeserv.grade_sample_service()

        self.__discserv.load_from_file()
        self.__gradeserv.load_from_file()
        self.__studentserv.load_from_file()

        while True:
            self.print_menu()
            option=int(input("Choose an option: "))
            if option == 0:
                exit()
            if option == 1:
                self.add_student_ui()
            if option == 2:
                self.add_discipline_ui()
            if option == 3:
                self.delete_student_ui()
            if option == 4:
                self.delete_discipline_ui()
            if option ==5:
                self.update_student_ui()
            if option==6:
                self.update_discipline_ui()
            if option ==7:
                self.print_list_student()
            if option == 8:
                self.print_list_disc()
            if option == 9:
                self.print_list_grade()
            if option ==10:
                self.grade_student_serv()
            if option==11:
                self.find_student_after_name()
            if option==12:
                self.find_student_after_id_ui()
            if option==13:
                self.find_discipline_after_name()
            if option==14:
                self.find_discipline_after_id()
            if option == 15:
                self.fail()
            if option == 16:
                self.sort()
            if option == 17:
                self.sort_di()
            if option == 18:
                self.undo_ui()
            if option == 19:
                self.redo_ui()




ui=UI(student_serv, discipline_serv, grade_serv, undo_serv)
ui.run_program()














