import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

class BasePortfolioOptimizer(ABC):
    """
    投资组合优化器的抽象基类
    """
    def __init__(self, returns: pd.DataFrame):
        self.returns = returns
        self.n_assets = returns.shape[1]
        self.asset_names = returns.columns.tolist()

    @abstractmethod
    def optimize(self) -> np.ndarray:
        """
        抽象方法：执行优化并返回权重
        """
        pass

    def portfolio_performance(self, weights: np.ndarray) -> tuple:
        """
        计算组合的收益和风险（年化）
        """
        mean_returns = self.returns.mean()
        cov_matrix = self.returns.cov()
        
        ret = np.sum(mean_returns * weights) * 252
        risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
        return ret, risk