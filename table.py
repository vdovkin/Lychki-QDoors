class Table:
    def __init__(self, basic_point, lenght_x, lenght_y, num_x, num_y, layer):
        self.basic_point = basic_point
        self.lenght_x = lenght_x
        self.lenght_y = lenght_y
        self.num_x = num_x
        self.num_y = num_y
        self.layer = layer
        self.generete_cell_grid()

    def create_x_line(self, basic_point, msp):
        for i in range(self.num_x):
            msp.add_line(
                (basic_point["x"], basic_point["y"]),
                (basic_point["x"] + self.lenght_x, basic_point["y"]),
                dxfattribs={"layer": self.layer},
            )
            basic_point["x"] += self.lenght_x

    def create_y_line(self, basic_point, msp):
        for i in range(self.num_y):
            msp.add_line(
                (basic_point["x"], basic_point["y"]),
                (basic_point["x"], basic_point["y"] + self.lenght_y),
                dxfattribs={"layer": self.layer},
            )
            basic_point["y"] += self.lenght_y

    def create_grid(self, msp):
        # set basic point
        bp = self.basic_point.copy()
        # create all rows
        for i in range(self.num_y + 1):
            self.create_x_line(bp, msp)
            bp["x"] -= self.lenght_x * self.num_x
            bp["y"] += self.lenght_y
        # reset basic point
        bp = self.basic_point.copy()
        # create all columns
        for i in range(self.num_x + 1):
            self.create_y_line(bp, msp)
            bp["x"] += self.lenght_x
            bp["y"] -= self.lenght_y * self.num_y

    def generete_cell_grid(self):
        grid = []
        x_point = self.lenght_x
        y_point = self.lenght_y * (self.num_y - 1)

        for j in range(self.num_y):
            row = []
            for i in range(self.num_x):
                cell = (x_point + self.lenght_x * i, y_point)
                row.append(cell)
            grid.append(row)
            y_point -= self.lenght_y
        self.grid = grid
