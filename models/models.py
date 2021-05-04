from typing import List, Optional, ClassVar
from pydantic import BaseModel, validator

class Event(BaseModel):
    uid: str
    project_uid: str
    type: str
    # dynamo
    pk: str = "project|"
    sk: str = "event|"

    @validator("pk", pre=True, always=True)
    def make_pk(cls, v, *, values, **kwargs):
        return v + values["uid"]  # project|<project_uid>
    
    @validator("sk", pre=True, always=True)
    def make_sk(cls, v, *, values, **kwargs):
        return v + values["timestamp"]  # event|<uid>