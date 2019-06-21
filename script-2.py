import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--input_file", nargs="*")
parser.add_argument("-s", "--sorted", nargs=1)

args = parser.parse_args()
standard_file = args.sorted[0]
#input_files = args.input_file

# get the standard header
df0 = pd.read_table(standard_file, delim_whitespace=True, header=None)
df0_len = len(df0.columns)
for i in range(df0_len):
    if df0.iloc[0][i] == 'Time':
        df0 = df0.rename(columns={i: 'Time'})
    elif df0.iloc[0][i][4:] == '01-02' or df0.iloc[0][i][4:] == 'O1-02' or df0.iloc[0][i][4:] == '01-O2':
        df0 = df0.rename(columns={i: 'O1-O2'})
    elif df0.iloc[0][i][4:] == '01-02':
        df0 = df0.rename(columns={i: 'O1-O2'})
    else:
        df0 = df0.rename(columns={i: df0.iloc[0][i][4:].upper()})

cols0 = df0.columns.tolist()
cols0 = sorted(cols0)
df2 = df0[cols0]
df2.to_csv(standard_file+'_copy.csv', index=False)

#cols_num = len(cols0)

## sort other files
#def mysort(file):
#    output_file_name = file + '_sorted.csv'
#    df = pd.read_table(file, delim_whitespace=True, header=None)
#    for i in range(cols_num):
#        if df.iloc[0][i] == 'Time':
#            df = df.rename(columns={i: 'Time'})
#        elif df.iloc[0][i][4:] == '01-02':
#            df = df.rename(columns={i: 'O1-O2'})
#        else:
#            df = df.rename(columns={i: df.iloc[0][i][4:].upper()})
#    df = df[cols0]
#    df.to_csv(output_file_name)
#
#
#for file in input_files:
#    try:
#        mysort(file)
#    except:
#        print('Can not process file {}.'.format(file))

# # get the sorted header
# df = pd.read_table('data1.txt', delim_whitespace=True, header=None)
# for i in range(24):
#     if df.iloc[0][i] == 'Time':
#         df = df.rename(columns={i:'Time'})
#     elif df.iloc[0][i][4:] == '01-02':
#         df = df.rename(columns={i: 'O1-O2'})
#     else:
#         df = df.rename(columns={i:df.iloc[0][i][4:]})
#
# cols0 = df.columns.tolist()

# add headers to other files
