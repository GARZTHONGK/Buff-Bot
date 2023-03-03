## Buff-Bot
English version of jiajiaxds Buff-bot
Program forked from https://github.com/jiajiaxd/Buff-Bot, All credit goes to [jiajiaxd](https://github.com/jiajiaxd) and [lupochan44](https://github.com/lupohan44) for creating the program. I translated it into english and documented some code. If you are looking for the chinese version you can find it [here](https://github.com/jiajiaxd/Buff-Bot).

程序从 https://github.com/jiajiaxd/Buff-Bot 分叉，所有功劳都归功于 jiajiaxd 和 lupochan44 制作程序。我只是将它翻译成英文并记录了一些代码，如果你想要中文版本我强烈建议你从他们的原始 github 下载


Netease BUFF  skin trading platform fully automatic delivery/purchasing and receiving using Python3 and Requests library,
**please read this document carefully before using it!**
**Those who are capable are welcome to submit PRs to improve this program.**
**Please do not violate the open source agreement, including but not limited to reselling this program, etc.**

## How to use?
1. Make sure Python is installed on your system
2. Download the repository and unzip it
3. install dependencies
   ```
    pip install -r requirements.txt
    ```
4. To execute the program, enter the command in commandline "Buff-Bot.py"
5. `Config.example.json` to `config.json` modify the configuration (see FAQ for related tutorials)
6. Open `steamaccount.json` modify all parameters (see FAQ for related tutorials)
7. Open cookies.txt, fill in the cookie of Netease BUFF (just include the session)
8. Enjoy.
## FAQ
1. Support Linux?
Perfect support.

2. `config.json` Instructions

dev: whether to enable the developer mode, non-developers please do not enable it, please check the code for the specific effect

sell_protection: whether to enable the sale protection, it will not automatically receive sales requests that are lower than the price

protection_price: sale protection Price, if the lowest price of other sellers is lower than this price, the sale protection will not be carried out

protection_price_percentage: selling price protection ratio, if the selling price is lower than this ratio * the lowest price of other sellers, the quotation will not be automatically received

sell_notification: sale notification (If you don’t need it, you can delete it)

title: Notification title

body: Notification content

protection_notification: Sale protection notification (if you don’t need it, you can delete it)

title: Notification title

body: Notification content

webhook: Discord channel to send notifications to

session_notification: session expired notification (if you don't need it, you can delete it)

3. `steamaccount.json` Description
steamid: Steam’s digital ID
shared_secret: Steam token parameter
identity_secret: Steam token parameter 
api_key: Steam webpage API key
steam_username: username filled in during Steam login 
steam_password: password filled in during Steam login
view appendix

4. Account security issues?
All source codes of Buff-Bot are open on GitHub, and everyone can check the code security by themselves.
If the user's computer is not invaded by malware, the account cannot be leaked.

**appendix**

The `steamaccount.json` parameter acquisition tutorials are all below.

[Obtain Steam web API KEY](http://steamcommunity.com/dev/apikey)

[Obtaining shared secret and identity secret using SteamDesktopAuthenticator (recommended method)](https://www.youtube.com/watch?v=JjdOJVSZ9Mo)

[Obtaining shared secret and identity secret from Android phone (advanced method)](https://www.reddit.com/r/Bitwarden/comments/zkr5w5/guide_extracting_steam_guard_totp_secrets_from/)

**Obtaining cookies.txt session in chrome using EditThisCookie**
1. Go [here](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en) and add the extension to Chrome.
2. Log into [buff.163.com](https://buff.163.com/)
3. Click on the extension in the top right corner.
4. Find the session tab and copy the value into cookies.txt.

## Thank you
Thanks to [@lupohan44](https://github.com/lupohan44) for the massive code submission for this project!
Special thanks to [JetBrains](https://www.jetbrains.com/) for providing free authorization of IDEs such as [PyCharm for open source projects](https://www.jetbrains.com/pycharm/)
