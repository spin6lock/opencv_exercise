import cv2

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
