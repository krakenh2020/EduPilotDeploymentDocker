import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import base64

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


step("Test connections", 1)

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



step("Register university DID", 1)

#    method : sidetree
#    header : {"alg":"","kid":"","operation":"create"}

# VDR:  Aries Verifiable Data Registry
# https://github.com/hyperledger/aries-framework-go/blob/main/docs/concepts/00_what_is_hl_aries.md#9-vdr


diddoc = {
    "name": "test6",
    "did": {

      "@context": ["https://w3id.org/did/v1"],
      "id": "did:sidetree:test:test5",
      "verificationMethod": [
        {
          "id": "did:sidetree:test:test5#keys-1",
          "type": "Secp256k1VerificationKey2018",
          "controller": "did:example:123456789abcdefghi",
          "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
        }
      ],
      "authentication": [
        "did:sidetree:test:test5#keys-1",
        {
          "id": "did:example:123456789abcdefghs#key3",
          "type": "RsaVerificationKey2018",
          "controller": "did:example:123456789abcdefghs",
          "publicKeyHex": "02b97c30de767f084ce3080168ee293053ba33b235d7116a3263d29f1450936b71"
        }
      ],
      "service": [
        {
          "id": "did:sidetree:test:test5#inbox",
          "type": "SocialWebInboxService",
          "serviceEndpoint": "https://social.example.com/83hfh37dj",
          "spamCost": {
            "amount": "0.50",
            "currency": "USD"
          }
        },
        {
          "id": "did:sidetree:test:test5#did-communication",
          "type": "did-communication",
          "serviceEndpoint": "https://agent.example.com/",
          "priority" : 0,
          "recipientKeys" : ["did:sidetree:test:test5#key2"],
          "routingKeys" : ["did:sidetree:test:test5#key2"]
        }
      ],
      "created": "2002-10-10T17:00:00Z"
    }
}



step("Register university DID", 1)

r = requests.post(AGENT1 + '/vdr/did', json=diddoc, verify=False)
print('ret: {}'.format(r.text))



step("Get DID", 1)

r = requests.get(AGENT1 + '/vdr/did/did:sidetree:test:test5', verify=False)
print('ret: {}'.format(r.text))



step("Resolve DID", 1)

r = requests.get(AGENT1 + '/vdr/did/resolve/did:sidetree:test:test5', verify=False)
print('ret: {}'.format(r.text))



#r = requests.post(AGENT1 + '/vdr/create-public-did', verify=False)
#print('ret: {}'.format(r.text))










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
