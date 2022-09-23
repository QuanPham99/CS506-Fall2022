def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    csv_file = open(csv_file_path, mode="r")

    csv_lines = csv_file.readlines()

    res = []
    for line in csv_lines:
        line_arr = []
        for elem in line.split(","):
            try:
                elem = int(elem)
            except ValueError:
                pass
            line_arr.append(elem)
                
        res.append(line_arr)
    
    csv_file.close()
    return res

    # np.loadtxt(open(csv_file_path, "rb"), delimiter=",", skiprows=1)

def isint(elem):
    if elem.isnumeric():
        return True