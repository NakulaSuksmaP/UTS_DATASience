import pandas as pd
import numpy as np
from numpy import genfromtxt

class class_dataset:
    X = []
    y = []
    name = ""

    def __init__(self, dataset_name=None):
        self.name = dataset_name
        self.pickDataset()

    def pickDataset(self):
        if self.name=="tamanBaca":
            self.TamanbacaDataset()        
        elif self.name == "2D":
            self.artificialDataset()
            

    def TamanbacaDataset(self):
        print("DATASET TamanBaca")
        df = genfromtxt('wine-clustering.csv', delimiter=',', skip_header=1)
        self.X = df[:, 1:13]
        y = df[:, 0:1]
        yy = []
        for i in range(len(y)):
            # print(y[i][0])
            yy.append(y[i][0])
        self.y = yy
    def artificialDataset(self):
        print("DATASET 2D")
        file = pd.read_excel(open('dataset_artificial.xlsx', 'rb'))
        X = pd.DataFrame(file, columns=(['x', 'y']))
        self.X = np.array(X)
        y = pd.DataFrame(file, columns=(['T']))
        y = np.array(y)
        yy = []
        for i in range(len(y)):
            yy.append(y[i][0])
        self.y = yy