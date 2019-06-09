import requests
import json
import time

daytime = time.asctime(time.localtime(time.time()))
print(daytime)
print()
Key = "Your key"
URL_user = "https://osu.ppy.sh/api/get_user"
URL_map = "https://osu.ppy.sh/api/get_scores"
URL_beat_peformance = "https://osu.ppy.sh/api/get_user_best"
URL_recently = "https://osu.ppy.sh/api/get_user_recent"
nickname = input("输入查询用户: ")

#查询用户信息
class Moeyu_check_user():
    def print_user_grade_in_osu(self):
        params = {"k":Key,"u":nickname,"type":"string","m":"0","event_days":31}
        req = requests.post(URL_user,data= params)
        js = req.text
        js = json.loads(js)
        print("username:  " + js[0]['username'],'\n'
        "global_world_rank:  " + js[0]['pp_rank'],'\n'
        "country_rank:  "+ js[0]['pp_country_rank'],'\n'
        "pp   "  + js[0]['pp_raw'],'\n'
        "acc:  " + ("%.2f" % float(js[0]['accuracy'])),'\n'
        "total_seconds_played： " + js[0]["total_seconds_played"],'\n'
        "Level:  " + js[0]['level'],'\n'
        "count_rank_ss： " + js[0]["count_rank_ss"],'\n'
        "count_rank_s： " + js[0]["count_rank_s"],'\n'
        "count_rank_a： " + js[0]["count_rank_a"])

    def print_user_grade_in_taiko(self):
        params = {"k":Key,"u":nickname,"type":"string","m":"1","event_days":31}
        req = requests.post(URL_user,data= params)
        js = req.text
        js = json.loads(js)
        print("username:  " + js[0]['username'],'\n'
        "global_world_rank:  " + js[0]['pp_rank'],'\n'
        "country_rank:  "+ js[0]['pp_country_rank'],'\n'
        "pp   "  + js[0]['pp_raw'],'\n'
        "acc:  " + ("%.2f" % float(js[0]['accuracy'])),'\n'
        "total_seconds_played： " + js[0]["total_seconds_played"],'\n'
        "Level:  " + js[0]['level'],'\n'
        "count_rank_ss： " + js[0]["count_rank_ss"],'\n'
        "count_rank_s： " + js[0]["count_rank_s"],'\n'
        "count_rank_a： " + js[0]["count_rank_a"])

    def print_user_grade_in_ctb(self):
        params = {"k":Key,"u":nickname,"type":"string","m":"2","event_days":31}
        req = requests.post(URL_user,data= params)
        js = req.text
        js = json.loads(js)
        print("username:  " + js[0]['username'],'\n'
        "global_world_rank:  " + js[0]['pp_rank'],'\n'
        "country_rank:  "+ js[0]['pp_country_rank'],'\n'
        "pp   "  + js[0]['pp_raw'],'\n'
        "acc:  " + ("%.2f" % float(js[0]['accuracy'])),'\n'
        "total_seconds_played： " + js[0]["total_seconds_played"],'\n'
        "Level:  " + js[0]['level'],'\n'
        "count_rank_ss： " + js[0]["count_rank_ss"],'\n'
        "count_rank_s： " + js[0]["count_rank_s"],'\n'
        "count_rank_a： " + js[0]["count_rank_a"])

    def print_user_grade_in_mania(self):
        params = {"k":Key,"u":nickname,"type":"string","m":"1","event_days":31}
        req = requests.post(URL_user,data= params)
        js = req.text
        js = json.loads(js)
        print("username:  " + js[0]['username'],'\n'
        "global_world_rank:  " + js[0]['pp_rank'],'\n'
        "country_rank:  "+ js[0]['pp_country_rank'],'\n'
        "pp   "  + js[0]['pp_raw'],'\n'
        "acc:  " + ("%.2f" % float(js[0]['accuracy'])),'\n'
        "total_seconds_played： " + js[0]["total_seconds_played"],'\n'
        "Level:  " + js[0]['level'],'\n'
        "count_rank_ss： " + js[0]["count_rank_ss"],'\n'
        "count_rank_s： " + js[0]["count_rank_s"],'\n'
        "count_rank_a： " + js[0]["count_rank_a"])
Moeyu_to_check = Moeyu_check_user()


#查询玩家最佳成绩的谱面信息
class Moeyu_check_performace():
    def check_user_beat_performance_osu(self):
        data = {"k":Key,"u":nickname,"type":"string","m":"0"}
        rep = requests.post(URL_beat_peformance , data = data)
        perfomance = json.loads(rep.text)
        for i in range(10):
            print("地图id：" + perfomance[i]["beatmap_id"],'\n'
            "得分：" + perfomance[i]["score"],'\n'
            "Max-Combo：" + perfomance[i]["maxcombo"],'\n'
            "成绩等级：" + perfomance[i]["rank"],'\n'
            "PP值：" + perfomance[i]["pp"],'\n'
            "成绩时间：" + perfomance[i]["date"], '\n')

    def check_user_beat_performance_taiko(self):
        data = {"k":Key,"u":nickname,"type":"string","m":"1"}
        rep = requests.post(URL_beat_peformance , data = data)
        perfomance = json.loads(rep.text)
        for i in range(10):
            print("地图id：" + perfomance[i]["beatmap_id"],'\n'
            "得分：" + perfomance[i]["score"],'\n'
            "Max-Combo：" + perfomance[i]["maxcombo"],'\n'
            "成绩等级：" + perfomance[i]["rank"],'\n'
            "PP值：" + perfomance[i]["pp"],'\n'
            "成绩时间：" + perfomance[i]["date"], '\n')

    def check_user_beat_performance_ctb(self):
        data = {"k":Key,"u":nickname,"type":"string","m":"2"}
        rep = requests.post(URL_beat_peformance , data = data)
        perfomance = json.loads(rep.text)
        for i in range(10):
            print("地图id：" + perfomance[i]["beatmap_id"],'\n'
            "得分：" + perfomance[i]["score"],'\n'
            "Max-Combo：" + perfomance[i]["maxcombo"],'\n'
            "成绩等级：" + perfomance[i]["rank"],'\n'
            "PP值：" + perfomance[i]["pp"],'\n'
            "成绩时间：" + perfomance[i]["date"], '\n')

    def check_user_beat_performance_mania(self):
        data = {"k":Key,"u":nickname,"type":"string","m":"3"}
        rep = requests.post(URL_beat_peformance , data = data)
        perfomance = json.loads(rep.text)
        for i in range(10):
            print("地图id：" + perfomance[i]["beatmap_id"],'\n'
            "得分：" + perfomance[i]["score"],'\n'
            "Max-Combo：" + perfomance[i]["maxcombo"],'\n'
            "成绩等级：" + perfomance[i]["rank"],'\n'
            "PP值：" + perfomance[i]["pp"],'\n'
            "成绩时间：" + perfomance[i]["date"], '\n')
user_performance = Moeyu_check_performace()


# 查询玩家最近一天游玩谱面记录前三图
class Moeyu_check_user_recently():
    def check_user_recently_osu(self):
        data = {"k":Key,"u":nickname, "type":"string", "m":"0","limit":70}
        rep = requests.post(URL_recently , data = data)
        recently = json.loads(rep.text)
        if recently != []:
            for i in range(0,10):
                print("https://osu.ppy.sh/beatmapsets/{}#fruits/{}".format("xxxxx/",recently[0]["beatmap_id"]),'\n'
                "地图id： " + recently[i]["beatmap_id"],'\n'
                "成绩： " + recently[i]["score"])
        else:
            print("最近此玩家在该模式下无游玩记录")
    def check_user_recently_taiko(self):
        data = {"k":Key,"u":nickname, "type":"string", "m":"1","limit":70}
        rep = requests.post(URL_recently , data = data)
        recently = json.loads(rep.text)
        if recently != []:
            for i in range(0,10):
                print("https://osu.ppy.sh/beatmapsets/{}#fruits/{}".format("xxxxx/",recently[0]["beatmap_id"]),'\n'
                "地图id： " + recently[i]["beatmap_id"],'\n'
                "成绩： " + recently[i]["score"])
        else:
            print("最近此玩家在该模式下无游玩记录")
    def check_user_recently_ctb(self):
        data = {"k":Key,"u":nickname, "type":"string", "m":"2","limit":70}
        rep = requests.post(URL_recently , data = data)
        recently = json.loads(rep.text)
        if recently != []:
            for i in range(0,10):
                print("https://osu.ppy.sh/beatmapsets/{}#fruits/{}".format("xxxxx/",recently[0]["beatmap_id"]),'\n'
                "地图id： " + recently[i]["beatmap_id"],'\n'
                "成绩： " + recently[i]["score"])
        else:
            print("最近此玩家在该模式下无游玩记录")
    def check_user_recently_mania(self):
        data = {"k":Key,"u":nickname, "type":"string", "m":"3","limit":70}
        rep = requests.post(URL_recently , data = data)
        recently = json.loads(rep.text)
        if recently != []:
            for i in range(0,10):
                print("https://osu.ppy.sh/beatmapsets/{}#fruits/{}".format("xxxxx/",recently[0]["beatmap_id"]),'\n'
                "地图id： " + recently[i]["beatmap_id"],'\n'
                "成绩： " + recently[i]["score"])
        else:
            print("最近此玩家在该模式下无游玩记录")
recently_grade = Moeyu_check_user_recently()



#此功能未完成(
# data = {"k":Key,"u":nickname, "type":"string", "m":"3","limit":70}
# rep = requests.post(URL_recently , data = data)
# beatmap = json.loads(rep.text)
# print(beatmap[0]["beatmap_id"])
# beatmap_id = beatmap[0]["beatmap_id"]
# print(beatmap_id)
# class Moeyu_check_beatmap_scores():
#     def check_user_beatmap_osu(self):
#         data = {"k":Key, "b":beatmap_id, "u":nickname, "type":"string", "m":"3","limit": 85}
#         rep = requests.post(URL_map , data = data)
#         print(rep.text)
# beatmaps = Moeyu_check_beatmap_scores()
# beatmaps.check_user_beatmap_osu()









if __name__ == '__main__':
    class find_user_information():
        def print_user_infomation(self):
            print("查询osu对应模式成绩: 1.osu! 2.taiko 3.catch the beats 4.mania")
            try:
                choose = int(input("choose: "))
            except ValueError:
                print("输入数据错误或数据格式错误")
            def choose_mode():
                if choose == 1:
                    Moeyu_to_check.print_user_grade_in_osu()
                elif choose == 2:
                    Moeyu_to_check.print_user_grade_in_taiko()
                elif choose == 3:
                    Moeyu_to_check.print_user_grade_in_ctb()
                else:
                    Moeyu_to_check.print_user_grade_in_mania()
            try:
                choose_mode()
            except TypeError:
                print("无此用户")
            except IndexError:
                print("用户名不达标,无法搜索到此用户")
            except ValueError as Value:
                print("数值错误")
                print(Value)
            except NameError:
                print("数据有误")

        def print_user_recently_play(self):
            print("查询对应模式最近游玩成绩成绩: 1.osu! 2.taiko 3.catch the beats 4.mania"),'\n'
            try:
                choose = int(input("choose: "))
            except ValueError:
                print("输入数据错误或数据格式错误")
            def choose_recently():
                if choose == 1:
                    recently_grade.check_user_recently_osu()
                elif choose == 2:
                    recently_grade.check_user_recently_taiko()
                elif choose == 3:
                    recently_grade.check_user_recently_ctb()
                else:
                    recently_grade.check_user_recently_mania()
            try:
                choose_recently()
            except TypeError as Error:
                print("无此用户")
            except IndexError:
                print("用户名不达标,无法搜索到此用户")
            except ValueError:
                print("数值错误")
            except NameError:
                print("数据有误")

        def print_user_best_performance(self):
            print("查询对应模式最佳成绩: 1.osu! 2.taiko 3.catch the beats 4.mania"),'\n'
            try:
                choose = int(input("choose: "))
            except ValueError:
                print("输入数据错误或数据格式错误")
            def performance():
                if choose == 1:
                    user_performance.check_user_beat_performance_osu()
                elif choose == 2:
                    user_performance.check_user_beat_performance_taiko()
                elif choose == 3:
                    user_performance.check_user_beat_performance_ctb()
                else:
                    user_performance.check_user_beat_performance_mania()
            try:
                performance()
            except TypeError :
                print("无此用户")
            except IndexError:
                print("用户名不达标,无法搜索到此用户，或数据无法显示")
            except ValueError:
                print("数值错误")
            except NameError:
                print("数据有误")
    print_information = find_user_information()

    def end_print():
        choose_option = int(input("选择查询模式:  1.user_infomation  2.user_recently_play  3.user_performance  4.map（未完成功能）， num: " ))
        if choose_option == 1:
            print_information.print_user_infomation()
        elif choose_option == 2:
            print_information.print_user_recently_play()
        elif choose_option == 3:
            print_information.print_user_best_performance()
        else:
            print("此功能未完成")
    end_print()