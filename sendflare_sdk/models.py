"""Sendflare SDK Models"""

from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field, asdict


@dataclass
class PaginateReq:
    """Pagination request entity"""
    page: int = 1
    page_size: int = 10


@dataclass
class PaginateResp:
    """Pagination response entity"""
    page: int = 0
    page_size: int = 0
    total_count: int = 0


@dataclass
class CommonResponse:
    """Common response entity"""
    request_id: str = ""
    code: int = 0
    success: bool = False
    message: str = ""
    ts: int = 0
    data: Optional[Any] = None


@dataclass
class SendEmailReq:
    """Send Email request entity"""
    from_: str
    to: str
    subject: str
    body: str

    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary"""
        return {
            'from': self.from_,
            'to': self.to,
            'subject': self.subject,
            'body': self.body
        }


@dataclass
class SendEmailResp(CommonResponse):
    """Send Email response entity"""
    pass

@dataclass
class ListContactReq(PaginateReq):
    """Get Contact list request entity"""
    app_id: str = ""


@dataclass
class ListContactResp(PaginateResp):
    """Get Contact list response entity"""
    list: List[Dict[str, str]] = field(default_factory=list)


@dataclass
class SaveContactReq:
    """Save contact request entity"""
    app_id: str
    email_address: str
    data: Optional[Dict[str, str]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {
            'appId': self.app_id,
            'emailAddress': self.email_address
        }
        if self.data is not None:
            result['data'] = self.data
        return result


@dataclass
class SaveContactResp(CommonResponse):
    """Save contact response entity"""
    pass


@dataclass
class DeleteContactReq:
    """Delete a contact request entity"""
    email_address: str
    app_id: str


@dataclass
class DeleteContactResp(CommonResponse):
    """Delete contact response entity"""
    pass

