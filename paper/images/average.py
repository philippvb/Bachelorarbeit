import numpy as np
import os
import pandas as pd

def average():
    directory = 'paper/images/network_csv/strength/MobileNetV2/run-'
    networkname= 'mobileNetV2_strength_e2' # 'ResNet32_strength_e1'
    tag = 'Validation_accuracy'
    #tag = 'distance0'
    file_dir = directory+networkname
    filename_1=file_dir + '_1-tag-' + tag + '.csv'
    filename_2=file_dir + '_1-tag-' + tag + '.csv'
    filename_3=file_dir + '_1-tag-' + tag + '.csv'
    out_name= 'paper/images/network_csv/strength/MobileNetV2/MobileNetV2_strength_e2_validation_acuracy.csv'
    #out_name= 'paper/images/network_csv/strength/ResNet32/ResNet32_strength_e3_distance0.csv'
    
    file1 = pd.read_csv(filename_1, delimiter=',')
    file2 = pd.read_csv(filename_2, delimiter=',')
    file3 = pd.read_csv(filename_3, delimiter=',')
    file_sum= file1 + file2 + file3
    file_sum = file_sum/3
    # file_sum['Value'] = file_sum['Value'].ewm(alpha=0.4, axis=0, adjust=False).mean() for smoothing
    file_sum.to_csv(out_name, index=False)
    

average()
    