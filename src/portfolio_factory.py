from .base_optimizer import BasePortfolioOptimizer
from .mean_variance_optimizer import MeanVarianceOptimizer

class PortfolioOptimizerFactory:
    """
    投资组合优化器工厂
    """
    @staticmethod
    def create_optimizer(optimizer_type: str, returns, **kwargs) -> BasePortfolioOptimizer:
        if optimizer_type == "mean_variance":
            return MeanVarianceOptimizer(returns, **kwargs)
        elif optimizer_type == "black_litterman":
            # 后续可以在这里添加BL模型
            raise NotImplementedError("Black-Litterman model not implemented yet")
        elif optimizer_type == "risk_parity":
            # 后续可以在这里添加风险平价模型
            raise NotImplementedError("Risk Parity model not implemented yet")
        else:
            raise ValueError(f"Unknown optimizer type: {optimizer_type}")