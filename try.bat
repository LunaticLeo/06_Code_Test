@echo off
title Sync floders to github
set message=%date:~6,4%%date:~0,2%%date:~3,2%
echo 'Sync Gradute Folder'
cd ../Graduate && git add . && git commit . -m %message% && git push
echo 'Sync Master Folder'
cd ../Master && git add . && git commit . -m %message% && git push
echo 'Sync Jobs Folder'
cd ../Jobs && git add . && git commit . -m %message% && git push
echo 'Sync Code_Try Folder'
cd ../Code_Try && git add . && git commit . -m %message% && git push
echo 'Sync Algorithm Folder'
cd ../Algorithm && git add . && git commit . -m %message% && git push
echo "Sync complete"
pause