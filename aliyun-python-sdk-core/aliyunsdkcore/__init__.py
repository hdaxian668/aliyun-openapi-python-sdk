__version__ = "2.15.2"


import logging


class NullHandler(logging.Handler):
    def emit(self, record):
        pass


logging.getLogger('aliyunsdkcore').addHandler(NullHandler())
