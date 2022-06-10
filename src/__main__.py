from multiprocessing import freeze_support

import uvicorn

from accountr.settings import settings

if __name__ == '__main__':
    uvicorn.run(
        'accountr.app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
    freeze_support()
