import pytest_asyncio
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from src.main import app  # Adjust path if needed


@pytest_asyncio.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
