import pandas as pd
data = pd.read_csv("D:\\data\Education\\A MAHASISWA ITB\\Pengkom\\AA Tubes 2\\Test panda\\adult.csv", usecols=[0,3,4,8,9,14])
print(data.groupby(["Sex","Income"]).sum())
print(data["Age"].corr(data["Edunum"]))