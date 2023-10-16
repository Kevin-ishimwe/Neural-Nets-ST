import numpy as np
import tensorflow as tf

rank_a =tf.constant([[ 3, 4],[9,1]])
rank_b =tf.constant([[ 1,2],[3,2]])
print(tf.reduce_max(rank_a).numpy(),tf.math.argmax(rank_a).numpy())




