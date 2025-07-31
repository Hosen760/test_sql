import pandas as pd
import numpy as np
from .portfolio_factory import PortfolioOptimizerFactory
from .base_optimizer import BasePortfolioOptimizer

class Backtester:
    def __init__(self, prices: pd.DataFrame, optimizer_type: str = "mean_variance", 
                 window: int = 252, **optimizer_kwargs):
        self.prices = prices
        self.optimizer_type = optimizer_type
        self.window = window
        self.optimizer_kwargs = optimizer_kwargs
        self.returns = prices.pct_change().dropna()

    def run(self):
        portfolio_values = [1.0]  # 初始净值为1
        portfolio_returns = []
        dates = []
        weights_history = []

        for i in range(self.window, len(self.returns)):
            # 滚动窗口训练
            train_returns = self.returns.iloc[i - self.window:i]
            
            optimizer: BasePortfolioOptimizer = PortfolioOptimizerFactory.create_optimizer(
                self.optimizer_type, train_returns, **self.optimizer_kwargs
            )
            
            weights = optimizer.optimize()
            weights_history.append(weights)

            # 计算当前组合收益
            current_return = self.returns.iloc[i]
            portfolio_return = np.dot(weights, current_return)
            portfolio_returns.append(portfolio_return)
            dates.append(self.returns.index[i])

            # 更新净值
            new_value = portfolio_values[-1] * (1 + portfolio_return)
            portfolio_values.append(new_value)

        # 构建净值序列
        portfolio_index = pd.Series(portfolio_values[1:], index=dates)  # 去掉初始值1.0

        return portfolio_index, weights_history