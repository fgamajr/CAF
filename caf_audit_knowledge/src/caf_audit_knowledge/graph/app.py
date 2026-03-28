from __future__ import annotations

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from caf_audit_knowledge.graph.schema import schema


def create_app() -> FastAPI:
    app = FastAPI(title="CAF Audit Knowledge")
    app.include_router(GraphQLRouter(schema), prefix="/graphql")

    @app.get("/healthz")
    def healthz() -> dict[str, str]:
        return {"status": "ok"}

    return app
