import os
import random
import string
import datetime
import tensorflow as tf
from itertools import islice

max_pic_num = 600 # define one class of dog total picture numbers.

def GetDataPath():
    ''' get origin picture path'''

    flags = tf.app.flags
    flags.DEFINE_string("data_path", "voc", "directory of dogs, for enhance data.")
    flags.DEFINE_string("enhance_data_path", "jpgimages", "directory for store enhance data.")
    FLAGS = flags.FLAGS

    print("data path:%s" % FLAGS.data_path)
    print("enhance data path:%s" % FLAGS.enhance_data_path)

    return FLAGS.data_path,FLAGS.enhance_data_path

def RandEnhancePicture(picname, savepath):
    ''' random use one of [tf.image.flip_up_down, tf.image.flip_left_right, tf.image.random_brightness,
    tf.image.random_contrast, tf.image.random_hue, tf.image.random_saturation, tf.image.adjust_gamma] image Ops
    to enhance origin picture, and save to enhance data path'''

    filename, suffix = os.path.splitext(picname)  # get picture name
    filename = os.path.basename(filename) # get base picture name
    filename += "_"
    img = None

    oldtime = datetime.datetime.now()

    tf.reset_default_graph()

    image = tf.read_file(picname) # read picture from gving path.
    image_decode_jpeg = tf.image.decode_jpeg(image)
    image_decode_jpeg = tf.image.convert_image_dtype(image_decode_jpeg, dtype=tf.float32) # convert image dtype to float
    newtime_1 = datetime.datetime.now()
    print("21 --> %s" % (newtime_1 - oldtime))

    rand = random.randint(1,7) # we only use 7 image Ops.
    if rand == 1: # flip up down
        image_flip_up_down = tf.image.flip_up_down(image_decode_jpeg)
        image_flip_up_down = tf.image.convert_image_dtype(image_flip_up_down, dtype=tf.uint8)
        img = tf.image.encode_jpeg(image_flip_up_down)
    if rand == 2: # flip left right
        image_flip_left_right = tf.image.flip_left_right(image_decode_jpeg)
        image_flip_left_right = tf.image.convert_image_dtype(image_flip_left_right, dtype=tf.uint8)
        img = tf.image.encode_jpeg(image_flip_left_right)
    if rand == 3: # random adjust brightness
        image_random_brightness = tf.image.random_brightness(image_decode_jpeg, max_delta=0.01)
        image_random_brightness = tf.image.convert_image_dtype(image_random_brightness, dtype=tf.uint8)
        img = tf.image.encode_jpeg(image_random_brightness)
    if rand == 4: # random adjust contrast
        image_random_contrast = tf.image.random_contrast(image_decode_jpeg, 0.8, 1)
        image_random_contrast = tf.image.convert_image_dtype(image_random_contrast, dtype=tf.uint8)
        img = tf.image.encode_jpeg(image_random_contrast)
    if rand == 5: # random adjust hue
        image_random_hue = tf.image.random_hue(image_decode_jpeg, max_delta=0.05)
        image_random_hue = tf.image.convert_image_dtype(image_random_hue, dtype=tf.uint8)
        img = tf.image.encode_jpeg(image_random_hue)
    if rand == 6: # random adjust saturation
        image_random_saturation = tf.image.random_saturation(image_decode_jpeg, 0.7, 1)
        image_random_saturation = tf.image.convert_image_dtype(image_random_saturation, dtype=tf.uint8)
        img = tf.image.encode_jpeg(image_random_saturation)
    if rand == 7: # adjust gamma
        image_adjust_gamma = tf.image.adjust_gamma(image_decode_jpeg, gamma=2)
        image_adjust_gamma = tf.image.convert_image_dtype(image_adjust_gamma, dtype=tf.uint8)
        img = tf.image.encode_jpeg(image_adjust_gamma)
    newtime_2 = datetime.datetime.now()
    print("22 --> %s" % (newtime_2 - newtime_1))
    # save image
    openfile = filename + "".join(random.sample(string.digits, 8)) + suffix  # random rename picture avoid conflict
    hd = tf.gfile.FastGFile(os.path.join(savepath, openfile), "w")
    with tf.Session() as sess:  # create tensorflow session
        img = sess.run(img)
        newtime_3 = datetime.datetime.now()
        print("23 --> %s" % (newtime_3 - newtime_2))
    tf.get_default_graph().finalize()

    hd.write(img)
    hd.close()
    newtime_4 = datetime.datetime.now()
    print("24 --> %s" % (newtime_4 - newtime_3))
    newtime = datetime.datetime.now()
    print("2 total --> %s" % (newtime - oldtime))


def EnhancePictureAndSave(picname, savepath):
    ''' use one of [tf.image.flip_up_down, tf.image.flip_left_right, tf.image.random_brightness,
    tf.image.random_contrast, tf.image.random_hue, tf.image.random_saturation, tf.image.adjust_gamma] image Ops
    to enhance origin picture, and save to enhance data path'''

    oldtime = datetime.datetime.now()

    tf.reset_default_graph()

    filename, suffix = os.path.splitext(picname) # get picture path
    filename = os.path.basename(filename) # get base picture name
    filename += "_"

    image = tf.read_file(picname) # read picture from gving path.
    image_decode_jpeg = tf.image.decode_jpeg(image)
    image_decode_jpeg = tf.image.convert_image_dtype(image_decode_jpeg, dtype=tf.float32) # convert image dtype to float
    newtime_1 = datetime.datetime.now()
    print("1 --> %s" % (newtime_1 - oldtime))

    # flip up down
    image_flip_up_down = tf.image.flip_up_down(image_decode_jpeg)
    image_flip_up_down = tf.image.convert_image_dtype(image_flip_up_down, dtype=tf.uint8)
    image_flip_up_down = tf.image.encode_jpeg(image_flip_up_down)
    newtime_2 = datetime.datetime.now()
    print("2 --> %s" % (newtime_2 - newtime_1))
    # save image
    openfile = filename +  "".join(random.sample(string.digits, 8)) + suffix # random rename picture avoid conflict
    hd_up_down = tf.gfile.FastGFile(os.path.join(savepath, openfile), "w")
    newtime_3 = datetime.datetime.now()
    print("3 --> %s" % (newtime_3 - newtime_2))

    # flip left right
    image_flip_left_right = tf.image.flip_left_right(image_decode_jpeg)
    image_flip_left_right = tf.image.convert_image_dtype(image_flip_left_right, dtype=tf.uint8)
    image_flip_left_right = tf.image.encode_jpeg(image_flip_left_right)
    newtime_4 = datetime.datetime.now()
    print("4 --> %s" % (newtime_4 - newtime_3))
    # save image
    openfile = filename + "".join(random.sample(string.digits, 8)) + suffix  # random rename picture avoid conflict
    hd_left_right = tf.gfile.FastGFile(os.path.join(savepath, openfile), "w")
    newtime_5 = datetime.datetime.now()
    print("5 --> %s" % (newtime_5 - newtime_4))

    # random adjust brightness
    image_random_brightness = tf.image.random_brightness(image_decode_jpeg, max_delta=0.01)
    image_random_brightness = tf.image.convert_image_dtype(image_random_brightness, dtype=tf.uint8)
    image_random_brightness = tf.image.encode_jpeg(image_random_brightness)
    newtime_6 = datetime.datetime.now()
    print("6 --> %s" % (newtime_6 - newtime_5))
    # save image
    openfile = filename + "".join(random.sample(string.digits, 8)) + suffix  # random rename picture avoid conflict
    hd_adj_brightness = tf.gfile.FastGFile(os.path.join(savepath, openfile), "w")
    newtime_7 = datetime.datetime.now()
    print("7 --> %s" % (newtime_7 - newtime_6))

    # random adjust contrast
    image_random_contrast = tf.image.random_contrast(image_decode_jpeg, 0.8, 1)
    image_random_contrast = tf.image.convert_image_dtype(image_random_contrast, dtype=tf.uint8)
    image_random_contrast = tf.image.encode_jpeg(image_random_contrast)
    newtime_8 = datetime.datetime.now()
    print("8 --> %s" % (newtime_8 - newtime_7))
    # save image
    openfile = filename + "".join(random.sample(string.digits, 8)) + suffix  # random rename picture avoid conflict
    hd_adj_contrast = tf.gfile.FastGFile(os.path.join(savepath, openfile), "w")
    newtime_9 = datetime.datetime.now()
    print("9 --> %s" % (newtime_9 - newtime_8))

    # random adjust hue
    image_random_hue = tf.image.random_hue(image_decode_jpeg, max_delta=0.05)
    image_random_hue = tf.image.convert_image_dtype(image_random_hue, dtype=tf.uint8)
    image_random_hue = tf.image.encode_jpeg(image_random_hue)
    newtime_10 = datetime.datetime.now()
    print("10 --> %s" % (newtime_10 - newtime_9))
    # save image
    openfile = filename + "".join(random.sample(string.digits, 8)) + suffix  # random rename picture avoid conflict
    hd_adj_hue = tf.gfile.FastGFile(os.path.join(savepath, openfile), "w")
    newtime_11 = datetime.datetime.now()
    print("11 --> %s" % (newtime_11 - newtime_10))

    # random adjust saturation
    image_random_saturation = tf.image.random_saturation(image_decode_jpeg, 0.7, 1)
    image_random_saturation = tf.image.convert_image_dtype(image_random_saturation, dtype=tf.uint8)
    image_random_saturation = tf.image.encode_jpeg(image_random_saturation)
    newtime_12 = datetime.datetime.now()
    print("12 --> %s" % (newtime_12 - newtime_11))
    # save image
    openfile = filename + "".join(random.sample(string.digits, 8)) + suffix  # random rename picture avoid conflict
    hd_adj_saturation = tf.gfile.FastGFile(os.path.join(savepath, openfile), "w")
    newtime_13 = datetime.datetime.now()
    print("13 --> %s" % (newtime_13 - newtime_12))

    # adjust gamma
    image_adjust_gamma = tf.image.adjust_gamma(image_decode_jpeg, gamma=2)
    image_adjust_gamma = tf.image.convert_image_dtype(image_adjust_gamma, dtype=tf.uint8)
    image_adjust_gamma = tf.image.encode_jpeg(image_adjust_gamma)
    newtime_14 = datetime.datetime.now()
    print("14 --> %s" % (newtime_14 - newtime_13))
    # save image
    openfile = filename + "".join(random.sample(string.digits, 8)) + suffix  # random rename picture avoid conflict
    hd_adj_gamma = tf.gfile.FastGFile(os.path.join(savepath, openfile), "w")

    with tf.Session() as sess:  # create tensorflow session
        img_up_down, img_left_right, img_brightness, img_contrast, img_hue, img_saturation, img_gamma \
            = sess.run([image_flip_up_down, image_flip_left_right, image_random_brightness, image_random_contrast,
                        image_random_hue, image_random_saturation, image_adjust_gamma])
    tf.get_default_graph().finalize()

    newtime_15 = datetime.datetime.now()
    print("15 --> %s" % (newtime_15 - newtime_14))
    hd_up_down.write(img_up_down)
    hd_up_down.close()
    hd_left_right.write(img_left_right)
    hd_left_right.close()
    hd_adj_brightness.write(img_brightness)
    hd_adj_brightness.close()
    hd_adj_contrast.write(img_contrast)
    hd_adj_contrast.close()
    hd_adj_hue.write(img_hue)
    hd_adj_hue.close()
    hd_adj_saturation.write(img_saturation)
    hd_adj_saturation.close()
    hd_adj_gamma.write(img_gamma)
    hd_adj_gamma.close()

    newtime_16 = datetime.datetime.now()
    print("16 --> %s" % (newtime_16 - newtime_15))
    newtime = datetime.datetime.now()
    print("total --> %s" % (newtime - oldtime))

def EnhanceData():
    '''enhance picture to max count 600 handling'''
    data_path,enhance_path = GetDataPath()

    if tf.gfile.Exists(enhance_path): # make enhance data directory
        tf.gfile.DeleteRecursively(enhance_path)

    walk = tf.gfile.Walk(data_path)
    walk = islice(walk, 1, None) # skip parent directory
    for info in walk:
        basedir = os.path.basename(info[0])
        tf.gfile.MakeDirs(os.path.join(enhance_path, basedir))

        for pic in info[2]: # copy origin picture to save path
            picname = os.path.join(info[0], pic)  # join path and picname
            tf.gfile.Copy(picname, os.path.join(enhance_path, basedir, os.path.basename(picname)))
            remaincount = max_pic_num - len(info[2])

        # picture total nums is 600, that will make every picture enhance enhance_times_per_pic
        if len(info[2]) <= (remaincount / 7):
            for pic in info[2]:
                picname = os.path.join(info[0], pic) # join path and picname
                EnhancePictureAndSave(picname, os.path.join(enhance_path, basedir))
                remaincount -= 7 # every time enhance picture will increase 7 frame.

        for index in range(remaincount):
            rand = random.randint(0, len(info[2])-1)
            picname = os.path.join(info[0], info[2][rand])  # join path and picname
            RandEnhancePicture(picname, os.path.join(enhance_path, basedir))
            #sess.close() # close tensorflow session

if __name__ == "__main__":
    print("begin to enhance picture data!!!")
    EnhanceData()
    print("end of enhance picture data, good luck!!!")