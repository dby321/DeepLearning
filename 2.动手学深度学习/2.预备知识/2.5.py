import torch

x = torch.arange(4.0)
x.requires_grad_(True)
print(x.grad)
y = 2 * torch.dot(x, x)
y.backward()
print(x.grad)
x.grad.zero_()
y = x.sum()
y.backward()
print(x.grad)
x.grad.zero_()
# tensor*tensor是按元素相乘
y = x * x
print(y)
y.sum().backward()
print(x.grad)
print('--------')
x.grad.zero_()
y = x * x
u = y.detach()
z = u * x
z.sum().backward()
print(x.grad == u)
x.grad.zero_()
y.sum().backward()
print(x.grad == 2 * x)
print("---------")


def f(a):
    b = a * 2
    while b.norm() < 100:
        print("b.norm()", b.norm())
        b = b * 2
    if b.sum() > 0:
        c = b
    else:
        c = 100 * b
    return c


a = torch.randn(size=(), requires_grad=True)
print(a)
d = f(a)
d.backward()
print(a.grad == d / a)
