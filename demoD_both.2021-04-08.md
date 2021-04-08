### Test connections to agents
* connection to university agent works!
* connection to student    agent works!

## University: Create invite

```json
{
    "invitation": {
        "serviceEndpoint": "https://agent.university-agent.demo:8081",
        "recipientKeys": [
            "did:key:z6Mkw38zvkXGvTuPiTzgAnbzTe5ZfxBnWsnMjAYLsmVWLMj1"
        ],
        "@id": "ced30989-8a9d-4c58-9d52-c258f6d73bb2",
        "label": "university-agent",
        "@type": "https://didcomm.org/didexchange/1.0/invitation"
    },
    "alias": "",
    "invitation_url": ""
}
```


### Student:   Receive invite

```json
{
    "state": "",
    "created_at": "0001-01-01T00:00:00Z",
    "updated_at": "0001-01-01T00:00:00Z",
    "connection_id": "ba44ee4b-9093-498d-ae9f-199ecaa34365",
    "request_id": "",
    "my_did": ""
}
```

connection ID: ba44ee4b-9093-498d-ae9f-199ecaa34365

### Student:   List connections

details last invite agent 2: 
```json
{
    "result": {
        "ConnectionID": "ba44ee4b-9093-498d-ae9f-199ecaa34365",
        "State": "invited",
        "ThreadID": "ced30989-8a9d-4c58-9d52-c258f6d73bb2",
        "ParentThreadID": "",
        "TheirLabel": "university-agent",
        "TheirDID": "",
        "MyDID": "",
        "ServiceEndPoint": "https://agent.university-agent.demo:8081",
        "RecipientKeys": [
            "did:key:z6Mkw38zvkXGvTuPiTzgAnbzTe5ZfxBnWsnMjAYLsmVWLMj1"
        ],
        "RoutingKeys": null,
        "InvitationID": "ced30989-8a9d-4c58-9d52-c258f6d73bb2",
        "InvitationDID": "",
        "Implicit": false,
        "Namespace": "my"
    }
}
```


### Student:   Accept invite

details accept invite at agent 2: 
```json
{
    "created_at": "0001-01-01T00:00:00Z",
    "updated_at": "0001-01-01T00:00:00Z",
    "connection_id": "ba44ee4b-9093-498d-ae9f-199ecaa34365"
}
```


### Student:   List accepted connection

connection agent 2: 
```json
{
    "ConnectionID": "ba44ee4b-9093-498d-ae9f-199ecaa34365",
    "State": "requested",
    "ThreadID": "ced30989-8a9d-4c58-9d52-c258f6d73bb2",
    "ParentThreadID": "",
    "TheirLabel": "university-agent",
    "TheirDID": "",
    "MyDID": "did:peer:1zQmehU3f6YKUNdshV8AdinxEE1a4L8zqoMwf6srCceJv3xt",
    "ServiceEndPoint": "https://agent.university-agent.demo:8081",
    "RecipientKeys": [
        "did:key:z6Mkw38zvkXGvTuPiTzgAnbzTe5ZfxBnWsnMjAYLsmVWLMj1"
    ],
    "RoutingKeys": null,
    "InvitationID": "ced30989-8a9d-4c58-9d52-c258f6d73bb2",
    "InvitationDID": "",
    "Implicit": false,
    "Namespace": "my"
}
```

* MyDID:    did:peer:1zQmehU3f6YKUNdshV8AdinxEE1a4L8zqoMwf6srCceJv3xt
* TheirDID: 

## University: List own invite again

connection agent 1: 
```json
{
    "ConnectionID": "5863b19b-4c6f-41a4-9a5e-ec1596a37af5",
    "State": "requested",
    "ThreadID": "ced30989-8a9d-4c58-9d52-c258f6d73bb2",
    "ParentThreadID": "",
    "TheirLabel": "student-agent",
    "TheirDID": "did:peer:1zQmehU3f6YKUNdshV8AdinxEE1a4L8zqoMwf6srCceJv3xt",
    "MyDID": "",
    "ServiceEndPoint": "",
    "RecipientKeys": null,
    "RoutingKeys": null,
    "InvitationID": "ced30989-8a9d-4c58-9d52-c258f6d73bb2",
    "InvitationDID": "",
    "Implicit": false,
    "Namespace": "their"
}
```

* MyDID:    
* TheirDID: did:peer:1zQmehU3f6YKUNdshV8AdinxEE1a4L8zqoMwf6srCceJv3xt

## University: Get connection states

connection agent 1: state = requested

### Student:   Get connection states

connection agent 2: state = requested

## University: Accept connection request

details accept invite at agent 1: 
```json
{
    "their_did": "",
    "request_id": "",
    "connection_id": "5863b19b-4c6f-41a4-9a5e-ec1596a37af5",
    "updated_at": "0001-01-01T00:00:00Z",
    "created_at": "0001-01-01T00:00:00Z",
    "state": ""
}
```


## University: Get connection states again

* connection agent 1: state = responded
* MyDID:    did:peer:1zQmP51LZPrS3GrLsf3pKRaXu5aR37fVjwBo7BmNm96iQMSC
* TheirDID: did:peer:1zQmehU3f6YKUNdshV8AdinxEE1a4L8zqoMwf6srCceJv3xt

### Student:   Get connection states again

* connection agent 2: state = completed
* MyDID:    did:peer:1zQmehU3f6YKUNdshV8AdinxEE1a4L8zqoMwf6srCceJv3xt
* TheirDID: did:peer:1zQmP51LZPrS3GrLsf3pKRaXu5aR37fVjwBo7BmNm96iQMSC

## University: Send credential offer

```json
{
    "piid": "54e17867-4329-4118-84d6-17c4823c999a"
}
```


### Student:   Accept credential offer with request

credential offer:
```json
{
    "PIID": "54e17867-4329-4118-84d6-17c4823c999a",
    "Msg": {
        "@id": "54e17867-4329-4118-84d6-17c4823c999a",
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
            "thid": "54e17867-4329-4118-84d6-17c4823c999a"
        }
    },
    "MyDID": "did:peer:1zQmehU3f6YKUNdshV8AdinxEE1a4L8zqoMwf6srCceJv3xt",
    "TheirDID": "did:peer:1zQmP51LZPrS3GrLsf3pKRaXu5aR37fVjwBo7BmNm96iQMSC"
}
```

--> accept-offer: OK {}

credential offer:
```json
{
    "PIID": "beb767cb-cab2-457f-892f-9c5351dc17de",
    "Msg": {
        "@id": "97d6c8d3-baf6-4b8c-a8f6-7735dad87666",
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
            "thid": "beb767cb-cab2-457f-892f-9c5351dc17de"
        }
    },
    "MyDID": "did:peer:1zQmPKjEcve7hxGWom8PLCSBw5FgAuMXJjQYXXMw7MVXCR5r",
    "TheirDID": "did:peer:1zQmVUG2y5pcv2FGPoZz9knFuNKeuZGjH9qnvmcQLziw375G"
}
```

--> accept-offer: OK {}


## University: Accept credential request, issue cred

--> accept-request 54e17867-4329-4118-84d6-17c4823c999a : OK {}

### Student:   Accept credential

issuecredential actions: {'actions': []}

### Student:   List credentials

```json
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

```json
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

