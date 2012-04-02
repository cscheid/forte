import conf
import sqlite3
import time

##############################################################################

class SessionLogger(object):

    def __init__(self):
        loc = conf.db_location()
        self.conn = sqlite3.connect(loc)
        self.ensure_table_exists(self.conn)
        self.session_id = self.create_session()

    def ensure_table_exists(self, conn):
        cur = conn.cursor()
        try:
            c = cur.execute('select key from key_events')
            return True
        except sqlite3.OperationalError:
            init_db(conn)

    def create_session(self):
        cur = self.conn.cursor()
        cur.execute('insert into session (time) values (?)',
                    (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),))
        result = cur.lastrowid
        self.conn.commit()
        return result

    def key_event(self, event, key, velocity, midi_time):
        cur = self.conn.cursor()
        cur.execute('''insert into key_events (eventsession, key, event_type, velocity, midi_time)
                     values (?,?,?,?,?)''',
                    (self.session_id, key, event, velocity, midi_time))
        result = cur.lastrowid
        self.conn.commit()
        return result

# ##############################################################################

def init_db(conn):
    cur = conn.cursor()
    cur.execute('''
    create table session (session_id integer primary key,
                          time text
                          )''')
    cur.execute('''create table key_events (event_id integer primary key,
                                            eventsession integer,
                                            key integer,
                                            event_type integer,
                                            velocity integer,
                                            midi_time integer,
                                            foreign key(eventsession) references session(session_id)
                                            )''')
    conn.commit()
    conn.close()
