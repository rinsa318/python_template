"""スクリプト例示モジュール

本モジュールでは、スクリプトの例を示すと共に、Googleスタイルのドキュメントの書き方を示す。
ただし、型ヒントについてはコード内への記載を必須とし、docstringには任意とする。

Attributes:
    NA

Todo:
    * For module TODOs

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""


def add(x: int, y: int) -> int:
    """足し算関数

    xとyの和を返す。

    Attributes:
        x: 足す数
        y: 足される数

    Returns:
        xとyの和
    """
    return x + y


def sub(x: int, y: int) -> int:
    """引き算関数

    xからyを引いた値を返す。

    Attributes:
        x: 引く数
        y: 引かれる数

    Returns:
        xからyを引いた値
    """
    return x - y


if __name__ == "__main__":
    print("1+1=", add(1, 1))
    print("1-1=", sub(1, 1))
