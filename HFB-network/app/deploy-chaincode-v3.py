import os
import asyncio
from hfc.fabric import Client

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

print("gopath", gopath)

# The response should be true if succeed
responses = loop.run_until_complete(cli.chaincode_install(
    requestor=org1_admin,
    peers=['peer0.org1.example.com',
           'peer1.org1.example.com'],
    cc_path='github.com/registration_cc_v2',
    cc_name='registration_cc_v2',
    cc_version='v1.0'
))

# The response should be true if succeed
responses = loop.run_until_complete(cli.chaincode_install(
    requestor=org2_admin,
    peers=['peer0.org2.example.com',
           'peer1.org2.example.com'],
    cc_path='github.com/registration_cc_v2',
    cc_name='registration_cc_v2',
    cc_version='v1.0'
))

# Instantiate Chaincode in Channel, the response should be true if succeed
args = ["Qmeq4hW6kK2abdbpE2vc7FjSX1xmn1tphg2hGrHFGxqk16"]

# policy, see https://hyperledger-fabric.readthedocs.io/en/release-1.4/endorsement-policies.html
policy = {
    'identities': [
        {'role': {'name': 'member', 'mspId': 'Org1MSP'}},
    ],
    'policy': {
        '1-of': [
            {'signed-by': 0},
        ]
    }
}
response = loop.run_until_complete(cli.chaincode_instantiate(
    requestor=org1_admin,
    channel_name='modbuschannel',
    peers=['peer0.org1.example.com'],
    args=args,
    cc_name='registration_cc_v2',
    cc_version='v1.0',
    # cc_endorsement_policy=policy,  # optional, but recommended
    collections_config=None,  # optional, for private data policy
    transient_map=None,  # optional, for private data
    wait_for_event=True  # optional, for being sure chaincode is instantiated#
))

print("response", response)

# Query a chaincode, [a]
args = ["client"]
# The response should be true if succeed
response = loop.run_until_complete(cli.chaincode_query(
    requestor=org1_admin,
    channel_name='modbuschannel',
    peers=['peer0.org1.example.com'],
    args=args,
    cc_name='registration_cc_v2'
))

# Query a chaincode
args = ["client"]
# The response should be true if succeed
response = loop.run_until_complete(cli.chaincode_query(
    requestor=org1_admin,
    channel_name='modbuschannel',
    peers=['peer1.org1.example.com'],
    args=args,
    cc_name='registration_cc_v2'
))

# Query a chaincode
args = ["client"]
# The response should be true if succeed
response = loop.run_until_complete(cli.chaincode_query(
    requestor=org2_admin,
    channel_name='modbuschannel',
    peers=['peer0.org2.example.com'],
    args=args,
    cc_name='registration_cc_v2'
))

# Query a chaincode
args = ["client"]
# The response should be true if succeed
response = loop.run_until_complete(cli.chaincode_query(
    requestor=org2_admin,
    channel_name='modbuschannel',
    peers=['peer1.org2.example.com'],
    args=args,
    cc_name='registration_cc_v2'
))
