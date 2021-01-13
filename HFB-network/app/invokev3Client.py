import os
import asyncio
from hfc.fabric import Client

import hashlib
import base64
import socket

def InvokeClient():

    loop = asyncio.get_event_loop()
    cli = Client(net_profile="../connection-profile/network.json")
    org1_admin = cli.get_user('org1.example.com', 'Admin')
    org2_admin = cli.get_user('org2.example.com', 'Admin')

    # Make the client know there is a channel in the network
    cli.new_channel('modbuschannel')

    # Install Example Chaincode to Peers
    # GOPATH setting is only needed to use the example chaincode inside sdk#
    gopath_bak = os.environ.get('GOPATH', '')
    gopath = os.path.normpath(os.path.join(
        os.path.dirname(os.path.realpath('__file__')),
        '../chaincode'
    ))
    os.environ['GOPATH'] = os.path.abspath(gopath)

    # Invoke a chaincode
    #args = ["client", "Qmeq4hW6k34a5dbpE2vc7FjSX1xmn1tphg2hGrHFGxqk16"]

    host_ip = socket.gethostbyname(socket.gethostname())
    name=host_ip.encode("utf-8")
    arg2=base64.b64encode(hashlib.sha256(name).digest())
    args = ["client", arg2]
    # The response should be true if succeed
    response = loop.run_until_complete(cli.chaincode_invoke(
        requestor=org1_admin,
        channel_name='modbuschannel',
        peers=['peer0.org1.example.com'],
        args=args,
        cc_name='registration_cc_v2',
        transient_map=None,  # optional, for private data
        # for being sure chaincode invocation has been commited in the ledger, default is on tx event
        wait_for_event=True,
        # cc_pattern='^invoked*' # if you want to wait for chaincode event and you have a `stub.SetEvent("invoked", value)` in your chaincode
    ))

# response = loop.run_until_complete(cli.chaincode_invoke(
#   requestor=org1_admin,
#   channel_name='modbuschannel',
#   peers=['peer1.org1.example.com'],
#   args=args,
#   cc_name='registration_cc_v2',
#   transient_map=None,  # optional, for private data
#   # for being sure chaincode invocation has been commited in the ledger, default is on tx event
#   wait_for_event=True,
#   # cc_pattern='^invoked*' # if you want to wait for chaincode event and you have a `stub.SetEvent("invoked", value)` in your chaincode
# ))

# response = loop.run_until_complete(cli.chaincode_invoke(
#   requestor=org2_admin,
#   channel_name='modbuschannel',
#   peers=['peer0.org2.example.com'],
#   args=args,
#   cc_name='registration_cc_v2',
#   transient_map=None,  # optional, for private data
#   # for being sure chaincode invocation has been commited in the ledger, default is on tx event
#   wait_for_event=True,
#   # cc_pattern='^invoked*' # if you want to wait for chaincode event and you have a `stub.SetEvent("invoked", value)` in your chaincode
# ))

# response = loop.run_until_complete(cli.chaincode_invoke(
#   requestor=org2_admin,
#   channel_name='modbuschannel',
#   peers=['peer1.org2.example.com'],
#   args=args,
#   cc_name='registration_cc_v2',
#   transient_map=None,  # optional, for private data
#   # for being sure chaincode invocation has been commited in the ledger, default is on tx event
#   wait_for_event=True,
#   # cc_pattern='^invoked*' # if you want to wait for chaincode event and you have a `stub.SetEvent("invoked", value)` in your chaincode
# ))
