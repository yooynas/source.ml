import tensorflow as tf
import predict_pb2

# Inputs
#   raw json (binary)
# Outputs
#   TensorFlow PredictRequest (protobuf) 
def input_transformer(inputs):
    input_str = inputs.decode('utf-8')
    input_json = json.loads(input_str)
    inputs_np = np.asarray([input_json['inputs']])
    inputs_tensor_proto = tf.contrib.util.make_tensor_proto(inputs_np,
                                                            dtype=tf.float32)
    request = predict_pb2.PredictRequest()
    request.inputs['inputs'].CopyFrom(inputs_tensor_proto)
    

# Inputs
#   TensorFlow PredictResponse (protobuf)
# Outputs
#   raw json 
def output_transformer(outputs):
    outputs_np_array = tf.contrib.util.make_ndarray(result.outputs['outputs'])
    return json.dumps({"outputs": outputs_np_array.tolist()[0]})
