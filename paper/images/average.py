import numpy as np
import os

def average():
    directory = 'paper/images/network_csv/baseline/baseline_scheduler_distance/run-'
    networkname='mobileNetV2_baseline_scheduler_distance'
    tag = 'Validation_accuracy'
    #tag = 'distance0'
    file_dir = directory+networkname
    filename_1=file_dir + '_1-tag-' + tag + '.csv'
    filename_2=file_dir + '_1-tag-' + tag + '.csv'
    filename_3=file_dir + '_1-tag-' + tag + '.csv'
    out_name= 'paper/images/network_csv/baseline/baseline_scheduler_distance/MobileNetV2_baseline_scheduler_distance_validation_acuracy.csv'
    #out_name= 'paper/images/network_csv/baseline/baseline_scheduler_distance/MobileNetV2_baseline_scheduler_distance_distance0.csv'
    
    file1 = np.genfromtxt(filename_1, delimiter=',', skip_header=1)
    file2 = np.genfromtxt(filename_2, delimiter=',', skip_header=1)
    file3 = np.genfromtxt(filename_3, delimiter=',', skip_header=1)
    file_sum = file1 + file2 + file3
    file_sum=file_sum/3
    # header=np.array(['Wall Time', 'Step', 'Value'])
    # out_file = np.vstack([header, file_sum])
    # print(out_file[1, 1])

    np.savetxt(out_name, file_sum, delimiter=",")
    # [TODO] add header Wall Time, Step, Value

average()
    