import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import numpy as np
import tensorflow as tf
import cv2
from scipy.misc import imsave, imread
import streamlit as st


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


class eyeGAN:

    batch_size = 256

    def __init__(self, model_src='models/eye'):

        
        self.img = None

        tf_config = tf.compat.v1.ConfigProto()
        tf_config.gpu_options.allow_growth = True
        self.sess = tf.compat.v1.Session(config=tf_config)

        self.load_model(model_src)

    def load_model(self, model_src = 'models/eye'):
        from model_def import generator
        assert(os.path.exists(model_src))
        checkpoint = tf.train.latest_checkpoint(model_src)
        
        self.gen, self.tf_angles, self.tf_input = generator()
        saver = tf.compat.v1.train.Saver()
        
        with self.sess.graph.as_default():
            saver.restore(self.sess, checkpoint)

        st.write("RESORTED MODEL")

        return self
            
    def load_image(self, f_img):
        img = cv2.imread(f_img)
        img = cv2.resize(img, (64, 64))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.astype(np.float32) / 127.5 - 1.0
        
        return img

    def run(self, feed_dict):
        return self.sess.run(self.gen, feed_dict=feed_dict)

    def __call__(self, f_img, a0_input, a1_input):
        # Copy it to the length of a0 and convert the files to images
        img = self.load_image(f_img)

        # Make the input is the right length
        assert(len(a0_input) == len(a1_input))

        img_out = []
        angles = [(a0,a1) for a0,a1 in zip(a0_input, a1_input)]
        
        for angle_chunk in chunks(angles, self.batch_size):
            imgs = [img] * len(angle_chunk)
            feed_dict = {self.tf_angles: angle_chunk, self.tf_input: imgs}
            imgs_generated = self.run(feed_dict)
            img_out.extend(imgs_generated)
        

        imgs_generated = np.array(imgs_generated)
        return imgs_generated



# Latent space for clf.angles_test_g
# [-1, 1] Uniform random
# (first col seems to be uniform distributed in training)
# (second col seems to only be one of -1, 0, 1, evenly distributed)
# Though it still looks ok outside this range!

if __name__ == "__main__":

    target_image = "sample.jpg"
    save_dest = "tmp/"
    if os.path.exists(save_dest):
        os.system(f"rm -rf {save_dest}")

    os.system(f"mkdir -p {save_dest}")

    a0_scale = 2.0
    a1_scale = 2.0

    # Create the angle space
    A0 = np.linspace(-1, 1, 11)*a0_scale
    A1 = np.linspace(-1, 1, 11)*a1_scale
    AX, AY = np.meshgrid(A0, A1)
    AX = AX.ravel()
    AY = AY.ravel()

    angles = np.array([AX.ravel(), AY.ravel()]).T

    G = eyeGAN()
    res = G('sample.jpg', AX, AY)
    print(res)




'''
#tf_config = tf.compat.v1.ConfigProto()
#tf_config.gpu_options.allow_growth = True
#load_dest = "models/eye"
#assert(os.path.exists(load_dest))
#checkpoint = tf.train.latest_checkpoint(load_dest)

#gen, tf_angles, tf_input = generator()
#saver = tf.compat.v1.train.Saver()

with tf.compat.v1.Session(config=tf_config) as sess:
    with sess.graph.as_default():
        saver.restore(sess, checkpoint)

        for angle_chunk in chunks(angles, batch_size):
            print(f"LEN{angle_chunk}")

            imgs = [img] * len(angle_chunk)
            feed_dict = {tf_angles: angle_chunk, tf_input: imgs}
            img_g = sess.run(gen, feed_dict=feed_dict)

            for (angle, img) in zip(angles, img_g):

                a0 = angle[0]/a0_scale
                a1 = angle[1]/a1_scale

                a0 = int(round(a0*5))
                a1 = int(round(a1*5))
                
                #f_save = f"{a0:0.5f}_{a1:0.5f}.jpg"
                f_save = f"{a0}_{a1}.jpg"
                
                f_save = os.path.join(save_dest, f_save)
                imsave(f_save, img)
                print(f_save)
'''
