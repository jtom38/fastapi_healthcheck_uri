from fastapi_healthcheck.domain import HealthCheckInterface
from fastapi_healthcheck.service import HealthCheckBase
from fastapi_healthcheck.enum import HealthCheckStatusEnum
from typing import List
from requests import get

class HealthCheckUri(HealthCheckBase, HealthCheckInterface):
    _tags: List[str]
    _connectionUri: str
    _healthyCode: int
    _unhealthyCode: int

    def __init__(self, connectionUri: str, alias: str, tags: List[str], healthyCode: int = 200, unhealthyCode: int = 500) -> None:
        self.setConnectionUri(connectionUri)
        self._alias = alias
        self._tags = tags
        self._healthyCode = healthyCode
        self._unhealthyCode = unhealthyCode

    def __checkHealth__(self) -> bool:
        res = get(url=self.getConnectionUri(), headers={"User-Agent": "FastAPI HealthCheck"})
        if res.status_code == self._healthyCode:
            return HealthCheckStatusEnum.HEALTHY
        elif res.status_code != self._unhealthyCode:
            return HealthCheckStatusEnum.UNHEALTHY
        return HealthCheckStatusEnum.UNHEALTHY
