import pandas as ps

data_fm = ps.read_csv("./data/국민건강보험공단_한국인 혈압 참조표준_20201205.csv", sep=",", encoding="cp949")

print(data_fm.head())