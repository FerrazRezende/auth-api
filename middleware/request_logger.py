from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from settings import setup_logger




# logger instance
logger = setup_logger()

# This class is responsible for logging the requests that arrive at the api and saving them in files according to the level of the log
class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            headers_str = ('             \n             '
                           .join([f"{key}: {value}" for key, value in request.headers.items()]))

            headers_scope = request.scope['headers']
            headers_scope_str = ('             \n             '
                                 .join([f"{key.decode()}: {value.decode()}" for key, value in headers_scope]))

            request.state.__setattr__("state", "received")

            # Log de nível INFO
            logger.info(f"""
                |-------------------------|
                |      Request scope      | 
                |-------------------------|

                Type: {request.scope['type']}
                ASGI Version: {request.scope['asgi']['version']}
                Spec Version: {request.scope['asgi']['spec_version']}
                HTTP Version: {request.scope['http_version']}
                ServerIP: {request.scope['server'][0]}
                ServerPort: {request.scope['server'][1]}
                ClientIP: {request.scope['client'][0]}
                ClientPort: {request.scope['client'][1]}
                Scheme: {request.scope['scheme']}
                Method: {request.scope['method']}
                Path: {request.scope['path']}
                Raw Path: {request.scope['raw_path']}


                |------------------------|
                |      Scope Headers     | 
                |------------------------|
                {headers_scope_str}


            """)

            logger.info(f"""
                Request url: {request.url}\n
                Request base_url: {request.base_url}\n
                Request query params: {request.query_params}\n
                Request path params: {request.path_params}\n
                Request cookies: {request.cookies}\n
                Request client: {request.client}\n
                Request session: {request.session}\n

                Request state: {request.state.__getattr__('state')}\n
                Request methods: {request.method}\n

                |------------------|
                |      Headers     | 
                |------------------|
                {headers_str}
            """)

            response = await call_next(request)
            return response

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise
