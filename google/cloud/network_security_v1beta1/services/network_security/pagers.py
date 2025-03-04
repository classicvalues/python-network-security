# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Sequence,
    Tuple,
    Optional,
    Iterator,
)

from google.cloud.network_security_v1beta1.types import authorization_policy
from google.cloud.network_security_v1beta1.types import client_tls_policy
from google.cloud.network_security_v1beta1.types import server_tls_policy


class ListAuthorizationPoliciesPager:
    """A pager for iterating through ``list_authorization_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1beta1.types.ListAuthorizationPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``authorization_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAuthorizationPolicies`` requests and continue to iterate
    through the ``authorization_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1beta1.types.ListAuthorizationPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., authorization_policy.ListAuthorizationPoliciesResponse],
        request: authorization_policy.ListAuthorizationPoliciesRequest,
        response: authorization_policy.ListAuthorizationPoliciesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1beta1.types.ListAuthorizationPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1beta1.types.ListAuthorizationPoliciesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = authorization_policy.ListAuthorizationPoliciesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[authorization_policy.ListAuthorizationPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[authorization_policy.AuthorizationPolicy]:
        for page in self.pages:
            yield from page.authorization_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthorizationPoliciesAsyncPager:
    """A pager for iterating through ``list_authorization_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1beta1.types.ListAuthorizationPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``authorization_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAuthorizationPolicies`` requests and continue to iterate
    through the ``authorization_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1beta1.types.ListAuthorizationPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[authorization_policy.ListAuthorizationPoliciesResponse]
        ],
        request: authorization_policy.ListAuthorizationPoliciesRequest,
        response: authorization_policy.ListAuthorizationPoliciesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1beta1.types.ListAuthorizationPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1beta1.types.ListAuthorizationPoliciesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = authorization_policy.ListAuthorizationPoliciesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[authorization_policy.ListAuthorizationPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[authorization_policy.AuthorizationPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.authorization_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServerTlsPoliciesPager:
    """A pager for iterating through ``list_server_tls_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1beta1.types.ListServerTlsPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``server_tls_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServerTlsPolicies`` requests and continue to iterate
    through the ``server_tls_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1beta1.types.ListServerTlsPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., server_tls_policy.ListServerTlsPoliciesResponse],
        request: server_tls_policy.ListServerTlsPoliciesRequest,
        response: server_tls_policy.ListServerTlsPoliciesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1beta1.types.ListServerTlsPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1beta1.types.ListServerTlsPoliciesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = server_tls_policy.ListServerTlsPoliciesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[server_tls_policy.ListServerTlsPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[server_tls_policy.ServerTlsPolicy]:
        for page in self.pages:
            yield from page.server_tls_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServerTlsPoliciesAsyncPager:
    """A pager for iterating through ``list_server_tls_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1beta1.types.ListServerTlsPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``server_tls_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServerTlsPolicies`` requests and continue to iterate
    through the ``server_tls_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1beta1.types.ListServerTlsPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[server_tls_policy.ListServerTlsPoliciesResponse]
        ],
        request: server_tls_policy.ListServerTlsPoliciesRequest,
        response: server_tls_policy.ListServerTlsPoliciesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1beta1.types.ListServerTlsPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1beta1.types.ListServerTlsPoliciesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = server_tls_policy.ListServerTlsPoliciesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[server_tls_policy.ListServerTlsPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[server_tls_policy.ServerTlsPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.server_tls_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListClientTlsPoliciesPager:
    """A pager for iterating through ``list_client_tls_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1beta1.types.ListClientTlsPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``client_tls_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListClientTlsPolicies`` requests and continue to iterate
    through the ``client_tls_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1beta1.types.ListClientTlsPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., client_tls_policy.ListClientTlsPoliciesResponse],
        request: client_tls_policy.ListClientTlsPoliciesRequest,
        response: client_tls_policy.ListClientTlsPoliciesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1beta1.types.ListClientTlsPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1beta1.types.ListClientTlsPoliciesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = client_tls_policy.ListClientTlsPoliciesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[client_tls_policy.ListClientTlsPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[client_tls_policy.ClientTlsPolicy]:
        for page in self.pages:
            yield from page.client_tls_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListClientTlsPoliciesAsyncPager:
    """A pager for iterating through ``list_client_tls_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1beta1.types.ListClientTlsPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``client_tls_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListClientTlsPolicies`` requests and continue to iterate
    through the ``client_tls_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1beta1.types.ListClientTlsPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[client_tls_policy.ListClientTlsPoliciesResponse]
        ],
        request: client_tls_policy.ListClientTlsPoliciesRequest,
        response: client_tls_policy.ListClientTlsPoliciesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1beta1.types.ListClientTlsPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1beta1.types.ListClientTlsPoliciesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = client_tls_policy.ListClientTlsPoliciesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[client_tls_policy.ListClientTlsPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[client_tls_policy.ClientTlsPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.client_tls_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
