import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import base64
import json

# https://github.com/hyperledger/aries-framework-go/blob/main/docs/rest/openapi_demo.md#steps-for-didexchange


def step(s, agentId=1):
    print()
    if agentId == 1:
        print('\033[91m\033[1m### {} \033[0m'.format(s))
    else:
        print('\033[95m\033[1m### {} \033[0m'.format(s))
    print()


AGENT1 = 'https://localhost:8082'  # university
AGENT2 = 'https://localhost:8092'  # student


step("Agent 1: Test connections", 1)

try:
    agent1online = agent2online = False
    r = requests.get(AGENT1 + '/connections', verify=False)
    if r.status_code == 200:
        print('connection to agent 1 works!')
        agent1online = True

    r = requests.get(AGENT2 + '/connections', verify=False)
    if r.status_code == 200:
        print('connection to agent 2 works!')
        agent2online = True

    if not agent1online or not agent2online:
        print('agents offline?')
        exit()
except BaseException:
    print('agents offline?')
    exit()


step("Agent 1: Create invite", 1)

invite = requests.post(
    AGENT1 +
    '/connections/create-invitation',
    verify=False).json()
print(invite)
invite = invite['invitation']
inviteIDagent1 = invite['@id']


#input('Press any key to continue ...')
step("Agent 2: receive invite", 2)

connection = requests.post(
    AGENT2 +
    '/connections/receive-invitation',
    json=invite,
    verify=False).json()
print(connection)
connectionIDagent2 = connection['connection_id']
print(connectionIDagent2)


#input('Press any key to continue ...')
#step("Agent 1: List connections")

#details = requests.get(AGENT1 + '/connections', verify=False)
#print('connections agent 1: ' + details.text)

#details = requests.get(AGENT2 + '/connections', verify=False)
#print('connections agent 2: ' + details.text)


step("Agent 2: List connections", 2)

details = requests.get(
    AGENT2 +
    '/connections/' +
    connectionIDagent2,
    verify=False)
print('details last invite agent 2: ' + details.text)


step("Agent 2: Accept invite", 2)

details = requests.post(
    AGENT2 +
    '/connections/' +
    connectionIDagent2 +
    '/accept-invitation',
    verify=False)
print('details accept invite at agent 2: ' + details.text)


step("Agent 2: List accepted connection", 2)

details = requests.get(
    AGENT2 +
    '/connections/' +
    connectionIDagent2,
    verify=False)
print('connection agent 2: ' + str(details.json()['result']))
print('MyDID:    ' + str(details.json()['result']['MyDID']))
print('TheirDID: ' + str(details.json()['result']['TheirDID']))

step("Agent 1: List own invite again", 1)

connections = requests.get(AGENT1 + '/connections', verify=False).json()
for connection in connections['results']:
    if connection['InvitationID'] == inviteIDagent1:
        print('connection agent 1: ' + str(connection))
        connectionIDagent1 = connection['ConnectionID']

        print('MyDID:    ' + str(connection['MyDID']))
        print('TheirDID: ' + str(connection['TheirDID']))


step("Get connection states")

details = requests.get(
    AGENT1 +
    '/connections/' +
    connectionIDagent1,
    verify=False)
print('connection agent 1: state = ' + str(details.json()['result']['State']))

details = requests.get(
    AGENT2 +
    '/connections/' +
    connectionIDagent2,
    verify=False)
print('connection agent 2: state = ' + str(details.json()['result']['State']))


#input('Press any key to continue ...')


step("Agent 1: Accept request", 1)

details = requests.post(
    AGENT1 +
    '/connections/' +
    connectionIDagent1 +
    '/accept-request',
    verify=False)
print('details accept invite at agent 1: ' + details.text)


step("Get connection states again")

details = requests.get(
    AGENT1 +
    '/connections/' +
    connectionIDagent1,
    verify=False)
print('connection agent 1: state = ' + str(details.json()['result']['State']))
print('MyDID:    ' + str(details.json()['result']['MyDID']))
print('TheirDID: ' + str(details.json()['result']['TheirDID']))
DID_AGENT1 = details.json()['result']['MyDID']

details = requests.get(
    AGENT2 +
    '/connections/' +
    connectionIDagent2,
    verify=False)
print('connection agent 2: state = ' + str(details.json()['result']['State']))
print('MyDID:    ' + str(details.json()['result']['MyDID']))
print('TheirDID: ' + str(details.json()['result']['TheirDID']))
DID_AGENT2 = details.json()['result']['MyDID']


# step("Agent 1: send some message to Agent 2", 1)
# TODO: follow
# https://github.com/hyperledger/aries-framework-go/blob/main/docs/rest/openapi_demo.md#steps-for-custom-message-handling

# msg = 'hallo student, agent zwei!'
# r = requests.post(AGENT1 + '/connections/' + connectionIDagent1 + '/send-message', json={'content': msg}, verify=False)
# print(r.text)


# step("Agent 1: register DID", 1)
# TODO: #
# https://github.com/hyperledger/aries-framework-go/blob/main/docs/rest/openapi_demo.md#steps-for-creating-public-did-using-vdr-endpoint


step("Agent 1: send credential offer", 1)
# TODO: issue credential, follow
# https://github.com/hyperledger/aries-framework-go/blob/main/docs/rest/openapi_demo.md#how-to-issue-credentials-through-the-issue-credential-protocol


credoffer = {
    "my_did": DID_AGENT1,
    "their_did": DID_AGENT2,
    "offer_credential": {}
}
r_credoffer = requests.post(
    AGENT1 +
    '/issuecredential/send-offer',
    json=credoffer,
    verify=False).json()
print(r_credoffer)

credoffer_piid = r_credoffer['piid']


step("Agent  2: accept credential offer with request", 2)

r = requests.get(AGENT2 + '/issuecredential/actions', verify=False).json()
#print('issuecredential actions: {}'.format(r))

for offer in r['actions']:
    print('credential offer: ' + str(offer))
    piid = offer['PIID']

    r_credofferaccept = requests.post(
        AGENT2 +
        '/issuecredential/' +
        piid +
        '/accept-offer',
        verify=False).json()
    print(r_credofferaccept)


step("Agent 1: accept credential request, issue cred", 1)


testcred1 = {
    "issue_credential": {
        "credentials~attach": [
            {
                "lastmod_time": "0001-01-01T00:00:00Z",
                "data": {
                    "json": {
                        "@context": [
                            "https://www.w3.org/2018/credentials/v1",
                            "https://www.w3.org/2018/credentials/examples/v1"
                        ],
                        "credentialSubject":{
                            "id": "sample-student-id2"
                        },
                        "id": "https://ssi.tugraz.at/credentials/18",
                        #"id": "at.tugraz.ssi.credentials.10",
                        "issuanceDate": "2021-01-01T19:23:24Z",
                        "issuer": {
                            "id": DID_AGENT1,
                            "name": "Example University"
                        },
                        "referenceNumber": 83294841,
                        "type": [
                            "VerifiableCredential",
                            "UniversityDegreeCredential"
                        ]
                    }
                }
            }
        ]
    }
}

# TODO: Sign cred?

r_credrequest = requests.post(
    AGENT1 +
    '/issuecredential/' +
    credoffer_piid +
    '/accept-request',
    json=testcred1,
    verify=False).json()
print(r_credrequest)


step("Agent  2: accept credential", 2)


r = requests.get(AGENT2 + '/issuecredential/actions', verify=False).json()
#print('issuecredential actions: {}'.format(r))

label = "demo-credentials18"
credlabel = {
    "names": [
        label
    ]
}


for offer in r['actions']:
    print('credential offer: ' + str(offer))
    piid = offer['PIID']

    r_credaccept = requests.post(
        AGENT2 + '/issuecredential/' + piid + '/accept-credential',
        json=credlabel,
        verify=False).json()
    print(r_credaccept)


step("Agent  2: list credentials", 2)


creds = requests.get(AGENT2 + '/verifiable/credentials', verify=False).json()
for cred in creds['result']:
    print(cred)


step("Agent  2: print '" + label + "' credential by name", 2)

c = requests.get(
    AGENT2 +
    '/verifiable/credential/name/' + label,
    verify=False).json()
#print(c)
print(json.dumps(c, indent=4))



step("Agent  2: print '" + label + "' credential by id", 2)

b64id = base64.b64encode(c['id'].encode('ascii')).decode('ascii')
#print(b64id)

c2 = requests.get(
    AGENT2 + '/verifiable/credential/' + b64id,
    verify=False).json()
#print(c2)
print(json.dumps(json.loads(c2['verifiableCredential']), indent=4))


exit()


step("Some more experiments (all on agent 1/university)", 1)

r = requests.get(AGENT1 + '/issuecredential/actions', verify=False)
print('issuecredential actions: {}'.format(r.text))

r = requests.get(AGENT1 + '/mediator/connections', verify=False)
print('mediator connections: {}'.format(r.text))

r = requests.get(AGENT1 + '/message/services', verify=False)
print('message services: {}'.format(r.text))

r = requests.get(AGENT1 + '/outofband/actions', verify=False)
print('outofband actions: {}'.format(r.text))

r = requests.get(AGENT1 + '/presentproof/actions', verify=False)
print('presentproofs: {}'.format(r.text))

r = requests.get(AGENT1 + '/vdr/did/records', verify=False)
print('dids: {}'.format(r.text))

r = requests.get(AGENT1 + '/verifiable/credentials', verify=False)
print('credentials: {}'.format(r.text))

r = requests.get(AGENT1 + '/verifiable/presentations', verify=False)
print('presentations: {}'.format(r.text))
