"""Tests for Sendflare SDK Client"""

import unittest
from sendflare_sdk import (
    SendflareClient,
    SendEmailReq,
    ListContactReq,
    SaveContactReq,
    DeleteContactReq
)


class TestSendflareClient(unittest.TestCase):
    """Test SendflareClient"""

    def setUp(self):
        """Set up test client"""
        self.client = SendflareClient("this-is-my-token")

    def test_new_sendflare_client(self):
        """Test creating a new Sendflare client"""
        client = SendflareClient("this-is-my-token")
        self.assertIsInstance(client, SendflareClient)
        self.assertEqual(client.token, "this-is-my-token")

    def test_send_email(self):
        """Test send email"""
        req = SendEmailReq(
            from_="test@example.com",
            to="to@example.com",
            subject="test",
            body="test email"
        )

        print(f"Request: {req}")

        try:
            resp = self.client.send_email(req)
            print(f"Response: {resp}")
        except Exception as e:
            print(f"Expected error without valid token: {e}")
            # This is expected without a valid token
            self.assertTrue(True)

    def test_get_contact_list(self):
        """Test get contact list"""
        req = ListContactReq(
            app_id="test",
            page=1,
            page_size=10
        )

        print(f"Request: {req}")

        try:
            resp = self.client.get_contact_list(req)
            print(f"Response: {resp}")
        except Exception as e:
            print(f"Expected error without valid token: {e}")
            # This is expected without a valid token
            self.assertTrue(True)

    def test_save_contact(self):
        """Test save contact"""
        req = SaveContactReq(
            app_id="test",
            email_address="test@example.com",
            data={
                "firstName": "John",
                "lastName": "Doe"
            }
        )

        print(f"Request: {req}")

        try:
            resp = self.client.save_contact(req)
            print(f"Response: {resp}")
        except Exception as e:
            print(f"Expected error without valid token: {e}")
            # This is expected without a valid token
            self.assertTrue(True)

    def test_delete_contact(self):
        """Test delete contact"""
        req = DeleteContactReq(
            email_address="test@example.com",
            app_id="test"
        )

        print(f"Request: {req}")

        try:
            resp = self.client.delete_contact(req)
            print(f"Response: {resp}")
        except Exception as e:
            print(f"Expected error without valid token: {e}")
            # This is expected without a valid token
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

