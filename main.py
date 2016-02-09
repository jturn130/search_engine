import os


def walk_through_directory(file_path):
    for f in os.walk(file_path):
        print f
