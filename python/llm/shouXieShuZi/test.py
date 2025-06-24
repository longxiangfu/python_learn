import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch.nn.functional import one_hot

# 获取设备
device = torch.device('cuda:0')

# 定义转换操作，将数据转化为PyTorch张量并归一化
transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 加载MNIST数据集
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transforms)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transforms)

# 创建数据加载器
train_loader = DataLoader(dataset=train_dataset, batch_size=6000, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=6000, shuffle=False)

# 定义模型   y = wx + b
# self.fc1 = nn.Linear(28 * 28, 200)
# 其中28 * 28表示输入的图像大小，或者说图像的特征数，即层中每个函数的x数，即层中每个函数的参数量（只考虑w）
# 200表示层中有200个输出，即有200个函数y
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 200)
        self.fc2 = nn.Linear(200, 200)
        self.fc3 = nn.Linear(200, 200)
        self.fc4 = nn.Linear(200, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)  # 展平图像为一维向量
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = self.fc4(x)
        return x

# 实例化模型
model = Net()

# 将模型移动到指定设备上
model = model.to(device)

#  定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=1)

for epoch in range(200):
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)

        # 转换标签为one-hot编码
        labels = one_hot(labels, num_classes=10).float()

        # 向前传播
        outputs = model(images)
        loss = criterion(outputs, labels)

        # 向后传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, 100, loss.item()))

# 保存模型
torch.save(model.state_dict(), 'test.pth')

