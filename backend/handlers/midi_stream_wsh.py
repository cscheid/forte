from threading import Thread
import time
import sys
import os
import midi_reader
import logger

def web_socket_do_extra_handshake(request):
    # This example handler accepts any request. See origin_check_wsh.py for how
    # to reject access from untrusted scripts based on origin value.
    pass  # Always accept.

def web_socket_transfer_data(request):
    reader = midi_reader.KeyReader()
    log = logger.SessionLogger()
    d = {144: 1, 128: 0}
    print logger
    for [[evt_type, key_code, velocity, _], timestamp] in reader.read():
        t = d[evt_type]
        log.key_event(evt_type, key_code, velocity, timestamp)
        request.ws_stream.send_message("[%d, %d]" % (key_code, t))
        
