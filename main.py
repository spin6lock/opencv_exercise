import cv2

def face_recognition(frame):
    face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转为灰度图
    # 检测脸部
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.1,
                                          minNeighbors=5,
                                          minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)
    print('Detected ', len(faces), " face")
    return faces

def mark_faces(img, faces):
    # 标记位置
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
    return img

def main():
    # 捕获指定摄像头的实时视频流
    cap = cv2.VideoCapture(0)
    print("摄像头是否已经打开 ？ {}".format(cap.isOpened()))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    cv2.namedWindow('image_win',flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
    image_count = 1
    while True:
        ret, frame = cap.read()
        if not ret:
            print("图像获取失败")
            continue
        faces = face_recognition(frame)
        frame = mark_faces(frame, faces)
        cv2.imshow("image_win", frame)
        key = cv2.waitKey(100)
        if key == ord('q'):
            print("exit")
            break
        elif key == ord('c'):
            cv2.imwrite(f'{image_count}.jpg', frame)
            print(f"截图并保存为 {image_count}.jpg")
            image_count = image_count + 1
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
