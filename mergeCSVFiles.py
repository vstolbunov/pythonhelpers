def mergeCSVFiles(filesToMerge,fileToWrite,singleHeader=False):
    """This function merges a list of .csv files into a single file.
    Inputs:
        filesToMerge - list of strings, each a file name
        singleHeader - (False) if all files have same header, only one is used
    Outputs:
        fileToWrite  - string, file name of output file
    """
    
    import csv
    rows = []

    # if all files have same header, read it from first file in list
    if (singleHeader):
        reader = csv.reader(open(filesToMerge[0], "rb"))
        headRow = reader.next()
    
    # for each file name in the list
    for f in filesToMerge:
        reader = csv.reader(open(f, "rb")) # open the file
        if (singleHeader): # skip the header if singleHeader is set
            reader.next()
        # for each subsequent row
        for row in reader:
            rows.append(row) # append to rows collection

    # open output file
    with open(fileToWrite, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        # if singleHeader, write header
        if (singleHeader):
            writer.writerow(headRow)
        # write each row
        writer.writerows(rows)