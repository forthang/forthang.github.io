from fastapi import FastAPI, Depends, HTTPException
  from fastapi.security import OAuth2PasswordBearer
  from fastapi.middleware.cors import CORSMiddleware
  from jose import JWTError, jwt
  from datetime import datetime, timedelta
  from pydantic import BaseModel
  import uvicorn
  import os

  app = FastAPI()

  SECRET_KEY = os.environ.get("SECRET_KEY")
  ALGORITHM = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES = 30

  oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

  # Hardcoded credentials - INSECURE, DO NOT USE IN PRODUCTION!
  CORRECT_USERNAME = os.environ.get("CORRECT_USERNAME")
  CORRECT_PASSWORD = os.environ.get("CORRECT_PASSWORD")

  class LoginRequest(BaseModel):
      username: str
      password: str

  # setting CORS
  origins = [
      "http://localhost:3000",
  ]

  app.add_middleware(
      CORSMiddleware,
      allow_origins=origins,
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )

  def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
      to_encode = data.copy()
      if expires_delta:
          expire = datetime.utcnow() + expires_delta
      else:
          expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

      to_encode.update({"exp": expire})
      encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
      return encoded_jwt

  def verify_token(token: str) -> str:
      try:
          payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
          username: str = payload.get("sub")

          if username is None:
              raise HTTPException(status_code=403, detail="Access forbidden")

          return username

      except JWTError:
          raise HTTPException(status_code=403, detail="Access forbidden")

  @app.post("/api/login/")
  async def login(login_request: LoginRequest) -> dict:
      if login_request.username == CORRECT_USERNAME and login_request.password == CORRECT_PASSWORD:
          access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
          access_token: str = create_access_token(data={"sub": login_request.username}, expires_delta=access_token_expires)
          return {"token": access_token}
      raise HTTPException(status_code=401, detail="Invalid username or password")

  @app.get("/api/protect-area/")
  async def protect_area(token: str = Depends(oauth2_scheme)):
      username = verify_token(token)
      return {"answer": 42}


  if __name__ == '__main__':
      uvicorn.run(app, host="0.0.0.0", port=8000)