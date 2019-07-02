<img src="https://www.sipgatedesign.com/wp-content/uploads/wort-bildmarke_positiv_2x.jpg" alt="sipgate logo" title="sipgate" align="right" height="112" width="200"/>

# sipgate.io Python incoming call example
This example demonstrates how to receive and process webhooks from [sipgate.io](https://developer.sipgate.io/).

For further information regarding the push functionalities of sipgate.io please visit https://developer.sipgate.io/push-api/api-reference/

- [Prerequisites](#Prerequisites)
- [Enabling sipgate.io for your sipgate account](#Enabling-sipgateio-for-your-sipgate-account)
- [How sipgate.io webhooks work](#How-sipgateio-webhooks-work)
- [Configure webhooks for sipgate.io](#Configure-webhooks-for-sipgateio)
- [Making your computer accessible from the internet](#Making-your-computer-accessible-from-the-internet)
- [Get the code example:](#Get-the-code-example)
- [Install dependencies:](#Install-dependencies)
- [Execution](#Execution)
- [How It Works](#How-It-Works)
- [Common Issues](#Common-Issues)
- [Related](#Related)
- [Contact Us](#Contact-Us)
- [License](#License)
- [External Libraries](#External-Libraries)


## Prerequisites
- python3
- pip3


## Enabling sipgate.io for your sipgate account
In order to use sipgate.io, you need to book the corresponding package in your sipgate account. The most basic package is the free **sipgate.io S** package.

If you use [sipgate basic](https://app.sipgatebasic.de/feature-store) or [simquadrat](https://app.simquadrat.de/feature-store) you can book packages in your product's feature store.
If you are a _sipgate team_ user logged in with an admin account you can find the option under **Account Administration**&nbsp;>&nbsp;**Plans & Packages**.


## How sipgate.io webhooks work

### What is a webhook?
A webhook is a POST request that sipgate.io makes to a predefined URL when a certain event occurs.
These requests contain information about the event that occurred in `application/x-www-form-urlencoded` format.

This is an example payload converted from `application/x-www-form-urlencoded` to JSON:
```json
{
  "event": "newCall",
  "direction": "in",
  "from": "492111234567",
  "to": "4915791234567",
  "callId":"12345678",
  "origCallId":"12345678",
  "user": [ "Alice" ],
  "xcid": "123abc456def789",
  "diversion": "1a2b3d4e5f"
}
```


### sipgate.io webhook events
sipgate.io offers webhooks for the following events:

- **newCall:** is triggered when a new incoming or outgoing call occurs 
- **onAnswer:** is triggered when a call is answered – either by a person or an automatic voicemail
- **onHangup:** is triggered when a call is hung up
- **dtmf:** is triggered when a user makes an entry of digits during a call

**Note:** Per default sipgate.io only sends webhooks for **newCall** events.
To subscribe to other event types you can reply to webhooks with XML responses.
These responses include the event type you would like to receive webhooks for as well as the URL they should be directed to.
You can find more information about the XML response here:
https://developer.sipgate.io/push-api/api-reference/#the-xml-response


## Configure webhooks for sipgate.io 
You can configure webhooks for sipgate.io as follows:

1. Navigate to [console.sipgate.com](https://console.sipgate.com/) and login with your sipgate account credentials.
2. Select the **Webhooks**&nbsp;>&nbsp;**URLs** tab in the left side menu
3. Click the gear icon of the **Incoming** or **Outgoing** entry
4. Fill in your webhook URL and click save. **Note:** your webhook URL has to be accessible from the internet. (See the section [Making your computer accessible from the internet](#making-your-computer-accessible-from-the-internet)) 
5. In the **sources** section you can select what phonelines and groups should trigger webhooks.


## Making your computer accessible from the internet
There are many possibilities to obtain an externally accessible address for your computer.
In this example, we use the service [serveo.net](serveo.net) which sets up a reverse ssh tunnel that forwards traffic from a public URL to your localhost.
The following command creates the specified subdomain at serveo.net and sets up a tunnel between the public port 80 on their server and your localhost:8080:

```bash
$ ssh -R [subdomain].serveo.net:80:localhost:8080 serveo.net
```

If you run this example on a server which can already be reached from the internet, you do not need the forwarding.
In that case, the webhook URL needs to be adjusted accordingly.

## Get the code example:
Clone Repository with HTTPS
```bash
git clone https://github.com/sipgate-io/sipgateio-incomingcall-python.git
```

Clone Repository with SSH
```bash
git clone git@github.com/sipgate-io/sipgateio-incomingcall-python.git
```

Navigate to the project's root directory.


## Install dependencies:
Please run the following command:
```bash
$ pip3 install -r requirements.txt
```

## Execution
Run the application:
```bash
python -m incoming_call 
```

## How It Works

In the `__main__.py`, which is a starting point of the application, we import the `server` module from our file `server.py` on the same directory.
It contains a _Flask_ application called `app`, which is started by calling its `run()` method with the desired port `8080`.  
```python
import incoming_call.server as server

if __name__ == "__main__":
    server.app.run(port=8080)
```
The application's behavior is defined in the `server.py` script.

At first, we import the necessary libraries, _Flask_ for starting the server and _json_ for transforming the request data:
```python
import flask
import json
```

We then create an HTTP server using the _Flask_ framework:
```python
app = flask.Flask(__name__)
```

Afterwards, we specify a route that handles incoming POST requests with the function `receive_new_call()`.
It returns an empty string and the corresponding HTTP status code `204` indicating that there is no content:
```python
@app.route('/', methods=["POST"])
def receive_new_call():
    ...
    return '', 204
```

Within the `receive_new_call()` function, we extract the `application/x-www-form-urlencoded` data from the request as a dictionary. In the next step, we format this dictionary into more readable JSON data.
We then print that data to the console.

```python
...
    request_data = flask.request.form.to_dict()
    json_data = json.dumps(request_data, indent=2)
    print(json_data)
...
```


## Common Issues

### web app displays "Feature sipgate.io not booked."
Possible reasons are:
- the sipgate.io feature is not booked for your account

See the section [Enabling sipgate.io for your sipgate account](#enabling-sipgateio-for-your-sipgate-account) for instruction on how to book sipgate.io


### "OSError: [Errno 98] Address already in use"
Possible reasons are:
- another instance of the application is already running
- the specified port is in use by another application


### "PermissionError: [Errno 13] Permission denied"
Possible reasons are:
- you do not have permission to bind to the specified port.
  This usually occurs if you try to use port 80, 443 or another well-known port which can only be bound with superuser privileges


### Call happened but no webhook was received 
Possible reasons are:
- the configured webhook URL is incorrect
- the SSH tunnel connection broke
- webhooks are not enabled for the phoneline that received the call


## Related
- [Flask](http://flask.pocoo.org/)


## Contact Us
Please let us know how we can improve this example.
If you have a specific feature request or found a bug, please use **Issues** or fork this repository and send a **pull request** with your improvements.


## License
This project is licensed under **The Unlicense** (see [LICENSE file](./LICENSE)).


## External Libraries
This code uses the following external libraries

- _Flask_:
  - Licensed under the [BSD License](http://flask.pocoo.org/docs/1.0/license/)
  - Website: http://flask.pocoo.org//


---

[sipgate.io](https://www.sipgate.io) | [@sipgateio](https://twitter.com/sipgateio) | [API-doc](https://api.sipgate.com/v2/doc)