@echo off
title Sync floders to github
set message=%date:~6,4%%date:~0,2%%date:~3,2%
echo '\nSync Gradute Folder' 
cd ../Graduate && git add . && git commit . -m %message% && git push

echo '\nSync Master Folder'
cd ../Master && git add . && git commit . -m %message% && git push

echo '\nSync Jobs Folder'
cd ../Jobs && git add . && git commit . -m %message% && git push

echo '\nSync Code_Test Folder'
cd ../Code_Test && git add . && git commit . -m %message% && git push

echo '\nSync Algorithm Folder'
cd ../Algorithm && git add . && git commit . -m %message% && git push

echo "\nSync complete"
pause