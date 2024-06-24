from main import Student
import unittest


class TestStudent(unittest.TestCase):
    def test_walk(self):
        go = Student('Alex')
        for _ in range(0, 10):
            go.walk()
        self.assertEqual(50, go.distance, 'Дистанции не равны '
                                          '[дистанция человека(объекта)] != 500')

    def test_run(self):
        run = Student('Max')
        for _ in range(0, 10):
            run.run()
        self.assertEqual(100, run.distance,
                         'Дистанции не равны [дистанция человека(объекта)] != 1000')

    def test_greater(self):
        student_1 = Student('Max')
        student_2 = Student('Alex')
        for i in range(10):
            student_1.run()
            student_2.walk()
        self.assertGreater(student_1.distance, student_2.distance,
                           f'Идущий человек - {student_2.name} '
                           f'должен преодолеть дистанцию меньше, '
                           f'чем бегущий человек - {student_1.name}')

    def test_less(self):
        student_1 = Student('Max')
        student_2 = Student('Alex')
        for i in range(10):
            student_2.walk()
            student_1.run()
        self.assertLess(student_2.distance, student_1.distance,
                        f'Идущий человек - {student_2.name} '
                        f'должен преодолеть дистанцию меньше, '
                        f'чем бегущий человек - {student_1.name}')
