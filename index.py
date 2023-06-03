import pandas as pd

# 1. what is the average Open, High, Low, Close of a given stock for the past year?
df = pd.read_csv("data/GOOG.csv")
print(f"All {df}\n")

# calculate the average price of the open column
open = df["Open"].mean()
print(f"Avg open ${round(open, 2)}")

# calculate the average price of the high column
high = df["High"].mean()
print(f"Avg high ${round(high, 2)}")

# calculate the average price of the low column
low = df["Low"].mean()
print(f"Avg low ${round(low, 2)}")

# calculate the average price of the close column
close = df["Close"].mean()
print(f"Avg close ${round(close, 2)}")

# 2. filter out any volume less than 30,000,000, count the number of rows
volume = df[df["Volume"].str.replace(',', '').astype(int) > 30000000]
print(f"\nFilter volume on\n {volume}")

# count the number of rows that matched the filter
print(f"\nNumber of rows with volume greater than 30,000,000 = {len(volume)}")

# sum column
sum = df["Open"].sum()
print(f"\nIt does not make sense to sum this data: ${sum}")