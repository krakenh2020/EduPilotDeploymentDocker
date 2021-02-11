#!/bin/sh


set -e

echo "Generating KRAKEN EduPilot demo PKI"

mkdir -p ./keys/tls

tmp=$(mktemp)
echo "subjectKeyIdentifier=hash
authorityKeyIdentifier = keyid,issuer
extendedKeyUsage = serverAuth
keyUsage = Digital Signature, Key Encipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = localhost
DNS.2 = agent.university-agent.demo
DNS.3 = openapi.university-agent.demo
DNS.4 = agent.student-agent.demo
DNS.5 = webhook.university-agent.demo
DNS.6 = webhook.student-agent.demo
DNS.7 = kms.demo" >> "$tmp"

#create CA
openssl ecparam -name prime256v1 -genkey -noout -out ./keys/tls/ec-cakey.pem
openssl req -new -x509 -key ./keys/tls/ec-cakey.pem -subj "/C=CA/ST=ON/O=Example KRAKEN Edu CA Inc.:CA Sec/OU=CA Sec" -out ./keys/tls/ec-cacert.pem

#create TLS creds
openssl ecparam -name prime256v1 -genkey -noout -out ./keys/tls/ec-key.pem
openssl req -new -key ./keys/tls/ec-key.pem -subj "/C=CA/ST=ON/O=KRAKEN Inc.:VC4SM/OU=Edu/CN=*.demo" -out ./keys/tls/ec-key.csr
openssl x509 -req -in ./keys/tls/ec-key.csr -CA ./keys/tls/ec-cacert.pem -CAkey ./keys/tls/ec-cakey.pem -CAcreateserial -extfile "$tmp" -out ./keys/tls/ec-pubCert.pem -days 365

#create master key for secret lock
openssl rand 32 | base64 | sed 's/+/-/g; s/\//_/g' > ./keys/tls/secret-lock.key

echo "done generating VC4SM demo PKI"
