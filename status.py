# -*- coding: utf-8 -*-

def network_status():
    """检测是否断网
    
    return：
            0：没有断网
            1：因 下线/故障 导致的断网
    """
    import os
    statu = 0
    ping_return = os.popen("ping 220.181.38.148")       # ping 百度
    for i in ping_return:
        if(i == "请求超时。\n"):
            statu = 1
            break
        if(i == "PING：传输失败。常见故障。 \n"):
            statu = 1
            break
    return statu


print(network_status())