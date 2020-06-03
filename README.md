# 基于resnet152模型的迁移学习-可用于验证码识别的基准模型

实际上，很少有人从头开始训练整个卷积网络（使用随机初始化），因为拥有足够大小的数据集相对很少。
相反，通常在非常大的数据集上对ConvNet进行预训练（例如ImageNet，其中包含120万个具有1000个类别的图像），
然后将ConvNet用作初始化或固定特征提取器以完成感兴趣的任务

----

<table style="width:100%">
  <tr>
    <td>
      <img src="data/2.jpeg">
    </td>
    <td align="center">
        <img src="data/1.jpeg">
    </td>
    <td>
      <img src="data/3.jpeg">
    </td>
  </tr>
</table>


# 描述

采取在ImageNet上进行预训练的ConvNet，删除最后一个完全连接的层，然后将ConvNet的其余部分视为新数据集的固定特征提取器

> 该层的输出是针对像ImageNet这样的不同任务的1000类分类

# 要求

PPython 3.7或更高版本，pip install -U -r requirements.txt包括以下所有软件包：
- `torch >= 1.2`
- `opencv-python`
- `Pillow`


# 讲解

* 基于 开源数据集 [82类 3w验证码轻量数据集 大小50M](https://github.com/vdjango/dataset) 共计29520张图
* 更多数据集请移步  [82类 40w验证码轻量数据集](https://github.com/vdjango/dataset)
* data/* 是数据集，测试集和训练集
* model/resnet/ 存放预训练模型及训练好的模型

# 训练

> 具体请参见train.py部分

**开始训练:** `python3.6 train.py`

## 模型

> 从以下位置下载： [正在训练 - 百度网盘 密码:]()

**GPU：** Nvidia RTX 2080 12G

**数据集：** 3w验证码轻量数据集 (82类)

**命令：** python3.6 train.py

GPU | data  | Loss | Acc | epoch |
--- |--- |--- |--- |--- |
| RTX 2080 12G | best_189_3551.pt | 3.0870 | 0.3551 | 189 |

# 推理

> 具体请参见 `test.py` 部分

```bash
python3.6 test.py
```

# 预训练模型

从以下位置下载： [正在训练 - 百度网盘 密码:]()

> pretrained 为True的时候，加载resnet152模型参数，进行迁移学习

```python
if __name__ == '__main__':
    train = TrainModel(pretrained=True)
    train(5000)
```
----



