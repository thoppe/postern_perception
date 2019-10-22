import tensorflow as tf
from utils.ops import relu, conv2d, lrelu, instance_norm, deconv2d, tanh


def generator():

    """ Generator.

    Parameters
    ----------
    input_: tensor, input images.
    angles: tensor, target gaze direction.
    reuse: bool, reuse the net if True.

    Returns
    -------
    x: tensor, generated image.

    """

    load_size = 64
    style_dim = 2

    angles = tf.compat.v1.placeholder(tf.float32, shape=[None, 2])
    input_ = tf.compat.v1.placeholder(tf.float32, shape=[None, load_size, load_size, 3])

    angles_reshaped = tf.reshape(angles, [-1, 1, 1, style_dim])
    angles_tiled = tf.tile(
        angles_reshaped, [1, tf.shape(input_)[1], tf.shape(input_)[2], 1]
    )
    x = tf.concat([input_, angles_tiled], axis=3)

    with tf.compat.v1.variable_scope("generator", reuse=False):

        # input layer
        x = conv2d(
            x,
            load_size,
            d_h=1,
            d_w=1,
            scope="conv2d_input",
            use_bias=False,
            pad=3,
            conv_filters_dim=7,
        )
        x = instance_norm(x, scope="in_input")
        x = relu(x)

        # encoder
        for i in range(2):

            x = conv2d(
                x,
                2 * load_size,
                d_h=2,
                d_w=2,
                scope="conv2d_%d" % i,
                use_bias=False,
                pad=1,
                conv_filters_dim=4,
            )
            x = instance_norm(x, scope="in_conv_%d" % i)
            x = relu(x)
            load_size = 2 * load_size

        # bottleneck
        for i in range(6):

            x_a = conv2d(
                x,
                load_size,
                conv_filters_dim=3,
                d_h=1,
                d_w=1,
                pad=1,
                use_bias=False,
                scope="conv_res_a_%d" % i,
            )
            x_a = instance_norm(x_a, "in_res_a_%d" % i)
            x_a = relu(x_a)
            x_b = conv2d(
                x_a,
                load_size,
                conv_filters_dim=3,
                d_h=1,
                d_w=1,
                pad=1,
                use_bias=False,
                scope="conv_res_b_%d" % i,
            )
            x_b = instance_norm(x_b, "in_res_b_%d" % i)

            x = x + x_b

        # decoder
        for i in range(2):

            x = deconv2d(
                x,
                int(load_size / 2),
                conv_filters_dim=4,
                d_h=2,
                d_w=2,
                use_bias=False,
                scope="deconv_%d" % i,
            )
            x = instance_norm(x, scope="in_decon_%d" % i)
            x = relu(x)
            load_size = int(load_size / 2)

        x = conv2d(
            x,
            3,
            conv_filters_dim=7,
            d_h=1,
            d_w=1,
            pad=3,
            use_bias=False,
            scope="output",
        )
        x = tanh(x)

    return x, angles, input_


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
