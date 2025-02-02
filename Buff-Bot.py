import logging
import os
import shutil
import sys
import json


import apprise
from apprise.AppriseAsset import *
from apprise.decorators import notify
from steampy.client import SteamClient
import requests
import time
import FileUtils

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
}


def checkaccountstate(dev=False):
    # if dev, use local fake trade.
    config = json.loads(FileUtils.readfile("config.json"))
    if dev and os.path.exists('dev/buff_account.json'):
        logger.info('Development mode, using a local account')
        return json.loads(FileUtils.readfile('dev/buff_account.json'))['data']['nickname']
    else:
        # get data, return data if found, else Error
        response_json = requests.get('https://buff.163.com/account/api/user/info', headers=headers).json()
        if response_json['code'] == 'OK':
            if 'data' in response_json:
                if 'nickname' in response_json['data']:
                    return response_json['data']['nickname']
        logger.error('The login status of the BUFF account is invalid, please check cookies.txt!')
        # sends session notification to discord webhook
        if 'session_notification' in config:
            logger.info("sending session invalid message to webhook")

            embed = {
                "title": config["session_notification"]
            }
            data = {
                "embeds": [
                    embed
                ]
            }
            head = {
                "Content-Type": "application/json"
            }
            result = requests.post(config["webhook"], json=data, headers=head)
            if 200 <= result.status_code < 300:
                logger.info(f"Webhook sent status code: {result.status_code}")
            else:
                logger.info(f"Not sent with status code: {result.status_code}, response:\n{result.json()}")
        logger.info("Press any key to continue...")
        os.system('pause >nul')
        sys.exit()

    # Returning True/False is a way to relay your status back to Apprise.
    # Returning nothing (None by default) is always interpreted as a Success


def format_str(text: str, trade):
    for good in trade['goods_infos']:
        good_item = trade['goods_infos'][good]
        created_at_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(trade['created_at']))
        text = text.format(item_name=good_item['name'], steam_price=good_item['steam_price'],
                           steam_price_cny=good_item['steam_price_cny'], buyer_name=trade['bot_name'],
                           buyer_avatar=trade['bot_avatar'], order_time=created_at_time_str, game=good_item['game'],
                           good_icon=good_item['original_icon_url'])
    return text


def main():
    client = None
    development_mode = False
    sell_protection = True
    protection_price = 30
    protection_price_percentage = 0.9
    asset = AppriseAsset(plugin_paths=[__file__])
    os.system("title Buff-Bot https://github.com/jiajiaxd/Buff-Bot")

    logger.info("Welcome to Buff-Bot Github: https://github.com/jiajiaxd/Buff-Bot")
    logger.info("initializing...")
    first_run = False
    if not os.path.exists("config.json"):  # if doesnt exist copy config.example.json to config.json
        first_run = True
        shutil.copy("config.example.json", "config.json")

    if not os.path.exists("cookies.txt"):  # if doesnt exist make cookies.txt
        first_run = True
        FileUtils.writefile("cookies.txt", "session=")

    if not os.path.exists("steamaccount.json"):  # if doesnt exist create steamaccount.json template
        first_run = True
        FileUtils.writefile("steamaccount.json", json.dumps({"steamid": "", "shared_secret": "",
                                                             "identity_secret": "", "api_key": "",
                                                             "steam_username": "", "steam_password": ""}))

    if first_run:
        logger.info("The first run is detected and a configuration file has been generated for you, please follow the README prompts to fill in the configuration file!")
        logger.info('Press any key to continue...')
        os.system('pause >nul')
    config = json.loads(FileUtils.readfile("config.json"))
    ignoredoffer = []
    orderinfo = {}
    if 'dev' in config and config['dev']:
        development_mode = True

    if development_mode:
        logger.info("Developer mode is enabled")

    if 'sell_protection' in config:
        sell_protection = config['sell_protection']

    if 'protection_price' in config:
        protection_price = config['protection_price']

    if 'protection_price_percentage' in config:
        protection_price_percentage = config['protection_price_percentage']

    logger.info("Preparing to log into BUFF...")
    headers['Cookie'] = FileUtils.readfile('cookies.txt')
    logger.info("cookies detected, try to log in ")
    logger.info("Already logged into BUFF username：" + checkaccountstate(dev=development_mode))

    if development_mode:
        logger.info("Developer mode is enabled, skip Steam login")
    else:
        try:
            # logs in using steamaccount.json
            logger.info("Logging into steam")
            acc = json.loads(FileUtils.readfile('steamaccount.json'))
            client = SteamClient(acc.get('api_key'))
            SteamClient.login(client, acc.get('steam_username'), acc.get('steam_password'), 'steamaccount.json')
            logger.info("Successfully logged in!\n")

        except FileNotFoundError:
            # could not find steamaccount.json
            logger.error('steamaccount.json not detected，Please add it to steamaccount.json before proceeding！')
            logger.info('Press any key to exit')
            os.system('pause >nul')
            sys.exit()

    while True:
        try:
            logger.info("Checking Steam account login status...")
            if not development_mode:
                if not client.is_session_alive():
                    # exit if steam session is not alive
                    logger.error("Steam login status invalid! program exited...")
                    sys.exit()

            logger.info("Steam account status is normal")
            logger.info("Pending shipment/pending accessories inspection...")
            checkaccountstate()
            if development_mode and os.path.exists("dev/message_notification.json"):
                logger.info("Developer mode is turned on, use local message notification file")
                to_deliver_order = json.loads(FileUtils.readfile("dev/message_notification.json")).get('data').get(
                    'to_deliver_order')

            else:
                response = requests.get("https://buff.163.com/api/message/notification", headers=headers)
                to_deliver_order = json.loads(response.text).get('data').get('to_deliver_order')

            if int(to_deliver_order.get('csgo')) != 0 or int(to_deliver_order.get('dota2')) != 0:
                # check if for any new sales
                logger.info("detected" + str(
                    int(to_deliver_order.get('csgo')) + int(to_deliver_order.get('dota2'))) + "delivery request！")
                logger.info("CSGO to be delivered: " + str(int(to_deliver_order.get('csgo'))) + "units")
                logger.info("DOTA2 to be delivered: " + str(int(to_deliver_order.get('dota2'))) + "units")

            if development_mode and os.path.exists("dev/steam_trade.json"):
                logger.info("Developer mode is turned on, using local files to be shipped")
                trade = json.loads(FileUtils.readfile("dev/steam_trade.json")).get('data')

            else:
                # get data from site
                response = requests.get("https://buff.163.com/api/market/steam_trade", headers=headers)
                trade = json.loads(response.text).get('data')
            logger.info("Found" + str(len(trade)) + "pending trade quote requests! ")
            try:
                if len(trade) != 0:
                    i = 0
                    for go in trade:
                        i += 1
                        offerid = go.get('tradeofferid')
                        logger.info("Processing the first" + str(i) + "Trade offer ID" + str(offerid))
                        if offerid not in ignoredoffer:
                            try:
                                if sell_protection:
                                    logger.info("Checking transaction amount...")
                                    # Only check the price of the first item, multiple items are purchased in bulk, theoretically the price of the bulk should be the same
                                    if go['tradeofferid'] not in orderinfo:
                                        if development_mode and os.path.exists("dev/sell_order_history.json"):
                                            # dev mode
                                            logger.info("Developer mode is enabled, use local data")
                                            resp_json = json.loads(FileUtils.readfile("dev/sell_order_history.json"))
                                        else:
                                            # constructs a history link and gets data from it
                                            sell_order_history_url = 'https://buff.163.com/api/market/sell_order/history' \
                                                                     '?appid=' + str(go['appid']) + '&mode=1 '
                                            resp = requests.get(sell_order_history_url, headers=headers)
                                            resp_json = resp.json()

                                        if resp_json['code'] == 'OK':
                                            # adds a key value pair to the "orderinfo" the key is set to the value of 'sell_item['tradeofferid'], and the value is set to the value of 'sell_item*
                                            for sell_item in resp_json['data']['items']:
                                                if 'tradeofferid' in sell_item and sell_item['tradeofferid']:
                                                    orderinfo[sell_item['tradeofferid']] = sell_item

                                    if go['tradeofferid'] not in orderinfo:
                                        logger.error("The transaction amount cannot be obtained, skip this transaction quotation")
                                        continue
                                    price = float(orderinfo[go['tradeofferid']]['price'])
                                    goods_id = str(list(go['goods_infos'].keys())[0])

                                    if development_mode and os.path.exists("dev/shop_listing.json"):
                                        # dev mode
                                        logger.info("Developer mode is enabled, use local price data")
                                        resp_json = json.loads(FileUtils.readfile("dev/shop_listing.json"))

                                    else:
                                        # constructs a link and gets data
                                        shop_listing_url = 'https://buff.163.com/api/market/goods/sell_order?game=' + \
                                                           go['game'] + '&goods_id=' + goods_id + \
                                                           '&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1'
                                        resp = requests.get(shop_listing_url, headers=headers)
                                        resp_json = resp.json()

                                    other_lowest_price = float(resp_json['data']['items'][0]['price'])
                                    if price < other_lowest_price * protection_price_percentage and \
                                            other_lowest_price > protection_price:
                                        # checks if price is too low compared to other items
                                        logger.error("The transaction amount is too low, skip this transaction quote")

                                        if 'protection_notification' in config:
                                            logger.info("Sending protection notification to webhook")
                                            embed = {
                                                "description": config["protection_notification"].get("body"),
                                                "title": config["protection_notification"].get("title")
                                            }
                                            data = {
                                                "embeds": [
                                                    embed
                                                ]
                                            }

                                            head = {
                                                "Content-Type": "application/json"
                                            }
                                            result = requests.post(config["webhook"], json=data, headers=head)
                                            if 200 <= result.status_code < 300:
                                                logger.info(f"Webhook sent status code: {result.status_code}")
                                            else:
                                                logger.info(f"Not sent with status code: {result.status_code}, response:\n{result.json()}")
                                        continue

                                logger.info("Accepting offers...")
                                if development_mode:
                                    # dev mode skip accepting offers
                                    logger.info("Developer mode is enabled, skip accepting offers")
                                else:
                                    # accepting trade
                                    client.accept_trade_offer(offerid)
                                ignoredoffer.append(offerid)  # adds offer to ignore list
                                logger.info("Trade complete! This transaction offer has been added to the ignore list! \n ")
                                if 'sell_notification' in config:
                                    logger.info("sending sell notification to webhook")

                                    embed = {
                                        "description": config["sell_notification"].get("body"),
                                        "title": config["sell_notification"].get("title")
                                    }
                                    data = {
                                        "embeds": [
                                            embed
                                        ]
                                    }
                                    head = {
                                        "Content-Type": "application/json"
                                    }
                                    result = requests.post(config["webhook"], json=data, headers=head)
                                    if 200 <= result.status_code < 300:
                                        logger.info(f"Webhook sent status code: {result.status_code}")
                                    else:
                                        logger.info(f"Not sent with status code: {result.status_code}, response:\n{result.json()}")
                            except Exception as e:
                                logger.error(e, exc_info=True)
                                logger.info("An error occurred , try again later!")
                        else:
                            # skip offer
                            logger.info("This quote has already been processed, skip. \n ")
                    logger.info("There is no BUFF quotation request. Will check the BUFF transaction information again after 600 seconds! \n ")
                else:
                    logger.info("There is no BUFF quotation request. Will check the BUFF transaction information again after 600 seconds! \n ")
            except KeyboardInterrupt:
                # kills program if interrupted
                logger.info("User stopped, program exited ... ")
                sys.exit()
            except Exception as e:
                logger.error(e, exc_info=True)
                logger.info(" An error occurred , try again later!")
            time.sleep(600)

        except KeyboardInterrupt:
            # kills program if interrupted
            logger.info("User stopped, program exited ... ")
            sys.exit()


if __name__ == '__main__':
    logger = logging.getLogger("Buff-Bot")
    logger.setLevel(logging.DEBUG)
    s_handler = logging.StreamHandler()  # creates a stream handler which outputs log messages to console
    s_handler.setLevel(logging.INFO)
    s_handler.setFormatter(logging.Formatter('[%(asctime)s] - %(filename)s - %(levelname)s: %(message)s'))
    logger.addHandler(s_handler)
    main()
