name_patient = str(input("Nhập họ tên: ")).strip()


if (name_patient ==""):
    print("Lỗi! Không được để trống!!")
    exit()

try:
    age_patient = int(input("Nhập tuổi: "))

except ValueError:
    print("Lỗi!! Tên hoặc tuổi(1-100) không hợp lệ")
    exit()

if (age_patient <= 0 and age_patient > 100 ):
    result = "Lỗi!! Tên hoặc tuổi(1-100) không hợp lệ"
elif (age_patient >= 1 and age_patient <= 6 ):
    result = "Ưu tiên! : Bệnh Nhi - Chuyển thẳng đến phòng khám Nhi"
elif (age_patient >= 80):
    result = "Ưu tiên! :Người cao tuổi - Hổ trợ xe lăn, chuyển đến phòng khám Lão Khoa"
else:
    result = "Khám thường! : Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh"


print("\n===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====")
print("Họ và tên:", name_patient)
print("Tuổi:", age_patient)
print("Phân luồng:", result)


