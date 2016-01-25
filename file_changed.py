import csv

def main():
    path = "/Users/ArseneLupin/Documents/edy/experiment_new_cascade/scaled/subject_32.csv"
    dest_path = "/Users/ArseneLupin/Documents/edy/experiment_new_cascade/new_scaled/subject_32.csv"

    temp_array=[]
    with open(path) as object_file:
        for line in object_file:
            raw_data = line.split()

            del raw_data[len(raw_data)-2]
            temp_array.append(raw_data)

    out_file = open(dest_path, "w")
    csv_writer = csv.writer(out_file, delimiter='\t')

    for i in temp_array:
        csv_writer.writerow(i)

    out_file.close

if __name__ == '__main__':
    main()
