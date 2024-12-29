import matplotlib.pyplot as plt
import torchvision

dataset = torchvision.datasets.MNIST(
    root='image_datasets/mnist/', train=True, download=False, transform=None
)

print(f'Number of images in the dataset: {len(dataset)}')
print(f'Image size: {dataset[0][0].size}')
print(f'Label: {dataset[0][1]}')

image, label = dataset[0]
plt.imshow(image, cmap='gray')
plt.title(f'Label: {label}')
plt.show()
