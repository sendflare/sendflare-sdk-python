"""Sendflare SDK Client"""

import json
from typing import Dict, Optional
from urllib.parse import urlencode
import urllib.request
from urllib.error import URLError, HTTPError

from .models import (
    SendEmailReq,
    SendEmailResp,
    ListContactReq,
    ListContactResp,
    SaveContactReq,
    SaveContactResp,
    DeleteContactReq,
    DeleteContactResp,
    ContactItem
)


class SendflareClient:
    """Sendflare SDK Client"""

    BASE_URL = "https://api.sendflare.io"
    REQUEST_TIMEOUT = 10  # seconds

    def __init__(self, token: str):
        """
        Create a new Sendflare client instance

        Args:
            token: API token
        """
        self.token = token

    def send_email(self, req: SendEmailReq) -> SendEmailResp:
        """
        Send an email

        Args:
            req: Send email request

        Returns:
            Send email response

        Raises:
            Exception: If request fails
        """
        path = "/v1/send"
        data = req.to_dict()

        response = self._make_request("POST", path, data=data)
        return self._map_to_object(response, SendEmailResp)

    def get_contact_list(self, req: ListContactReq) -> ListContactResp:
        """
        Get contact list

        Args:
            req: List contact request

        Returns:
            List contact response

        Raises:
            Exception: If request fails
        """
        path = "/v1/contact"
        params = {
            'appId': req.app_id,
            'page': str(req.page),
            'pageSize': str(req.page_size)
        }

        response = self._make_request("GET", path, params=params)
        
        # Map the response
        result = ListContactResp(
            page=response.get('page', 0),
            page_size=response.get('pageSize', 0),
            total_count=response.get('totalCount', 0),
            data=[]
        )
        
        # Map contact items
        if 'data' in response and isinstance(response['data'], list):
            result.data = [self._map_to_object(item, ContactItem) for item in response['data']]
        
        return result

    def save_contact(self, req: SaveContactReq) -> SaveContactResp:
        """
        Create or update contact

        Args:
            req: Save contact request

        Returns:
            Save contact response

        Raises:
            Exception: If request fails
        """
        path = "/v1/contact"
        data = req.to_dict()

        response = self._make_request("POST", path, data=data)
        return self._map_to_object(response, SaveContactResp)

    def delete_contact(self, req: DeleteContactReq) -> DeleteContactResp:
        """
        Delete a contact

        Args:
            req: Delete contact request

        Returns:
            Delete contact response

        Raises:
            Exception: If request fails
        """
        path = "/v1/contact"
        params = {
            'appId': req.app_id,
            'emailAddress': req.email_address
        }

        response = self._make_request("DELETE", path, params=params)
        return self._map_to_object(response, DeleteContactResp)

    def _make_request(
        self,
        method: str,
        path: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None
    ) -> Dict:
        """
        Make HTTP request

        Args:
            method: HTTP method
            path: Request path
            data: Request body data
            params: Query parameters

        Returns:
            Response data as dictionary

        Raises:
            Exception: If request fails
        """
        url = self.BASE_URL + path

        if params:
            url += '?' + urlencode(params)

        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        req_data = None
        if data:
            req_data = json.dumps(data).encode('utf-8')

        request = urllib.request.Request(
            url,
            data=req_data,
            headers=headers,
            method=method
        )

        try:
            with urllib.request.urlopen(request, timeout=self.REQUEST_TIMEOUT) as response:
                body = response.read().decode('utf-8')
                return json.loads(body)
        except HTTPError as e:
            raise Exception(f"HTTP error {e.code}: {e.reason}")
        except URLError as e:
            raise Exception(f"URL error: {e.reason}")
        except json.JSONDecodeError as e:
            raise Exception(f"JSON decode error: {e}")

    def _map_to_object(self, data: Dict, cls):
        """
        Map dictionary to object

        Args:
            data: Source dictionary
            cls: Target class

        Returns:
            Mapped object
        """
        # Convert camelCase keys to snake_case
        mapped_data = {}
        for key, value in data.items():
            # Convert camelCase to snake_case
            snake_key = self._camel_to_snake(key)
            mapped_data[snake_key] = value

        try:
            return cls(**mapped_data)
        except TypeError:
            # If direct mapping fails, create object and set attributes
            obj = cls()
            for key, value in mapped_data.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            return obj

    @staticmethod
    def _camel_to_snake(name: str) -> str:
        """Convert camelCase to snake_case"""
        import re
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

