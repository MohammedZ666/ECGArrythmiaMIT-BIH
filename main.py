import wfdb
import matplotlib.pyplot as plt
import numpy as np
import os
from wfdb import processing

# count = 0;
# for i in range(100, 235):
#     directory = '/mitdbdir/'+str(i)+'.atr'
#     if os.path.isfile(directory):
#         annotation = wfdb.rdann('/mitdbdir/'+str(i), 'atr')
#         count += annotation.ann_len
# print(count)

record = wfdb.rdrecord('/mitdbdir/100')
annotation = wfdb.rdann('/mitdbdir/100', 'atr')
print(len(annotation.subtype), len(annotation.sample))
# fig, ax = plt.subplots()
# ax.plot(np.linspace(0, record.p_signal.shape[0], record.p_signal.shape[0]),record.p_signal[:, 0])
# plt.show()
count = 0
wfdb.plot_wfdb(record=record, annotation=annotation, plot_sym=True,
               time_units='seconds', title='MIT-BIH Record 100', figsize=(10, 4),
               ecg_grids='all')
