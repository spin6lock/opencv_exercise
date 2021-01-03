# OpenCV人脸识别笔记

* 插入usb摄像头，通过fswebcam这款小工具测试摄像头是否正常：`sudo dnf install fswebcam` 和 `fswebcam --no-banner -r 640x480 image.jpg`
* 安装opencv的python版本，测试是否安装正常: 在python解释器中输入`import cv2; print(cv2.__version__)`
* 下载opencv仓库：`git clone https://github.com/opencv/opencv.git` 分类器在: `data\haarcascades`
* 运行捕获视频的代码

