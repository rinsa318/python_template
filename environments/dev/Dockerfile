# -------------------------------------------
# Base
# -------------------------------------------
# [NOTE]
# build時は「compose.yaml->Dockerfile」の順にARGの値が優先される。
# compose.yamlに設定がなかったとき用にデフォルト値を設定
ARG PYTHON_VERSION=3.12.9
ARG UV_VERSION=0.5.29
# "COPY --from"の中ではARGは使用できないため、余分なFROMを定義
# 参考：https://github.com/docker/buildx/issues/1050#issuecomment-1090026399
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS astral_uv
FROM python:${PYTHON_VERSION}-slim-bookworm

# -------------------------------------------
# ディレクトリの設定
# -------------------------------------------
ARG DEPLOY_TARGET=/app/
WORKDIR ${DEPLOY_TARGET}


# -------------------------------------------
# 依存関係のインストール
# -------------------------------------------
# apt
COPY environments/dev/package.txt .
RUN apt update && \
    sed 's/#.*//' package.txt | xargs apt-get install -y --no-install-recommends

# uv
# uvのインストール
COPY --from=astral_uv /uv /uvx /bin/
# uvを用いてpythonのライブラリをインストール
ARG UV_PROJECT_ENVIRONMENT_PATH=/usr/local
ENV UV_PROJECT_ENVIRONMENT=${UV_PROJECT_ENVIRONMENT_PATH}
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project


# -------------------------------------------
# PYTHONPATHに追加
# -------------------------------------------
ARG PYTHONPATH
ENV PYTHONPATH=${PYTHONPATH}:${DEPLOY_TARGET}