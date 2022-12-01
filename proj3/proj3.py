import streamlit as st
import os
import ntpath
import glob
import pandas as pd
import numpy as np
import datetime
from pathlib import Path
from datetime import datetime


_constant_fk2d = st.number_input(label="constant_fk2d", step=1., format="%.2f")
_multiplying_factor_3d = st.number_input(
    label="multiplying_factor_3d", step=1., format="%.2f")
_Shear_velocity = st.number_input(
    label="Shear_velocity", step=1., format="%.2f")

st.write('1. C')
st.write('2. S')
st.write('3. A')
st.write('4. C & S')
st.write('5. C & A')
st.write('6. S & A')
st.write('7. C & S & A')
st.write('8. all combine')
_tch = int(st.number_input('Choose Filtering Method From Above: '))
if _tch == 1:
    _corr = int(st.number_input('Enter thresold value C:'))
elif _tch == 2:
    _SNR = int(st.number_input('Enter thresold value S:'))
elif _tch == 3:
    _Lambda = float(st.number_input(
        label="Enter Lambda value for A:", step=1., format="%.2f"))
    _k = st.number_input(label="Enter k value for A:", step=1., format="%.2f")

elif _tch == 4:
    _corr = int(st.number_input('Enter thresold value C:'))
    _SNR = int(st.number_input('Enter thresold value S:'))
elif _tch == 5:
    _corr = int(st.number_input('Enter thresold value C:'))
    _Lambda = float(st.number_input(
        label="Enter Lambda value for A:", step=1., format="%.2f"))
    _k = float(st.number_input(label="Enter k value for A:", step=1., format="%.2f"))
elif _tch == 6:
    _SNR = int(st.number_input('Enter thresold value S:'))
    _Lambda = float(st.number_input(
        label="Enter Lambda value for A:", step=1., format="%.2f"))
    _k = float(st.number_input(label="Enter k value for A:", step=1., format="%.2f"))
elif _tch == 7 or _tch == 8:
    _corr = int(st.number_input('Enter thresold value C:'))
    _SNR = int(st.number_input('Enter thresold value S:'))
    _Lambda = float(st.number_input(
        label="Enter Lambda value for A:", step=1., format="%.2f"))
    _k = float(st.number_input(label="Enter k value for A:", step=1., format="%.2f"))
st.write('1. previous point')
st.write('2. 2*last-2nd_last')
st.write('3. overall_mean')
st.write('4. 12_point_strategy')
st.write('5. mean of previous 2 point')
st.write('6. all sequential')
st.write('7. all parallel')
_sch = st.number_input('Choose Replacement Method From Above: ')
if _sch > 7:
    st.write('Please make a correct choice')

if st.button('compute'):
    start_time = datetime.now()
    st.write("Files has been made")
    print(start_time.strftime("%c"))

    fileList = open('input_file_list.txt', 'r')
    files = fileList.readlines()
    for file in files:
        input_filename = file.strip()

        base = (Path(input_filename).stem.strip())
        output_csv = base+".csv"

        header_list = ['Time', 'SL', 'counter', 'U', 'V', 'W', 'W1', 'AMP-U', 'AMP-V', 'AMP-W',
                       'AMP-W1', 'SNR_U', 'SNR_V', 'SNR_W', 'SNR-W1', 'Corr_U', 'Corr_V', 'Corr_W', 'Corr-W1']
        dataframe = pd.read_csv(input_filename, delimiter=" +")
        dataframe.to_csv(output_csv, encoding='utf-8',
                         header=header_list, index=False)

    index = 0
    g = 9.81

    with open(r"Results_v2.csv", mode='a') as file_:
        file_.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(start_time.strftime("%c"), "average_velocity_U", "average_velocity_V", "average_velocity_W", "U_variance_Prime", "V_variance_Prime", "W_variance_Prime", "U_stdev_Prime", "V_stdev_Prime", "W_stdev_Prime", "Skewness_U_Prime", "Skewness_V_Prime", "Skewness_W_Prime", "Kurtosis_U_Prime", "Kurtosis_V_Prime", "Kurtosis_W_Prime", "Reynolds_stress_u\'v\'", "Reynolds_stress_u\'w\'", "Reynolds_stress_v\'w\'", "Anisotropy", "M30", "M03", "M12", "M21",
                    "fku_2d", "Fku_2d", "fkw_2d", "Fkw_2d", "fku_3d", "Fku_3d", "fkw_3d", "Fkw_3d", "TKE_3d", "Q1_K_Value", "Q2_K_Value", "Q3_K_Value", "Q4_K_Value", "e", "ED", "Octant_plus_1", "Octant_minus_1", "Octant_plus_2", "Octant_minus_2", "Octant_plus_3", "Octant_minus_3", "Octant_plus_4", "Octant_minus_4", "Total_Octant_sample", "Probability_Octant_plus_1", "Probability_Octant_minus_1", "Probability_Octant_plus_2", "Probability_Octant_minus_2", "Probability_Octant_plus_3", "Probability_Octant_minus_3", "Probability_Octant_plus_4", "Probability_Octant_minus_4", "Min_Octant_Count", "Min_Octant_Count_id", "Max_Octant_Count", "Max_Octant_Count_id", "\n"))

    def write_timestamp_to_file(name):
        # creating the csv writer
        # storing current date and time
        current_date_time = datetime.now()
        print("\nCurrent System Time: ", current_date_time)
        file1 = open("methods_timestamp.csv", "a")  # append mode
        file1.write(name + "," + str(current_date_time)+"\n")
        file1.close()



    end_time = datetime.now()

    print("-------------------------------------------------------------------")
    print("\nStart Time :", start_time.strftime("%c"))
    print("\nEnd Time :", end_time.strftime("%c"))
    print('\nDuration: {}'.format(end_time - start_time))
    duration = end_time - start_time
    name = "Complete Duration"
    duration_timestamp_to_file(name, duration)

    print("-------------------------------------------------------------------")
