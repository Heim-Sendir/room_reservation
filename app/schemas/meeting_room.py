from typing import Optional

from pydantic import BaseModel, root_validator


class MeetingRoomCreate(BaseModel):
    name: str
    description: Optional[str]

    class Config:

        @root_validator
        def validate_name(cls, values):
            if not values['name']:
                raise ValueError('Name is required')
            elif len(values['name']) > 100:
                raise ValueError('Name is too long')
            return values
