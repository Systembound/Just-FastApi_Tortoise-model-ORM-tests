import asyncio

import httpx
import pytest

from src.config import drop_databases, db_init, clean_up
from web import app


@pytest.fixture(scope="session")
def loop():
    _loop = asyncio.get_event_loop()
    _loop._close_loop = _loop.close
    _loop.close = lambda: ()
    yield _loop
    _loop._close_loop()


@pytest.fixture(scope="function", autouse=True)
def prepare_db(request, loop):
    async def setup_db():
        await db_init(generate_schema=False)
        try:
            await drop_databases()
        except:
            pass
        await db_init(
            "sqlite://:memory:"
        )

    loop.run_until_complete(setup_db())
    request.addfinalizer(lambda: loop.run_until_complete(clean_up()))


@pytest.fixture(scope="module")
def client():
    client = httpx.AsyncClient(base_url="http://test", app=app)
    yield client
