import argparse
import pandas as pd
import os

DESKTOP = os.path.join(os.environ["HOME"], "Desktop")

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sort", nargs="*")
parser.add_argument("-o", "--output_directory", nargs=1, default=[DESKTOP])
# parser.add_argument("--overwrite", nargs=1, default=["N"])

args = parser.parse_args()
input_file_paths = args.sort
output_directory = args.output_directory[0]
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
# overwrite = args.overwrite[0].upper()


def mysort(file_path):
    file_name = file_path.split(os.sep)[-1]
    df = pd.read_table(file_path, delim_whitespace=True, header=None)
    df_len = len(df.columns)
    for i in range(df_len):
        if df.iloc[0][i] == 'Time':
            df = df.rename(columns={i: 'Time'})
        elif df.iloc[0][i][4:] == '01-02' or df.iloc[0][i][4:] == 'O1-02' or df.iloc[0][i][4:] == '01-O2':
            df = df.rename(columns={i: 'O1-O2'})
        elif df.iloc[0][i][4:] == '01-02':
            df = df.rename(columns={i: 'O1-O2'})
        else:
            df = df.rename(columns={i: df.iloc[0][i][4:].upper()})

    cols0 = df.columns.tolist()
    cols0 = sorted(cols0)
    try:
        cols0.insert(0, cols0.pop(cols0.index("Time")))
    except:
        pass
    df = df[cols0]
    output_file_path = os.path.join(output_directory, file_name + '_copy.csv')
    df.to_csv(output_file_path, index=False)
    # if os.path.exists(output_file_path) and overwrite == "Y":
    #     df.to_csv(output_file_path, index=False)
    #     print("Overwriting file {}.".format(output_file_path))
    # elif os.path.exists(output_file_path) and overwrite == "N":
    #     print("\nError:\nOutput file {} exist.\nTo overwrite, include the following in your command:\n--overwrite Y.".format(output_file_path))
    # elif not os.path.exists(output_file_path):
    #     df.to_csv(output_file_path, index=False)


for file_path in input_file_paths:
    try:
        mysort(file_path)
    except:
        print("Cannot sort file {0}.".format(file_path.split(os.sep)[-1]))