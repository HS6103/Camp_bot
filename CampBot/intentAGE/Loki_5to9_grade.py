#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 5to9_grade

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

DEBUG_5to9_grade = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_5to9_grade.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_5to9_grade:
        print("[5to9_grade] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
        
    if utterance == "[5]":

        if args[0] in ["5", "6"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = "我知道了，小朋友是國小{}年級，請問您想問什麼呢?".format(args[0])
                resultDICT["age_grade"] = "senior"
                pass
        elif args[0] in ["7", "8", "9"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = "我知道了，小朋友是{}年級，請問您想問什麼呢?".format(args[0])
                resultDICT["age_grade"] = "senior"                
                pass            
        else:
            if resultDICT:
                pass
            else:
                resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
            

    if utterance == "[五]年級":
        if args[0] in ["5", "6", "五", "六"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = "我知道了，小朋友是國小{}年級，請問您想問什麼呢?".format(args[0])
                resultDICT["age_grade"] = "senior"                
                pass
        elif args[0] in ["7", "8", "9","七", "八", "九"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = "我知道了，小朋友是{}年級，請問您想問什麼呢?".format(args[0])
                resultDICT["age_grade"] = "senior"                                
                pass
        else:
            if resultDICT:
                pass
            else:
                resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
            

    if utterance == "[小][五]":
        if args[1] in ["5", "6", "五", "六"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = "我知道了，小朋友是國小{}年級，那請問您想問什麼呢?".format(args[1])
                resultDICT["age_grade"] = "senior"                               
                pass
        else:
            if resultDICT:
                pass
            else:
                resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
            

    if utterance == "中學[一]年級":
        if args[0] in ["1", "2", "3", "一", "二", "三"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = "我知道了，小朋友是國中{}年級，請問您想問什麼呢?".format(args[0])
                resultDICT["age_grade"] = "senior"                                
                pass        
        else:
            if resultDICT:
                pass
            else:
                resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
    
    if utterance == "國中[三]年級":
        if args[0] in ["1", "2", "3", "一", "二", "三"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = "我知道了，小朋友是國中{}年級，請問您想問什麼呢?".format(args[0])
                resultDICT["age_grade"] = "senior"                                
                pass        
        else:
            if resultDICT:
                pass
            else:
                resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"
            
    if utterance == "國[一]":
        if args[0] in ["1", "2", "3", "一", "二", "三"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = "我知道了，小朋友是國中{}年級，請問您想問什麼呢?".format(args[0])
                resultDICT["age_grade"] = "senior"                                
                pass        
        else:
            if resultDICT:
                pass
            else:
                resultDICT["response"] = "抱歉，我們沒有適合您的小孩的營隊喔!"            
    return resultDICT



