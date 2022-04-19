def read_data(filename):
    i = 0
    file_open = open(filename, "r")
    file_read = file_open.read()
    file_read = file_read.replace("\n", " ")
    file_list = file_read.split(" ")
    while i in file_list:
        int(file_list[i])
    print(file_list)




def is_in_linear(search_val, values):
    i = 0
    while i in values:
        if search_val == values:
            return True
        else:
            return False


def main():
    value_list = [1, 3, 7, 9, 10]
    read_data("data_sorted.txt")
    is_in_linear(11, value_list)

if __name__ == '__main__':
    main()