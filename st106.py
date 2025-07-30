class Testpaper:
    def __init__(self, subject, correct_answers, min_percentage):
        self.subject = subject
        self.correct_answers = correct_answers
        self.min_percentage = int(min_percentage.strip('%'))

class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self, testpaper, student_answers):
        if isinstance(self.tests_taken, str):
            self.tests_taken = {}

        correct_count = 0
        total_questions = len(testpaper.correct_answers)

        for correct_answer in testpaper.correct_answers:
            q_number, correct_option = correct_answer[:-1], correct_answer[-1]
            student_answer = None
            for ans in student_answers:
                if ans.startswith(q_number):
                    student_answer = ans[-1]
                    break
            if student_answer == correct_option:
                correct_count += 1

        # Используем round() для правильного округления
        percentage = round((correct_count / total_questions) * 100)

        if percentage >= testpaper.min_percentage:
            result_str = f"Passed! ({percentage}%)"
        else:
            result_str = f"Failed! ({percentage}%)"

        self.tests_taken[testpaper.subject] = result_str
            
# TEST_1:
paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

student1 = Student()
student2 = Student()

student1.take_test(paper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(paper2, ['1C', '2D', '3A', '4C'])
student2.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])

print(student1.tests_taken)
print(student2.tests_taken)

# TEST_2:
paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

student = Student()

print(student.tests_taken)

# TEST_3:
papers = [
    Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%'),
    Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%'),
    Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%'),
    Testpaper(
        'Informatics',
        ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8A', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
         '18B', '19D', '20D'],
        '90%'
    )
]

student1 = Student()
student2 = Student()

student1.choices = [
    ['1C', '2B', '3D', '4C', '5B'],
    ['1A', '2D', '3A', '4D'],
    ['1B', '2D', '3D', '4C', '5B', '6C', '7C'],
    ['1B', '2A', '3C', '4C', '5A', '6B', '7C', '8B', '9D', '10C', '11A', '12D', '13C', '14A', '15B', '16A', '17C',
     '18B', '19C', '20B']
]

student2.choices = [
    ['1A', '2A', '3A', '4A', '5C'],
    ['1A', '2C', '3C', '4A'],
    ['1A', '2B', '3C', '4A', '5D', '6D', '7D'],
    ['1B', '2A', '3C', '4C', '5A', '6D', '7C', '8D', '9A', '10B', '11D', '12A', '13B', '14B', '15C', '16D', '17A',
     '18A', '19D', '20C']
]

for student in [student1, student2]:
    for i in range(4):
        student.take_test(papers[i], student.choices[i])
print(student1.tests_taken)
print(student2.tests_taken)

# TEST_4:
papers = [
    Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%'),
    Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%'),
    Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%'),
    Testpaper(
        'Informatics',
        ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8A', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
         '18B', '19D', '20D'],
        '90%'
    )
]

student = Student()

student.choices = [
    ['1A', '2C', '3D', '4B', '5A'],
    ['1C', '2A', '3D', '4A'],
    ['1D', '2C', '3C', '4B', '5D', '6A', '7A'],
    ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8B', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
     '18B', '19D', '20D']
]

for i in range(4):
    student.take_test(papers[i], student.choices[i])

print(student.tests_taken)
            