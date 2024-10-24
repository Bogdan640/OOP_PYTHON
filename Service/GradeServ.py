import copy

from src.repository.GradeRepo import *



class GradeService:
    def __init__(self, grade_repo, student_repo, discipline_repo, undo_service ):
        self.__grade_repo=grade_repo
        self.__student_repo=student_repo
        self.__discipline_repo=discipline_repo
        self.__undo_service=undo_service

    def save_grade_file(self):
        try:
            self.__grade_repo.save_file()
        except:
            pass

    def grade_sample_service(self):
        return self.__grade_repo.grade_sample()

    def display_list(self):
        return self.__grade_repo.get_list()

    def get_specific_grades(self, student_id):
        list=self.__grade_repo.get_list
        wanted=[grade for grade in list if grade.student_id==student_id]
        return wanted

    def get_list(self):
        return self.__grade_repo.get_list()

    def remove_discipline_grades(self):
        self.__grade_repo.remove_for_discipline()

    def remove_student_grades(self, id):
        self.__grade_repo.remove_for_student(id)

    def fail_student(self):
        mylist=[]
        for grade in self.__grade_repo.get_list():
            if grade.grade_value<50:
                mylist.append(grade.student_id)
        return mylist

    def grade_student(self, student_id, discipline_id, value):
        grade=Grade(student_id, discipline_id, value)
        self.__grade_repo.add(grade)

    def calculate_avg_dis(self, student_id, discipline_id):
        avg=0
        cnt=0
        for grade in self.__grade_repo.get_list():
            if grade.student_id == student_id and grade.discipline_id==discipline_id:
                avg=avg+grade.grade_value
                cnt=cnt+1
        return avg/cnt

    def all_avg(self, stundent_id):
        avg=0
        cnt=0
        for grade in self.__grade_repo.get_list():
            if grade.student_id == stundent_id:
                avg=avg+grade.grade_value
                cnt=cnt+1
        return avg/cnt

    def sort_avg(self):
        mylist=copy.deepcopy(self.get_list())
        new_list=sorted(mylist, key=lambda grades: self.all_avg(grades.student_id), reverse=True)
        return new_list

    def all_avg_dis(self, discipline_id):
        avg=0
        cnt=0
        for grade in self.__grade_repo.get_list():
            if grade.discipline_id == discipline_id:
                avg=avg+grade.grade_value
                cnt=cnt+1
        return avg/cnt

    def sort_avg_dis(self):
        mylist=copy.deepcopy(self.get_list())
        new_list=sorted(mylist, key=lambda grades: self.all_avg_dis(grades.discipline_id), reverse=True)
        return new_list

    def load_from_file(self):
        try:
            self.__grade_repo.read_from_file()
        except:
            pass












