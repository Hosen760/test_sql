import numpy as np
from scipy.optimize import minimize
from .base_optimizer import BasePortfolioOptimizer 

class MeanVarianceOptimizer(BasePortfolioOptimizer):
    """
    均值方差优化器
    """
    def __init__(self, returns, risk_free_rate=0.0, max_weight_ratio=None):
        super().__init__(returns)
        self.risk_free_rate = risk_free_rate
        self.mean_returns = returns.mean()
        self.cov_matrix = returns.cov()
        # 如果没有指定最大权重比例，则默认为 1/n
        self.max_weight_ratio = max_weight_ratio or (2.0 / self.n_assets)

    def negative_sharpe_ratio(self, weights):
        """
        目标函数：最大化夏普比率
        """
        p_ret, p_risk = self.portfolio_performance(weights)
        return -(p_ret - self.risk_free_rate) / p_risk

    def optimize(self):
        """
        执行均值方差优化
        """
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        # 修改边界：最小值0，最大值为 self.max_weight_ratio
        bounds = tuple((0, self.max_weight_ratio) for _ in range(self.n_assets))
        init_guess = self.n_assets * [1. / self.n_assets,]

        result = minimize(
            self.negative_sharpe_ratio,
            init_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        return result.x