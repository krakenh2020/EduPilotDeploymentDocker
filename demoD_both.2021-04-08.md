### Test connections to agents
* connection to university agent works!
* connection to student    agent works!

## University: Create invite

```json
<class 'dict'>
{
    "invitation": {
        "serviceEndpoint": "https://agent.university-agent.demo:8081",
        "recipientKeys": [
            "did:key:z6MkmVrCradV9BqvxrF8J8CphVQpcYjumPn6K7AkVHGNF7SQ"
        ],
        "@id": "45284d2c-a8ab-4631-969c-c7afdb2f752b",
        "label": "university-agent",
        "@type": "https://didcomm.org/didexchange/1.0/invitation"
    },
    "alias": "",
    "invitation_url": ""
}
```


### Student:   Receive invite

```json
<class 'dict'>
{
    "state": "",
    "created_at": "0001-01-01T00:00:00Z",
    "updated_at": "0001-01-01T00:00:00Z",
    "connection_id": "63585758-eba1-4f4e-b949-06c11df99c4b",
    "request_id": "",
    "my_did": ""
}
```

connection ID: 63585758-eba1-4f4e-b949-06c11df99c4b

### Student:   List connections

details last invite agent 2: 
```json
<class 'str'>
{
    "result": {
        "ConnectionID": "63585758-eba1-4f4e-b949-06c11df99c4b",
        "State": "invited",
        "ThreadID": "45284d2c-a8ab-4631-969c-c7afdb2f752b",
        "ParentThreadID": "",
        "TheirLabel": "university-agent",
        "TheirDID": "",
        "MyDID": "",
        "ServiceEndPoint": "https://agent.university-agent.demo:8081",
        "RecipientKeys": [
            "did:key:z6MkmVrCradV9BqvxrF8J8CphVQpcYjumPn6K7AkVHGNF7SQ"
        ],
        "RoutingKeys": null,
        "InvitationID": "45284d2c-a8ab-4631-969c-c7afdb2f752b",
        "InvitationDID": "",
        "Implicit": false,
        "Namespace": "my"
    }
}
```


### Student:   Accept invite

details accept invite at agent 2: 
```json
<class 'str'>
{
    "created_at": "0001-01-01T00:00:00Z",
    "updated_at": "0001-01-01T00:00:00Z",
    "connection_id": "63585758-eba1-4f4e-b949-06c11df99c4b"
}
```


### Student:   List accepted connection

connection agent 2: 
```json
<class 'dict'>
{
    "ConnectionID": "63585758-eba1-4f4e-b949-06c11df99c4b",
    "State": "requested",
    "ThreadID": "45284d2c-a8ab-4631-969c-c7afdb2f752b",
    "ParentThreadID": "",
    "TheirLabel": "university-agent",
    "TheirDID": "",
    "MyDID": "did:peer:1zQmVQ26moGLYUEopCh5SEqekaRf2veJamHbL37WBXvQzVr6",
    "ServiceEndPoint": "https://agent.university-agent.demo:8081",
    "RecipientKeys": [
        "did:key:z6MkmVrCradV9BqvxrF8J8CphVQpcYjumPn6K7AkVHGNF7SQ"
    ],
    "RoutingKeys": null,
    "InvitationID": "45284d2c-a8ab-4631-969c-c7afdb2f752b",
    "InvitationDID": "",
    "Implicit": false,
    "Namespace": "my"
}
```

* MyDID:    did:peer:1zQmVQ26moGLYUEopCh5SEqekaRf2veJamHbL37WBXvQzVr6
* TheirDID: 

## University: List own invite again

connection agent 1: 
```json
<class 'dict'>
{
    "ConnectionID": "eff75f1b-bcaf-47bc-894a-9efa66e3646b",
    "State": "requested",
    "ThreadID": "45284d2c-a8ab-4631-969c-c7afdb2f752b",
    "ParentThreadID": "",
    "TheirLabel": "student-agent",
    "TheirDID": "did:peer:1zQmVQ26moGLYUEopCh5SEqekaRf2veJamHbL37WBXvQzVr6",
    "MyDID": "",
    "ServiceEndPoint": "",
    "RecipientKeys": null,
    "RoutingKeys": null,
    "InvitationID": "45284d2c-a8ab-4631-969c-c7afdb2f752b",
    "InvitationDID": "",
    "Implicit": false,
    "Namespace": "their"
}
```

* MyDID:    
* TheirDID: did:peer:1zQmVQ26moGLYUEopCh5SEqekaRf2veJamHbL37WBXvQzVr6

## University: Get connection states

connection agent 1: state = requested

### Student:   Get connection states

connection agent 2: state = requested

## University: Accept connection request

details accept invite at agent 1: 
```json
<class 'str'>
{
    "their_did": "",
    "request_id": "",
    "connection_id": "eff75f1b-bcaf-47bc-894a-9efa66e3646b",
    "updated_at": "0001-01-01T00:00:00Z",
    "created_at": "0001-01-01T00:00:00Z",
    "state": ""
}
```


## University: Get connection states again

* connection agent 1: state = responded
* MyDID:    did:peer:1zQmZo9r4edMTPUPdviCnwUS3i8zdDQRVUuby7vg4Wd7H9wb
* TheirDID: did:peer:1zQmVQ26moGLYUEopCh5SEqekaRf2veJamHbL37WBXvQzVr6

### Student:   Get connection states again

* connection agent 2: state = completed
* MyDID:    did:peer:1zQmVQ26moGLYUEopCh5SEqekaRf2veJamHbL37WBXvQzVr6
* TheirDID: did:peer:1zQmZo9r4edMTPUPdviCnwUS3i8zdDQRVUuby7vg4Wd7H9wb

## University: Send credential offer

{'piid': '6ab476d8-438d-456c-a075-3e3ff0784274'}

### Student:   Accept credential offer with request

credential offer:
```json
<class 'dict'>
{
    "PIID": "6ab476d8-438d-456c-a075-3e3ff0784274",
    "Msg": {
        "@id": "6ab476d8-438d-456c-a075-3e3ff0784274",
        "@type": "https://didcomm.org/issue-credential/2.0/offer-credential",
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
        },
        "~thread": {
            "thid": "6ab476d8-438d-456c-a075-3e3ff0784274"
        }
    },
    "MyDID": "did:peer:1zQmVQ26moGLYUEopCh5SEqekaRf2veJamHbL37WBXvQzVr6",
    "TheirDID": "did:peer:1zQmZo9r4edMTPUPdviCnwUS3i8zdDQRVUuby7vg4Wd7H9wb"
}
```

--> accept-offer: OK {}

credential offer:
```json
<class 'dict'>
{
    "PIID": "6d5a9209-4aa0-4f5b-b77f-511a668c113f",
    "Msg": {
        "@id": "c0565b01-c71d-40f1-a2cf-c671b0f6c344",
        "@type": "https://didcomm.org/issue-credential/2.0/issue-credential",
        "credentials~attach": [
            {
                "data": {
                    "json": {
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
                }
            }
        ],
        "~thread": {
            "thid": "6d5a9209-4aa0-4f5b-b77f-511a668c113f"
        }
    },
    "MyDID": "did:peer:1zQmfBQethrzJjH9BEJbzwWRFGR2tYtN1y3w77Mha88GfwTz",
    "TheirDID": "did:peer:1zQmNWvoq2wTDRpiK9BbiBV85pXzXfRaLhHi4WpUhnxgKrzZ"
}
```

--> accept-offer: OK {}


## University: Accept credential request, issue cred

--> accept-request 6ab476d8-438d-456c-a075-3e3ff0784274 : OK {}

### Student:   Accept credential

issuecredential actions: {'actions': []}

### Student:   List credentials

```json
<class 'dict'>
{
    "name": "demo-credentials18",
    "id": "http://example.edu/credentials/1874",
    "context": [
        "https://www.w3.org/2018/credentials/v1",
        "https://www.w3.org/2018/credentials/examples/v1"
    ],
    "type": [
        "VerifiableCredential",
        "UniversityDegreeCredential"
    ],
    "my_did": "did:peer:1zQmUbPtJVDbDh38L8kSUQ3wVd3TDi9aKiMzsBRpDR89pU4u",
    "their_did": "did:peer:1zQmVGNAdnsin3A5pLQNvi3WdtnJgpzxLdZgfbMocsGr9CM1"
}
```

```json
<class 'dict'>
{
    "name": "http://example.edu/credentials/1874",
    "id": "http://example.edu/credentials/1874",
    "context": [
        "https://www.w3.org/2018/credentials/v1",
        "https://www.w3.org/2018/credentials/examples/v1"
    ],
    "type": [
        "VerifiableCredential",
        "UniversityDegreeCredential"
    ],
    "my_did": "did:peer:1zQmSDwn35H69ZGG8WAeNKhYc6avVnzu2odDYBeJRbvdLnmp",
    "their_did": "did:peer:1zQmWiH2HSWNMLdHqvEBvXBTKLB49i9f6zBVpicVzYovZdDx"
}
```


### Student:   Print 'demo-credentials18' credential by name

```json
<class 'str'>
{
    "name": "demo-credentials18",
    "id": "http://example.edu/credentials/1874"
}
```


### Student:   Print 'demo-credentials18' credential by id

```json
<class 'str'>
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

