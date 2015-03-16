def merge_csv_files(files_to_merge,file_to_write,single_header=False):
    """This function merges a list of .csv files into a single file.
    Inputs:
        files_to_merge - list of strings, each a file name
        single_header - (False) if all files have same header, only one is used
    Outputs:
        file_to_write  - string, file name of output file
    """
    import csv
    rows = []

    # if all files have same header, read it from first file in list
    if (single_header):
        reader = csv.reader(open(f[0], "rb"))
        headRow = reader.next()
    
    # for each file name in the list
    for f in files_to_merge:
        reader = csv.reader(open(f, "rb")) # open the file
        if (single_header): # skip the header if single_header is set
            reader.next()
        # for each subsequent row
        for row in reader:
            rows.append(row) # append to rows collection

    # open output file
    with open(file_to_write, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        # if single_header, write header
        if (single_header):
            writer.writerow(headRow)
        # write each row
        writer.writerows(rows)