import pandas
import openpyxl
import xlrd
from model.Matrix import Matrix
from model.Cell import Cell

from model.MatrixUpdater import MatrixUpdater

class ExcelController:


    def export_excel(self, export_path: str, m: MatrixUpdater):

        names = []
        weights_lis = []
        l = list(m.states)

        for i in range(m.iterations):

            name = l[i].getName()
            names.append("P1 Weights "+name)
            names.append("P2 Weights "+name)


            p1ws = l[i].getp1Weights()
            p2ws = l[i].getp2Weights()

            weights_lis.append(p1ws)
            weights_lis.append(p2ws)


        fr = pandas.DataFrame(list(zip(*weights_lis)), columns = names)



        fr.to_excel(export_path +"output.xlsx", index = False)



    def import_excel(self, import_path: str):



        df = pandas.read_excel(import_path)

        cols = df["columns"].tolist()
        col = int(cols[0])
        rows = df["rows"].tolist()
        row = int(rows[0])
        epsilon = df["epsilon"].tolist()
        eps = float(epsilon[0])
        delts = df["delta"].tolist()
        delt = float(delts[0])
        its = df["iterations"].tolist()
        iters = int(its[0])


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

        updater = MatrixUpdater(iters, [])
        updater.itter(m1)


        return updater