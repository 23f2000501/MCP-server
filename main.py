import os
from hashlib import sha256

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

EMAIL = "23f2000501@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("Exam MCP")


@mcp.tool
async def solve_challenge() -> str:
    headers = get_http_headers()
    challenge = headers.get("x-exam-challenge", "")

    return sha256(
        f"{challenge}:{EMAIL}".encode("utf-8")
    ).hexdigest()[:16]


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
    )