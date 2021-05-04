import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from models.models import Event
from helpers import dynamo
import json

def handler(event, context):
    # Given the org_id, get organization settings for this org_id
    project_id = event["queryStringParameters"]["project_id"]
    try:
        project = dynamo.get_items(pk=f"project|{project_id}", sk="event|")
    except Exception as e:
        print(e)
        return {
            "statusCode": 404,
            "body": json.dumps({"error": f"No events found for project_id={project_id}"}),
        }
    msg = {"statusCode": 200, "body": json.dumps(project)}
    return msg