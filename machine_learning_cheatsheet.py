# https://github.com/tensorflow/tensorflow/issues/7457

# UnboundLocalError: local variable 'status' referenced before assignment #7457

# https://github.com/tensorflow/tensorflow/issues/3388

# /home/magnus/anaconda3/envs/tensorflow/bin/python /home/magnus/development/TensorFlow-Tutorials/sandbox3.py
# 56088x`
# Exception ignored in: <bound method BaseSession.__del__ of <tensorflow.python.client.session.Session object at 0x7fb4ecd301d0>>
# Traceback (most recent call last):
#   File "/home/magnus/anaconda3/envs/tensorflow/lib/python3.5/site-packages/tensorflow/python/client/session.py", line 171, in __del__
#   File "/home/magnus/anaconda3/envs/tensorflow/lib/python3.5/site-packages/tensorflow/python/client/session.py", line 167, in close
# AttributeError: 'NoneType' object has no attribute 'raise_exception_on_not_ok_status'

# Process finished with exit code 0
# https://stackoverflow.com/questions/40560795/tensorflow-attributeerror-nonetype-object-has-no-attribute-tf-deletestatus

# Load Data.
# Define Model.
# Compile Model.
# Fit Model.
# Evaluate Model.
# Tie It All Together.

model.fit_generator(train_generator, samples_per_epoch= /
            len(train_samples), validation_data=validation_generator, /
            nb_val_samples=len(validation_samples), nb_epoch=3)

keras.layers.convolutional.Conv2D(
	filters,
	kernel_size,
	strides=(1, 1),
	padding='valid',
	data_format=None,
	dilation_rate=(1, 1),
	activation=None,
	use_bias=True,
	kernel_initializer='glorot_uniform',
	bias_initializer='zeros',
	kernel_regularizer=None,
	bias_regularizer=None,
	activity_regularizer=None,
	kernel_constraint=None,
	bias_constraint=None)