
import os
from datetime import datetime

mediapath = "Media"
gamespath = mediapath + "/Games"
game_name_list = [x for x in os.listdir(gamespath)]


for x in game_name_list:
    #creation_time = time.ctime(os.path.getctime(os.path.join(gamespath, x)))



    creation_time = (datetime.fromtimestamp(os.path.getctime(os.path.join(gamespath, x)))).strftime("%m/%d/%y %H:%M:%S")
    sort_time = (datetime.fromtimestamp(os.path.getctime(os.path.join(gamespath, x)))).strftime("%y/%m/%d/%H/%M/%S")
    
    print(creation_time)
    


