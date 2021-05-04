from typing import List, Optional, ClassVar
from pydantic import BaseModel, validator

class Event(BaseModel):
    uid: str
    project_id: str
    type: str
    # dynamo
    pk: str = "project|"
    sk: str = "event|"

    @validator("pk", pre=True, always=True)
    def make_pk(cls, v, *, values, **kwargs):
        return v + values["project_id"]  # project|<project_uid>
    
    @validator("sk", pre=True, always=True)
    def make_sk(cls, v, *, values, **kwargs):
        return v + values["uid"]  # event|<uid>