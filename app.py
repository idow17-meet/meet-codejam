from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
import uvicorn

from backend.api import api


app = FastAPI()
app.include_router(api, prefix='/api')

static_files = StaticFiles(directory='./dist/static')
html_index = StaticFiles(directory='./dist', html=True)
app.mount('/static', static_files)
app.mount('/', html_index)


if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=5000, reload=True, debug=True)
