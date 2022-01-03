def move(path):
    subprocess.call("cd " + path, shell=True)

def get_string(filepath):
    path = filepath + "/lockfile"
    info = ""
    try:
        file = open(path, "r")
        for line in file:
            info = line
        file.close()
    except FileNotFoundError:
        pass
    return info

def parse_lockfile(info):
    num_list = info.split(":")
    port = num_list[2]
    passw = num_list[3]
    output = "https://riot:" + passw + "@127.0.0.1:" + port
    return output 

def main():
    path = "/mnt/c/Riot Games/League of Legends"
    info = get_string(path)
    if(info != ""):
        output = parse_lockfile(info)
        print(output)
        return output

if __name__ == "__main__":
    main()
