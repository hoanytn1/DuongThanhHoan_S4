import pandas as pd

# Dữ liệu môn học
data = {
    "STT": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Lớp Mã": ["20222FE6051001", "20222FE6051002", "20222FE6051003", "20222FE6051004", "20222FE6051005", "20222FE6051006", "20222FE6051007", "20222FE6051008", "20222FE6051009"],
    "Số SV": [44, 65, 61, 65, 62, 57, 52, 56, 57],
    "Loại A+": [0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Loại A": [20, 15, 5, 12, 9, 3, 9, 6, 7],
    "Loại B+": [11, 7, 9, 10, 9, 5, 5, 7, 4],
    "Loại B": [3, "số 8", 6, 12, "số 8", 4, 2, 15, 6],
    "Loại C+": [4, 14, 2, 11, "số 8", 13, 10, 3, 7],
    "Loại C": [1, 5, 14, 1, 5, 5, 6, 6, 7],
    "Loại D+": [1, 4, 5, 3, "số 8", 9, 5, 6, 4],
    "Loại D": [3, 3, 4, 6, 6, 3, 3, 4, 4],
    "Loại F": [41, 52, 42, 57, 47, 15, 12, "số 8", 9],
    "L1": [41, 56, 47, 59, 53, 44, 39, 50, 48],
    "L2": [39, 45, 31, 48, 39, 22, 27, 31, 34],
    "TX1": [41, 62, 54, 63, 62, 43, 39, 42, 33],
    "TX2": [41, 64, 60, 62, 62, 46, 46, 49, 54],
    "Cuối kỳ": [40, 52, 42, 57, 47, 44, 33, 48, 46]
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Tính tỉ lệ các loại giỏi
total_students = df["Số SV"].sum()
excellent = df["Loại A+"].sum() + df["Loại A"].sum()
good = df["Loại B+"].sum() + df["Loại B"].sum()
average = df["Loại C+"].sum() + df["Loại C"].sum()
poor = df["Loại D+"].sum() + df["Loại D"].sum()
fail = df["Loại F"].sum()

excellent_percentage = (excellent / total_students) * 100
good_percentage = (good / total_students) * 100
average_percentage = (average / total_students) * 100
poor_percentage = (poor / total_students) * 100
fail_percentage = (fail / total_students) * 100

# Xếp hạng các lớp theo tỉ lệ các loại giỏi
df["Tỉ lệ loại A+"] = (df["Loại A+"] / df["Số SV"]) * 100
df["Tỉ lệ loại A"] = (df["Loại A"] / df["Số SV"]) * 100
df["Tỉ lệ loại B+"] = (df["Loại B+"] / df["Số SV"]) * 100
df["Tỉ lệ loại B"] = (df["Loại B"] / df["Số SV"]) * 100
df["Tỉ lệ loại C+"] = (df["Loại C+"] / df["Số SV"]) * 100
df["Tỉ lệ loại C"] = (df["Loại C"] / df["Số SV"]) * 100
df["Tỉ lệ loại D+"] = (df["Loại D+"] / df["Số SV"]) * 100
df["Tỉ lệ loại D"] = (df["Loại D"] / df["Số SV"]) * 100
df["Tỉ lệ loại F"] = (df["Loại F"] / df["Số SV"]) * 100

# Sắp xếp và xếp hạng các lớp theo tỉ lệ loại A+
df_sorted = df.sort_values(by="Tỉ lệ loại A+", ascending=False)
df_sorted["Xếp hạng"] = range(1, len(df_sorted) + 1)

# In báo cáo tỉ lệ các loại giỏi
print("BÁO CÁO TỈ LỆ CÁC LOẠI GIỎI")
print(f"Tỉ lệ Loại A+: {excellent_percentage:.2f}%")
print(f"Tỉ lệ Loại A: {good_percentage:.2f}%")
print(f"Tỉ lệ Loại B+: {average_percentage:.2f}%")
print(f"Tỉ lệ Loại B: {poor_percentage:.2f}%")
print(f"Tỉ lệ Loại F: {fail_percentage:.2f}%")

# In báo cáo xếp hạng các lớp
print("\nBÁO CÁO XẾP HẠNG CÁC LỚP THEO TỈ LỆ LOẠI A+")
print(df_sorted[["Lớp Mã", "Số SV", "Tỉ lệ loại A+", "Xếp hạng"]])