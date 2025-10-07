import math

# Fungsi sistem non-linear
def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*(y**2) - 57

def fvec(x, y):
    return [f1(x, y), f2(x, y)]

# Parameter awal
x = 2.5
y = 2.5
epsilon = 0.000001
max_iter = 1000

# Inisialisasi matriks Jacobian aproksimasi awal (identitas)
B = [[1.0, 0.0],
     [0.0, 1.0]]

print("-----------------------------------------------------------")
print("i\t   x\t\t   y\t\tdeltax\t\tdeltay")
print("-----------------------------------------------------------")

# Evaluasi fungsi awal
fx, fy = fvec(x, y)
for i in range(max_iter):
    # Hitung invers matriks B (2x2)
    detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
    if abs(detB) < 1e-12:
        print("Determinant B terlalu kecil, iterasi berhenti.")
        break
    invB = [[ B[1][1]/detB, -B[0][1]/detB],
            [-B[1][0]/detB,  B[0][0]/detB]]

    # Hitung koreksi (delta_x, delta_y)
    delta_x = -(invB[0][0]*fx + invB[0][1]*fy)
    delta_y = -(invB[1][0]*fx + invB[1][1]*fy)

    x_new = x + delta_x
    y_new = y + delta_y

    print(f"{i}\t{x:.6f}\t{y:.6f}\t{abs(delta_x):.6f}\t{abs(delta_y):.6f}")

    # Cek konvergensi
    if abs(delta_x) < epsilon and abs(delta_y) < epsilon:
        print("-----------------------------------------------------------")
        print(f"Konvergen pada iterasi ke-{i}")
        print(f"Hasil: x = {x_new:.6f}, y = {y_new:.6f}")
        break

    # Hitung vektor fungsi baru
    fx_new, fy_new = fvec(x_new, y_new)

    # vektor s = [dx, dy], yvec = f(x_new) - f(x)
    s = [x_new - x, y_new - y]
    yvec = [fx_new - fx, fy_new - fy]

    # Update B menggunakan formula Broyden
    Bs0 = B[0][0]*s[0] + B[0][1]*s[1]
    Bs1 = B[1][0]*s[0] + B[1][1]*s[1]
    Bs = [Bs0, Bs1]
    denom = s[0]*s[0] + s[1]*s[1]
    if denom < 1e-15:
        print("Divergen atau stagnan, iterasi dihentikan.")
        break

    # (y - B*s) outer s^T / (s^T*s)
    for r in range(2):
        for c in range(2):
            B[r][c] += ( (yvec[r] - Bs[r]) * s[c] ) / denom

    # Update nilai untuk iterasi berikut
    x, y = x_new, y_new
    fx, fy = fx_new, fy_new

else:
    print("Iterasi mencapai batas maksimum tanpa konvergensi.")
