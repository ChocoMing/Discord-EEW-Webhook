@echo off
:TNMENU
color 0b
echo -
echo -------------------------------------------------------------------------
echo - �a��Wake UP!�s�� Discord-Webhook-EEW
echo - By.Eric101201 , ChocoMing
echo -
echo - ��1.�}�l�w�� Start Install                             
echo - ��0.���} Exit      
echo --------------------------------------------------------------------------
echo -

set choice=
set /p choice= �п�J�Ʀr :
if '%choice%'=='1' goto ST
if '%choice%'=='0' goto OEND
echo "%choice%" is not vaild, try again
goto TNMENU

:ST
echo - �w��discord_webhook�M�󤤡C
pip install discord_webhook
echo - �w�˧����C
echo - �w��dotenv�M�󤤡C
pip install python-dotenv
echo - �w�˧����C
echo - By.Eric101201 , ChocoMing
goto OEND

:OEND
echo *
echo *
echo *
echo *
echo *
echo -------------------------------------------------------------------------
echo - �a��Wake UP!�s�� Discord-Webhook-EEW
echo - By.Eric101201 , ChocoMing
echo -
echo - �T�w���}? Sure Leave?
echo -
echo - ��1.���� Cancel
echo - ��0.���} Exit      
echo --------------------------------------------------------------------------

set choice=
set /p choice= �п�J�Ʀr :
if '%choice%'=='1' goto TNMENU
if '%choice%'=='0' goto END
echo "%choice%" is not vaild, try again
goto OEND

:END

