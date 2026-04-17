def write_log(message):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

def read_logs():
    with open("log.txt", "r") as f:
        for line in f:
            print(line.strip())

write_log("System started")
write_log("User logged in")

read_logs()