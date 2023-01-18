@echo off
title Sync floders to github
set message=%date:~10,4%
echo %message%
echo. && echo 'Sync Gradute Folder' 
cd ../Graduate && git commit -am %message% && git push

echo. && echo 'Sync Master Folder'
cd ../Master && git commit -am %message% && git push

echo. && echo 'Sync Jobs Folder'
cd ../Jobs && git commit -am %message% && git push

echo. && echo 'Sync Code_Test Folder'
cd ../Code_Test && git commit -am %message% && git push

echo. && echo 'Sync Algorithm Folder'
cd ../Algorithm && git commit -am %message% && git push

echo. && echo "Sync complete"
pause