### Test connections to agents
* connection to university agent works!
* connection to student    agent works!

## University: Create invite

```json
{'invitation': {'serviceEndpoint': 'https://agent.university-agent.demo:8081', 'recipientKeys': ['did:key:z6MkrpmbcZitQqCzBLBZeprDZ4mogwfHPXJktaDRfwHaXHqx'], '@id': 'cc1874b9-1d86-493b-bda2-11dfe28d5826', 'label': 'university-agent', '@type': 'https://didcomm.org/didexchange/1.0/invitation'}, 'alias': '', 'invitation_url': ''}
```


### Student:   Receive invite

```json
{'state': '', 'created_at': '0001-01-01T00:00:00Z', 'updated_at': '0001-01-01T00:00:00Z', 'connection_id': 'e37fbd49-34b3-4012-bf63-e1eb49c9d637', 'request_id': '', 'my_did': ''}
```

connection ID: e37fbd49-34b3-4012-bf63-e1eb49c9d637

### Student:   List connections

details last invite agent 2: 
```json
{"result":{"ConnectionID":"e37fbd49-34b3-4012-bf63-e1eb49c9d637","State":"invited","ThreadID":"cc1874b9-1d86-493b-bda2-11dfe28d5826","ParentThreadID":"","TheirLabel":"university-agent","TheirDID":"","MyDID":"","ServiceEndPoint":"https://agent.university-agent.demo:8081","RecipientKeys":["did:key:z6MkrpmbcZitQqCzBLBZeprDZ4mogwfHPXJktaDRfwHaXHqx"],"RoutingKeys":null,"InvitationID":"cc1874b9-1d86-493b-bda2-11dfe28d5826","InvitationDID":"","Implicit":false,"Namespace":"my"}}

```


### Student:   Accept invite

details accept invite at agent 2: 
```json
{"created_at":"0001-01-01T00:00:00Z","updated_at":"0001-01-01T00:00:00Z","connection_id":"e37fbd49-34b3-4012-bf63-e1eb49c9d637"}

```


### Student:   List accepted connection

connection agent 2: 
```json
{'ConnectionID': 'e37fbd49-34b3-4012-bf63-e1eb49c9d637', 'State': 'requested', 'ThreadID': 'cc1874b9-1d86-493b-bda2-11dfe28d5826', 'ParentThreadID': '', 'TheirLabel': 'university-agent', 'TheirDID': '', 'MyDID': 'did:peer:1zQmcxJEkpBfjDoSSDw9QG9xBqNVrfJ3PJDL8sZ4S9hj8J18', 'ServiceEndPoint': 'https://agent.university-agent.demo:8081', 'RecipientKeys': ['did:key:z6MkrpmbcZitQqCzBLBZeprDZ4mogwfHPXJktaDRfwHaXHqx'], 'RoutingKeys': None, 'InvitationID': 'cc1874b9-1d86-493b-bda2-11dfe28d5826', 'InvitationDID': '', 'Implicit': False, 'Namespace': 'my'}
```

* MyDID:    did:peer:1zQmcxJEkpBfjDoSSDw9QG9xBqNVrfJ3PJDL8sZ4S9hj8J18
* TheirDID: 

## University: List own invite again

connection agent 1: 
```json
{'ConnectionID': '8ec2b17f-6c55-4447-b7a9-6a0a36a03eeb', 'State': 'requested', 'ThreadID': 'cc1874b9-1d86-493b-bda2-11dfe28d5826', 'ParentThreadID': '', 'TheirLabel': 'student-agent', 'TheirDID': 'did:peer:1zQmcxJEkpBfjDoSSDw9QG9xBqNVrfJ3PJDL8sZ4S9hj8J18', 'MyDID': '', 'ServiceEndPoint': '', 'RecipientKeys': None, 'RoutingKeys': None, 'InvitationID': 'cc1874b9-1d86-493b-bda2-11dfe28d5826', 'InvitationDID': '', 'Implicit': False, 'Namespace': 'their'}
```

* MyDID:    
* TheirDID: did:peer:1zQmcxJEkpBfjDoSSDw9QG9xBqNVrfJ3PJDL8sZ4S9hj8J18

## University: Get connection states

connection agent 1: state = requested

### Student:   Get connection states

connection agent 2: state = requested

## University: Accept connection request

details accept invite at agent 1: 
```json
{"their_did":"","request_id":"","connection_id":"8ec2b17f-6c55-4447-b7a9-6a0a36a03eeb","updated_at":"0001-01-01T00:00:00Z","created_at":"0001-01-01T00:00:00Z","state":""}

```


## University: Get connection states again

* connection agent 1: state = responded
* MyDID:    did:peer:1zQmYZoTDg6JRE8JKwXA94KGWYpWzHPdzci1Z4xZgvt9Rjms
* TheirDID: did:peer:1zQmcxJEkpBfjDoSSDw9QG9xBqNVrfJ3PJDL8sZ4S9hj8J18

### Student:   Get connection states again

* connection agent 2: state = completed
* MyDID:    did:peer:1zQmcxJEkpBfjDoSSDw9QG9xBqNVrfJ3PJDL8sZ4S9hj8J18
* TheirDID: did:peer:1zQmYZoTDg6JRE8JKwXA94KGWYpWzHPdzci1Z4xZgvt9Rjms

## University: Send credential offer

{'piid': 'b9248984-9dda-46d2-b69b-ed576636261c'}

### Student:   Accept credential offer with request

credential offer:
```json
{'PIID': '1808351b-a95b-48d3-8299-5605c5b552b6', 'Msg': {'@id': 'd4614577-94c5-4c75-85d2-3b08709161c5', '@type': 'https://didcomm.org/issue-credential/2.0/issue-credential', 'credentials~attach': [{'data': {'json': {'@context': ['https://www.w3.org/2018/credentials/v1', 'https://www.w3.org/2018/credentials/examples/v1'], 'credentialSubject': {'first_name': 'Alice', 'given_name': 'Doe'}, 'id': 'http://example.edu/credentials/1874', 'issuanceDate': '2010-01-01T19:23:24Z', 'issuer': {'id': 'did:uni:76e12ec712ebc6f1c221ebfeb1f', 'name': 'Example University'}, 'type': ['VerifiableCredential', 'UniversityDegreeCredential']}}}], '~thread': {'thid': '1808351b-a95b-48d3-8299-5605c5b552b6'}}, 'MyDID': 'did:peer:1zQmSb9v2tZCE73dvjJY1XcpMR2yjVE75ybrmFXEJyHS9LkR', 'TheirDID': 'did:peer:1zQmZjHGKnNSi5jSP28RRYV1VnjdfjKmMqByHAj3dMAFYy87'}
```

--> accept-offer: OK {}

credential offer:
```json
{'PIID': 'b9248984-9dda-46d2-b69b-ed576636261c', 'Msg': {'@id': 'b9248984-9dda-46d2-b69b-ed576636261c', '@type': 'https://didcomm.org/issue-credential/2.0/offer-credential', 'credential_preview': {'@type': 'VerifiableCredential', 'attributes': [{'mime-type': 'string', 'name': 'first_name', 'value': 'Your first name'}, {'mime-type': 'string', 'name': 'given_name', 'value': 'Your given name'}]}, '~thread': {'thid': 'b9248984-9dda-46d2-b69b-ed576636261c'}}, 'MyDID': 'did:peer:1zQmcxJEkpBfjDoSSDw9QG9xBqNVrfJ3PJDL8sZ4S9hj8J18', 'TheirDID': 'did:peer:1zQmYZoTDg6JRE8JKwXA94KGWYpWzHPdzci1Z4xZgvt9Rjms'}
```

--> accept-offer: OK {}


## University: Accept credential request, issue cred

--> accept-request b9248984-9dda-46d2-b69b-ed576636261c : OK {}

### Student:   Accept credential

issuecredential actions: {'actions': []}

### Student:   List credentials

```json
{'name': 'demo-credentials18', 'id': 'http://example.edu/credentials/1874', 'context': ['https://www.w3.org/2018/credentials/v1', 'https://www.w3.org/2018/credentials/examples/v1'], 'type': ['VerifiableCredential', 'UniversityDegreeCredential'], 'my_did': 'did:peer:1zQmUbPtJVDbDh38L8kSUQ3wVd3TDi9aKiMzsBRpDR89pU4u', 'their_did': 'did:peer:1zQmVGNAdnsin3A5pLQNvi3WdtnJgpzxLdZgfbMocsGr9CM1'}
```

```json
{'name': 'http://example.edu/credentials/1874', 'id': 'http://example.edu/credentials/1874', 'context': ['https://www.w3.org/2018/credentials/v1', 'https://www.w3.org/2018/credentials/examples/v1'], 'type': ['VerifiableCredential', 'UniversityDegreeCredential'], 'my_did': 'did:peer:1zQmSDwn35H69ZGG8WAeNKhYc6avVnzu2odDYBeJRbvdLnmp', 'their_did': 'did:peer:1zQmWiH2HSWNMLdHqvEBvXBTKLB49i9f6zBVpicVzYovZdDx'}
```


### Student:   Print 'demo-credentials18' credential by name

```json
{
    "name": "demo-credentials18",
    "id": "http://example.edu/credentials/1874"
}
```


### Student:   Print 'demo-credentials18' credential by id

```json
{
    "@context": [
        "https://www.w3.org/2018/credentials/v1",
        "https://www.w3.org/2018/credentials/examples/v1"
    ],
    "credentialSubject": {
        "first_name": "Alice",
        "given_name": "Doe"
    },
    "id": "http://example.edu/credentials/1874",
    "issuanceDate": "2010-01-01T19:23:24Z",
    "issuer": {
        "id": "did:uni:76e12ec712ebc6f1c221ebfeb1f",
        "name": "Example University"
    },
    "type": [
        "VerifiableCredential",
        "UniversityDegreeCredential"
    ]
}
```

