import pytest


@pytest.mark.asyncio
async def test_get_patient_by_code_success(async_client):
    response = await async_client.get("/patient?code=42212")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_patient_by_code_failure(async_client):
    response = await async_client.get("/patient?code=0")
    assert response.status_code == 404

    response = await async_client.get("/patient?code=-1")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_patient_by_string_success(async_client):
    response = await async_client.get("/patient?string=test")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_patient_by_string_failure(async_client):
    response = await async_client.get("/patient?string=")
    assert response.status_code == 422
