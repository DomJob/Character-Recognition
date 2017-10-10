import numpy as np
import neurolab as nl

input = np.random.uniform(-0.5, 0.5, (10, 2))
target = (input[:, 0] + input[:, 1]).reshape(10, 1)

print(input)
print(target)

net = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5]], [5, 1])

err = net.train(input, target, show=15)

print(net.sim([[0.2, 0.1]]))