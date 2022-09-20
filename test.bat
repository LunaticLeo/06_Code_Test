@echo off
title Sync floders to github
set message=%date:~6,4%%date:~0,2%%date:~3,2%
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