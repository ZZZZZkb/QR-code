#videocapture 在第138行
# -*- coding:utf-8 –*-
import cv2
import pyzbar.pyzbar as pyzbar


def decodeDisplay(video):
    # 转为灰度图像
    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    for barcode in barcodes:
        # 提取二维码的位置,然后用边框标识出来在视频中
        (x, y, w, h) = barcode.rect
        cv2.rectangle(video, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 字符串转换
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        # 在图像上面显示识别出来的内容
        text = "{}".format(barcodeData)
        cv2.putText(video, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # 打印识别后的内容

        a = format(barcodeData)
        print("[扫描结果] 二维码类别： {0} 内容： {1}".format(barcodeType, barcodeData))




        from urllib import parse, request
        textmod = {'password': 'admin'}
        textmod = parse.urlencode(textmod)

        # 输出内容:user=admin&password=admin
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
        url = a
        req = request.Request(url='%s%s%s' % (url, '?', textmod), headers=header_dict)
        res = request.urlopen(req)
        res = res.read()
        shuchu = res.decode(encoding='utf-8')
        # 输出内容(python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码):b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f'
        print(shuchu)
        # 输出内容:登录成功--MichaelAn--
        zhengli = shuchu[0:6]
        print(zhengli)
        print(zhengli.endswith('0'))
        jieguo = zhengli.endswith('0')
        print(jieguo)
        if zhengli.endswith('0'):
            print('zzzz')
        else:
            print('kkkk')

        # coding:utf-8
        if zhengli.endswith('0'):
            # coding:utf-8

            import webbrowser

            # 命名生成的html
            GEN_HTML = "test.html"
            # 打开文件，准备写入
            f = open(GEN_HTML, 'w')

            # 准备相关变量
            str1 = res.decode(encoding='utf-8')
            str2 = ' '

            # 写入HTML界面中
            message = """
            <html>
            <head></head>
            <body>
            <p>%s</p>
            <p>%s</p>
            </body>
            </html>
            """ % (str1, str2)

            # 写入文件
            f.write(message)
            # 关闭文件
            f.close()

            # 运行完自动在网页中显示
            webbrowser.open(GEN_HTML, new=1)
            '''
            webbrowser.open(url, new=0, autoraise=True) 
            Display url using the default browser. If new is 0, the url is opened in the same browser window if possible. If new is 1, a new browser window is opened if possible. If new is 2, a new browser page (“tab”) is opened if possible. If autoraise is True, the window is raised if possible (note that under many window managers this will occur regardless of the setting of this variable).
            '''

        else:
            # coding:utf-8

            import webbrowser

            # 命名生成的html
            GEN_HTML = "test.html"
            # 打开文件，准备写入
            f = open(GEN_HTML, 'w')

            # 准备相关变量
            str1 = res.decode(encoding='utf-8')
            str2 = 'zzzz'

            # 写入HTML界面中
            message = """
            <html>
            <head>
                <style>
                    p {
                        color: green;
                    }
                </style>
            </head>
            <body>
            <p>%s</p>
             </body>
            </html>
            """ % (str1)

            # 写入文件
            f.write(message)
            # 关闭文件
            f.close()

            # 运行完自动在网页中显示
            webbrowser.open(GEN_HTML, new=1)
            '''
            webbrowser.open(url, new=0, autoraise=True) 
            Display url using the default browser. If new is 0, the url is opened in the same browser window if possible. If new is 1, a new browser window is opened if possible. If new is 2, a new browser page (“tab”) is opened if possible. If autoraise is True, the window is raised if possible (note that under many window managers this will occur regardless of the setting of this variable).
            '''

    cv2.imshow("cam", video)


def detect():
    cv2.namedWindow("cam", cv2.WINDOW_NORMAL)
    cam = cv2.VideoCapture(0)
    while True:
        # 读取当前帧
        ret, frame = cam.read()
        decodeDisplay(frame)
        # 按ESC键退出
        if (cv2.waitKey(5) == 27):
            break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect()