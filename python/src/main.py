import fileinput
from datetime import timedelta
#import pandas as pd
import datetime

wtime = {}
wtime["wtime_stat"] = []
night_otime = timedelta()
inlegal_delta_time = timedelta()
outlegal_wtime = 0
inlegal_wtime = 0
week_awtime = timedelta()
day_awtime = timedelta()

for line in fileinput.input():
    print(line)
    #if(len(line.split(" ")) >= 2) :
        #data = [{"date":line.split(" ",1)[0]}, {"wtime_data":line.split(" ",1)[-1]}]
        #wtime["wtime_stat"].append(data)
        #print(line)

#print(wtime["wtime_stat"])
#for each_wtime in wtime["wtime_stat"] :  #日付順に見ていく
    
   

        
#         start_time = datetime.strptime(each_wtime[0]["date"]+wtimezone.split("-")[0],'%Y/%m/%d%H:%M') #ある労働時間の開始時間
        #start_time =  pd.to_datetime(each_wtime[0]["date"]) + pd.to_timedelta(wtimezone.split("-")[0]+":00")
#         end_time = datetime.strptime(each_wtime[0]["date"]+wtimezone.split("-")[1],'%Y/%m/%d%H:%M') #ある労働時間の終了時間
        #end_time = pd.to_datetime(each_wtime[0]["date"]) + pd.to_timedelta(wtimezone.split("-")[1]+":00")

