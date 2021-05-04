import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from models.models import Event
from lambda_decorators import json_http_resp, load_json_body

@json_http_resp
def handler(event, context):
    # Given the org_id, get organization settings for this org_id
    project_id = event["queryStringParameters"]["project_id"]
    try:
        project = dynamo.get_items(pk=f"project|{project_id}", sk="event|")
        msg = {"statusCode": 200, "body": json.dumps(org)}
    except:
        msg = {
            "statusCode": 404,
            "body": json.dumps({"error": f"No events found for project_id={project_id}"}),
        }
    finally:
        return msg