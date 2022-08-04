import re

def logs():
    file = #Put file location and name here
    with open(file, "r") as file:
        logdata = file.read()

        entries = logdata.split("\n")

        log_list = []

        for each in entries:
            host = re.findall("(^\d+\.\d+\.\d+\.\d+)", each)[0]
            print(host)
            username = re.findall("(?<=\-\s)(.*?|-)(?=\s\[)", each)[0]
            time = re.findall("(?<=\[)(.*?)(?=\])", each)[0]
            request = re.findall("(?<=\")(.*?)(?=\")", each)[0]

            entry_dictionary = {"host":host, "user_name":username, "time":time, "request":request}
            log_list.append(entry_dictionary)

        return log_list

#Get IP address and total amount of them
logs = logs()
print(len(logs))
