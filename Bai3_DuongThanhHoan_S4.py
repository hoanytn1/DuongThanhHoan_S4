import tkinter as tk
from tkinter import messagebox
import math

def check_triangle():
    try:
        # Lấy thông tin từ người dùng
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())
        x3 = float(entry_x3.get())
        y3 = float(entry_y3.get())

        # Tính độ dài các cạnh
        AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
        AC = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

        # Kiểm tra kiểu tam giác
        if AB == BC == AC:
            result = "Tam giác đều"
        elif AB == BC or BC == AC or AC == AB:
            result = "Tam giác cân"
        elif AB**2 + BC**2 == AC**2 or BC**2 + AC**2 == AB**2 or AC**2 + AB**2 == BC**2:
            result = "Tam giác vuông"
        elif AB**2 + BC**2 > AC**2 or BC**2 + AC**2 > AB**2 or AC**2 + AB**2 > BC**2:
            result = "Tam giác nhọn"
        elif AB**2 + BC**2 < AC**2 or BC**2 + AC**2 < AB**2 or AC**2 + AB**2 < BC**2:
            result = "Tam giác tù"
        else:
            result = "Tam giác bình thường"

        # Hiển thị kết quả
        messagebox.showinfo(title="Kết quả", message=result)

    except ValueError:
        messagebox.showerror(title="Lỗi", message="Vui lòng nhập số hợp lệ")

def check_quadrilateral():
    try:
        # Lấy thông tin từ người dùng
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())
        x3 = float(entry_x3.get())
        y3 = float(entry_y3.get())
        x4 = float(entry_x4.get())
        y4 = float(entry_y4.get())

        # Kiểm tra đường thẳng
        if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
            result = "Không phải tứ giác"
        else:
            # Tính độ dài các cạnh
            AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
            CD = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
            DA = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)

            # Kiểm tra kiểutứ giác
            if AB == BC == CD == DA:
                result = "Hình vuông"
            elif AB == CD and BC == DA:
                result = "Hình chữ nhật"
            elif AB == CD and BC != DA:
                result = "Hình bình hành"
            elif AB != CD and BC == DA:
                result = "Hình bình hành"
            elif AB == CD and BC != DA:
                result = "Hình thang"
            elif AB == CD and BC == DA and AB != BC:
                result = "Hình thoi"
            else:
                result = "Tứ giác bình thường"

        # Hiển thị kết quả
        messagebox.showinfo(title="Kết quả", message=result)

    except ValueError:
        messagebox.showerror(title="Lỗi", message="Vui lòng nhập số hợp lệ")

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Hỗ trợ học tập hình học")

# Tạo các label và entry cho tọa độ 3 điểm
label_x1 = tk.Label(window, text="X1:")
label_x1.grid(row=0, column=0)
entry_x1 = tk.Entry(window)
entry_x1.grid(row=0, column=1)
label_y1 = tk.Label(window, text="Y1:")
label_y1.grid(row=0, column=2)
entry_y1 = tk.Entry(window)
entry_y1.grid(row=0, column=3)

label_x2 = tk.Label(window, text="X2:")
label_x2.grid(row=1, column=0)
entry_x2 = tk.Entry(window)
entry_x2.grid(row=1, column=1)
label_y2 = tk.Label(window, text="Y2:")
label_y2.grid(row=1, column=2)
entry_y2 = tk.Entry(window)
entry_y2.grid(row=1, column=3)

label_x3 = tk.Label(window, text="X3:")
label_x3.grid(row=2, column=0)
entry_x3 = tk.Entry(window)
entry_x3.grid(row=2, column=1)
label_y3 = tk.Label(window, text="Y3:")
label_y3.grid(row=2, column=2)
entry_y3 = tk.Entry(window)
entry_y3.grid(row=2, column=3)

label_x4 = tk.Label(window, text="X4:")
label_x4.grid(row=3, column=0)
entry_x4 = tk.Entry(window)
entry_x4.grid(row=3, column=1)
label_y4 = tk.Label(window, text="Y4:")
label_y4.grid(row=3, column=2)
entry_y4 = tk.Entry(window)
entry_y4.grid(row=3, column=3)

# Tạo nút kiểm tra tam giác và tứ giác
button_triangle = tk.Button(window, text="Kiểm tra tam giác", command=check_triangle)
button_triangle.grid(row=4, column=0, columnspan=2)
button_quadrilateral = tk.Button(window, text="Kiểm tra tứ giác", command=check_quadrilateral)
button_quadrilateral.grid(row=4, column=2, columnspan=2)

# Chạy chương trình
window.mainloop()