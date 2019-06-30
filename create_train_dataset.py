import os
import glob
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
    DATA_PATH = "/data/cv_data/ShanghaiTech/part_A/train_data/"
    image_path_list = glob.glob(os.path.join(DATA_PATH, "images", "*.jpg"))
    print(image_path_list)
