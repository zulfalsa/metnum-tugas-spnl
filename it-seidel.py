import math

# Fungsi iterasi (dari f1 dan f2)
def g1A(x, y):
    # g1A = (10 - x^2) / y
    return (10 - x**2) / y

def g2B(x, y):
    # g2B = sqrt((57 - y) / (3*x))
    val = (57 - y) / (3 * x)
    if val < 0:
        return float('nan')  # cegah akar negatif
    return math.sqrt(val)

# Parameter awal
x0 = 2.5
y0 = 2.5
epsilon = 0.000001
max_iter = 1000

# Inisialisasi iterasi
x = [x0]
y = [y0]
divergent = False

# Variabel untuk pantau kestabilan error
prev_error = float("inf")
stagnant_count = 0

print("---------------------------------------------------------")
print("i\t   x\t\t   y\t\tdeltax\t\tdeltay")
print("---------------------------------------------------------")

for i in range(max_iter):
    # ====== Metode Seidel ======
    # Gunakan nilai baru x_(i+1) saat menghitung y_(i+1)
    x_new = g1A(x[i], y[i])
    y_new = g2B(x_new, y[i])   # <--- Seidel: pakai x baru
    
    delta_x = abs(x_new - x[i])
    delta_y = abs(y_new - y[i])
    total_error = delta_x + delta_y

    # Cetak iterasi
    print(f"{i}\t{x[i]:.6f}\t{y[i]:.6f}\t{delta_x:.6f}\t{delta_y:.6f}")

    # Simpan hasil iterasi
    x.append(x_new)
    y.append(y_new)

    # === Kondisi berhenti ===
    if delta_x < epsilon and delta_y < epsilon:
        print("---------------------------------------------------------")
        print(f"Konvergen pada iterasi ke-{i}")
        print(f"Hasil: x = {x_new:.6f}, y = {y_new:.6f}")
        break

    # === Deteksi divergensi ===
    if (not math.isfinite(x_new)) or (not math.isfinite(y_new)):
        print("Divergen: Nilai menjadi NaN atau tak hingga.")
        divergent = True
        break

    if abs(x_new) > 1e6 or abs(y_new) > 1e6:
        print("Divergen: Nilai terlalu besar, kemungkinan tidak konvergen.")
        divergent = True
        break

    # Jika error tidak membaik selama 10 iterasi berturut-turut
    if total_error >= prev_error - 1e-9:
        stagnant_count += 1
        if stagnant_count >= 10:
            print("Divergen: Error tidak membaik selama 10 iterasi berturut-turut.")
            divergent = True
            break
    else:
        stagnant_count = 0  # reset jika error membaik

    prev_error = total_error

# Jika selesai tapi belum konvergen
if not divergent and i >= max_iter - 1:
    print("Iterasi mencapai batas maksimum tanpa konvergensi.")
elif divergent:
    print("Iterasi dihentikan karena terdeteksi divergensi.")
