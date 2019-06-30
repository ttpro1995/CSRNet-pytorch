import os
import glob
from sklearn.model_selection import train_test_split
import json
"""
create a list of file (full directory)
"""

DATA_PATH = "/data/cv_data/shanghaitech-with-people-density-map/ShanghaiTech/part_A/train_data"
def create_training_image_list(data_path):
    """
    create a list of absolutely path of jpg file
    :param data_path: must contain subfolder "images" with *.jpg  (example ShanghaiTech/part_A/train_data/)
    :return:
    """
    DATA_PATH = data_path
    image_path_list = glob.glob(os.path.join(DATA_PATH, "images", "*.jpg"))
    return image_path_list


if __name__ == "__main__":
    image_path_list = glob.glob(os.path.join(DATA_PATH, "images", "*.jpg"))
    train, val = train_test_split(image_path_list, test_size=0.1)

    print("train size ", len(train))
    print("val size ", len(val))
    json.dump(train, open("json/meow_train.json", 'w'))
    json.dump(val, open("json/meow_val.json", 'w'))