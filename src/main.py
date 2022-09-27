# coding: utf-8

class tire():
    def rotate(self, angle: int) -> int:
        return angle

class handle():
    def rotate(self, angle: int) -> int:
        return angle

class car():
    def __init__(self, t: tire, h: handle):
        self.t = t
        self.h = h

    def drive(self, angle: int) -> int:
        return self.t.rotate(self.h.rotate(angle))

if __name__ == '__main__':
    human_hundle_control = 10
    t = tire()
    h = handle()
    c = car(t, h)
    print(c.drive(human_hundle_control))