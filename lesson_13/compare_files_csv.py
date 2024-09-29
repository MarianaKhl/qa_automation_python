import pandas as pd

def test_compare_csv_files():
    # download two CSV files
    file1 = 'https://raw.githubusercontent.com/dntpanix/automation_qa/main/ideas_for_test/work_with_csv/random.csv'
    file2 = 'https://raw.githubusercontent.com/dntpanix/automation_qa/main/ideas_for_test/work_with_csv/random-michaels.csv'

    # reading files
    rf1 = pd.read_csv(file1)
    rf2 = pd.read_csv(file2)

    # pd.concat() allows you to merge two files into one dataframe
    unit_files_1_2 = pd.concat([rf1, rf2])  # [df1, df2] — це список, що містить два датафрейми df1 і df2

    # delete duplicate
    result_delete_duplicate = unit_files_1_2.drop_duplicates()

    # safe result in new csv file
    new_file = 'khlivnenko.csv'
    result_delete_duplicate.to_csv(new_file, index=False)

test_compare_csv_files()

