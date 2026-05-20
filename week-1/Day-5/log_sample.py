import logging

#path ="sample_log.log"
with open("sample_log.log", 'r')as file:
    for line in file:
        if "INFO" in line:
            print("failure log found")
            print(line.strip())

            print("===========================")
