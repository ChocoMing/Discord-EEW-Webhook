@echo off
:TNMENU
color 0b
echo -
echo -------------------------------------------------------------------------
echo - 地牛Wake UP!連動 Discord-Webhook-EEW
echo - By.Eric101201 , ChocoMing
echo -
echo - 按1.開始安裝 Start Install                             
echo - 按0.離開 Exit      
echo --------------------------------------------------------------------------
echo -

set choice=
set /p choice= 請輸入數字 :
if '%choice%'=='1' goto ST
if '%choice%'=='0' goto OEND
echo "%choice%" is not vaild, try again
goto TNMENU

:ST
echo - 安裝discord_webhook套件中。
pip install discord_webhook
echo - 安裝完成。
echo - 安裝dotenv套件中。
pip install python-dotenv
echo - 安裝完成。
echo - By.Eric101201 , ChocoMing
goto OEND

:OEND
echo *
echo *
echo *
echo *
echo *
echo -------------------------------------------------------------------------
echo - 地牛Wake UP!連動 Discord-Webhook-EEW
echo - By.Eric101201 , ChocoMing
echo -
echo - 確定離開? Sure Leave?
echo -
echo - 按1.取消 Cancel
echo - 按0.離開 Exit      
echo --------------------------------------------------------------------------

set choice=
set /p choice= 請輸入數字 :
if '%choice%'=='1' goto TNMENU
if '%choice%'=='0' goto END
echo "%choice%" is not vaild, try again
goto OEND

:END

