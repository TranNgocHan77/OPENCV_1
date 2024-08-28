import cv2

def threshold_real_time():
    # Khởi tạo video capture từ camera mặc định
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Đọc khung hình từ camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            break

        # Chuyển đổi khung hình sang ảnh grayscale
        imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Áp dụng ngưỡng ảnh
        ret, thresh = cv2.threshold(imgray, 100, 255, cv2.THRESH_BINARY_INV)

        # Hiển thị hình ảnh gốc và hình ảnh đã áp dụng ngưỡng
        cv2.imshow('Original Frame', frame)
        cv2.imshow('Threshold Frame', thresh)

        # Thoát khi nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng tài nguyên
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    threshold_real_time()
