# Import libraries
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from torchvision.datasets import MNIST
from torchvision import transforms
import wandb
import matplotlib.pyplot as plt

# Initialize W&B
wandb.init(project="pytorch-opencampus")


# Define the neural network model
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


# Load MNIST dataset
transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)
train_dataset = MNIST(root="./data", train=True, transform=transform, download=True)
test_dataset = MNIST(root="./data", train=False, transform=transform, download=True)

# Hyperparameters
input_size = 28 * 28
hidden_size = 128
output_size = 10
learning_rate = 0.001
batch_size = 64
epochs = 5

# Initialize the model
model = SimpleNN(input_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# DataLoader
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# Training loop
for epoch in range(epochs):
    for batch_idx, (data, target) in enumerate(train_loader):
        data = data.view(-1, input_size)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

    # Evaluate on the test set
    test_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in test_loader:
            data = data.view(-1, input_size)
            output = model(data)
            test_loss += criterion(output, target).item()
            _, predicted = output.max(1)
            total += target.size(0)
            correct += predicted.eq(target).sum().item()

    accuracy = correct / total

    # Log metrics to W&B
    wandb.log(
        {
            "epoch": epoch + 1,
            "accuracy": accuracy,
            "test_loss": test_loss / len(test_loader),
        }
    )

# Log hyperparameters to W&B
wandb.config.update(
    {
        "input_size": input_size,
        "hidden_size": hidden_size,
        "output_size": output_size,
        "learning_rate": learning_rate,
        "batch_size": batch_size,
        "epochs": epochs,
    }
)

# Visualize a sample image (example chart)
sample_image = train_dataset[0][0].numpy().reshape(28, 28)
plt.imshow(sample_image, cmap="gray")
wandb.log({"sample_image": plt})

# Finish W&B run
wandb.finish()
