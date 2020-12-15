import pandas
from model.Matrix import Matrix
from model.MatrixUpdater import MatrixUpdater

class ExcelController:

    Updater: MatrixUpdater
    Mat: Matrix

    def __init__(self, Updater: MatrixUpdater, Mat: Matrix):

        self.Updater = Updater
        self.Mat = Mat


    def export_excel(self, export_path: str):

        names = []
        weights_lis = []
        l = list(self.Updater.states)

        for i in range(self.Updater.iterations):

            name = l[i].getName()
            names.append(name)
            names.append(name)

            p1ws = l[i].getp1Weights()
            p2ws = l[i].getp2Weights()

            weights_lis.append(p1ws)
            weights_lis.append(p2ws)


        fr = pandas.DataFrame(list(zip(*weights_lis)), columns = names)

        fr.to_excel(export_path+"output.xlsx")


    def import_excel(self, import_path: str):

        df = pandas.read_excel(import_path)
















