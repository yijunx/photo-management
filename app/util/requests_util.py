from app.schemas.response import StandardResponse
from pydantic import BaseModel


def create_response(
    response: BaseModel = None, success: bool = True, message: str = None
):
    resp = StandardResponse(success=success, response=response, message=message)
    return resp.dict()


def process_request_header():
    return


def process_response_from_other_services():
    return
