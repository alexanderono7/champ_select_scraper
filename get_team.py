import requests
import urllib3
import re
import get_league_url

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url_base = get_league_url.main() #global var

def return_http(extension):
    #r = requests.get('https://riot:NUlYtQWeJcfYhWl7KVXoWw@127.0.0.1:55707/lol-chat/v1/conversations', verify=False)
    r = requests.get(url_base + extension, verify=False)
    y = str(r.content) #r.content = txt information pulled from http request
    return y

def print_http(extension):
    r = requests.get(url_base + extension, verify=False)
    print("\n")
    y = str(r.content) #r.content = txt information pulled from http request
    print(y)

def main():
    conv = "/lol-chat/v1/conversations"
    if(url_base == None):
        print("The lockfile at C:/Riot Games/League of Legends doesn't seem to exist... are you sure that league is open and you are logged in?") 
        quit()
    y = return_http(conv)
    #print(y)
    x = re.findall(r'"[^"]*?@champ-select\.na1\.pvp\.net', y) #Super helpful. The generic form is START[^START]*?END (where START and END are your start and end character regexs). It essentially means "match anything from START to END where the in-between characters do not include START again"
   # x = re.findall(r'"name"[^("name")]', y) #Super helpful. The generic form is START[^START]*?END (where START and END are your start and end character regexs). It essentially means "match anything from START to END where the in-between characters do not include START again"

    if(x == []):
        print("Are you certain you're in champion select?")
        quit()
    print(x[0])    
    champ_select_id = (x[0])
    champ_select_id = champ_select_id[1:]
    #champ_select_id = champ_select_id.replace("@", "%40")
    #print(champ_select_id)
    cs_thread = return_http("/lol-chat/v1/conversations/" + champ_select_id + "/participants")
    
    a = re.findall(r'"name"[^("name")](.*?)",', cs_thread) 
    for i in a:
        i = i[1:]
    print(a)

if __name__ == "__main__":
    main()
