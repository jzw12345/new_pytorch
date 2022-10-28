import torch
# 创建元素值为范围[0, 10)步长为1的1D整数序列张量
a = torch.randn(1, 256,32,32)
b = torch.randn(1, 256,1,1)
b.expand_as(a)
print(b.expand_as(a).shape)

c=torch.tensor([[],[]])
print(c.shape)