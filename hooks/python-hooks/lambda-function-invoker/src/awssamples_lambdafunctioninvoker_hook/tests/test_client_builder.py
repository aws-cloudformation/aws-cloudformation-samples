"""Unit tests for ClientBuilder."""


from unittest.mock import MagicMock

from cloudformation_cli_python_lib import SessionProxy  # type: ignore

from ..client_builder import ClientBuilder


def test_given_no_instance_of_session_proxy_when_get_session_client_called_then_should_return_none():  # noqa: E501
    session = None

    lambda_client = ClientBuilder.get_session_client(
        session=session,
        aws_service_name="lambda",
    )

    assert lambda_client is None


def test_given_instance_of_session_proxy_when_get_session_client_called_then_should_not_return_none():  # noqa: E501
    session = MagicMock(
        name="session",
    )
    session.client = MagicMock(
        name="client",
        return_value=MagicMock(
            name="client",
        ),
    )
    lambda_client = ClientBuilder.get_session_client(
        session=SessionProxy(
            session=session,
        ),
        aws_service_name="lambda",
    )

    assert lambda_client is not None
