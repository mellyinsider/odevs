class Triangle:
    def __init__(self, angle1, angle2, angle3):

        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        sum = self.angle1+self.angle2+self.angle3
        if sum == 180:
            return True
        else:
            return False

my_triangle = Triangle(80,50,50)
print(my_triangle.check_angles())
print(my_triangle.number_of_sides)