import pyreadstat

df, meta = pyreadstat.read_xport("Original Data/LLCP2023.XPT", encoding="latin1")
df.to_csv("data.csv", index=False)