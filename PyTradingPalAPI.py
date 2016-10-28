
# -- ------------------------------------------------------------------------------- -- #
# -- Initial Developer: TradingPal ------------------------------------------------- -- #
# -- Contributions: IFFranciscoME -------------------------------------------------- -- #
# -- GitHub Repository: https://github.com/IFFranciscoME/PyTradingPalAPI ----------- -- #
# -- License: GNU General Public License ------------------------------------------- -- #
# -- ------------------------------------------------------------------------------- -- #

import requests

# -- Lista de funciones contenidas en este codigo para API Trading Pal ------------- -- #

# -- Get Validation Token ----------------------------------------------------- ------- #
# -- ------------------------------------------------- GET /token?token=[token] -- 1 -- #
# -- -------------------------------------------------------------------------- ------- #


def tp_token(p0_email, p1_password):

    http = "http://www.tradingpal.com/api/auth?email="
    http_url = http + str(p0_email) + "&password=" + p1_password
    http_result = requests.get(http_url)
    data = str(http_result.json()['token'])

    return data


# -- Get Actual Bid/Ask Price ------------------------------------------------- ------- #
# -- ------------------------------------------------------------ GET /[symbol] -- 2 -- #
# -- -------------------------------------------------------------------------- ------- #


# -- Get Historical Prices ---------------------------------------------------- ------- #
# -- -------------- GET /[symbol]/chart?period=[period]&from=[from]&till=[till] -- 3 -- #
# -- -------------------------------------------------------------------------- ------- #


def tp_historical_prices(p0_symbol, p1_period, p2_from, p3_token):

    http = "www.tradingpal.com/api/instruments/"

    return Data


# # -- Get Actual Active Trades for an Account -------------------------------- ------- #
# # -- --------------------------- GET /active Description Return active trades -- 4 -- #
# # -- ------------------------------------------------------------------------ ------- #


def tp_actual_trades(p0_userid):

    http1 = "http://www.tradingpal.com/api/users/"

    return Data


# -- Get Historical Trades per User ------------------------------------------- ------- #
# -- GET /users/[uID]/trades/closed Returns close trades by traderID ---------- -- 5 -- #
# -- -------------------------------------------------------------------------- ------- #


def tp_historical_trades(p0_userid):

    http = "http://www.tradingpal.com/api/users/"

    return Data


# -- Modify TakeProfit and StopLoss of a Trade -------------------------------- ------- #
# -- ------------------ PUT /[tradeID]?sl=[sl]&tp=[tp] Description Update trade -- 8 -- #
# -- -------------------------------------------------------------------------- ------- #


def tp_modify_trade(P0_Token, P1_tradeID, P2_SL, P3_TP):

    http = "www.tradingpal.com/api/trades/"

    return Data


# -- Open Trade --------------------------------------------------------------- ------- #
# -- ------------------------- POST /?token=[token] Descriptions Open new trade -- 9 -- #
# -- -------------------------------------------------------------------------- ------- #


def tp_open_trade(P0_Token, P1_symbol, P2_sl, P3_tp, P4_lots, P5_op_type):

    http = "www.tradingpal.com/api/trades/?token="

    return Data


# -- Close Trade -------------------------------------------------------------- ------- #
# -- ----------------- DELETE /[tradeID]?token=[token] Description Close trade -- 10 -- #
# -- -------------------------------------------------------------------------- ------- #


def tp_closetrade(P0_Token, P1_tradeID, P2_userID):

    http = "www.tradingpal.com/api/trades/"

    return Data


# -- Get Account Info -------------------------------------------------------- -------- #
# -- ---------------------------------------- GET /api/users/[user-id]/account -- 12 -- #
# -- ------------------------------------------------------------------------- -------- #


def tp_account_info(P0_Token, P1_userID):

    http = "www.tradingpal.com/api/users/"

    return RetJson

