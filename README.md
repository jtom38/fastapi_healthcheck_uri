# fastapi_healthcheck_uri

A module to have a FastAPI HealthCheck reach out to a URI to validate external service health.

## Adding Health Checks

Here is what you need to get started.

```python
from fastapi import FastAPI
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute
from fastapi_healthcheck_uri import HealthCheckUri

app = FastAPI()

# Add Health Checks
_healthChecks = HealthCheckFactory()
_healthChecks.add(
    HealthCheckUri(
        alias='reddit', 
        connectionUri="https://www.reddit.com/r/aww.json", 
        tags=('external', 'reddit', 'aww'),
        healthyCode=200,
        unhealthyCode=500
    )
)
app.add_api_route('/health', endpoint=healthCheckRoute(factory=_healthChecks))

```
