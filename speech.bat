@ECHO OFF
SET /A "sec=%2-5"
IF %sec% LSS 0 SET "sec=0"
IF %1 == 0 SET "text=地震速報，預估震度%1級，%sec%秒後抵達"
IF %1 == 1 SET "text=地震速報，預估震度%1級，%sec%秒後抵達"
IF %1 == 2 SET "text=地震速報，預估震度%1級，%sec%秒後抵達"
IF %1 == 3 SET "text=地震速報，預估震度%1級，%sec%秒後抵達"
IF %1 == 4 SET "text=地震速報，預估震度%1級，%sec%秒後抵達"
IF %1 == 5- SET "text=強震警報，預估震度5弱，%sec%秒後抵達"
IF %1 == 5+ SET "text=強震警報，預估震度5強，%sec%秒後抵達"
IF %1 == 6- SET "text=強震警報，預估震度6弱，%sec%秒後抵達"
IF %1 == 6+ SET "text=強震警報，預估震度6強，%sec%秒後抵達"
IF %1 == 7 SET "text=強震警報，預估震度%1級，%sec%秒後抵達"

@echo {"1":"%1","2":"%sec%"} >file.json

PowerShell -WindowStyle Hidden -Command "py bot.py"