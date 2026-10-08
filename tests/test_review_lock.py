import pytest
from PyPlayerokAPI.stream.events.event_factory import EventFactory


@pytest.mark.asyncio
async def test_review_lock():

    factory = EventFactory()

    await factory.mark_review_check("deal1")
    await factory.mark_review_check("deal2")

    deals = await factory.get_review_check_deals()

    assert "deal1" in deals
    assert "deal2" in deals

    await factory.unmark_review_check("deal1")

    deals = await factory.get_review_check_deals()

    assert "deal1" not in deals