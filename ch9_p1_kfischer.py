"""
File: student.py
Resources to manage a student's name and test scores.

EDIT:
Author: Kelley Fischer
Date:   11/16/19

Added comparison operators for student name's.
"""


class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " +                " ".join(map(str, self.scores))

    def __eq__(self, other):
        """Compares two students using ==."""
        return self.name == other.name

    def __lt__(self, other):
        """Compares two students using <."""
        return self.name < other.name

    def __ge__(self, other):
        """Compares two students using >=."""
        return self.name >= other.name


def main():
    """A simple test."""
    student1 = Student('Ken', 5)
    print(f'{student1} \n')

    student2 = Student('Laura', 5)
    print(f'{student2} \n')

    student3 = Student('Ken', 5)
    print(f'{student3} \n')

    # Test each comparison operater for
    print(f'{student1.name}\'s name is less than {student2.name}\'s name: {student1 < student2}')
    print(f'{student2.name}\'s name is less than {student1.name}\'s name: {student2 < student1}')
    print(f'{student1.name}\'s name is greater than or equal to {student2.name}\'s name: {student1 >= student2}')
    print(f'{student2.name}\'s name is greater than or equal to {student1.name}\'s name: {student2 >= student1}')
    print(f'{student1.name}\'s name is greater than or equal to {student1.name}\'s name: {student1 >= student1}')
    print(f'{student1.name}\'s name is equal to {student2.name}\'s name: {student1 == student2}')
    print(f'{student1.name}\'s name is equal to {student3.name}\'s name: {student1 == student3}')


if __name__ == "__main__":
    main()
