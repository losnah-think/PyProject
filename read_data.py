import pandas as ps
import matplotlib.pyplot as plt

df = ps.read_csv("./data/국민건강보험공단_한국인 혈압 참조표준_20201205.csv", sep=",", encoding="cp949")
print("기존 데이터의 측정 건수는 {}개입니다.".format(df["측정수(건)"].count()))
# 데이터 출력 연습
print(df)

# 데이터 자르기 연습
# print(df.iloc[0:-1,2:16].head())

# 데이터 요약
# print(df['측정수(건)'].describe())

# 최소값으로부터 구간별 분류
section = list(range(0,370000,10000))
data_label = [str(x)+"이상 "+str(x+10000)+"미만" for x in section]

# 레이블링 확인용
# print(data_label)

# cut 을 통해 구간을 나눌 수 있음
df["측정값 범위"] = ps.cut(df["측정수(건)"], section, right=False, labels=data_label[:-1])
print(df["측정값 범위"].describe())


# 그래프 그리기
plt.plot([2,3,5,10])
plt.plot(df['측정수(건)'])
plt.show()