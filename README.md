# TicTacToe
```
git pull & git tag -d v1.0 & git push -d origin v1.0 & git tag v1.0 && git push origin v1.0
```
Fast build:
```
pip install -r requirements.txt
pyinstaller --noconsole --noconfirm --clean --onedir --contents-directory "." --name TicTacToe src/main.py
```
