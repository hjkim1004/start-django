from time import localtime,strftime

def getYMD_HM():
    return strftime("%y%m%d_%H%M", localtime())