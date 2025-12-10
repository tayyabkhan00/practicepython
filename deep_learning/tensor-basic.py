import torch

# Creating Tensors
x = torch.tensor([1, 2, 3])        # 1D tensor
m = torch.tensor([[1, 2], [3, 4]]) # 2D tensor

# Tensor Operations (like NumPy)
a = torch.tensor([1., 2., 3.])
b = torch.tensor([4., 5., 6.])

print(a + b)
print(a * b)
print(a @ b)   # dot product

# GPU Tensors
device = "cuda" if torch.cuda.is_available() else "cpu"
x = torch.tensor([1, 2, 3]).to(device)
print(x.device)

# Tensor Gradients (Autograd)
x = torch.tensor(2.0, requires_grad=True)
y = x ** 3 + 2 * x
y.backward()
print(x.grad)   # derivative of y wrt x
