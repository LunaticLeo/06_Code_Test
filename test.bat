@echo off
title Sync floders to github

echo. && echo 'Sync Gradute Folder' 
cd ../Graduate && git add . && git commit -am auto && git push

echo. && echo 'Sync Master Folder'
cd ../Master && git add . && git commit -am auto && git push

echo. && echo 'Sync Jobs Folder'
cd ../Jobs && git add . && git commit -am auto && git push

echo. && echo 'Sync Code_Test Folder'
cd ../Code_Test && git add . && git commit -am auto && git push

echo. && echo 'Sync Algorithm Folder'
cd ../Algorithm && git add . && git commit -am auto && git push

echo. && echo "Sync complete"
pause