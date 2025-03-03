# Python Template

Japanese followed by English

## What's this?

python で開発するためのテンプレートレポジトリ

↓ 以下、project 用 readme テンプレート ↓

# プロジェクトのタイトル

## プロジェクト概要

{プロジェクトの概要を記載}

## 環境

[mise](https://mise.jdx.dev/getting-started.html) を用いてローカル環境の主要ツール（初期状態は python と [uv](https://docs.astral.sh/uv/getting-started/features/#projects)）を管理し、[uv](https://docs.astral.sh/uv/getting-started/features/#projects) を用いて python のライブラリを管理する構成をとっています。docker コンテナ上での環境構築を前提として作成していますが、ローカル環境で直接開発する方針でも使用可能です。

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| 言語・フレームワーク               | バージョン |
| ---------------------------------- | ---------- |
| Python                             | 3.12.9     |
| uv                                 | 0.5.29     |
| poethepoet                         | ^0.32.2    |
| mypy                               | ^1.15.0    |
| ruff                               | ^0.9.5     |
| pytest                             | ^8.3.4     |
| coverage                           | ^7.6.10    |
| {language \| framework \| package} | {version}  |

細かい設定は[mise.toml](./mise.toml)と[pyproject.toml](pyproject.toml)を参照してください。

その他必要なツールやライブラリがある場合は、適宜 mise コマンドか uv コマンドを使用し追加してください。

## 開発方法

{開発方法の概要}

### 環境構築

```bash
# 1. mise.tomlに記載のツールをローカル環境にインストール
#（後述の.envの作成パートで必要）
mise install

# 2. 環境変数ファイル（.env）の生成
# TODO: .env.exampleを適宜編集する
eval "echo \"$(cat .env.example)\"" > .env
# or
mise run make-env

# Optional. ローカル環境での開発用にライブラリをインストール
uv sync --frozen
```

### 実行方法

[Dockerfile](./environments/dev/Dockerfile)と[compose.yaml](./environments/dev/compose.yaml)を編集し、以下を実行する。

**NOTE: 以下コマンドはすべて mise.toml 中でタスクとして定義しているので、`mise run <タスク名>` or `mise run # --> タスクを選択` でも実行可能。**

```bash
# イメージをビルド(キャッシュを使用しない)
cd environments/dev && docker compose build --parallel --no-cache

# イメージをビルド（キャッシュは使用される）し、コンテナをデーモンとして実行
cd environments/dev && docker compose up -d

# コンテナを停止。ボリュームとネットワークも削除
cd environments/dev && docker compose down --volumes --remove-orphans

# コンテナ内に入る
cd environments/dev && docker compose exec <compose.yamlで定義するservice名> bash
# or
mise run exec --service <compose.yamlで定義するservice名>

# CIジョブを実行
poe lint && poe type-check && poe test-coverage --cov-report=term-missing && coverage report --format=markdown
# or
mise run ci
```

---

# Project Title

## Overview

{Project Summary}

## Environment

We use [mise](https://mise.jdx.dev/getting-started.html) to manage the main tools in the local environment (initially python and [uv](https://docs.astral.sh/uv/getting-started/features/#projects)) and [uv](https://docs.astral.sh/uv/getting-started/features/#projects) is configured to manage python libraries. Although it was created with the assumption that the environment is built on a docker container, it can also be used with a policy of developing directly in a local environment.

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| item                               | version   |
| ---------------------------------- | --------- |
| Python                             | 3.12.9    |
| uv                                 | 0.5.29    |
| poethepoet                         | ^0.32.2   |
| mypy                               | ^1.15.0   |
| ruff                               | ^0.9.5    |
| pytest                             | ^8.3.4    |
| coverage                           | ^7.6.10   |
| {language \| framework \| package} | {version} |

See [mise.toml](./mise.toml) and [pyproject.toml](pyproject.toml) for detailed configuration.

If other tools or libraries are needed, please add them by using the mise or uv command as appropriate.

## Development

{Overview of Development}

### Environment Building

```bash
# 1. Install the tools listed in mise.toml in your local environment
#（Necessary in the .env creation part below）
mise install

# 2. Generating environment variable files (.env)
# TODO: Edit .env.example as appropriate
eval "echo \"$(cat .env.example)\"" > .env
# or
mise run make-env

# Optional. Install libraries for development in local environment
uv sync --frozen
```

### 実行方法

Edit the [Dockerfile](./environments/dev/Dockerfile) and [compose.yaml](./environments/dev/compose.yaml) and execute the following.

**NOTE: The following commands are all defined as tasks in mise.toml, so they can be executed by `mise run <task name>` or `mise run # --> select task`.**

```bash
# Build image (without cache)
cd environments/dev && docker compose build --parallel --no-cache

# Build image (cache is used) and run container as daemon
cd environments/dev && docker compose up -d

# Stop the container. Volume and network also deleted.
cd environments/dev && docker compose down --volumes --remove-orphans

# Entering the Container
cd environments/dev && docker compose exec <compose.yamlで定義するservice名> bash
# or
mise run exec --service <compose.yamlで定義するservice名>

# Run CI job
poe lint && poe type-check && poe test-coverage --cov-report=term-missing && coverage report --format=markdown
# or
mise run ci
```
