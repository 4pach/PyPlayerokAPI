import pytest
import asyncio

from PyPlayerokAPI.stream.events.event_factory import EventFactory


@pytest.mark.asyncio
async def test_processed_ttl_cleanup():

    factory = EventFactory(processed_ttl=1)

    assert await factory.mark_processed("deal1") is True
    assert await factory.mark_processed("deal1") is False

    await asyncio.sleep(1.1)

    await factory._cleanup_processed()

    assert await factory.mark_processed("deal1") is True