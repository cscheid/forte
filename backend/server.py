import sys
import os
import logging
from mod_pywebsocket.standalone import WebSocketServer
from mod_pywebsocket import dispatch

def _configure_logging(options):
    logger = logging.getLogger()
    logger.setLevel(logging.getLevelName(options.log_level.upper()))
    if options.log_file:
        handler = logging.handlers.RotatingFileHandler(
                options.log_file, 'a', options.log_max, options.log_count)
    else:
        handler = logging.StreamHandler()
    formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

class Opts(object):
    def __init__(self):
        self.scan_dir = '../backend/handlers'
        self.port = 8880
        self.websock_handlers = '../backend/handlers'
        self.log_level = 'warn'
        self.certificate = ''
        self.strict = False
        self.websock_handlers_map_file = None
        self.is_executable_method = None
        self.use_tls = False
        self.server_host = ''
        self.allow_draft75 = False
        self.document_root = '../frontend'
        self.private_key = ''
        self.config_file = ''
        self.allow_handlers_outside_root_dir = True
        self.thread_monitor_interval_in_sec = -1
        self.validation_port = None
        self.request_queue_size = 128
        self.log_max = 262144
        self.cgi_paths = None
        self.cgi_directories = []
        self.log_count = 5
        self.log_file = ''

class Server(object):
    def __init__(self):
        opts = Opts()
        _configure_logging(opts)
        os.chdir(opts.document_root)
        opts.dispatcher = dispatch.Dispatcher(
            opts.websock_handlers,
            opts.scan_dir,
            opts.allow_handlers_outside_root_dir)
        self._ws_server = WebSocketServer(opts)
    def serve(self):
        self._ws_server.serve_forever()
