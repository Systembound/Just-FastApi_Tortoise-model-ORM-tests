import pytest

from src.models import PersonModel


@pytest.mark.asyncio()
async def test_person_model_creation():
    person = PersonModel(
        first_name="Ammad",
        last_name="Khalid"
    )
    await person.save()
    assert person == await PersonModel.first()
