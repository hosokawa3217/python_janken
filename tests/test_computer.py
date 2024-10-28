import pytest
from  src.computer import computer_pon

def test_pon_returns_hand():
    """pon関数は"グー", "チョキ", "パー"のいずれかを返す"""
    hands = ["グー", "チョキ", "パー"]
    result = computer_pon()
    assert result in hands

def test_pon_has_no_arguments():
    """pon関数は引数を取らない"""
    with pytest.raises(TypeError):
        computer_pon(1)

def test_pon_returns_string():
    """pon関数の戻り値は文字列"""
    result = computer_pon()
    assert isinstance(result, str)

if __name__ == "__main__":
    pass

""" 
テストの目的
関数 pon() が、"グー", "チョキ", "パー" のいずれかをランダムに返すことを確認する。
引数がないことを確認する。
戻り値の型が文字列であることを確認する。
""" 

"""    テストケース:
test_pon_returns_hand(): pon 関数が "グー", "チョキ", "パー" のいずれかを返すことを確認します。
test_pon_has_no_arguments(): pon 関数が引数を取らないことを確認します。pytest.raises() を使って、引数を与えた際に TypeError が発生することを確認します。
test_pon_returns_string(): pon 関数の戻り値が文字列であることを確認します。isinstance を使って型をチェックします。
"""