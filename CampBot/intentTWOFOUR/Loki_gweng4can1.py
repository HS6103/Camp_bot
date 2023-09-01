#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for gweng4can1

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

DEBUG_gweng4can1 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_gweng4can1.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gweng4can1:
        print("[gweng4can1] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[自行]攜帶[午餐]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "中午[會]吃什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "供應午餐":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "午餐吃什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "帶[零食]":
        if args[0] in userDefinedDICT["吃的東西"]:
            
        
            if CHATBOT_MODE:
                tmpSTR = getResponse(utterance, args)
                resultDICT["response"] = tmpSTR.format(args[0])             
            else:
                # write your code here
                pass
        else: resultDICT["response"] = "請問是要帶什麼呢?是吃的嗎?"

    if utterance == "帶[零食]進去":
        if args[0] in userDefinedDICT["吃的東西"]:
            
        
            if CHATBOT_MODE:
                tmpSTR = getResponse(utterance, args)
                resultDICT["response"] = tmpSTR.format(args[0])             
            else:
                # write your code here
                pass
        else: resultDICT["response"] = "請問是要帶什麼呢?是吃的嗎?"

    if utterance == "把[零食]帶進去":
        if args[0] in userDefinedDICT["吃的東西"]:
            
        
            if CHATBOT_MODE:
                tmpSTR = getResponse(utterance, args)
                resultDICT["response"] = tmpSTR.format(args[0])             
            else:
                # write your code here
                pass
        else: resultDICT["response"] = "請問是要帶什麼呢?是吃的嗎?"

    if utterance == "提供[午餐]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "早餐是[自己]解決":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "早餐是[自行]解決":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有沒[有]點心":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有沒[有]點心吃？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有點心":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "自備[午餐]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT