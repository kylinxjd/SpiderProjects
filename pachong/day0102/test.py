import csv


def readfile(filename):
    """
    以列表形式读
    :param filename:
    :return:
    """
    with open(filename, 'r') as fcsv:
        reader = csv.reader(fcsv)
        print(reader)
        # reader是一个可迭代对象
        for item in reader:
            print(item)


def readfile_dic(filename):
    """
    以字典形式读
    :param filename:
    :return:
    """
    with open(filename, 'r') as fcsv:
        reader = csv.DictReader(fcsv)
        for item in reader:
            print(item)


def writefile(filename):
    """
    以列表形式写
    :param filename:
    :return:
    """
    with open(filename, 'a+', newline='') as fcsv:
        writer = csv.writer(fcsv)
        # 一次写一行
        writer.writerow(['a', 'b', 'c'])
        # 一次写多行
        writer.writerows([('a', 'b', 'c'), ('d', 'e', 'f')])


def writefile_dic(filename):
    """
    以字典形式写
    :param filename:
    :return:
    """
    # 设置列字段（表头）
    fieldnames = ['head1', 'head2', 'head3']
    with open(filename, 'a+', newline='') as fcsv:
        writer = csv.DictWriter(fcsv, fieldnames=fieldnames)
        # 写第一行表头
        writer.writeheader()
        # 一次写一行
        writer.writerow({'head1': 1, 'head2': 2, 'head3': 3})
        # 一次写多行
        writer.writerows([{'head1': 2, 'head2': 2, 'head3': 2},
                          {'head1': 3, 'head2': 4, 'head3': 6}])


def chuli():

    with open('test.csv', 'r') as f:
        r = csv.reader(f)
        print(r)


if __name__ == '__main__':
    # print("以列表方式写文件")
    # writefile('test.csv')
    # print("写入成功")
    # print("以字典方式写文件")
    # writefile_dic('test.csv')
    # print("写入成功")
    # print("以列表方式读文件")
    # readfile('test.csv')
    # print("以字典方式读文件")
    # readfile_dic('test.csv')
    chuli()
