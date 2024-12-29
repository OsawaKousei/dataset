import torchvision

dataset = torchvision.datasets.MNIST(
    root='image_datasets/mnist/', train=True, download=True, transform=None
)
