import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import os

database = boto3.resource("dynamodb", region_name="eu-west-1")
table = database.Table(os.environ["eventsTable"])


def get_item(pk, sk):
    # get one item
    response = table.query(
        KeyConditionExpression=Key("pk").eq(pk) & Key("sk").begins_with(sk),
        ConsistentRead=True,
    )
    items = response.get("Items", None)
    try:
        return items[0]
    except:
        raise Exception(f" Item with pk= {pk} and sk= {sk} not found.")


def create_item(item):
    # item should be a dict
    return table.put_item(Item=item)

def get_items(pk, sk):
    response = table.query(
        KeyConditionExpression=Key("pk").eq(pk) & Key("sk").begins_with(sk)
    )

    return {"Items": response["Items"], "Count": response["Count"]}