from itertools import chain

plants_name = {
    'C': 'Clover',
    'G': 'Grass',
    'V': 'Violets',
    'R': 'Radishes'
}
kids = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 
        'Ginny','Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

class Garden:
    def __init__(self, diagram, students=kids):
        self.diagram = diagram.upper().splitlines()
        self.students = sorted(students)

    def plants(self, student):
        place = self.students.index(student) * 2
        result = []
        for row in range(2):
            for col in range(place, place + 2):
                result.append(plants_name[self.diagram[row][col]])
        return result
