from typing import Union

import uvicorn
from asgiref import ASGIApplication
from libs.uvicornx.settings import Settings


def run(
    app: Union[ASGIApplication, str],
    s: Settings,
):
    uvicorn.run(
        app,
        host=s.host,
        port=s.port,
        reload=s.reload,
        log_level=s.log_level,
    )
