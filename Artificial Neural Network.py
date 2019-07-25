#Prediksi Cuaca

from numpy import exp, array, random, dot, argmax

#hyperparameter

input_node = 4
hidden_node = 10
output_node  = 3
learning_rate = 0.01
epoch = 1000

#input
inputs = input("masukkan input: ")
inputs =[int(i) for i in inputs.split() if(i.isdigit())]
inputs = array(inputs, ndmin=2).T
print(inputs)

output = input("Masukkan output: ")
output = [int (o) for o in output.split() if(o.isdigital())]
output = array(output, ndmin=2).T
print (output)

#weight atau bobot
input_to_hidden_weight = 2*(random.random((hidden_node, input_node)) - 0.5)
hidden_to_output_weight = 2*(random.random((hidden_node, output_node)) - 0.5)

print(input_to_hidden_weight)
print(hidden_to_output_weight)

#training
for ep in range(epoch):
    #forward propagation
    output_hidden = 1/(1 + exp (-(dot(input_to_hidden_weight, inputs))))
    output_ann = 1/(1 + exp (-(dot(hidden_to_ouput_weight, output_hidden))))
    
    #backpropagation
    error_output = output - ouput_ann
    error_hidden = dot(hidden_to_output_weight.T, error_output)
    hidden_to_output_weight += learning_rate*dot(error_output*output_ann*(1-output_ann))
    input_to_hidden_weight += learning_rate*dot(error_hidden*output_hidden*(1-output_hidden))
    
#evaluation
print("True Output: {}\nArtificial Neural Network Output: {}\Accuracy: {}%".format(output.T, output_ann.T, (1-(output[argmax(output)]-output_ann[argmax(output_ann)]))[0]*100.0))
