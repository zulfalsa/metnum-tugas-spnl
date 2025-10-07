import math

# Fungsi sistem non-linear
def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*(y**2) - 57

# Turunan parsial (Jacobian)
def df1dx(x, y): return 2*x + y
def df1dy(x, y): return x
def df2dx(x, y): return 3*(y**2)
def df2dy(x, y): return 1 + 6*x*y

# Parameter awal
x = 2.5
y = 2.5
epsilon = 0.000001
max_iter = 1000

print("-----------------------------------------------------------")
print("i\t   x\t\t   y\t\tdeltax\t\tdeltay")
print("-----------------------------------------------------------")

for i in range(max_iter):
    # Hitung nilai fungsi
    F1 = f1(x, y)
    F2 = f2(x, y)
    
    # Hitung elemen Jacobian
    J11 = df1dx(x, y)
    J12 = df1dy(x, y)
    J21 = df2dx(x, y)
    J22 = df2dy(x, y)
    
    # Hitung determinan Jacobian
    detJ = J11*J22 - J12*J21
    if abs(detJ) < 1e-12:
        print("Determinant Jacobian terlalu kecil (mendekati nol). Iterasi berhenti.")
        break
    
    # Hitung invers Jacobian (untuk sistem 2x2)
    invJ11 =  J22 / detJ
    invJ12 = -J12 / detJ
    invJ21 = -J21 / detJ
    invJ22 =  J11 / detJ
    
    # Hitung koreksi (delta x, delta y)
    delta_x = -(invJ11*F1 + invJ12*F2)
    delta_y = -(invJ21*F1 + invJ22*F2)
    
    # Update nilai x dan y
    x_new = x + delta_x
    y_new = y + delta_y
    
    # Cetak iterasi
    print(f"{i}\t{x:.6f}\t{y:.6f}\t{abs(delta_x):.6f}\t{abs(delta_y):.6f}")
    
    # Cek konvergensi
    if abs(delta_x) < epsilon and abs(delta_y) < epsilon:
        print("-----------------------------------------------------------")
        print(f"Konvergen pada iterasi ke-{i}")
        print(f"Hasil: x = {x_new:.6f}, y = {y_new:.6f}")
        break
    
    # Update nilai untuk iterasi berikutnya
    x, y = x_new, y_new

else:
    print("Iterasi mencapai batas maksimum tanpa konvergensi.")
