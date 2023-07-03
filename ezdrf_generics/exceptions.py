from rest_framework.exceptions import APIException


class CustomResponse(APIException):
    status_code = 201
    default_detail = "Custom Response!"
    default_code = "custom_response"


class NotAcceptable(APIException):
    status_code = 406
    default_detail = "Not Acceptable"
    default_code = "Not_Acceptable"


class NotFound(APIException):
    status_code = 404
    default_detail = "Not Found"
    default_code = "Not_Found"


class InsufficientBalance(APIException):
    status_code = 402
    default_detail = "Insufficient Balance"
    default_code = "Insufficient_Balance"


class AlreadyExists(APIException):
    status_code = 409
    default_detail = "Already Exists"
    default_code = "Already_Exists"


class BadRequest(APIException):
    status_code = 400
    default_detail = "Bad Request"
    default_code = "Bad_Request"

class TooLate(APIException):
    status_code = 419
    default_detail = "Too Late"
    default_code = "Too_Late"

class ThirdPartyError(APIException):
    status_code = 428
    default_detail = "Third Party Error"
    default_code = "Third_Party_Error"