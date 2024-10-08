class Diamond:
    def __init__(self, side_a, angle_a):
        self.set_side_a(side_a)
        self.set_angle_a(angle_a)

    def set_side_a(self, side_a):
        if side_a > 0:
            setattr(self, 'side_a', side_a)
        else:
            raise ValueError("The side length must be greater than 0.")

    def set_angle_a(self, angle_a):
        if 0 < angle_a < 180:
            setattr(self, 'angle_a', angle_a)
            setattr(self, 'angle_b', 180 - angle_a)
        else:
            raise ValueError("The angle should be between 0 and 180 degrees, and greater than 0.")

    def __repr__(self):
        return f"Diamond: side a = {self.side_a}, angle a = {self.angle_a}, angle b = {self.angle_b}"

diamond = Diamond(side_a=10, angle_a=10)
print(diamond)
