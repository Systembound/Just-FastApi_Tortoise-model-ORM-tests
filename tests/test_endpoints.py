import pytest


@pytest.mark.asyncio
async def test_create_ammad_endpoint(client):
    response = await client.post("/create-ammad")
    assert response.status_code == 200
