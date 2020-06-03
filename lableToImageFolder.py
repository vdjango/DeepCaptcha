import os
import shutil
import sys

url = '验证码识别'  # 102花朵数据集
save_url = 'data/VerificationCode/'  # 处理后的数据集存放路径

image_dataset_path = {
    'train_data': os.path.join(save_url, 'train'),
    'val_data': os.path.join(save_url, 'val'),
    'test_data': os.path.join(save_url, 'test'),
    'train': os.path.join(url, 'train'),
    'test': os.path.join(url, 'test')
}

image_train_path = {}
image_val_path = {}

if not os.path.exists(url):
    print('路径不存在')

if not os.path.exists(image_dataset_path['train_data']):
    os.makedirs(image_dataset_path['train_data'])
    pass

if not os.path.exists(image_dataset_path['val_data']):
    os.makedirs(image_dataset_path['val_data'])

with open(os.path.join(url, 'train.txt')) as file:
    for line in file.readlines():
        s = line.split(',')
        _class_id = s[0].split('.')[0]
        _name = s[0]
        print('mkdir', _class_id)

        source = os.path.join(image_dataset_path['train'], _name)

        train_target_out = os.path.join(image_dataset_path['train_data'], _class_id)
        val_target_out = os.path.join(image_dataset_path['val_data'], _class_id)

        if not os.path.exists(train_target_out):
            os.makedirs(train_target_out)

        if not os.path.exists(val_target_out):
            os.makedirs(val_target_out)

        if not image_train_path.get(_class_id, None):
            image_train_path[_class_id] = []

        image_train_path[_class_id].append({
            'source': source,
            'train_target': os.path.join(train_target_out, _name),
            'val_target': os.path.join(val_target_out, _name),
        })

    pass

for i in image_train_path:
    _n = int(len(image_train_path[i]) * .2)
    print(len(image_train_path[i]))
    if not image_val_path.get(i, None):
        image_val_path[i] = []

    for val in image_train_path[i][:_n + 1]:
        image_val_path[i].append(val)

    image_train_path[i] = image_train_path[i][_n:]

for i in image_train_path:
    for _target in image_train_path[i]:
        source = _target['source']
        target = _target['train_target']

        print('source', source)
        print('target', target)

        if not os.path.exists(target):
            shutil.copy(source, target)

for i in image_val_path:
    for _target in image_val_path[i]:
        source = _target['source']
        target = _target['val_target']

        if not os.path.exists(target):
            try:
                shutil.copy(source, target)
                # print(source, target)
            except IOError as e:
                print("Unable to copy file. %s" % e)
            except:
                print("Unexpected error:", sys.exc_info())

if os.path.exists(image_dataset_path['test']):
    if not os.path.exists(image_dataset_path['test_data']):
        os.makedirs(image_dataset_path['test_data'])

        for root, dirs, files in os.walk(image_dataset_path['test']):
            for file in files:
                _name = file.split('.')[1]
                _class_id = file.split('.')[0]

                source = os.path.join(root, file)
                test_target_out = os.path.join(image_dataset_path['test_data'], _class_id)

                if not os.path.exists(test_target_out):
                    os.makedirs(test_target_out)

                shutil.copy(source, test_target_out)
                print(test_target_out, file)
