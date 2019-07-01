# -*- coding:utf8 -*-
#!/usr/bin/python3.6
import os


class BatchRename():
    def __init__(self):
        self.path = 'F:/fire/voc2019/jpgimages'

    def rename(self):
        f = open(r'F:/fire/voc2019/imagesets/main/train.txt', 'a')
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1

        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                str1 = str(i)
                dst = os.path.join(os.path.abspath(self.path), str1.zfill(6) + '.jpg')
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))

                    # 写入 txt 文本中的名称形式，前面加上绝对路径
                    f.write('F:/fire/VOC2019/jpgimages/' + str1.zfill(6) + '.jpg' + '\n')
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()

