# [NOTE]
# build時はcompose.yamlの値が優先されるため、
# compose.yamlに設定が存在する場合はdockerfile中でARGの値を変更しても反映されない。
# 設定がなかったとき用にデフォルト値を設定
ARG PYTHON_VERSION=${PYTHON_VERSION:-3.12.9}
ARG UV_VERSION=${UV_VERSION:-0.5.29}

# baseの用意
# "COPY --from"の中ではARGは使用できないため、余分なFROMを定義
# 参考：https://github.com/docker/buildx/issues/1050#issuecomment-1090026399
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS astral_uv
FROM python:${PYTHON_VERSION}-slim-bookworm

# install uv
COPY --from=astral_uv /uv /uvx /bin/

# Change the working directory to the ${DEPLOY_TARGET} directory
ARG DEPLOY_TARGET=${DEPLOY_TARGET:-/app/}
WORKDIR ${DEPLOY_TARGET}

# Install dependencies
ARG UV_PROJECT_ENVIRONMENT_PATH=${UV_PROJECT_ENVIRONMENT_PATH:-/usr/local}
ENV UV_PROJECT_ENVIRONMENT=${UV_PROJECT_ENVIRONMENT_PATH}
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# add DEPLOY_TARGET to PYTHONPATH
ENV PYTHONPATH ${PYTHONPATH}:${DEPLOY_TARGET}