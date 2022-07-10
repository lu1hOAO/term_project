import logging

logging.basicConfig(level=logging.INFO) # log 輸出模式，可將 INFO 改成 DEBUG 檢視詳細資訊

MODE = 3 # 演算法種類選擇，1~3，第四個演算法請手動將 SIGNAL_THRESHOLD 調低即可
REFRESH_TIME = 60 # 刷新時間，以秒為單位
SIMULATION_TIME = 60 # 總模擬時長，以分鐘為單位
MAP_RANGE = 10  # 長寬格數
BOX_SIZE = 2.5  # 每格的長寬，單位為km
CAR_CHANCE = 65  # 汽車生成機率的倒數，1/65
BASE_STATION_CHANCE = 10  # 基地台生成機率，1/10
CAR_SPEED = 0.02  # 0.02km/s, 72km/hr
CALL_CHANCE = 1/1800  # 每台車每秒撥出電話的機率，2次/小時
CALL_TIME = 3*60  # 每次通話時間，單位為秒，3分鐘/次
BASE_STATION_PT = 200 # 基地台訊號強度，單位為db
SIGNAL_THRESHOLD = 25  # 演算法3的閾值，E=25dB
MINIMUM_THRESHOLD = 100 # 演算法 1 的最小強度，單位為db

DIRECTION_POS = {
    0: {  # up
        "x": 0,
        "y": 1
    },
    1: {  # right
        "x": 1,
        "y": 0
    },
    2: {  # down
        "x": 0,
        "y": -1
    },
    3: {  # left
        "x": -1,
        "y": 0
    },
}
