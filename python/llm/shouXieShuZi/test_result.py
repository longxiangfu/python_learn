import torch
import torch.nn as nn
import torch.optim as optim
from PIL import Image
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch.nn.functional import one_hot

# 获取设备
device = torch.device('cuda:0')

# 定义转换操作，将数据转化为PyTorch张量并归一化
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 定义模型
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

# 加载训练好的模型权重
model.load_state_dict(torch.load('test.pth'))

def load_image(image_path):
    image = Image.open(image_path).convert('L')  # 转换为灰度图像
    image = transform(image)
    image = image.unsqueeze_(0) # 添加批次维度
    return image

image_path = "image6.jpg"
image = load_image(image_path)
image = image.to(device)

model.eval() #设置模型为评估模式
with torch.no_grad():
    outputs = model(image)
    predicted = torch.argmax(outputs, dim=1)
    print('Predicted digit:', predicted.item())

