import matplotlib
# Bắt buộc dùng Agg cho QEMU vì nó không có giao diện hiển thị ảnh trực tiếp
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
from sensor_sim import SimUltrasonic, SimPotentiometer
from time import sleep

# ==========================================
# BƯỚC 5: Khởi tạo và thu thập dữ liệu
# ==========================================
us = SimUltrasonic(echo=24, trigger=23, base_distance=50.0)
pot = SimPotentiometer(initial_value=0.4)  # Đặt mức ban đầu là 0.4 (tương đương span = 40cm)
span = pot.value * 100  # Chuyển đổi sang cm

distances = []
# Thu thập 50 mẫu dữ liệu
for i in range(50):
    d = us.distance
    distances.append(d)
    print(f"  Mẫu {i+1}/50: {d:.1f} cm")
    sleep(0.1)  # Đợi 0.1s cho lẹ

print(f"\nThu thập xong {len(distances)} mẫu.")

# ==========================================
# BƯỚC 6: Vẽ đồ thị lưu ra file
# ==========================================
fig, ax = plt.subplots(figsize=(10, 5))
x = range(len(distances))

# Vẽ đường biểu diễn khoảng cách (màu xanh)[cite: 1]
ax.plot(x, distances, 'b-', linewidth=1.5, label='Khoảng cách (cm)')

# Vẽ đường ngưỡng span (màu đỏ, nét đứt)[cite: 1]
ax.axhline(y=span, color='r', linestyle='--', linewidth=2, label=f'Span = {span:.0f} cm')

# Tô màu vùng Span (khi khoảng cách < ngưỡng span)[cite: 1]
ax.fill_between(x, 0, [min(d, span) for d in distances],
                 alpha=0.2, color='red', label='Vùng Span!')

# Định dạng các nhãn và tiêu đề[cite: 1]
ax.set_title('Ultrasonic Sensor Simulation — Span Detection')
ax.set_xlabel('Sample')
ax.set_ylabel('Distance (cm)')
ax.set_ylim(0, max(distances) + 10)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
# Lưu đồ thị ra file ảnh[cite: 1]
plt.savefig('sensor_chart.png', dpi=150)
print('Saved: sensor_chart.png')
