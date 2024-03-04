"""Client builder module."""


from typing import (
    Any,
    Optional,
)

from cloudformation_cli_python_lib import SessionProxy  # type: ignore


class ClientBuilder:
    """Return a SessionProxy-based client for a given AWS service."""

    @staticmethod
    def get_session_client(
        session: Optional[SessionProxy],
        aws_service_name: str,
    ) -> Any:
        """Return a SessionProxy-based client for a given aws_service_name."""
        if isinstance(
            session,
            SessionProxy,
        ):
            return session.client(
                aws_service_name,
            )

        return None
