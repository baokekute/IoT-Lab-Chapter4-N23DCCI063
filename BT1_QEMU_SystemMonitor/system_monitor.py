import psutil
from datetime import datetime
from time import sleep

# Bước 5: Mở file log ở chế độ ghi mới
log_file = open('system_log.txt', 'w')

try:
    print("--- Bắt đầu giám sát hệ thống (Nhấn Ctrl+C để dừng) ---")
    while True:
        # Bước 2: Đọc CPU từng lõi và tính trung bình
        cpu_list = psutil.cpu_percent(interval=1, percpu=True)
        cpu_avg = sum(cpu_list) / len(cpu_list)

        # Bước 3: Đọc RAM (đổi sang MB) và Disk
        ram = psutil.virtual_memory()
        ram_used_mb = ram.used // (1024 ** 2)
        ram_total_mb = ram.total // (1024 ** 2)
        ram_pct = ram.percent
        
        disk = psutil.disk_usage('/')
        disk_pct = disk.percent

        # Bước 7: Phân loại trạng thái cảnh báo 3 mức
        if cpu_avg >= 70:
            status = 'CRITICAL'
        elif cpu_avg >= 30:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        # Bước 4 & 7: Định dạng chuỗi output chuẩn format bao gồm trạng thái
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = f'[{now}] CPU: {cpu_avg:.1f}% | RAM: {ram_used_mb}/{ram_total_mb} MB ({ram_pct}%) | Disk: {disk_pct}% | {status}'
        
        # In kết quả ra terminal
        print(line)
        
        # Bước 7: In dòng cảnh báo riêng nếu CPU cao
        if status != 'NORMAL':
            print(f'  ⚠ {status}: CPU đang ở mức cao {cpu_avg:.1f}%')

        # Bước 5: Ghi dữ liệu vào file và ép dữ liệu xuống đĩa (flush)[cite: 1]
        log_file.write(line + '\n')
        log_file.flush() 

        # Bước 4: Lặp lại mỗi 2 giây[cite: 1]
        sleep(2)

except KeyboardInterrupt:
    # Bước 6: Bắt sự kiện dừng chương trình bằng phím Ctrl+C[cite: 1]
    print('\n[Thông báo] Đã dừng giám sát.')
finally:
    # Bước 6: Đảm bảo đóng file an toàn sau khi dừng[cite: 1]
    log_file.close()
    print('Log đã được lưu thành công vào system_log.txt')
