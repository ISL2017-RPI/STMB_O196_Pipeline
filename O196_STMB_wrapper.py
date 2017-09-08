import sys
import numpy as np
import STMB_O196

def STMB(data_file, target_file):
    my_STMB = STMB_O196.initialize()
    feat = my_STMB.STMB_primitive_O196(data_file, target_file)
    return feat


if __name__ == "__main__":
    data = 'trainData.csv'
    target = 'trainTargets.csv'
    selected_feature = np.array(STMB(data, target), dtype=np.int16)
    np.savetxt('Features_O196_STMB.csv', selected_feature, delimiter=',')
    print selected_feature
