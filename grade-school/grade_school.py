class School:
    def __init__(self):
        self.students = dict()

    def add_student(self, name, grade):
        if grade in self.students:
            self.students[grade].append(name)
        else:
            self.students.update({grade:[name]})

    def roster(self):
        names = []
        for i in sorted(self.students):
            self.students[i].sort()
            names += self.students[i]
        return names

    def grade(self, grade_number):
        if grade_number not in self.students.keys():
            return []
        else:
            self.students[grade_number].sort()
            return self.students[grade_number]
