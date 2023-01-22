from .index import index
from .problem.poc.training import index as training
from .problem.recommend.recommend import index as recommend
from .admin.auth import index as admin_route

__all__ = ["index", "training", "recommend", "admin_route"]
