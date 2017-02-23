# This script tests if TensorFlow is setup properly
# Be sure to use python version 3.5.x
# install tensor flow using pip3
#

import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
