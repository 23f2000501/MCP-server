import os
from hashlib import sha256

from fastmcp import FastMCP
from starlette.requests import Request

EMAIL = "23f2000501@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("Exam MCP")


@mcp.tool
async def solve_challenge(request: Request) -> str:
    challenge = request.headers.get("X-Exam-Challenge", "")

    return sha256(
        f"{challenge}:{EMAIL}".encode()
    ).hexdigest()[:16]


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
    )