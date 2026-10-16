from abc import ABC, abstractmethod


class IStudentRepo(ABC):
    @abstractmethod
    def get_students(self):
        ...

    @abstractmethod
    def get_student_by_id(self, student_id):
        ...

    @abstractmethod
    def add_student(self, name, group):
        ...

    @abstractmethod
    def update_student(self, student_id, name, group):
        ...

    @abstractmethod
    def delete_student(self, student_id):
        ...
