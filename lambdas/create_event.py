import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from models.models import Event
from lambda_decorators import json_http_resp, load_json_body
from helpers import dynamo

@json_http_resp
@load_json_body
def handler(event, context):
    event = Event(**event['body'])
    resp = dynamo.create_item(event.dict())
    return {"message": f"Event {event.uid} created"}