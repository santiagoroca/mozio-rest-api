class MOZIOPolygon():
    def __init__(self, polygon):
        self.polygon = polygon

    def contains(self, x, y):

        x = float(x)
        y = float(y)
        i = 0
        j = len(self.polygon) - 1
        oddNodes = False

        while i < j:
            i += 1
            if (self.polygon[i][1] < y and self.polygon[j][1] >= y or self.polygon[j][1] < y and self.polygon[i][
                1] >= y) and (self.polygon[i][0] <= x or self.polygon[j][0] <= x):
                oddNodes ^= (
                    self.polygon[i][0] + (y - self.polygon[i][1]) / (self.polygon[j][1] - self.polygon[i][1]) * (
                        self.polygon[j][0] - self.polygon[i][0]) < x)
                j = i

        print (oddNodes)
        return oddNodes
