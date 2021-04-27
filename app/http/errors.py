from abc import ABC, abstractmethod

from app.http.http_statuses import HTTP_UNAUTHORIZED, HTTP_CONFLICT, HTTP_BAD_REQUEST, HTTP_NOT_FOUND


class HttpException(Exception, ABC):
    @property
    @abstractmethod
    def status(self):
        pass


class BadRequestException(HttpException):
    @property
    def status(self):
        return HTTP_BAD_REQUEST


class ConflictException(HttpException):
    @property
    def status(self):
        return HTTP_CONFLICT


class UnauthorizedException(HttpException):
    @property
    def status(self):
        return HTTP_UNAUTHORIZED


class NotFoundException(HttpException):
    @property
    def status(self):
        return HTTP_NOT_FOUND
