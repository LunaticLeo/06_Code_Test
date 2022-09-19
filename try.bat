@echo off
title Sync floders to github
set message=%date:~6,4%%date:~0,2%%date:~3,2%
cd ../Graduate && git add . && git commit . -m %message% && git push
cd ../Master && git add . && git commit . -m %message% && git push
cd ../Jobs && git add . && git commit . -m %message% && git push
cd ../Code_Try && git add . && git commit . -m %message% && git push
cd ../Algorithm && git add . && git commit . -m %message% && git push
echo "Sync complete"
pause