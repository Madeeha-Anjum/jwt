# Company package
# check to make sure a specific header is passes in the request

from fastapi import Header, HTTPException

# Header(...) mean no default is specified so it is required
async def get_token_header(internal_token: str = Header(...)):
    print(internal_token)
    if internal_token != "internal":
        raise HTTPException(status_code=418, detail="Internal Token header is invalid")
