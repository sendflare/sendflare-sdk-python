"""Sendflare SDK for Python"""

from .client import SendflareClient
from .models import (
    PaginateReq,
    PaginateResp,
    CommonResponse,
    SendEmailReq,
    SendEmailResp,
    ContactItem,
    ListContactReq,
    ListContactResp,
    SaveContactReq,
    SaveContactResp,
    DeleteContactReq,
    DeleteContactResp,
)

__version__ = "1.0.0"
__all__ = [
    "SendflareClient",
    "PaginateReq",
    "PaginateResp",
    "CommonResponse",
    "SendEmailReq",
    "SendEmailResp",
    "ContactItem",
    "ListContactReq",
    "ListContactResp",
    "SaveContactReq",
    "SaveContactResp",
    "DeleteContactReq",
    "DeleteContactResp",
]

