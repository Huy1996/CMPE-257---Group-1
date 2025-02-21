import pyreadstat

file = "Original Data/LLCP2023.XPT"
csv = "data.csv"
print("Reading data ...")
df, meta = pyreadstat.read_xport(file, encoding="latin1")

print("Converting to CSV file ...")
df.to_csv(csv, index=False)

print("Converted successful.")
print(f"Output file: {csv}")