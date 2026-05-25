donor_age = int(input("Nhập số tuổi: "))
donor_weight = float(input("Nhập số cân nặng: "))


print("---Kiểm tra sức khỏe----")


if (donor_age >= 18 and donor_weight >= 50):
    print("Đủ điều kiện hiến máu")

else:
    print("không đủ điều kiện, sức khỏe không đủ!!")

print("Hoàn thành kiểm tra.")