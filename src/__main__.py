"""
This file will be run when the src module gets executed.
@Created by its-haze
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="src.api.main:app",
        log_level="info",
        port=8080,
        host="0.0.0.0",
    )  # type: ignore
