# -*- coding: utf-8 -*-
import os
import pickle

directory = os.path.dirname(os.path.abspath(__file__))
# use /tmp/data.txt instead of {directory}/data.txt because of perrmission
FILE = '/tmp/data.txt'.format(directory=directory)


def write_file(todos, file_path=FILE):
    with open(file_path, 'w') as fp:
        pickle.dump(todos, fp, protocol=2)


def read_file(file_path=FILE):
    todos = []
    if not os.path.exists(file_path):
        return todos
    with open(file_path, 'r') as fp:
        todos = pickle.load(fp)
    return todos
