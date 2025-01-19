import tensorflow as tf

print("GPUs disponibles:", tf.config.list_physical_devices('GPU'))

# gpus = tf.config.list_physical_devices('GPU')
# if gpus:
#     print(f"TensorFlow detectó {len(gpus)} GPU(s): {[gpu.name for gpu in gpus]}")
# else:
#     print("TensorFlow no detecta ninguna GPU.")
