class Student:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

    def __str__(self):
        return "%s %s" % (self.name, [class_.name for class_ in self.classes])

class Class:
    def __init__(self, name, students, conflicts):
        self.name = name
        self.students = students
        self.conflicts = conflicts
        self.color = None

    def __str__(self):
        return "%s %s" % (self.name, self.students)

f = open("classlists.txt")

classes = {}
students = {}

for line in f.readlines():
    line = line[:-1]
    linesplit = line.split(',')
    name = linesplit[0]

    class_students = linesplit[1:]

    class_ = Class(name, class_students, [])
    classes[name] = class_

    for student_name in class_students:
        if student_name not in students:
            students[student_name] = Student(student_name, [])

        students[student_name].classes.append(class_)

for class1 in classes.values():
    for class2 in classes.values():
        if class1 is not class2:
            is_conflict = False
            for student1 in class1.students:
                for student2 in class2.students:
                    if student1 == student2:
                        class1.conflicts.append(class2)
                        is_conflict = True
                    if is_conflict:
                        break
                if is_conflict:
                    break
def get_colors(classes):
    class_colors = {
            'red': [],
            'orange': [],
            'yellow': [],
            'green': [],
            'blue': [],
            'violet': [],
    }

    def color_is_ok(color, class1):
        for conflict in class1.conflicts:
            for class2 in color:
                if class2 is conflict:
                    return False

        return True
        

    for color, color_classes in class_colors.iteritems():
        for class1 in classes:
            if class1.color is None and color_is_ok(color_classes, class1):
                    color_classes.append(class1)
                    class1.color = color

    return class_colors

print '\n1. View all class names in the class list:'
print '\n'.join([class_.name for class_ in classes.values()])

print '\n2. View the students in a selected class:'
print '\n'.join([class_.__str__() for class_ in classes.values()])

print '\n3. View all the classes of a student:'
print '\n'.join([student.__str__() for student in students.values()])

print '\n4. Given a class, show all the other classes in which it has common students:'
print '\n'.join(['%s %s' % (class_.name, [conflict.name for conflict in class_.conflicts])
    for class_ in classes.values()])

print '\n5. Implement a graph coloring algorithm used in class:'
print '\n'.join('%s: %s' % (color_name, [class_.name for class_ in classes]) for color_name, classes
        in get_colors(classes.values()).iteritems())

