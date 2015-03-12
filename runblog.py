#! /usr/bin/env python


import os
import sys
import re
from tempfile import TemporaryFile
import subprocess
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
RAILS_SERVER = os.path.join(os.environ['HOME'], 'RoR', 'blog')
#BLOGAPP = os.path.join(ROOT, 'blog_util', 'server.py')

def run_tests(args):
    start_blog_application()
    time.sleep(5)
    os.environ['PO_VAR_FILE'] = os.path.join(ROOT, 'vars.py')
    subprocess.call(['pybot'] + args, shell=(os.sep == '\\'))
    stop_blog_application()

def start_blog_application():
    #subprocess.Popen(['python', BLOGAPP, '--start', '/home/victor/RoR/blog'], stdout=TemporaryFile(), stderr=subprocess.STDOUT)
    subprocess.Popen(['rails', 'server'], cwd=RAILS_SERVER, stdout=TemporaryFile(), stderr=subprocess.STDOUT)


def stop_blog_application():
    #subprocess.call(['python', BLOGAPP, '--stop'], stdout=TemporaryFile(), stderr=subprocess.STDOUT)
    output = subprocess.check_output(['ps', '-ef'], stderr=subprocess.STDOUT)
    match = re.search(r'(\w+)(\s+)(\d+)(\s+)(.+)\sbin/rails', output)
    if match:
        print "Stopping server..."
        pid = match.group(3)
        result = subprocess.call(['kill', '-9', pid])
        if result:
            print "Error stopping the server!"
        else:
            print "Server stopped successfully"


def print_help():
    print __doc__

def print_usage():
    print 'Usage: rundemo.py [options] datasource'
    print '   or: rundemo.py blogapp start|stop'
    print '   or: rundemo.py help'


if __name__ == '__main__':
    action = {'blogapp-start': start_blog_application,
              'blogapp-stop': stop_blog_application,
              'help': print_help,
              '': print_usage}.get('-'.join(sys.argv[1:]))
    if action:
        action()
    else:
        run_tests(sys.argv[1:])
