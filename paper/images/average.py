import numpy as np
import os

def average():
    directory = test
    filename='test'
    file_dir = os.path.join(directory, filename)
    filename_1=file_dir + '_1.csv'
    filename_2=file_dir + '_2.csv'
    filename_3=file_dir + '_3.csv'
    out_name='paper/images/' + filename + 'average.csv'
    
    file1 = np.genfromtxt(filename_1, delimiter=',', skip_header=1)
    file2 = np.genfromtxt(filename_2, delimiter=',', skip_header=1)
    file3 = np.genfromtxt(filename_3, delimiter=',', skip_header=1)
    file_sum = file1 + file2 + file3
    file_sum=file_sum/3
    header=np.array(['Wall Time', 'Step', 'Value'])
    out_file = np.vstack([header, file_sum])
    print(out_file[1, 1])

    # np.savetxt(out_name, file_sum, delimiter=",")

average()
    