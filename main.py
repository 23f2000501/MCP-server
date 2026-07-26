import os
from hashlib import sha256

from mcp.server.fastmcp import FastMCP, Context

EMAIL = "23f2000501@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP(
    "Exam MCP",
    stateless_http=True,
    json_response=True,
)


@mcp.tool(name="solve_challenge")
async def solve_challenge(ctx: Context) -> str:
    headers = ctx.headers or {}

    challenge = (
        headers.get("x-exam-challenge")
        or headers.get("X-Exam-Challenge")
        or ""
    )

    digest = sha256(
        f"{challenge}:{EMAIL}".encode("utf-8")
    ).hexdigest()[:16]

    return digest


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        path="/mcp",
    )