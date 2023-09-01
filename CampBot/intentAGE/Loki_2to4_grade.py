#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 2to4_grade

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

DEBUG_2to4_grade = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_2to4_grade.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_2to4_grade:
        print("[2to4_grade] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[2]":

        if args[0] in ["2","3","4"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = ("我知道了，小朋友是國小{}年級，那請問您想問什麼呢?".format(args[0]))
                resultDICT["age_grade"] = "junior"
                pass
        else:
            resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
            pass

    if utterance == "[二]年級":
        if args[0] in ["二","三","四"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = ("我知道了，小朋友是國小{}年級，那請問您想問什麼呢?".format(args[0]))
                resultDICT["age_grade"] = "junior"
                pass
        else:
            resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
            pass

    if utterance == "[小][二]":
        if args[1] in ["二","三","四"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = ("我知道了，小朋友是國小{}年級，那請問您想問什麼呢?".format(args[1]))
                resultDICT["age_grade"] = "junior"
                pass
        else:
            resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
            pass

    if utterance == "國小[二]年級":
        if args[0] in ["二","三","四"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = ("我知道了，小朋友是國小{}年級，那請問您想問什麼呢?".format(args[0]))
                resultDICT["age_grade"] = "junior"
                pass
        else:
            resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
            pass
        
    if utterance == "國小[2]年級":
        if args[0] in ["2","3","4"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = ("我知道了，小朋友是國小{}年級，那請問您想問什麼呢?".format(args[0]))
                resultDICT["age_grade"] = "junior"
                pass
        else:
            resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
            pass
        
    if utterance == "[8]歲":
        if args[0] in ["8","八"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = ("我知道了，小朋友是國小二年級，那請問您想問什麼呢?")
                resultDICT["age_grade"] = "junior"
                pass
            
        elif args[0] in ["9", "九"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = ("我知道了，小朋友是國小二年級，那請問您想問什麼呢?")
                resultDICT["age_grade"] = "junior"
                pass
            
        elif args[0] in ["10", "十"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = ("我知道了，小朋友是國小二年級，那請問您想問什麼呢?")
                resultDICT["age_grade"] = "junior"
                pass
            
        elif args[0] in ["11", "十一"]:
            resultDICT["response"] = "請問是五年級還是六年級呢?"
            resultDICT["age_grade"] = "tmp"
        else:
            resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
            pass

        
    return resultDICT