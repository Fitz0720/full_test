import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()


"""
opencv自带的VideoCapture()函数定义摄像头对象，其参数0表示第一个摄像头，有多个摄像头的情况下参数换1、2、3……试试
在while循环中，利用摄像头对象的read()函数读取视频的某帧，并显示，然后等待1个单位时间，如果期间检测到了键盘输入q，则退出，即关闭窗口。
调用release()释放摄像头，调用destroyAllWindows()关闭所有图像窗口。

"""
