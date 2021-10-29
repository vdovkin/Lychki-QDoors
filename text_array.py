class TextArray:
    def __init__(self, font_height, font_rotation, margin, style, start_number):
        self.font_height = font_height
        self.font_rotation = font_rotation
        self.margin = margin
        self.style = style
        self.start_number = start_number

    def insert_text(self, msp, cell, text):
        position = (cell[0] - self.margin[0], cell[1] + self.margin[1])
        msp.add_text(
            text,
            dxfattribs={
                "height": self.font_height,
                "rotation": self.font_rotation,
                "style": self.style,
            },
        ).set_pos(position, align="LEFT")

    def generate_numbers(self, row, columns):
        numbers_grid = []
        number = self.start_number
        for i in range(row):
            row_numbers = [str(number + x * 11) for x in range(columns)]
            numbers_grid.append(row_numbers)
            number += 1
        self.numbers_grid = numbers_grid

    def generate_text(self, msp, grid):
        rows = len(grid)
        cols = len(grid[0])
        self.generate_numbers(rows, cols)
        for i in range(rows):
            for j in range(cols):
                self.insert_text(msp, grid[i][j], self.numbers_grid[i][j])
