from __future__ import annotations

import httpx
import pytest

pytestmark = pytest.mark.anyio("asyncio")


async def test_meta_returns_cache_headers(async_client: httpx.AsyncClient) -> None:
    response = await async_client.get("/v1/meta", follow_redirects=False)
    assert response.status_code == 200
    assert response.headers.get("cache-control") == "public, max-age=86400"
    assert response.headers.get("etag") is not None


async def test_meta_etag_uses_304(async_client: httpx.AsyncClient) -> None:
    first = await async_client.get("/v1/meta", follow_redirects=False)
    etag = first.headers.get("etag")
    assert etag

    second = await async_client.get(
        "/v1/meta",
        headers={"If-None-Match": etag},
        follow_redirects=False,
    )
    assert second.status_code == 304
    assert second.headers.get("etag") == etag
