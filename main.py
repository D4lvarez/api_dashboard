from fastapi import FastAPI

from shared.libs import lifespan

app = FastAPI(lifespan=lifespan)
