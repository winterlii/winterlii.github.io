<!--
 * @Description: 
 * @Version: 1.0
 * @Autor: Wantong.Li
 * @Date: 2026-09-14 14:28:24
 * @LastEditors: Wantong.Li
 * @LastEditTime: 2026-09-14 15:05:19
-->
## Guide for html file deploy
This github.io webset mainly deploy ghp-page for webset display, so the mark down store in main branch , and static components in branch ghp-import, which import from the output file of main.

### Tool revision
- python: python3.11


### steps for deploy environment in local machina
```
## clone repo
git clone git@github.com:wantong/wantong.github.io.git

## setup venv
python -m venv docfiles

## install pelican and requirements
pip install "pelican[markdonw]" -r requirements.txt

## source virtual environment
source Script/active

## pull the flex theme
git submodule update --init --recursive

## build pelican static website
pelican content -s pelicanconf.py

## import ghp-import for gitbub branch load
ghp-import -n -p -f output -b gh-pages
```
