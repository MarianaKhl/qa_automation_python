from datetime import datetime, timedelta

def analyze_heartbeat_log(input_file, key, output_file):
    # list to store filtered records with the required key
    filtered_log = []

    # read the file and select the lines containing the given key
    with open(input_file, 'r') as file:
        for line in file:
            if key in line:
                filtered_log.append(line.strip())

    # let's convert the time in lines, calculate the difference and log the result
    with open(output_file, 'w') as log_file:
        for i in range(1, len(filtered_log)):
            # extract the time in HH:MM:SS format for two consecutive records
            timestamp1_str = filtered_log[i-1][filtered_log[i-1].find("Timestamp ") + 10:filtered_log[i-1].find("Timestamp ") + 18]
            timestamp2_str = filtered_log[i][filtered_log[i].find("Timestamp ") + 10:filtered_log[i].find("Timestamp ") + 18]

            # convert time to datetime format to calculate the difference
            timestamp1 = datetime.strptime(timestamp1_str, "%H:%M:%S")
            timestamp2 = datetime.strptime(timestamp2_str, "%H:%M:%S")

            # time difference calculation
            heartbeat_diff = abs((timestamp2 - timestamp1).total_seconds())

            # checking conditions and logging depending on the time difference
            if 31 < heartbeat_diff < 33:
                log_file.write(f"WARNING: Heartbeat delay of {heartbeat_diff} seconds at {timestamp2_str}\n")
            elif heartbeat_diff >= 33:
                log_file.write(f"ERROR: Heartbeat delay of {heartbeat_diff} seconds at {timestamp2_str}\n")

# call the function with the specified parameters
input_file = '/Users/marianna/PycharmProjects/demo/Lesson_2-GitHub-/lesson_21/hblog (1).txt'
key = 'Key TSTFEED0300|7E3E|0400'
output_file = 'hb_test.log'
analyze_heartbeat_log(input_file, key, output_file)
