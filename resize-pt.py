import cv2
import os


fullfilename=[]
filepath = "F:/fire/voc2019/jpgimages1"   # 不能包含中文路径
filepath1 = "F:/fire/voc2019/jpgimages"
for filename in os.listdir(filepath):
    print(filename)
    print(os.path.join(filepath, filename))
    filelist = os.path.join(filepath, filename)
    fullfilename.append(filelist)
i = 1
for imagename in fullfilename:
    img = cv2.imread(imagename)
    img = cv2.resize(img, (416, 416))   # 该句报错，路径中包含中文
    resizename = str(i)+'.jpg'          # 命名形式为1,2,3... 需重新命名位000001,000002，000003...
    isExists = os.path.exists(filepath1)
    if not isExists:
        os.makedirs(filepath1)
        print('mkdir resizename accomploshed')
    savename = filepath1+'/'+resizename
    cv2.imwrite(savename, img)
    print('{} is resized'.format(savename))
    i = i+1
