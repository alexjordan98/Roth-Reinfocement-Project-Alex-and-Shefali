import pandas
import openpyxl
import xlrd
from model.Matrix import Matrix
from model.Cell import Cell

from model.MatrixUpdater import MatrixUpdater

class ExcelController:

    Updater: MatrixUpdater

    def __init__(self, Updater: MatrixUpdater):

        self.Updater = Updater



    def export_excel(self, export_path: str):

        names = []
        weights_lis = []
        l = list(self.Updater.states)

        for i in range(self.Updater.iterations):

            name = l[i].getName()
            names.append("P1 Weights "+name)
            names.append("P2 Weights "+name)


            p1ws = l[i].getp1Weights()
            p2ws = l[i].getp2Weights()

            weights_lis.append(p1ws)
            weights_lis.append(p2ws)


        fr = pandas.DataFrame(list(zip(*weights_lis)), columns = names)



        fr.to_excel(export_path +"output.xlsx", index = False)


    o = 0

    def import_excel(self, import_path: str):

        self.o = 1


        df = pandas.read_excel(import_path)

        cols = df["columns"].tolist()
        col = int(cols[0])
        rows = df["rows"].tolist()
        row = int(rows[0])
        epsilon = df["epsilon"].tolist()
        eps = float(epsilon[0])
        delts = df["delta"].tolist()
        delt = float(delts[0])

        p1 = df["p1weights"].tolist()
        p2 = df["p2weights"].tolist()


        pays = df["payoffs"].tolist()
        #print(pays)

        x = 0
        y = 0

        l2 = []
        while x < row:
            z = 0
            rs = []
            while z < col :
                strs = str(pays[y]).split(",")
                p1s = float(strs[0])
                p2s = float(strs[1])
                print(strs)
                print(p1s)
                print(p2s)


                rs.append(Cell(p1s, p2s, 0, 0, 0))
                y+=1
                z+=1
            l2.append(rs)

            x+=1

        m1 = Matrix("M1", col, row, eps, delt, l2, p1, p2)
        return m1









def main():
    l1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    l2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    updater3 = MatrixUpdater(20, [])

    con = ExcelController(updater3)

    m4 = con.import_excel("C:/Users/George/Desktop/test.xls")#Matrix("M1", 10, 10, 0.5, 0.1, [], l1, l2)

    updater3.itter(m4)


    con.export_excel("C:/Users/George/Desktop/")


if __name__ == "__main__":
       main()











