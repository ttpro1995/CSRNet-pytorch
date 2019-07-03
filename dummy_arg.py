"""
contain dummy args with config
helpfull for copy paste Kaggle
"""
import argparse


def make_args(train_json= "", test_json="", pre="", gpu="0", task="task_one_"):
    """
    these arg does not have any required commandline arg (all with default value)
    :param train_json:
    :param test_json:
    :param pre:
    :param gpu:
    :param task:
    :return:
    """
    parser = argparse.ArgumentParser(description='PyTorch CSRNet')

    # parser.add_argument('train_json', metavar='TRAIN',
    #                     help='path to train json', default=train_json)
    # parser.add_argument('test_json', metavar='TEST',
    #                     help='path to test json', default=test_json)
    # parser.add_argument('--pre', '-p', metavar='PRETRAINED', default=pre,type=str,
    #                     help='path to the pretrained model')
    # parser.add_argument('gpu',metavar='GPU', type=str, default=gpu,
    #                     help='GPU id to use.')
    # parser.add_argument('task',metavar='TASK', type=str,
    #                 help='task id to use.', default=task)

    args = parser.parse_args()
    args.gpu = gpu
    args.task = task
    args.pre = None
    return args


class Meow():
    def __init__(self):
        pass


def make_meow_args(gpu="0", task="task_one_"):
    args = Meow()
    args.gpu = gpu
    args.task = task
    args.pre = None
    return args