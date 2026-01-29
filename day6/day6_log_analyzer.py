# Read a file and print its contents
file = open("day6/system.log", "r")
content = file.read()
# read() reads the entire file content used for small files
print(content)
file.close()


# Read file line by line
file = open("day6/system.log", "r")
for line in file:
  print(line.strip())
file.close()


# Count Errors in log file
file = open("day6/system.log", "r")
error_count = 0
for line in file:
  if "ERROR" in line:
    error_count += 1
file.close()
print("Total ERROR entries:", error_count)


# Write to a log file
file = open("day6/summary.txt", "w")
file.write("Log analysis summary\n")
file.write("Total Error entries:" + str(error_count))
file.close()


# with statement for file handling
with open("day6/system.log", "r") as file:
  for line in file:
    if "WARNING" in line:
      print(line.strip())


# Log analyzer that counts different log levels
with open("day6/system.log", "r") as file:
  count_error = 0
  count_warning = 0
  count_info = 0
  for line in file:
    if "ERROR" in line:
      count_error += 1
    elif "WARNING" in line:
      count_warning += 1
    elif "INFO" in line:
      count_info += 1
with open("day6/log_summary.txt", "w") as summary_file:
  summary_file.write("Log summary:\n")
  summary_file.write("ERROR entries:" + str(count_error) + "\n")
  summary_file.write("WARNING entries:" + str(count_warning) + "\n")
  summary_file.write("INFO entries:" + str(count_info) + "\n")
  print("summary written to log_summary.txt")

