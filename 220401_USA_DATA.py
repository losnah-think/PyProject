from hashlib import new
import pandas as ps
import matplotlib.pyplot as plt


# DateTime, Date, Month, Day, Year, Dayofwk, Time, Hour, Meal_Time, Sys(mmHg), SysExcess, Dias, DiaExcess, bpDelta, Pulse(bpm)
df = ps.read_csv("./data/Blood_pressure.csv", sep=",", encoding="cp949")
# print(df.head())

# 시간의 오름차순 : 과거에서 현재순
reverse_df = df.sort_values(["DateTime"],ascending=True)
# print(df["DateTime"])
# print(df.iloc[0:-1,9:-1])

# concat([합칠 데이터프레임1, 합칠 데이터프레임2], axis=1) # a
# new_df = ps.concat([df["DateTime"],df["Sys(mmHg)"]],axis=1)
# print(new_df.head())

plt.plot(reverse_df["DateTime"],reverse_df["Sys(mmHg)"], color="pink")
plt.show()