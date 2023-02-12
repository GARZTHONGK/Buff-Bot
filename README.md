Buff-Bot
English version of jiajiaxds Buff-bot
Program forked from https://github.com/jiajiaxd/Buff-Bot, All credit goes to [jiajiaxd](https://github.com/jiajiaxd) and [lupochan44](https://github.com/lupohan44) for creating the program. I translated it into english and documented some code. If you are looking for the chinese version you can find it [here](https://github.com/jiajiaxd/Buff-Bot).

程序从 https://github.com/jiajiaxd/Buff-Bot 分叉，所有功劳都归功于 jiajiaxd 和 lupochan44 制作程序。我只是将它翻译成英文并记录了一些代码，如果你想要中文版本我强烈建议你从他们的原始 github 下载


Netease BUFF  jewelry trading platform fully automatic delivery/purchasing and receiving using Python3 and Requests library,
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

sell_notification: sale notification (such as If you don’t need it, you can delete it directly)

title: Notification title

body: Notification content

protection_notification: Sale protection notification (if you don’t need it, you can delete it directly)

title: Notification title

body: Notification content

servers: Apprise format server list - see [Apprise for details](https://github.com/caronc/apprise)

* Additional support for [Server sauce](https://sct.ftqq.com/) format is `isftqq://<SENDKEY>`
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
If the user's computer is not invaded by malware, the account cannot be leaked

**appendix**
The `steamaccount.json` parameter acquisition tutorials are all below, please refer to the
personal recommendation to use [Watt Toolkit](https://github.com/BeyondDimension/SteamTools) to obtain Steam token parameter operation is very simple

[Obtain Steam web page API KEY](http://steamcommunity.com/dev/apikey)

[Steam token introduction and extract and transfer](https://steam.red/blog/archives/Steamguard.html)

[buffhelp NetEase buff automatic delivery-哔哩哔哩(Please check P2-P7)](https://www.bilibili.com/video/BV1DT4y1P7Dx)

[Obtaining SteamGuard from mobile device](https://github.com/SteamTimeIdler/stidler/wiki/Getting-your-%27shared_secret%27-code-for-use-with-Auto-Restarter-on-Mobile-Authentication)

[Obtaining SteamGuard using Android emulation](https://github.com/codepath/android_guides/wiki/Genymotion-2.0-Emulators-with-Google-Play-support)

## Thank you
Thanks to [@lupohan44](https://github.com/lupohan44) for the massive code submission for this project!
Special thanks to [JetBrains](https://www.jetbrains.com/) for providing free authorization of IDEs such as [PyCharm for open source projects](https://www.jetbrains.com/pycharm/)
