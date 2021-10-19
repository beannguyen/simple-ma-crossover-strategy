import backtrader as bt


class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=50,  # period for the fast moving average
        pslow=200  # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):

        if self.crossover > 0:  # if fast crosses slow to the upside
            self.order_target_size(target=1)
            print("Buy {} shares".format(self.data.close[0]))
            print(self.position)

        elif self.crossover < 0:  # in the market & cross to the downside
            self.order_target_size(target=-1)
            print("Sale {} shares".format(self.data.close[0]))
            print(self.position)
