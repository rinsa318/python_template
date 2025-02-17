ARG PYTHON_VERSION=3.12.9
FROM python:${PYTHON_VERSION}-slim-bookworm

# install uv
COPY --from=ghcr.io/astral-sh/uv:0.5.29 /uv /uvx /bin/

# Change the working directory to the ${DEPLOY_TARGET} directory
ARG DEPLOY_TARGET=/app/
WORKDIR ${DEPLOY_TARGET}

# Install dependencies
ARG UV_PROJECT_ENVIRONMENT_PATH=/usr/local
ENV UV_PROJECT_ENVIRONMENT=${UV_PROJECT_ENVIRONMENT_PATH}
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --compile-bytecode --link-mode=copy

# add DEPLOY_TARGET to PYTHONPATH
ENV PYTHONPATH ${PYTHONPATH}:${DEPLOY_TARGET}