import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import base64
import json

# https://github.com/hyperledger/aries-framework-go/blob/main/docs/rest/openapi_demo.md#steps-for-didexchange


# def step(s, agentId=1):
#     print()
#     if agentId == 1:
#         print('\033[91m\033[1m### University: {} \033[0m'.format(s))
#     else:
#         print('\033[95m\033[1m### Student:    {} \033[0m'.format(s))
#     print()


def step(s, agentId=1):
    print()
    if agentId == 1:
        print('## University: {}'.format(s))
    else:
        print('### Student:   {}'.format(s))
    print()


def printJSON(d):
    print('```json')
    if isinstance(d, dict):
    	print(json.dumps(d, indent=4))
    elif isinstance(d, str):
    	print(json.dumps(json.loads(d), indent=4))
    else:
    	print(d)
    print('```')
    print()


AGENT1 = 'https://localhost:8082'  # university
AGENT2 = 'http://localhost:8092'  # student


print('### Test connections to agents')

try:
    agent1online = agent2online = False
    r = requests.get(AGENT1 + '/connections', verify=False)
    if r.status_code == 200:
        print('* connection to university agent works!')
        agent1online = True
    else:
        print('* university agent offline?')

    r = requests.get(AGENT2 + '/connections', verify=False)
    if r.status_code == 200:
        print('* connection to student    agent works!')
        agent2online = True
    else:
        print('* student    agent offline?')

    if not agent1online or not agent2online:
        exit()
except BaseException:
    print('* **agents offline?**')
    exit()




step("Create invite", 1)

invite = requests.post(
    AGENT1 +
    '/connections/create-invitation',
    verify=False).json()
printJSON(invite)
invite = invite['invitation']
inviteIDagent1 = invite['@id']




#input('Press any key to continue ...')
step("Receive invite", 2)

connection = requests.post(
    AGENT2 +
    '/connections/receive-invitation',
    json=invite,
    verify=False).json()
printJSON(connection)

connectionIDagent2 = connection['connection_id']
print('connection ID:', connectionIDagent2)


#input('Press any key to continue ...')
#step("Agent 1: List connections")

#details = requests.get(AGENT1 + '/connections', verify=False)
#print('connections agent 1: ' + details.text)

#details = requests.get(AGENT2 + '/connections', verify=False)
#print('connections agent 2: ' + details.text)




step("List connections", 2)

details = requests.get(
    AGENT2 +
    '/connections/' +
    connectionIDagent2,
    verify=False)
print('details last invite agent 2: ')
printJSON(details.text)




step("Accept invite", 2)

details = requests.post(
    AGENT2 +
    '/connections/' +
    connectionIDagent2 +
    '/accept-invitation',
    verify=False)
print('details accept invite at agent 2: ')
printJSON(details.text)




step("List accepted connection", 2)

details = requests.get(
    AGENT2 +
    '/connections/' +
    connectionIDagent2,
    verify=False)
print('connection agent 2: ')
printJSON(details.json()['result'])

print('* MyDID:    ' + str(details.json()['result']['MyDID']))
print('* TheirDID: ' + str(details.json()['result']['TheirDID']))




step("List own invite again", 1)

connections = requests.get(AGENT1 + '/connections', verify=False).json()
for connection in connections['results']:
    if connection['InvitationID'] == inviteIDagent1:
        print('connection agent 1: ')
        printJSON(connection)
        connectionIDagent1 = connection['ConnectionID']

        print('* MyDID:    ' + str(connection['MyDID']))
        print('* TheirDID: ' + str(connection['TheirDID']))




step("Get connection states", 1)

details = requests.get(
    AGENT1 +
    '/connections/' +
    connectionIDagent1,
    verify=False)
print('connection agent 1: state = ' + str(details.json()['result']['State']))


step("Get connection states", 2)

details = requests.get(
    AGENT2 +
    '/connections/' +
    connectionIDagent2,
    verify=False)
print('connection agent 2: state = ' + str(details.json()['result']['State']))




#input('Press any key to continue ...')




step("Accept connection request", 1)

details = requests.post(
    AGENT1 +
    '/connections/' +
    connectionIDagent1 +
    '/accept-request',
    verify=False)
print('details accept invite at agent 1: ')
printJSON(details.text)




step("Get connection states again", 1)

details = requests.get(
    AGENT1 +
    '/connections/' +
    connectionIDagent1,
    verify=False)
print('* connection agent 1: state = ' + str(details.json()['result']['State']))
print('* MyDID:    ' + str(details.json()['result']['MyDID']))
print('* TheirDID: ' + str(details.json()['result']['TheirDID']))
DID_AGENT1 = details.json()['result']['MyDID']




step("Get connection states again", 2)

details = requests.get(
    AGENT2 +
    '/connections/' +
    connectionIDagent2,
    verify=False)
print('* connection agent 2: state = ' + str(details.json()['result']['State']))
print('* MyDID:    ' + str(details.json()['result']['MyDID']))
print('* TheirDID: ' + str(details.json()['result']['TheirDID']))
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


step("Send credential offer", 1)
# TODO: issue credential, follow
# https://github.com/hyperledger/aries-framework-go/blob/main/docs/rest/openapi_demo.md#how-to-issue-credentials-through-the-issue-credential-protocol


# credoffer = {
#     "my_did": DID_AGENT1,
#     "their_did": DID_AGENT2,
#     "offer_credential": {}
# }

credoffer = {
    "my_did": DID_AGENT1,
    "their_did": DID_AGENT2,
    "offer_credential": {
      "@type": "VerifiableCredential",
      "credential_preview": {
        "@type": "VerifiableCredential",
        "attributes": [
          {
            "mime-type": "string",
            "name": "first_name",
            "value": "Your first name"
          },
          {
            "mime-type": "string",
            "name": "given_name",
            "value": "Your given name"
          }
        ]
      }
    }
  }


r_credoffer = requests.post(
    AGENT1 +
    '/issuecredential/send-offer',
    json=credoffer,
    verify=False).json()
printJSON(r_credoffer)

credoffer_piid = r_credoffer['piid']





step("Accept credential offer with request", 2)

def getOK(r):
    return 'OK' if r.status_code == requests.codes.ok else 'ERROR {}'.format(r.status_code)



r = requests.get(AGENT2 + '/issuecredential/actions', verify=False).json()
#print('issuecredential actions: {}'.format(r))

for offer in r['actions']:
    print('credential offer:')
    printJSON(offer)
    piid = offer['PIID']

    r_credofferaccept = requests.post(
        AGENT2 +
        '/issuecredential/' +
        piid +
        '/accept-offer',
        verify=False)
    print('--> accept-offer:', getOK(r_credofferaccept), r_credofferaccept.json())
    print()




step("Accept credential request, issue cred", 1)


# testcred1 = {
#     "issue_credential": {
#         "credentials~attach": [
#             {
#                 "lastmod_time": "0001-01-01T00:00:00Z",
#                 "data": {
#                     "json": {
#                         "@context": [
#                             "https://www.w3.org/2018/credentials/v1",
#                             "https://www.w3.org/2018/credentials/examples/v1"
#                         ],
#                         "credentialSubject":{
#                             "id": "sample-student-id2"
#                         },
#                         "id": "https://ssi.tugraz.at/credentials/18",
#                         #"id": "at.tugraz.ssi.credentials.10",
#                         "issuanceDate": "2021-01-01T19:23:24Z",
#                         "issuer": {
#                             "id": DID_AGENT1,
#                             "name": "Example University"
#                         },
#                         "referenceNumber": 83294841,
#                         "type": [
#                             "VerifiableCredential",
#                             "UniversityDegreeCredential"
#                         ]
#                     }
#                 }
#             }
#         ]
#     }
# }

testcred1 = {
    "issue_credential":{
        "credentials~attach":[
          {
             "data":{
                "json":{
                   "@context":[
                      "https://www.w3.org/2018/credentials/v1",
                      "https://www.w3.org/2018/credentials/examples/v1"
                   ],
                   "id":"http://example.edu/credentials/1874",
                   "type":[
                        "VerifiableCredential",
                        "UniversityDegreeCredential"
                    ],
                   "credentialSubject":{
                      "first_name":"Alice",
                      "given_name":"Doe"
                   },
                   "issuanceDate":"2010-01-01T19:23:24Z",
                   "issuer":{
                      "id":"did:uni:76e12ec712ebc6f1c221ebfeb1f",
                      "name":"Example University"
                   }
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
    verify=False)
print('--> accept-request', credoffer_piid, ':', getOK(r_credrequest), r_credrequest.json())





step("Accept credential", 2)


r = requests.get(AGENT2 + '/issuecredential/actions', verify=False).json()
print('issuecredential actions: {}'.format(r))

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
        verify=False)
    print(r_credaccept.status_code, r_credaccept.json())






step("List credentials", 2)


creds = requests.get(AGENT2 + '/verifiable/credentials', verify=False).json()
#print(creds)
for cred in creds['result']:
    printJSON(cred)


step("Print '" + label + "' credential by name", 2)

c = requests.get(
    AGENT2 +
    '/verifiable/credential/name/' + label,
    verify=False).json()
#print(c)
printJSON(json.dumps(c, indent=4))



step("Print '" + label + "' credential by id", 2)

b64id = base64.b64encode(c['id'].encode('ascii')).decode('ascii')
#print(b64id)

c2 = requests.get(
    AGENT2 + '/verifiable/credential/' + b64id,
    verify=False).json()
#print(c2)
printJSON(json.dumps(json.loads(c2['verifiableCredential']), indent=4))

