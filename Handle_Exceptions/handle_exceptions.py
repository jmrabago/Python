#!/usr/bin/env python3

"""
ERRORS AND EXCEPTIONS
"""

# Try / Except
try:
    1 / 0
except Exception as e:
    print(type(e))

# Finally
try:
    1 / 0
except Exception as e:
    print('Some exception occured.')
finally:
    print('This will execute.')

# Catching exceptions by type
try:
    1 / 0
except ZeroDivisionError:
    print('You cannot divide a number by 0')
except TypeError:
    print('A TypeError has occured.')
except Exception:
    print('Some other error occured.')

# Custom Decorators


def handleException(func):
    def wrapper():
        try:
            1 / 0
        except TypeError:
            print('A TypeError has occured.')
        except ZeroDivisionError:
            print('You cannot divide a number by 0')
        except Exception:
            print('Some other error occured.')

        return wrapper


@handleException
def causeError():
    return 1 / 0


causeError()

# Raising Exceptions


@handleException
def raiseError():
    raise Exception()


raiseError()

# Custom Exception


class HttpException(Exception):
    statusCode = None
    message = None

    def __init__(self):
        super().__init__(
            f'Status code: {self.statusCode} and message: {self.message}')


class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found.'


class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up.'


def raiseServerError():
    raise ServerError()


raiseServerError()
