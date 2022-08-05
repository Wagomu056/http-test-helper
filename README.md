# Usage
Start http server with port and callback function.
```
port = 8000
httptesthelper.start_server(port, http_callback)
```
Callback received body as String.
```
def http_callback(requestBody):
    global bodyJson
    bodyJson = json.loads(requestBody)
    print(bodyJson)
```
