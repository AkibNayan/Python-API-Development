async def app(scope, receive, send):
    assert scope["type"] == "http"
    
    try:
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text-plain"]
            ]
        })
        
        await send({
            "type": "http.response.body",
            "body": b"<div><h1>Hello Akib</h1><h2>What's going on?</h2></div>"
        })
        
    except:
        print("Failed to create server!")