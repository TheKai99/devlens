from fastapi import FastAPI


app = FastAPI(title="github analyzer")







@app.get("/")
def begin():
    return{"msg":"lets start"}