import os
import asyncio
from hfc.fabric import Client
import json

def QueryClient():
    loop = asyncio.get_event_loop()

    cli = Client(net_profile="../connection-profile/network.json")
    org1_admin = cli.get_user('org1.example.com', 'Admin')
    org2_admin = cli.get_user('org2.example.com', 'Admin')

    # Make the client know there is a channel in the network    
    cli.new_channel('modbuschannel')

    # Install Example Chaincode to Peers
    # GOPATH setting is only needed to use the example chaincode inside sdk
    gopath_bak = os.environ.get('GOPATH', '')
    gopath = os.path.normpath(os.path.join(
        os.path.dirname(os.path.realpath('__file__')),
        '../chaincode'
    ))
    os.environ['GOPATH'] = os.path.abspath(gopath)

    # Query a chaincode
    args = ["server"]
    # The response should be true if succeed#
    response = loop.run_until_complete(cli.chaincode_query(
        requestor=org1_admin,
        channel_name='modbuschannel',
        peers=['peer0.org1.example.com'],
        args=args,
        cc_name='registration_cc_v2'
    ))

    response=json.loads(response) 

    return(response)
# Query a chaincode
#args = ['b']
# The response should be true if succeed
# response = loop.run_until_complete(cli.chaincode_query(
#    requestor=org1_admin,
#    channel_name='modbuschannel',
#    peers=['peer1.org1.example.com'],
#    args=args,
#    cc_name='registration_cc_v2'
# ))

# Query a chaincode
#args = ['b']
# The response should be true if succeed
# response = loop.run_until_complete(cli.chaincode_query(
#    requestor=org2_admin,
#    channel_name='modbuschannel',
#    peers=['peer0.org2.example.com'],
#    args=args,
#    cc_name='registration_cc_v2'
# ))

# Query a chaincode
#args = ['b']
# The response should be true if succeed
# response = loop.run_until_complete(cli.chaincode_query(
#    requestor=org2_admin,
#    channel_name='businesschannel',
#    peers=['peer1.org2.example.com'],
#    args=args,
#    cc_name='registration_cc_v2'
# ))
