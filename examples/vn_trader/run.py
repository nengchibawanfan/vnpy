# flake8: noqa
from vnpy.event import EventEngine

from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

from vnpy.gateway.binance import BinanceGateway
from vnpy.gateway.bitmex import BitmexGateway


from vnpy.gateway.okex import OkexGateway
from vnpy.gateway.huobi import HuobiGateway
from vnpy.gateway.bitfinex import BitfinexGateway
from vnpy.gateway.onetoken import OnetokenGateway
from vnpy.gateway.okexf import OkexfGateway
from vnpy.gateway.hbdm import HbdmGateway

from vnpy.app.cta_strategy import CtaStrategyApp
from vnpy.app.csv_loader import CsvLoaderApp
# from vnpy.app.algo_trading import AlgoTradingApp
from vnpy.app.cta_backtester import CtaBacktesterApp
# from vnpy.app.data_recorder import DataRecorderApp
from vnpy.app.risk_manager import RiskManagerApp
# from vnpy.app.script_trader import ScriptTraderApp
# from vnpy.app.rpc_service import RpcServiceApp


def main():
    """"""
    qapp = create_qapp()

    event_engine = EventEngine()

    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(BinanceGateway)


    main_engine.add_gateway(BitmexGateway)


    main_engine.add_gateway(OkexGateway)
    main_engine.add_gateway(HuobiGateway)
    main_engine.add_gateway(BitfinexGateway)
    main_engine.add_gateway(OnetokenGateway)
    main_engine.add_gateway(OkexfGateway)
    main_engine.add_gateway(HbdmGateway)

    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)
    main_engine.add_app(CsvLoaderApp)
    # main_engine.add_app(AlgoTradingApp)
    # main_engine.add_app(DataRecorderApp)
    main_engine.add_app(RiskManagerApp)
    # main_engine.add_app(ScriptTraderApp)
    # main_engine.add_app(RpcServiceApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
