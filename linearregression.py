import tensorflow as tf

# tf.enable_eager_execution()

NUM_EXAMPLES = 1000
training_inputs = tf.random.normal([NUM_EXAMPLES])
noise = tf.random.normal([NUM_EXAMPLES])
training_outputs = training_inputs * 3 + 2 + noise

def prediction(x, w, b):
    return x * w + b

# A loss function using mean-squared error
def loss(weights, biases):
    error = prediction(training_inputs, weights, biases) - training_outputs
    return tf.reduce_mean(tf.square(error))

train_steps = 200
learning_rate = 0.1
# Start with arbitrary values for W and B on the same batch of data
weight = tf.Variable(5.)
bias = tf.Variable(10.)
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
optimizer = tf.optimizers.SGD(learning_rate=learning_rate)

for i in range(20):
    print("Initial loss: {:.3f}".format(loss(weight, bias)))
    optimizer.minimize(lambda: loss(weight, bias), var_list=training_outputs)

print("Final loss: {:.3f}".format(loss(weight, bias)))
print("W = {}, B = {}".format(weight.numpy(), bias.numpy()))