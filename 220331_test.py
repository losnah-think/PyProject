import pandas as ps
import matplotlib.pyplot as plt

df = ps.read_csv("./data/국민건강보험공단_한국인 혈압 참조표준_20201205.csv", sep=",", encoding="cp949")
# 데이터 정리
# filt_df = df.iloc[0:-1,2:-9]
# 데이터 미 정리
filt_df = df


# 성별 분류, 평균
sex_df = filt_df.groupby(["성별"]).mean()
# print(sex_df)

# 나이 분류 ,평균
age_df = filt_df.groupby(["나이(세)"]).mean()
# age_count_df = filt_df.groupby(["나이(세)"]).count()
# print(age_df)
# print(age_count_df)

# 성별, 나이개로 분류해보기
mix_df = filt_df.groupby(["성별","나이(세)"]).mean()
print(mix_df)
