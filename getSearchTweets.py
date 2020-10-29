#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import schedule
from datetime import datetime, date, timedelta
from requests_oauthlib import OAuth1Session

# CONSUMER_KEY = '************'
# CONSUMER_SECRET = '************'
# ACCESS_TOKEN = '************'
# ACCESS_TOKEN_SECRET = '************'
CONSUMER_KEY = 'ZYA53tMZKfNzBLs2TaO55FoPb'
CONSUMER_SECRET = 't4cWmCPrfWCsX1h8plNmDKECWo2cT1FzeElkTPRgctzzBzx4bK'
ACCESS_TOKEN = '2394621961-tvFfqY9WwddA2eInYZEcz4g2iOhikNbHg4VGluj'
ACCESS_TOKEN_SECRET = 'mLYxC4ilMWDih9uhePtGrVrRthzweeSBE3tPHtpgKDpsb'

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#昨日の日付を取得
today = datetime.today()
yesterday = today - timedelta(days=1)
yesterdays = datetime.strftime(yesterday, '%Y-%m-%d')

#ツイートを取得
url = 'https://api.twitter.com/1.1/search/tweets.json'
max_id = -1
keyword='#contributter_report {yesterdays} exclude:retweets' .format(yesterdays=yesterdays) # #contributter_reportと昨日の日付
params ={
         'count' : 100,      # 取得するtweet数
         'q'     :keyword,  # 検索キーワード
         'max_id' : max_id  #100件以上取得するために設定
         }

tweets = []    #ここに取得したツイートを格納  

#昨日の#contributter_reportのツイートを全て取得
while(True):
  if max_id != -1:
    params['max_id'] = max_id - 1

  req = twitter.get(url, params = params)

  if req.status_code == 200:
     res = json.loads(req.text)

     if res['statuses'] == []:
          break 

     for tweet in res['statuses']:
      tweets.append(tweet)

     max_id = res['statuses'][-1]['id']



#tweetsのユーザー名とcontribution数が対応したリストを作る
#ユーザ名のリスト
list1=[]
s=0
for getname in tweets:
 list1.append(tweets[s]['user']['screen_name'])
 s=s+1

#contibution数のリスト
list3=[]
c=0
target = ":"
index = -1
for getfigure in tweets:
 x=tweets[c]['text']
 y=x[x.find(":"):]
 list3.append(y)
 c=c+1 

#コロンを削除
list4=[]
d=0
for getnumber in tweets:
  list4.append(list3[d][1:])
  d=d+1

#後ろからスライスして数字のみにする
list5=[]
e=0
for get_c_number in tweets:
  list5.append(list4[e][:-22])
  e=e+1

#list1とlist2を辞書にする
rank_data=dict(zip(list1,list5))

#***さんを除外
removed_rank_data = rank_data.pop('***')

#contiributionが多い順に並び替える
rank_data2=sorted(rank_data.items(),key=lambda x:int(x[1]), reverse=True)

#上位３人を取得
top_contributor=rank_data2[0:3]

#上位３人のユーザIDとcontribution数を格納
no1=top_contributor[0]
no1_name=no1[0]
no1_number=no1[1]
no2=top_contributor[1]
no2_name=no2[0]
no2_number=no2[1]
no3=top_contributor[2]
no3_name=no3[0]
no3_number=no3[1]

#ツイートする処理
twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
url = 'https://api.twitter.com/1.1/statuses/update.json'
tweet_post = "👑 @{no1_name}さん  contribution数{no1_number}\n 2 @{no2_name}さん  contribution数{no2_number}\n 3 @{no3_name}さん  contribution数{no3_number}" .format(no1_name=no1_name,no1_number=no1_number,no2_name=no2_name,no2_number=no2_number,no3_name=no3_name,no3_number=no3_number) 
params = {'status': tweet_post}
twitter.post(url, params=params)


