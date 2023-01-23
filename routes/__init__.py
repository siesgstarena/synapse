from .index import index
from .problem.poc.training import index as training
from .problem.recommend.recommend import index as recommend
from .auth.auth import index as auth_route

__all__ = ["index", "training", "recommend", "auth_route"]
