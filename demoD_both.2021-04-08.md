### Test connections to agents
* connection to university agent works!
* connection to student    agent works!

## University: Create invite

```json
{
    "invitation": {
        "serviceEndpoint": "https://agent.university-agent.demo:8081",
        "recipientKeys": [
            "did:key:z6Mkm5hbK52JfbKWTWkndTie3xj19Ys23rR9rM7Nq4DFstai"
        ],
        "@id": "2e4d4461-411c-41f0-b5ce-2fe3ad8e6e9f",
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
    "connection_id": "d7c5eab4-88fc-42e7-9cba-9365c340b38d",
    "request_id": "",
    "my_did": ""
}
```

connection ID: d7c5eab4-88fc-42e7-9cba-9365c340b38d

### Student:   List connections

details last invite agent 2: 
```json
{
    "result": {
        "ConnectionID": "d7c5eab4-88fc-42e7-9cba-9365c340b38d",
        "State": "invited",
        "ThreadID": "2e4d4461-411c-41f0-b5ce-2fe3ad8e6e9f",
        "ParentThreadID": "",
        "TheirLabel": "university-agent",
        "TheirDID": "",
        "MyDID": "",
        "ServiceEndPoint": "https://agent.university-agent.demo:8081",
        "RecipientKeys": [
            "did:key:z6Mkm5hbK52JfbKWTWkndTie3xj19Ys23rR9rM7Nq4DFstai"
        ],
        "RoutingKeys": null,
        "InvitationID": "2e4d4461-411c-41f0-b5ce-2fe3ad8e6e9f",
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
    "connection_id": "d7c5eab4-88fc-42e7-9cba-9365c340b38d"
}
```


### Student:   List accepted connection

connection agent 2: 
```json
{
    "ConnectionID": "d7c5eab4-88fc-42e7-9cba-9365c340b38d",
    "State": "requested",
    "ThreadID": "2e4d4461-411c-41f0-b5ce-2fe3ad8e6e9f",
    "ParentThreadID": "",
    "TheirLabel": "university-agent",
    "TheirDID": "",
    "MyDID": "did:peer:1zQmPKjEcve7hxGWom8PLCSBw5FgAuMXJjQYXXMw7MVXCR5r",
    "ServiceEndPoint": "https://agent.university-agent.demo:8081",
    "RecipientKeys": [
        "did:key:z6Mkm5hbK52JfbKWTWkndTie3xj19Ys23rR9rM7Nq4DFstai"
    ],
    "RoutingKeys": null,
    "InvitationID": "2e4d4461-411c-41f0-b5ce-2fe3ad8e6e9f",
    "InvitationDID": "",
    "Implicit": false,
    "Namespace": "my"
}
```

* MyDID:    did:peer:1zQmPKjEcve7hxGWom8PLCSBw5FgAuMXJjQYXXMw7MVXCR5r
* TheirDID: 

## University: List own invite again

connection agent 1: 
```json
{
    "ConnectionID": "34aed231-c950-4588-bf8e-8e6038e4779c",
    "State": "requested",
    "ThreadID": "2e4d4461-411c-41f0-b5ce-2fe3ad8e6e9f",
    "ParentThreadID": "",
    "TheirLabel": "student-agent",
    "TheirDID": "did:peer:1zQmPKjEcve7hxGWom8PLCSBw5FgAuMXJjQYXXMw7MVXCR5r",
    "MyDID": "",
    "ServiceEndPoint": "",
    "RecipientKeys": null,
    "RoutingKeys": null,
    "InvitationID": "2e4d4461-411c-41f0-b5ce-2fe3ad8e6e9f",
    "InvitationDID": "",
    "Implicit": false,
    "Namespace": "their"
}
```

* MyDID:    
* TheirDID: did:peer:1zQmPKjEcve7hxGWom8PLCSBw5FgAuMXJjQYXXMw7MVXCR5r

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
    "connection_id": "34aed231-c950-4588-bf8e-8e6038e4779c",
    "updated_at": "0001-01-01T00:00:00Z",
    "created_at": "0001-01-01T00:00:00Z",
    "state": ""
}
```


## University: Get connection states again

* connection agent 1: state = responded
* MyDID:    did:peer:1zQmVUG2y5pcv2FGPoZz9knFuNKeuZGjH9qnvmcQLziw375G
* TheirDID: did:peer:1zQmPKjEcve7hxGWom8PLCSBw5FgAuMXJjQYXXMw7MVXCR5r

### Student:   Get connection states again

* connection agent 2: state = completed
* MyDID:    did:peer:1zQmPKjEcve7hxGWom8PLCSBw5FgAuMXJjQYXXMw7MVXCR5r
* TheirDID: did:peer:1zQmVUG2y5pcv2FGPoZz9knFuNKeuZGjH9qnvmcQLziw375G

## University: Send credential offer

{'piid': 'beb767cb-cab2-457f-892f-9c5351dc17de'}

### Student:   Accept credential offer with request

credential offer:
```json
{
    "PIID": "6ab476d8-438d-456c-a075-3e3ff0784274",
    "Msg": {
        "@id": "b120297b-7d8d-43c1-adcd-05f7b06c754d",
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
{
    "PIID": "beb767cb-cab2-457f-892f-9c5351dc17de",
    "Msg": {
        "@id": "beb767cb-cab2-457f-892f-9c5351dc17de",
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
            "thid": "beb767cb-cab2-457f-892f-9c5351dc17de"
        }
    },
    "MyDID": "did:peer:1zQmPKjEcve7hxGWom8PLCSBw5FgAuMXJjQYXXMw7MVXCR5r",
    "TheirDID": "did:peer:1zQmVUG2y5pcv2FGPoZz9knFuNKeuZGjH9qnvmcQLziw375G"
}
```

--> accept-offer: OK {}


## University: Accept credential request, issue cred

--> accept-request beb767cb-cab2-457f-892f-9c5351dc17de : OK {}

### Student:   Accept credential

issuecredential actions: {'actions': []}

### Student:   List credentials

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

