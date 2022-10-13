import torch
import numpy as np

def manuallyCrossEntropy(input, target):
    N = target.view(1,-1).size()[1]

    l = torch.sum(target* torch.log(input)+(1-target)*torch.log(1-input)) / N * -1
    return l

# input = torch.tensor([0.9995])
# target = torch.tensor([0.])

data = np.loadtxt("test.txt")
input = data[:, 0:2]
target = data[:,2]

print("manually:", manuallyCrossEntropy(input, target))
# loss = torch.nn.CrossEntropyLoss()
loss = torch.nn.BCELoss()
output = loss(input, target)
print(output)


