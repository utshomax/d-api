from typing import Union
from infer import make_prediction
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict")
def read_message(message : Union[str, None] = None):
    listmessage = filter(lambda x: x != '',message.split(','))
    listmessage = [x.strip() for x in listmessage]
    symps = dict(zip(listmessage, [1]*len(listmessage)))
    res = list(make_prediction(symps))
    print(res)
    #return symps
    jsonres = jsonable_encoder(res)
    return JSONResponse(content={"pred":jsonres})