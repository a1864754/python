import datetime
import time

import itchat
import requests
from itchat.content import *


def get_sentence(api):
    santence = requests.get(api)

    return santence.json()


def get_weather_forcast():
    apikey = '550347cd71aa9b5f71345e2e00ed72e6'
    url = 'http://apis.juhe.cn/simpleWeather/query?city=%E5%8C%97%E4%BA%AC&key=' + apikey
    weather_forcast = requests.get(url).json()
    return weather_forcast


def get_response(question):
    apikey = '17216627bdd6495480ec7608fa1f4aeb'
    url = 'http://openapi.tuling123.com/openapi/api/v2' + apikey + '&info=' + question
    res = requests.get(url).json()
    return res['text']


@itchat.msg_register(TEXT, isFriendChat=True)
def auto_reply(msg):
    print("消息是：%s" % msg['Content'])
    itchat.send_msg(get_response(msg['Content']), toUserName=msg['FromUserName'])
    print('auto_reply:%s' % get_response(msg['Content']))


if __name__ == '__main__':
    jinshanapi = 'http://open.iciba.com/dsapi'
    itchat.auto_login(hotReload=True)

    santence = get_sentence(jinshanapi)
    content = santence['content']  # 抓取英文的句子
    translation = santence['note']  # 抓取的中文句子

    weather_forcast = get_weather_forcast()
    #    print(weather_forcast)
    today_weather = weather_forcast['result']["realtime"]
    print(today_weather)
    temperature = today_weather['temperature']
    weather = today_weather['info']
    wind = today_weather['wid']
    #    week = today_weather['week']
    city = "北京"
    #   date_y = today_weather['date_y']
    #    dressing_index = today_weather['dressing_index']
    #    dressing_advice = today_weather['dressing_advice']
    #    uv_index = today_weather['uv_index']
    # comfort_index = today_weather['comfort_index']
    # wash_index = today_weather['wash_index']
    # travel_index = today_weather['travel_index']
    # exercise_index = today_weather['exercise_index']
    # print('今日气温：%s\n天气：%s\n风力：%s\n星期：%s\n所在城市：%s\n当前日期：%s\n'
    #       '穿衣指数：%s\n穿衣建议：%s\n紫外线强度：%s\n' %
    #       (temperature,weather,wind,week,city,date_y,dressing_index,dressing_advice,uv_index))
    users = itchat.search_friends('坚持')  # 找到用户
    userName = users[0]['UserName']
    while 1:
        t = datetime.datetime.now()
        hour = t.hour
        minute = t.minute
        second = t.second
        # print('%d:%d:%d' % (hour,minute,second))
        if hour == 18 and minute == 5:
            itchat.send_msg('现在是北京时间：%s' % t)
            itchat.send_msg('%s:%s' % (content, translation), toUserName=userName)
            itchat.send_msg('今日气温：%s\n天气%s\n风力：%s\n所在城市：%s\n' % (temperature, weather, wind, city,))
            print(1)
            break
        else:
            time.sleep(5)
            continue
    itchat.run()
    time.sleep(86400)
