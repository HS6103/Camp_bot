#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for tan4swo3sheng1tai4dao3

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

DEBUG_tan4swo3sheng1tai4dao3 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replytwofour/reply_tan4swo3sheng1tai4dao3.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_tan4swo3sheng1tai4dao3:
        print("[tan4swo3sheng1tai4dao3] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "探索生態島[都]在戶外活動嗎":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("探索生態島")
        else:
            # write your code here
            pass

    if utterance == "探索生態島在做什麼":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("探索生態島")
        else:
            # write your code here
            pass

    if utterance == "探索生態島在幹嘛":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("探索生態島")
        else:
            # write your code here
            pass

    if utterance == "探索生態島的[特色]是什麼":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("探索生態島")
        else:
            # write your code here
            pass

    if utterance == "探索生態島的[細節]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("探索生態島")
        else:
            # write your code here
            pass

    if utterance == "探索生態島的[詳細][內容]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("探索生態島")
        else:
            # write your code here
            pass

    if utterance == "有探索生態島的課表嗎":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("探索生態島")
        else:
            # write your code here
            pass

    return resultDICT