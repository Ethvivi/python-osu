import requests
import json
import time

Key = "your key"
URL = "https://osu.ppy.sh/api/get_user"
nickname = input("输入查询用户: ")

class Moeyu_check():

    def print_user_grade_in_osu(self):
        params = {"k":Key,"u":nickname,"type":"string","m":"0"}
        req = requests.post(URL,data= params)
        js = req.text
        js = json.loads(js)
        print("username:  " + js[0]['username'])
        print("global_world_rank:  " + js[0]['pp_rank'])
        print("country_rank:  "+ js[0]['pp_country_rank'])
        print("pp   "  + js[0]['pp_raw'])
        print("acc:  " +  js[0]['accuracy'])
        print("country:  " + js[0]['country'])
        print("Level:  " + js[0]['level'])

    def print_user_grade_in_taiko(self):
        params = {"k":Key,"u":nickname,"type":"string","m":"1"}
        req = requests.post(URL,data= params)
        js = req.text
        js = json.loads(js)
        print("username:  " + js[0]['username'])
        print("global_world_rank:  " + js[0]['pp_rank'])
        print("country_rank:  "+ js[0]['pp_country_rank'])
        print("pp   "  + js[0]['pp_raw'])
        print("acc:  " +  js[0]['accuracy'])
        print("country:  " + js[0]['country'])
        print("Level:  " + js[0]['level'])

    def print_user_grade_in_ctb(self):
        params = {"k":Key,"u":nickname,"type":"string","m":"2"}
        req = requests.post(URL,data= params)
        js = req.text
        js = json.loads(js)
        print("username:  " + js[0]['username'])
        print("global_world_rank:  " + js[0]['pp_rank'])
        print("country_rank:  "+ js[0]['pp_country_rank'])
        print("pp   "  + js[0]['pp_raw'])
        print("acc:  " +  js[0]['accuracy'])
        print("country:  " + js[0]['country'])
        print("Level:  " + js[0]['level'])

    def print_user_grade_in_mania(self):
        params = {"k":Key,"u":nickname,"type":"string","m":"1"}
        req = requests.post(URL,data= params)
        js = req.text
        js = json.loads(js)
        print("username:  " + js[0]['username'])
        print("global_world_rank:  " + js[0]['pp_rank'])
        print("country_rank:  "+ js[0]['pp_country_rank'])
        print("pp   "  + js[0]['pp_raw'])
        print("acc:  " +  js[0]['accuracy'])
        print("country:  " + js[0]['country'])
        print("Level:  " + js[0]['level'])
Moeyu_to_check = Moeyu_check()

if __name__ == '__main__':
    print("查询osu对应模式成绩: 1.osu! 2.taiko 3.catch the beats 4.mania")
    choose = int(input("choose: "))
    def choose_mode():
        if choose == 1:
            Moeyu_to_check.print_user_grade_in_osu()
        elif choose == 2:
            Moeyu_to_check.print_user_grade_in_taiko()
        elif choose == 3:
            Moeyu_to_check.print_user_grade_in_ctb()
        else:
            Moeyu_to_check.print_user_grade_in_mania()
    choose_mode()
