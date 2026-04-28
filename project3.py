#import modules
import time
import pandas as pd
import numpy as np

#create loop for outputting data to csv files to be read as streaming data
#randomly sample five rows of data at a time to write to csv files
#put in a pause between loops

pwr_str_data = pd.read_csv("power_streaming_data.csv")

for i in range(0, 20):
    temp = pwr_str_data.loc[np.random.randint(pwr_str_data.shape[0], size = 5)]
    temp.to_csv("csv_files/pwr_str_data" + str(i) + ".csv", index = False, header = True)
    time.sleep(20)