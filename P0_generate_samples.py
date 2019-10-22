import os
import numpy as np
import tensorflow as tf
import cv2
from scipy.misc import imsave, imread
from model_def import generator, chunks

batch_size = 256

# Latent space for clf.angles_test_g
# [-1, 1] Uniform random
# (first col seems to be uniform distributed in training)
# (second col seems to only be one of -1, 0, 1, evenly distributed)
# Though it still looks ok outside this range!

target_image = "sample.jpg"
save_dest = "tmp/"
if os.path.exists(save_dest):
    os.system(f"rm -rf {save_dest}")

os.system(f"mkdir -p {save_dest}")

# Create the angle space
A0 = np.linspace(-1, 1, 20)
A1 = np.linspace(-1, 1, 20)
AX, AY = np.meshgrid(A0, A1)
angles = np.array([AX.ravel(), AY.ravel()]).T

img = cv2.imread(target_image)
img = cv2.resize(img, (64, 64))
img = img.astype(np.float32) / 127.5 - 1.0


tf_config = tf.compat.v1.ConfigProto()
tf_config.gpu_options.allow_growth = True
checkpoint = tf.train.latest_checkpoint("models/log")

gen, tf_angles, tf_input = generator()
saver = tf.compat.v1.train.Saver()

with tf.compat.v1.Session(config=tf_config) as sess:
    with sess.graph.as_default():
        saver.restore(sess, checkpoint)

        for angle_chunk in chunks(angles, batch_size):
            print(f"LEN{angle_chunk}")

            imgs = [img] * len(angle_chunk)
            feed_dict = {tf_angles: angle_chunk, tf_input: imgs}
            img_g = sess.run(gen, feed_dict=feed_dict)

            for (angle, img) in zip(angles, img_g):
                f_save = f"{angle[0]:0.5f}_{angle[1]:0.5f}.jpg"
                f_save = os.path.join(save_dest, f_save)
                imsave(f_save, img)
                print(f_save)
