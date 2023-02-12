Goals:
Translate everything into english
Document everything
format README.md correctly


Chinese: 

# Buff-Bot
使用Python3和Requests库实现的网易BUFF饰品交易平台全自动发货/求购收货  
**使用前请仔细阅读本文档！**  
**欢迎有能力者提交PR来完善本程序。**  
**请勿违反开源协议，包括但不限于倒卖此程序等。**

## 如何使用?
1. 确保你的系统内已经安装Python  
2. 下载仓库并解压
3. 安装依赖
    ```
    pip install -r requirements.txt
    ```
4. 执行程序, 在命令行内输入```python Buff-Bot.py```
5. 将 `config.example.json` 复制到 `config.json` 并修改配置(相关教程见FAQ)
6. 打开`steamaccount.json`, 修改所有参数(相关教程见FAQ)
7. 打开`cookies.txt`, 填入[网易BUFF](https://buff.163.com)的cookie(包含session即可)
8. Enjoy.
## FAQ
**1.支持Linux?**  
完美支持.

**2. `config.json` 说明**  
dev:是否开启开发者模式, 非开发者请勿开启, 具体效果请自行查看代码  
sell_protection:是否开启出售保护, 开启后将不会自动接收低于价格过低的出售请求  
protection_price:出售保护价格, 若其他卖家最低价低于此价格, 则不会进行出售保护  
protection_price_percentage:出售价格保护比例, 若出售价格低于此比例*其他卖家最低价格, 则不会自动接收报价  
sell_notification:出售通知(如不需要可直接删除)  
title:通知标题  
body:通知内容  
protection_notification:出售保护通知(如不需要可直接删除)  
title:通知标题  
body:通知内容  
servers:Apprise格式服务器列表 - 详见[Apprise](https://github.com/caronc/apprise)  
- 额外支持 [Server酱](https://sct.ftqq.com/) 格式为`ftqq://<SENDKEY>`

**3.`steamaccount.json`说明**  
steamid:Steam的数字ID  
shared_secret:Steam令牌参数  
identity_secret:Steam令牌参数  
api_key:Steam网页API密钥  
steam_username:Steam登录时填写的用户名  
steam_password:Steam登录时填写的密码  
**部分参数获取教程请查看附录**

**4.账号安全问题?**  
Buff-Bot所有源代码均开放在GitHub，可供所有人自行查看代码安全性  
在用户的电脑不被恶意软件入侵的情况下，账号不可能泄露  

## 附录
关于`steamaccount.json`相关参数的获取教程都在下面, 请自行参阅  
个人推荐使用[ Watt Toolkit ](https://github.com/BeyondDimension/SteamTools)获取Steam令牌参数 操作非常简便

[获取Steam网页API KEY](http://steamcommunity.com/dev/apikey)   
[Steam令牌介绍以及提取转移](https://steam.red/blog/archives/Steamguard.html)  
[buffhelp 网易buff自动发货-哔哩哔哩(请查看P2-P7)](https://www.bilibili.com/video/BV1DT4y1P7Dx)  
[Obtaining SteamGuard from mobile device]( https://github.com/SteamTimeIdler/stidler/wiki/Getting-your-%27shared_secret%27-code-for-use-with-Auto-Restarter-on-Mobile-Authentication )  
[Obtaining SteamGuard using Android emulation]( https://github.com/codepath/android_guides/wiki/Genymotion-2.0-Emulators-with-Google-Play-support)

## 鸣谢
感谢 [**@lupohan44**](https://github.com/lupohan44) 为本项目提交的大量代码！  
特别感谢 [JetBrains](https://www.jetbrains.com/) 为开源项目提供免费的 [PyCharm](https://www.jetbrains.com/pycharm/) 等 IDE 的授权  
[<img src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg" width="200"/>](https://jb.gg/OpenSourceSupport)
[<img src="https://resources.jetbrains.com/storage/products/company/brand/logos/PyCharm_icon.svg" width="200"/>](https://jb.gg/OpenSourceSupport)


-------------------------------------------------------------

English: 

Buff-Bot
Netease BUFF jewelry trading platform fully automatic delivery/purchasing and receiving using Python3 and Requests library,
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
