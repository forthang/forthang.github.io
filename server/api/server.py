from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
from renderSindle import render_single
import uvicorn

app = FastAPI()

SECRET_KEY = "my_cool_secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#imitation of db
fake_users_db = {
    "admin": {
        "username": "admin",
        "full_name": "Admin User",
        "hashed_password": "admin", #need to add hashing
    }
}


class LoginRequest(BaseModel):
    username: str
    password: str

class BuildingData(BaseModel):
    BuildingName: str
    address: str
    info: str
    color: str
    img: str
    html: str


# setting CORS
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], #allow all methods
    allow_headers=["*"], #allow all headers
)
# creating unique token for access admin panel and allow for 30min
#  * @param {data} dictionary with name and password from  request
#  * @param {expires_delta} expires time delta which counting with data time
#  * @returns {str} Returns the encoded jwt str
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt



#  validate token and throw exception if wrong
#  * @param {token} token stringify
#  * @returns {str} Returns the username as str
def verify_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=403, detail="Access forbidden")

        return username

    except JWTError:
        raise HTTPException(status_code=403, detail="Access forbidden")




# async function for post login. Compare request data and db data. If success returns token. else throw exception
#  * @param {login_request} login request LoginRequest.username str LoginRequest.password str
#  * @returns {str} returns access_token json formatted like dict
@app.post("/api/login/")
async def login(login_request: LoginRequest) -> dict:
    user:dict = fake_users_db.get(login_request.username)

    if user and user["hashed_password"] == login_request.password:
        access_token_expires:timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token: str = create_access_token(data={"sub": login_request.username}, expires_delta=access_token_expires)
        return {"token": access_token}

    raise HTTPException(status_code=401, detail="Invalid username or password")


@app.post("/api/draw-building/")
async def draw_building_endpoint(building_data: BuildingData):
    if render_single(building_data):
        return {"response": building_data.BuildingName}

    raise HTTPException(status_code=500, detail="Failed to draw building")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
