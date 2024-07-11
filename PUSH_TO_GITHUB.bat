@echo off
cd /d "C:\Users\Andy\Desktop\python_work_github\Equity_Research_Tools_GITHUB\Equity_Research_Tools"
rem cd /d %cd%
python change_TXT_to_PY.py
git add . 
git commit -m "New Updates for generating Equity Report"
git push