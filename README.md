= Python API Wrapper Documentation
:toc:
Matthew1471 <https://github.com/matthew1471[@Matthew1471]>;

// Document Settings:

// Set the ID Prefix and ID Separators to be consistent with GitHub so links work irrespective of rendering platform. (https://docs.asciidoctor.org/asciidoc/latest/sections/id-prefix-and-separator/)
:idprefix:
:idseparator: -

// Any code examples will be in Python by default.
:source-language: python

ifndef::env-github[:icons: font]

// Set the admonitions to have icons (Github Emojis) if rendered on GitHub (https://blog.mrhaki.com/2016/06/awesome-asciidoctor-using-admonition.html).
ifdef::env-github[]
:status:
:caution-caption: :fire:
:important-caption: :exclamation:
:note-caption: :paperclip:
:tip-caption: :bulb:
:warning-caption: :warning:
endif::[]

// Document Variables:
:release-version: 1.0
:url-org: https://github.com/Matthew1471
:url-repo: {url-org}/Enphase-API
:url-contributors: {url-repo}/graphs/contributors

== Introduction

This unofficial API wrapper written in Python allows your applications to call the APIs and access information.

More general details on the project are available from the xref:../../../README.adoc[project's homepage].

== Getting Started

=== Dependencies

The wrapper uses 2 main third-party libraries. These can be installed by typing into your terminal:

[source,bash]
----
pip install PyJWT
pip install requests
----

=== Project Structure

The main wrapper lives in the `src\enphase_api` folder and the files in the `examples` directory are example scripts to show how to use the library. The examples are written to be fairly feature complete and considered fairly production ready, so they can be used as applications in their own right.

For configuration, each example refers to one of the two credentials files in the folder `configuration`; to make the examples work you will need to edit either `credentials_token.json` or `credentials.json` (depending on the file referenced in the example) to include your Enphase(R) credentials.

Some examples use `credentials.json` as they are then able to repeatedly request a token to communicate with your IQ Gateway on their own, others are programmed to be run on embedded devices such as a Raspberry Pi where you may not wish to store your Enphase(R) username and password.

WARNING: A token behaves like a time limited version of your username and password and so reasonable effort should be taken to protect any obtained tokens as they will have access to your account and device.

Some of the examples either put or get messages from an https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol[Advanced Message Queuing Protocol (AMQP)] server/broker, this is because the IQ Gateway is not designed for a large number of requests, so it is better to query the data once and then make it available for other consuming clients via a message queue rather than have multiple scripts repeatedly query the same data. A free, open source and recommended AMQP server that runs on a variety of platforms is https://www.rabbitmq.com/download.html[RabbitMQ(R)]

=== Sample Code

To obtain a token you can use the Authentication class:

[source]
----
# All the shared Enphase® functions are in these packages.
from enphase_api.cloud.authentication import Authentication

# Connection Variables.
ENPHASE_USERNAME = 'barry@example.com'
ENPHASE_PASSWORD = 'mySecretPassW0rd!'
IQ_GATEWAY_SERIAL_NUMBER = '123456'

# Authenticate with Enphase®'s authentication server and get a token.
authentication = Authentication()
authentication.authenticate(ENPHASE_USERNAME, ENPHASE_PASSWORD)
token = authentication.get_token_for_commissioned_gateway(IQ_GATEWAY_SERIAL_NUMBER)
print(token)
----

Assuming your username and password is correct and you have permission to obtain a token for that IQ Gateway serial number, the authentication server (Entrez) should grant you a https://en.wikipedia.org/wiki/JSON_Web_Token[JWT (JSON Web Token)]. A JWT is basically a time-limited password where the issuer can be securely verified.

To reduce the load placed on the authentication server, you should store the JWT token in a file and then retrieve it for future sessions. Tokens created from a system owner username and password expire 1 year after issue, installers typically only have tokens valid for 12 hours (as they typically will only need access during installation or maintenance).

To make a call to the IQ Gateway you can simply run code similar to the following:

[source]
----
# All the shared Enphase® functions are in these packages.
from enphase_api.local.gateway import Gateway

# Connection Variables.
IQ_GATEWAY_HOST = 'https://192.168.0.100'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dnZWRJbkFzIjoiYWRtaW4iLCJpYXQiOjE0MjI3Nzk2Mzh9.gzSraSYS8EXBxLN_oWnFSRgCzcmJmMjLiuyu5CSpyHI'

# Connect locally to the IQ Gateway, login and request production details.
gateway = Gateway(IQ_GATEWAY_HOST)
if gateway.login(TOKEN):
    response = gateway.api_call('/production.json')
    print(response)
----

Note how the script connected to the IQ Gateway via HTTPS but yet did not protest about an invalid certificate? It is far better security practice to store the trusted certificate and then ensure all future sessions rely on that specific certificate:

[source]
----
# All the shared Enphase® functions are in these packages.
from enphase_api.local.gateway import Gateway

Gateway.trust_gateway('https://192.168.0.100')
----

This will download the certificate from the IQ Gateway and create a `configuration/gateway.cer` file (the path can be over-ridden with the optional parameter `cert_file`).
The next time a request is made the IQ Gateway connection will be validated against this stored certificate (if you have over-ridden the path you will also have to over-ride your `Gateway(` command to include your over-ridden `cert_file`, otherwise the certificate will not be used).

The gateway has its own mechanism for checking the validity of JWT values, however there is also a static `check_token_valid()` function inside the Authentication module that will allow you to check token validity before bothering the IQ Gateway with a request.

It is highly recommended you look at the examples in a text-editor to learn more about the features of the library (and to see how this flow is typically implemented).

The IQ Gateway API endpoints are documented in the xref:../../IQ Gateway API/README.adoc[IQ Gateway API Documentation].

== Examples

[cols="1,1,1,1,1,2", options="header"]
|===
|Filename
|Config File
|Dependencies
|Source Data
|Output Data
|Description

|link:../../../Python/examples/amqp_database_meters.py[`amqp_database_meters.py`]
|`credentials_token.json`
|`mysql.connector` and `pika`
|AMQP
|MySQL(R)/MariaDB(R)
|Consumes meter messages from AMQP and stores it in a MySQL(R)/MariaDB(R) database (schema is in the resources folder).

|link:../../../Python/examples/amqp_unicorn_hat_hd.py[`amqp_unicorn_hat_hd.py`]
|`credentials_token.json`
|`pika` and `unicornhathd`
|AMQP
|https://shop.pimoroni.com/products/unicorn-hat-hd[Unicorn HAT HD]
|Consumes meter messages from AMQP and displays production and consumption data on a https://shop.pimoroni.com/products/unicorn-hat-hd[Unicorn HAT HD] running on a https://www.raspberrypi.com/products/[Raspberry Pi].

|link:../../../Python/examples/database_pyplot_meters.py[`database_pyplot_meters.py`]
|None
|`mysql.connector` and `matplotlib`
|MySQL(R)/MariaDB(R)
|PyPlot
|Displays meter production and consumption databased data in a chart using PyPlot.

|link:../../../Python/examples/gateway_amqp_meters.py[`gateway_amqp_meters.py`]
|`credentials_token.json`
|`pika`
|IQ Gateway
|AMQP
|Obtains meter information and publishes it to AMQP for consumption and statistics in other systems.

|link:../../../Python/examples/gateway_console.py[`gateway_console.py`]
|`credentials.json`
|None
|IQ Gateway
|Console
|Displays production data on the console/terminal then exits. Will attempt to refresh any expired tokens.

|link:../../../Python/examples/gateway_database_meters.py[`gateway_database_meters.py`]
|`credentials_token.json`
|`mysql.connector`
|IQ Gateway
|MySQL(R)/MariaDB(R)
|Obtains meter information and stores it in a MySQL(R)/MariaDB(R) database (schema is in the resources folder).

|link:../../../Python/examples/gateway_generate_docs.py[`gateway_generate_docs.py`]
|`credentials.json`
|None
|IQ Gateway
|Documentation Files
|This is a project resource to semi-automatically generate the documentation files. Will attempt to refresh any expired tokens.

|link:../../../Python/examples/gateway_pyplot_meters.py[`gateway_pyplot_meters.py`]
|`credentials_token.json`
|`matplotlib`
|IQ Gateway
|PyPlot
|Displays production and consumption data in a chart using PyPlot.

|link:../../../Python/examples/gateway_unicorn_hat_hd.py[`gateway_unicorn_hat_hd.py`]
|`credentials_token.json`
|`pillow` and `unicornhathd`
|IQ Gateway
|https://shop.pimoroni.com/products/unicorn-hat-hd[Unicorn HAT HD]
|Displays production and consumption data on a https://shop.pimoroni.com/products/unicorn-hat-hd[Unicorn HAT HD] running on a https://www.raspberrypi.com/products/[Raspberry Pi].

|===
