#!/usr/bin/env python

import struct
import time
import io_scene_mwm.mwm_functions as mwm


def load():
    file = open("test1.mwm", "rb")

    version_number = mwm.load_mwm_header(file)

    print("Version: %s" % version_number)

    if version_number > 1066002:
        print("This is at least version 1066002")
        load_01066002(file, version_number)
    else:
        print("Model format is older than 1066002")
        file.seek(0)
        load_classic(file, version_number)


def load_01066002(file, version):
    index_dict = mwm.load_index(file)

    print(index_dict)


    print("Loading vertex data")
    vertex_data = mwm.load_mesh_data(index_dict, file)

    print("Loading model parameters")
    model_params = mwm.load_mesh_sections(index_dict, file)

    print("Loading model parts")
    model_parts = mwm.load_mesh_parts(index_dict, file, version)

    print(model_parts)

    file.close()
    exit()


def load_classic(file, version):
    print("Loading dummies")
    dummies = mwm.load_dummies(file)

    print("Loading vertex data")
    vertex_data = mwm.load_vertex_data(file)

    print("Loading model parameters")
    model_params = mwm.load_mesh_sections(file)

    print("Loading model parts")
    model_parts = mwm.load_mesh_parts(file)

    file.close()
    exit()


def main():
    load()


if __name__ == "__main__":
    main()
