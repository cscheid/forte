from threading import Thread
import time
import sys
import os
import midi_reader

def web_socket_do_extra_handshake(request):
    # This example handler accepts any request. See origin_check_wsh.py for how
    # to reject access from untrusted scripts based on origin value.
    pass  # Always accept.

def web_socket_transfer_data(request):
    reader = midi_reader.KeyReader()
    # for i in xrange(21, 109):
    #     time.sleep(1)
    #     request.ws_stream.send_message("[%d, %d]" % (i, 1))
    #     time.sleep(1)
    #     request.ws_stream.send_message("[%d, %d]" % (i, 0))
    d = {144: 1, 128: 0}
    for [[evt_type, key_code, velocity, _], timestamp] in reader.read():
        t = d[evt_type]
        request.ws_stream.send_message("[%d, %d]" % (key_code, t))
    # while True:
    #     line = request.ws_stream.receive_message()
    #     if line is None:
    #         return
    #     if isinstance(line, unicode):
    #         request.ws_stream.send_message(line, binary=False)
    #         if line == _GOODBYE_MESSAGE:
    #             return
    #     else:
    #         request.ws_stream.send_message(line, binary=True)


# vi:sts=4 sw=4 et
