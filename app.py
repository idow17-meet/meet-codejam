from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.responses import FileResponse
import uvicorn

from backend.api import api


app = FastAPI()
app.include_router(api, prefix='/api')

static_files = StaticFiles(directory='./dist/static')
app.mount('/static', static_files)


@app.get('/{path:path}')
async def serve_static_app(path):
    return FileResponse('./dist/index.html')


if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=5000, reload=True)
