#!/usr/bin/env python3
# collect status of ICMP Ping via IP address of OS (not via SourceIP).
#
# Usage: fping <target> <packets> <interval> <size> <timeout> <source_ip>
#
# Copyright (C) 2022 Cybertrust Japan Co., Ltd. All rights reserved.
#
import sys
import os
import re
import shlex
import socket
import string
import subprocess
from netaddr.ip import IPAddress
import logging

log_file = '/var/log/zabbix/fping.log'
logging.basicConfig(
    level = logging.DEBUG,
    filename = log_file,
    format = "%(asctime)s %(levelname)s %(message)s")

exec_cmd = '/usr/sbin/fping'

def printUsage():
    print('Usage: %s <target> <packets> <interval> <size> <timeout> <source_ip>' % (argv[0]))
    print('  target: should be set {HOST.IP}')
    print('  interval, timeout: milliscconds (default 500)')
    print('  defaults of all parameters are same as fping')

def check_addr(given_addr):
    try:
        chk_addr = IPAddress(given_addr)
    except Exception:
        return False
    else:
        if chk_addr.version == 4:
           return True
        else:
           return False

def check_number(given_str):
    if re.match('^[0-9]*$',given_str):
        return True
    else:
        return False

if __name__ == '__main__':
    os.environ['LANG'] = 'C'
    argv = sys.argv
    argc = len(argv)
    logging.debug('argv: ' + str(argv))
    logging.debug('argc: ' + str(argc))

    # initialize internal params
    target = ''
    packets = ''
    interval = ''
    size = ''
    timeout = ''
    source_ip = ''
    ret_val = ''

    if argc < 2 or argc > 7:
        logging.debug('wrong number of params')
        printUsage()
        sys.exit(1)

    if check_addr(sys.argv[1]) == False:
        logging.debug('wrong value for target argv[1]')
        sys.exit(1)
    else:
        target = sys.argv[1]

    if argc > 3:
        for i in range (2, argc):
            logging.debug('i: '+ str(i))
            logging.debug('sys.argv['+ str(i) + ']: ' + sys.argv[i])
            if i == 6:
                break
            else:
                if len(sys.argv[i]) > 0 and check_number(sys.argv[i]) == False:
                    logging.debug('wrong value for argv[' + str(i) + ']')
                    sys.exit(1)
                else:
                    if len(sys.argv[i]) > 0:
                        if i == 2:
                            packets = sys.argv[2]
                        if i == 3:
                            interval = sys.argv[3]
                        if i == 4:
                            size = sys.argv[4]
                        if i == 5:
                            timeout = sys.argv[5]

    if argc == 7 and len(sys.argv[6]) > 0 and check_addr(sys.argv[6]) == False:
        logging.debug('wrong value for sys.argv[6]')
        sys.exit(1)
    elif argc == 7 and len(sys.argv[6]):
        source_ip = sys.argv[6]


    cmd_str = exec_cmd + ' -q '
    if len(packets) > 0:
        cmd_str = cmd_str + ' -c ' + str(packets)
    if len(interval) > 0:
        cmd_str = cmd_str + ' -i ' + str(interval)
    if len(size) > 0:
        cmd_str = cmd_str + ' -b ' + str(size)
    if len(timeout) > 0:
        cmd_str = cmd_str + ' -t ' + str(timeout)
    if len(source_ip) > 0:
        cmd_str = cmd_str + ' -S ' + str(source_ip)
    cmd_str = cmd_str + ' ' + target

    try:
        logging.debug('cmd_str: ' + cmd_str)

        p = subprocess.Popen(shlex.split(cmd_str),
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=False)

        exit_stat = p.wait()

    except OSError:
        logging.error('execution failed: ' + cmd_str)
        printUsage()
        sys.exit(1)

    # target address sent ack fping got it, exit status will be 0
    if exit_stat == 0:
        ret_val = 1
    else:
        ret_val = 0

    if check_number(str(ret_val)):
        print(ret_val)
    else:
        sys.exit(1)

