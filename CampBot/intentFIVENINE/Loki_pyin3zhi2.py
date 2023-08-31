#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for pyin3zhi2

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

DEBUG_pyin3zhi2 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replyfivenine/reply_pyin3zhi2.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_pyin3zhi2:
        print("[pyin3zhi2] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "如何把關教學品質":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "如何控制教學品質？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "如何確保教學品質":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "如何管理教學品質？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "如何維護教學品質？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "師生之間的比例是多少？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "師生比例是多少？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "師生比是多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "帶幾[個][小孩]":
        if args[1] in userDefinedDICT["小孩"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)            

        else:
            # write your code here
            pass

    if utterance == "確保[教師]素質":
        if args[0] in userDefinedDICT["老師"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)            

        else:
            # write your code here
            pass

    if utterance == "確保[教師]具備高水準的[專業]能力":
        if args[0] in userDefinedDICT["老師"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "確保營隊[師資][品質]":
        if args[0] in userDefinedDICT["老師"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "老師和學生的比例":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "老師和學生的比例是多少？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT