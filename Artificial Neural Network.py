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
