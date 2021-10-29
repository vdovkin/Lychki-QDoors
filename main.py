import ezdxf

# Create a new DXF document.
doc = ezdxf.new(dxfversion="R2010")

doc.layers.add("TABLE")

msp = doc.modelspace()


class Table:
    def __init__(self, basic_point, lenght_x, lenght_y, num_x, num_y, layer):
        self.basic_point = basic_point
        self.lenght_x = lenght_x
        self.lenght_y = lenght_y
        self.num_x = num_x
        self.num_y = num_y
        self.layer = layer

    def create_x_line(self, basic_point):
        for i in range(self.num_x):
            msp.add_line(
                (basic_point["x"], basic_point["y"]),
                (basic_point["x"] + self.lenght_x, basic_point["y"]),
                dxfattribs={"layer": self.layer},
            )
            basic_point["x"] += self.lenght_x

    def create_y_line(self, basic_point):
        for i in range(self.num_y):
            msp.add_line(
                (basic_point["x"], basic_point["y"]),
                (basic_point["x"], basic_point["y"] + self.lenght_y),
                dxfattribs={"layer": self.layer},
            )
            basic_point["y"] += self.lenght_y

    def create_grid(self):
        # set basic point
        bp = self.basic_point.copy()
        # create all rows
        for i in range(self.num_y + 1):
            self.create_x_line(bp)
            bp["x"] -= self.lenght_x * self.num_x
            bp["y"] += self.lenght_y
        # reset basic point
        bp = self.basic_point.copy()
        # create all columns
        for i in range(self.num_x + 1):
            self.create_y_line(bp)
            bp["x"] += self.lenght_x
            bp["y"] -= self.lenght_y * self.num_y


PARAMETRS = {
    "basic_point": {"x": 0, "y": 0},
    "lenght_x": 27.63,
    "lenght_y": 89.75,
    "num_x": 17,
    "num_y": 11,
    "layer": "TABLE",
}

t = Table(**PARAMETRS)
t.create_grid()
# create_grid(**PARAMETRS)

doc.saveas("test.dxf")
