#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ke4cheng2

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_ke4cheng2 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replytwofour/reply_ke4cheng2.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ke4cheng2:
        print("[ke4cheng2] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "中午休息時[通常][會]做什麼":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")
        else:
            # write your code here
            pass

    if utterance == "中午休息時[都][會]做什麼事":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")
        else:
            # write your code here
            pass

    if utterance == "中午休息時間[會]做什麼":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")
        else:
            # write your code here
            pass

    if utterance == "中午休息時間[會]進行哪些活動":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")
        else:
            # write your code here
            pass

    if utterance == "中午休息時間[都][會]做什麼事情":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")
        else:
            # write your code here
            pass

    if utterance == "了解[營隊]課表":
        if CHATBOT_MODE:
            if args[0] in ("營隊", "活動", "課程", "行程"):
                if args[0] in userDefinedDICT.keys():
                    args.append(userDefinedDICT[args[0]][0])
                    tmpReplySTR = getResponse(utterance, args).format(*args)
                    resultDICT["response"] = tmpReplySTR
                else:
                    pass
            else:
                pass
        else:
            # write your code here
            pass

    if utterance == "什麼是同樂會?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "午休時[會]做哪些事情呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "午休時間[通常][會]做什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "午休的[時候][會]做什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "午休的[時候][會]做什麼事情":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "同樂會在做什麼?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "同樂會在幹嘛?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "安排[一些]戶外[活動]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "安排戶外[活動]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有哪些戶外[活動]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有戶外[活動]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "知道[營隊]的課程內容和時間分配":
        if CHATBOT_MODE:
            if args[0] in ("營隊", "活動", "課程", "行程"):
                if args[0] in userDefinedDICT.keys():
                    args.append(userDefinedDICT[args[0]][0])
                    tmpReplySTR = getResponse(utterance, args).format(*args)
                    resultDICT["response"] = tmpReplySTR
                else:
                    pass
            else:
                pass
        else:
            # write your code here
            pass

    if utterance == "知道[營隊]課表":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "空課指的是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "要參加同樂會嗎?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "詢問有關[營隊]的課程時間和安排":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "詢問關於[營隊]課表":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT