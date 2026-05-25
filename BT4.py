# áp dụng try và except try dùng để chạy đoạn code bên dưới khi code trong try bị lỗi sẽ dừng lại ngay đó 
#và khối lệnh except sẽ chạy và báo lỗi không hợp lệ
try:
    age = int(input("Nhập tuổi bệnh nhân: "))
    bp = int(input("Nhập huyết áp tâm thu (mmHg): "))
    sugar = int(input("Nhập đường huyết (mg/dL): "))

    if age < 0 or bp < 0 or sugar < 0:
        print("Dữ liệu nhập vào không hợp lệ")

    else:
        # Xét duyệt y khoa
        if age >= 75:
            print("TỪ CHỐI PHẪU THUẬT: Tuổi vượt quá giới hạn cho phép")

        elif bp < 90 or bp > 140:
            print("TỪ CHỐI PHẪU THUẬT: Huyết áp không an toàn")

        elif sugar >= 150:
            print("TỪ CHỐI PHẪU THUẬT: Đường huyết quá cao")

        else:
            print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")

except ValueError:
    print("Dữ liệu nhập vào không hợp lệ")