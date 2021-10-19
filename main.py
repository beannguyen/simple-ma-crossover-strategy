import backtrader as bt
import pandas as pd

from backtest import SmaCross


def run():
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    df = pd.read_csv(f"data/FPT.csv",
                     parse_dates=True,
                     index_col=['timestamp'])
    data = bt.feeds.PandasData(dataname=df)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # add strategy
    cerebro.addstrategy(SmaCross)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()

    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())


if __name__ == '__main__':
    run()
