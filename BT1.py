print("---EMERGENCY TRIAGE SYSTEM---")
heart_rate = int(input(" Enter patinet's heart rate(bpm): "))

if (heart_rate >= 60 and heart_rate <= 100 ):
    print("|GREEN|--Nhịp tim ổn định, chờ theo thứ tự")

elif(heart_rate < 60):
    print("|BLUE|--Nhịp tim chậm, cần kiểm tra thêm")

elif(heart_rate > 100 and heart_rate < 120):
    print("|YELLOW|--Nhịp tim bất thường, cần theo dõi sát")

else:
    print("|RED|--Nguy kịch!!!, cần cấp cứu ngay")

    print("Hoàn thành kiểm tra!!!")