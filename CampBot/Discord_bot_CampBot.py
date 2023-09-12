#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint


from CampAge import runLoki as Age_runloki
from five_nine_grade import runLoki as fivenine_runloki
from two_four_grade import runLoki as twofour_runloki



logging.basicConfig(level=logging.DEBUG)




punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR, context=""):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    
    if context == "grade":
        resultDICT = Age_runloki(inputLIST, filterLIST)
        
    elif context == "senior":
        resultDICT = fivenine_runloki(inputLIST, filterLIST)
        
    elif context == "junior":
        resultDICT = twofour_runloki(inputLIST, filterLIST)
    
    
        
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

class BotClient(discord.Client):  ##和discord連線

    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄 ## multi session composition 多輪對話
        '''
        templateDICT = {    "id": messageAuthorID,
                             "updatetime" : datetime.now(),
                             "latestQuest": "",
                             "age_grade": None,
                             "Q_cnt": 0
                             
        }
        return templateDICT

    async def on_ready(self):
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        
        self.templateDICT = {
        }
        self.mscDICT = { #userid:templateDICT
        }
        # ####################################################################################
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
            logging.debug("本 bot 被叫到了！")
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "ping":
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR = "pong pong"

# ##########初次對話：這裡是 keyword trigger 的。
            
            elif msgSTR.lower() in ["掰掰","掰","88","bye bye","bye","再見", "沒有", "拜拜"]:
                replySTR = "掰掰，謝謝您的使用，期待下次為您服務!"
                self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)

            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我是台北區的玩轉營隊客服機器人，請重新輸入小朋友目前幾年級，我們將會為您做客製化回覆!"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        if self.mscDICT[message.author.id]["age_grade"] == None:
                            replySTR = "嗨嗨，歡迎回來，您上次還沒輸入小朋友的年級，請幫我輸入喔~"  #判斷是否已輸入年紀
                        elif self.mscDICT[message.author.id]["Q_cnt"] == 0:  
                            replySTR = "嗨嗨，歡迎回來，您上次還沒問問題喔~"  #判斷有無問過問題
                        else:
                            replySTR = "嗨嗨，歡迎回來，您上次問到「{}」".format(self.mscDICT[message.author.id]["latestQuest"])  #提醒使用者上次問的問題
                            

            #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = msgSTR.title() + "\n" + "我是台北區的玩轉營隊客服機器人，請先輸入小朋友目前幾年級，我們將會為您做客製化回覆!" #works (tested)
                        
                    
                    

# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                           
                    
                
                if (self.mscDICT[message.author.id]["age_grade"] == None):
                    try:
                        resultDICT = getLokiResult(msgSTR, "grade")
                        logging.debug("######\nLoki 處理結果如下：")
                        logging.debug(resultDICT)
                        replySTR = resultDICT["response"][0]
                        self.mscDICT[message.author.id]["age_grade"] = resultDICT["age_grade"][0]
                        print(self.mscDICT[message.author.id]["age_grade"])
                        
                    except KeyError:
                        replySTR = "我們沒有適合的營隊喔!"
                        self.mscDICT[message.author.id]["age_grade"] = None
                
            
                elif self.mscDICT[message.author.id]["age_grade"] == "senior":
                    try:
                        self.mscDICT[message.author.id]["latestQuest"] = msgSTR
                        
                        self.mscDICT[message.author.id]["Q_cnt"] += 1
                        print(msgSTR)
                        resultDICT = getLokiResult(msgSTR, "senior")
                        
                        if "age_grade" in resultDICT:
                            self.mscDICT[message.author.id]["age_grade"] = resultDICT["age_grade"][0]
                            replySTR = resultDICT["response"][0]
                        else:
                            print(resultDICT)
                            logging.debug("######\nLoki 處理結果如下：")
                            logging.debug(resultDICT)
                            if resultDICT["response"][0] == '':
                                replySTR = "抱歉，我沒有辦法回答你的問題。若您有需要的話歡迎在LINE 官方 @pleyschool聯絡真人客服~"
                            else:
                                replySTR = resultDICT["response"][0]  + "\n\n請問還有想問什麼問題嗎~"
                        resultDICT["response"] = ''
                            
                        resultDICT = {}
                        print (resultDICT)
                         
                        
                    except Exception:
                        replySTR = "抱歉，我沒有辦法回答你的問題。若您有需要的話歡迎在LINE 官方 @pleyschool聯絡真人客服~~"
                    
                elif self.mscDICT[message.author.id]["age_grade"] == "junior":
                    try:
                        self.mscDICT[message.author.id]["latestQuest"] = msgSTR
                        
                        self.mscDICT[message.author.id]["Q_cnt"] += 1                                                                            
                        print(msgSTR)
                        resultDICT = getLokiResult(msgSTR, "junior")
                        
                        if "age_grade" in resultDICT:
                            self.mscDICT[message.author.id]["age_grade"] = resultDICT["age_grade"][0]
                            replySTR = resultDICT["response"][0]
                        else:
                            print(resultDICT)
                            logging.debug("######\nLoki 處理結果如下：")
                            logging.debug(resultDICT)
                            if resultDICT["response"][0] == '':
                                replySTR = "抱歉，我沒有辦法回答你的問題。若您有需要的話歡迎在LINE 官方 @pleyschool聯絡真人客服~"
                            else:
                                replySTR = resultDICT["response"][0]  + "\n\n請問還有想問什麼問題嗎~"
                        resultDICT["response"] = ''
                        self.mscDICT[message.author.id]["latestQuest"] = msgSTR
                            
                        resultDICT = {}
                        
                        print (resultDICT)
                        #print(self.mscDICT[message.author.id]["latestQuest"])
                        
                        
                    except Exception:
                        replySTR = "抱歉，我沒有辦法回答你的問題。若您有需要的話歡迎在LINE 官方 @pleyschool聯絡真人客服~"
                        
                        
            
            await message.reply(replySTR)


if __name__ == "__main__":
    with open("account.info", encoding="utf-8") as f: #讀取account.info
        accountDICT = json.loads(f.read())
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])
