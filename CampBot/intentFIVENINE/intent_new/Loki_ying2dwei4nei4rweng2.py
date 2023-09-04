#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ying2dwei4nei4rweng2

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

DEBUG_ying2dwei4nei4rweng2 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_ying2dwei4nei4rweng2.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ying2dwei4nei4rweng2:
        print("[ying2dwei4nei4rweng2] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[創新創業營]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[創新創業營][幾天]幾[夜]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[創新創業營][都]在幹嘛":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[創新創業營]在做什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[創新創業營]在幹嘛":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[創新創業營]是啥":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[創新創業營]的[詳細]內容":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[創新創業營]的特色是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[創新創業營]的細節":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[創新創業營]聽起來很有趣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "介紹一下[創新創業營]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有[創新創業營]的課表嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT