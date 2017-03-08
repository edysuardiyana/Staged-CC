import csv
from collections import namedtuple

FALL_ANNOT = 2
NON_FALL_ANNOT = 0

FALL_FORWARD = 2
FALL_BACKWARD = 6
FALL_LEFT = 10
FALL_RIGHT = 11
FALL_BLIND_FORWARD = 12
FALL_BLIND_BACKWARD = 13

FALL_SET = set([FALL_FORWARD,
                FALL_BACKWARD,
                FALL_LEFT,
                FALL_RIGHT,
                FALL_BLIND_FORWARD,
                FALL_BLIND_BACKWARD])

ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC'
                             ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOT')

def change_annot(source_path, dest_path):
    new_data = []
    print "Modifying annotations"
    with open(source_path) as obj_file:
        for line in obj_file:
            data_read = line.split()
            ori_data = [float(x) for x in data_read[:len(data_read)]]
            data = ARRAY_TUPLED(*ori_data)
            if data.ANNOT in FALL_SET:
                new_annot = FALL_ANNOT
            else:
                new_annot = NON_FALL_ANNOT

            new_data.append([data.AXC, data.AYC, data.AZC, data.GXC, data.GYC, data.GZC,
            data.AVMC, data.GVMC, data.AXT, data.AYT, data.AZT, data.GXT, data.GYT,
            data.GZT, data.AVMT, data.GVMT, new_annot])

    write_file(dest_path, new_data)

def write_file(path, data):
    out_file = open(path, "w")
    csvWriter = csv.writer(out_file, delimiter='\t')

    for elem in data:
        csvWriter.writerow(elem)
    out_file.close()
