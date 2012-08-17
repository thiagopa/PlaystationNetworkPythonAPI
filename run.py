#!/usr/bin/env python

## Data is persisted in a sqlite database in the current directory
DB = 'storage.sqlite3'

## Wrapper class for friends
class Friend:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    @property
    def status(self):
        import datetime
        if not self.last_online:
            return 'Offline'

        state = 'Online' if self.online else 'Offline'

        diff = datetime.datetime.now() - datetime.datetime.fromtimestamp(self.last_online)
        periods = (
            (diff.days, "day", "days"),
            (diff.seconds / 3600, "hour", "hours"),
            (diff.seconds / 60, "minute", "minutes"),
            (diff.seconds, "second", "seconds"),
        )
        for period, singular, plural in periods:
            if period:
                return "%s for %d %s" % (state, period, singular if period == 1 else plural)
        return state


def update(email, passwd, proxy=None):
    import time
    import network
    import sqlite3

    connection = sqlite3.connect(DB)
    cursor = connection.cursor()

    ## Double check that DB is set up
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS friends (
            handle TEXT PRIMARY KEY,
            online INTEGER,
            playing TEXT,
            avatar TEXT,
            last_online NUMERIC
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vars (
            key TEXT PRIMARY KEY,
            val TEXT
        )
    """)


    print 'Updating...'
    print 'Logging in %s...' % email

    p = network.PSN(email=email, passwd=passwd, proxy=proxy)
    try:
        handles = cursor.execute("SELECT val FROM vars WHERE  key='handles'").fetchone()[0]
        handles = handles.split(',')
    except TypeError:
        handles = []
    handles.append(p.handle)
    handles = ','.join(list(set(handles)))
    cursor.execute("INSERT OR REPLACE INTO vars (key, val) VALUES ('handles', ?)", (handles,))
    cursor.execute("INSERT OR REPLACE INTO vars (key, val) VALUES ('handle', ?)", (p.handle,))

    for friend in p.friends:
        print 'Updating status for %s...' % friend.handle

        try:
            prev_timestamp, prev_online = cursor.execute("SELECT last_online, online FROM friends WHERE handle=?", (friend.handle,)).fetchone()
        except:
            prev_timestamp = None
            prev_online = False

        # last_online time is only updated with a change in online status.
        # This allows us to compute time since online vs. time offline
        if friend.online != prev_online or prev_timestamp is None:
            cursor.execute("INSERT OR REPLACE INTO friends (handle, online, playing, avatar, last_online) VALUES (?, ?, ?, ?, ?)",
                (friend.handle, friend.online, friend.playing, friend.avatar, time.time()))
        else:
            cursor.execute("INSERT OR REPLACE INTO friends (handle, online, playing, avatar, last_online) VALUES (?, ?, ?, ?, ?)",
                (friend.handle, friend.online, friend.playing, friend.avatar, prev_timestamp))


    cursor.execute("INSERT OR REPLACE INTO vars (key, val) VALUES ('last_update', ?)", (unicode(time.time()),))

    connection.commit()
    cursor.close()
    connection.close()
    print 'Done'

def render(outfile):
    import codecs
    import datetime
    from jinja2 import Environment, FileSystemLoader
    import os
    import sqlite3

    connection = sqlite3.connect(DB)
    cursor = connection.cursor()

    try:
        handles = cursor.execute("SELECT val FROM vars WHERE key='handles'").fetchone()[0]
        handle = cursor.execute("SELECT val FROM vars WHERE key='handle'").fetchone()[0]
    except:
        raise RuntimeError('Statuses have not been updated, please run update')

    friends = cursor.execute("SELECT * FROM friends")
    labels = [i[0] for i in friends.description]
    friends = [Friend(**dict(zip(labels, i))) for i in friends.fetchall()]

    updated = cursor.execute("SELECT val FROM vars WHERE key='last_update'").fetchone()[0]
    updated = datetime.datetime.fromtimestamp(float(updated)).strftime('%A, %B %d, %Y at %I:%M %p')

    connection.commit()
    cursor.close()
    connection.close()

    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__) ,'templates')))
    template = env.get_template('index.html')
    rendered = template.render(handle=handle, handles=handles, friends=friends, updated=updated)

    with codecs.open(outfile, 'w', 'UTF-8') as out:
        out.write(rendered)

    print 'Rendered to %s' % outfile


def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-r', '--render', action='store', dest='file', help='Render template to FILE')
    parser.add_option('-u', '--update', action='store_true', dest='update', help='Update friendlist from PSN')
    parser.add_option('-c', '--credentials', action='store', dest='credentials', help='PSN login credentials in the form email@example.com:password123,email1@example.com:password2,...')
    parser.add_option('-p', '--proxy', action='store', dest='proxy', help='HTTP proxy in the form of host:port. Eg. localhost:9050 for Tor running on localhost port 9050')

    (options, args) = parser.parse_args()
    if options.update:
        if not options.credentials:
            raise RuntimeError('Credentials are required for update')
        accounts = options.credentials.split(',')
        for account in accounts:
            email, passwd = account.strip().split(':', 1)
            update(email, passwd, options.proxy)
    if options.file:
        render(options.file)

if __name__ == '__main__':
    main()
