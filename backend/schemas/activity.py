from pydantic import BaseModel


class ActivityBase(BaseModel):
    title: str
    activity_type: str  # e.g., 'story_mode', 'drill', etc.
    target_phoneme: str | None = None  # e.g., "/ʃ/"
    config: dict = {}  # extra config per activity, default to empty dict


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(ActivityBase):
    id: int


class ActivityOut(ActivityBase):
    id: int

    model_config = {"from_attributes": True}
