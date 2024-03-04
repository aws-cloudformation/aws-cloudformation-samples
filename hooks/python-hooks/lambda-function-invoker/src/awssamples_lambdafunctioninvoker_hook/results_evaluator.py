"""AWS Lambda function results evaluator module."""

from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Any,
    Dict,
    List,
)

from cloudformation_cli_python_lib import OperationStatus  # type: ignore


@dataclass
class ResultsEvaluator:
    """Evaluate results of user-provided AWS Lambda function invocations."""

    # List of Lambda functions with respective ProgressEvent objects,
    # that are returned after user-defined Lambda functions have been
    # invoked.
    invoke_results_info: List[Dict[str, Any]] = field(default_factory=list)

    # Failed events.
    _failed_events: List[Dict[str, Any]] = field(default_factory=list)

    # Events that are in progress.
    _in_progress_events: List[Dict[str, Any]] = field(default_factory=list)

    # Events that succeeded.
    _success_events: List[Dict[str, Any]] = field(default_factory=list)

    # All events.
    _events: List[Dict[str, Any]] = field(default_factory=list)

    # List of all ProgressEvent string messages returned by Lambda
    # functions that have been invoked by the hook.
    _events_messages: List[str] = field(default_factory=list)

    # List of all failed ProgressEvent string messages returned by Lambda
    # functions that have been invoked by the hook.
    _failed_events_messages: List[str] = field(default_factory=list)

    def evaluate(self) -> None:
        """Evaluate results provided in invoke_results_info."""
        self._failed_events = [
            invoke_result_info
            for invoke_result_info in self.invoke_results_info
            if invoke_result_info["progress_event"].status
            == OperationStatus.FAILED
        ]

        self._in_progress_events = [
            invoke_result_info
            for invoke_result_info in self.invoke_results_info
            if invoke_result_info["progress_event"].status
            == OperationStatus.IN_PROGRESS
        ]

        self._success_events = [
            invoke_result_info
            for invoke_result_info in self.invoke_results_info
            if invoke_result_info["progress_event"].status
            == OperationStatus.SUCCESS
        ]

        self._events = [
            invoke_result_info
            for invoke_result_info in self.invoke_results_info
        ]

        self._events_messages = [
            invoke_result_info["progress_event"].message
            for invoke_result_info in self.invoke_results_info
        ]

        self._failed_events_messages = [
            invoke_result_info["progress_event"].message
            for invoke_result_info in self.invoke_results_info
            if invoke_result_info["progress_event"].status
            == OperationStatus.FAILED
        ]

    def has_events(
        self,
    ) -> bool:
        """Determine whether invoke_results_info has events."""
        return any(self._events)

    def get_events(
        self,
    ) -> List[Dict[str, Any]]:
        """Return events from invoke_results_info."""
        return self._events

    def has_failed_events(
        self,
    ) -> bool:
        """Determine whether invoke_results_info has failed events."""
        return any(self._failed_events)

    def get_failed_events(
        self,
    ) -> List[Dict[str, Any]]:
        """Return failed events from invoke_results_info."""
        return self._failed_events

    def get_first_failed_event(
        self,
    ) -> Dict[str, Any]:
        """Return the first failed event in invoke_results_info."""
        try:
            return self._failed_events[0]
        except IndexError:
            raise IndexError("There are no failed ProgressEvent events.")

    def has_in_progress_events(
        self,
    ) -> bool:
        """Determine whether invoke_results_info has events in progress."""
        return any(self._in_progress_events)

    def get_in_progress_events(
        self,
    ) -> List[Dict[str, Any]]:
        """Return in-progress events from invoke_results_info."""
        return self._in_progress_events

    def get_highest_callback_delay_seconds(
        self,
    ) -> int:
        """Return the highest callback delay for all in-progress functions."""
        callback_delay_values = [
            invoke_result_info["progress_event"].callbackDelaySeconds
            for invoke_result_info in self.invoke_results_info
        ]

        return sorted(
            callback_delay_values,
            reverse=True,
        )[0]

    def has_success_events(
        self,
    ) -> bool:
        """Determine whether invoke_results_info has success events."""
        return any(self._success_events)

    def get_success_events(
        self,
    ) -> List[Dict[str, Any]]:
        """Return success events from invoke_results_info."""
        return self._success_events

    def get_events_messages(
        self,
    ) -> List[str]:
        """Return messages for all events."""
        return self._events_messages

    def get_failed_events_messages(
        self,
    ) -> List[str]:
        """Return messages for all failed events."""
        return self._failed_events_messages
