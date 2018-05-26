#!/usr/bin/env python

import struct

def read_long(file):
    acc = 0
    unpack = struct.unpack
    s = file.read(4)
    length = len(s)
    if length % 4:
        extra = (4 - length % 4)
        s = b('\000') * extra + s
        length = length + extra
    for i in range(0, length, 4):
        acc = (acc << 32) + unpack('>I', s[i:i+4])[0]
    return acc


def read_float(file):
    bytes = file.read(4)
    value = struct.unpack('f', bytes)[0]
    return value


def read_string(file):
    byte = file.read(1)
    nChars = int.from_bytes(byte, "little")
    chars = []

    for i in range(nChars):
        byte = file.read(1)
        chars.append(chr(int.from_bytes(byte, "little")))
    if nChars == 0:
        return False

    string = "".join(chars)
    print("string size %s" % nChars)
    print("%s\n" % string)

    return string


def read_bool(file):
    byte = file.read(1)
    return struct.unpack('?', byte)[0]


def load_dummies(file):
    section = read_string(file)
    nDummies = read_long(file)

    dummies = []
    for i in range(nDummies):
        dummy = load_dummy(file)
        dummies.append(dummy)

    return dummies


def load_vertext_data(file):

    positions = load_positions(file)
    normals = load_normals(file)
    uv_coords = load_uv_coords(file)
    binormals = load_binormals(file)
    tangents = load_tangents(file)
    tex_coords = load_text_coord(file)

    return VertexData(positions, normals, uv_coords, binormals, tangents, tex_coords)


def load_model_parts(file):

    section = read_string(file)
    nParts = read_long(file)

    parts = []
    for i in range(nParts):
        part = load_part(file)
        parts.append(part)

    return parts


def load_model_params(file):

    params = {}

    # RescaleToLengthInMeters param
    key = read_string(file)
    value = read_bool(file)
    params[key] = value

    # LengthInMeters param
    key = read_string(file)
    value = read_float(file)
    params[key] = value

    # RescaleFactor param
    key = read_string(file)
    value = read_float(file)
    params[key] = value

    # Centered param
    key = read_string(file)
    value = read_bool(file)
    params[key] = value

    # UseChannelTextures param
    key = read_string(file)
    value = read_bool(file)
    params[key] = value

    # SpecularShininess param
    key = read_string(file)
    value = read_float(file)
    params[key] = value

    # SpecularPower param
    key = read_string(file)
    value = read_float(file)
    params[key] = value

    # BoundingBox param
    key = read_string(file)

    x = read_float(file)
    y = read_float(file)
    z = read_float(file)
    min = (x, y, z)

    x = read_float(file)
    y = read_float(file)
    z = read_float(file)
    max = (x, y, z)

    value = BoundingBox(min, max)
    params[key] = value

    # BounginSphere param
    key = read_string(file)

    x = read_float(file)
    y = read_float(file)
    z = read_float(file)
    pos = (x, y, z)
    radius = read_float(file)

    value = BoundingSphere(pos, radius)
    params[key] = value

    # SwapWindingOrder param
    key = read_string(file)
    value = read_bool(file)
    params[key] = value

    return params





def load_dummy(file):

    name = read_string(file)
    matrix = load_matrix(file)

    nParams = read_long(file)

    params = {}
    for i in range(nParams):
        key = read_string(file)
        value = read_string(file)
        params[key] = value

    return Dummy(name, matrix, params)


def load_matrix(file):

    mat = [[0 for x in range(4)] for x in range(4)]

    mat[0][0] = read_float(file)
    mat[0][1] = read_float(file)
    mat[0][2] = read_float(file)
    mat[0][3] = read_float(file)

    mat[1][0] = read_float(file)
    mat[1][1] = read_float(file)
    mat[1][2] = read_float(file)
    mat[1][3] = read_float(file)

    mat[2][0] = read_float(file)
    mat[2][1] = read_float(file)
    mat[2][2] = read_float(file)
    mat[2][3] = read_float(file)

    mat[3][0] = read_float(file)
    mat[3][1] = read_float(file)
    mat[3][2] = read_float(file)
    mat[3][3] = read_float(file)

    return mat


def load():
    file = open("test1.mwm", "rb")

    # reading the headder
    section = read_string(file)
    print("Section: %s" % section)
    flag = read_long(file)
    print("Flag: %s" % flag)
    version = read_string(file)
    print("Version: %s" % version)

    print("Loading dummies")
    dummies = load_dummies(file)

    print("Loading vertex data")
    vertex_data = load_vertext_data(file)

    print("Loading model parameters")
    model_params = load_model_params(file)

    print("Loading model parts")
    model_parts = load_model_parts(file)

    file.close()
    exit()


def main():
    load()


if __name__ == "__main__":
    main()

