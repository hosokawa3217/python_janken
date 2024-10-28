import pytest
from  src.player import player_pon
from unittest.mock import patch
'''
このコードをPytestでテストするために、標準入力をモックする必要があります。
'''

def test_pon_guu():
# return_value
# モックが呼び出された際に返す値を設定
    with patch('builtins.input', return_value='1'):
        assert player_pon() == 'グー'

def test_pon_choki():
# return_value
# モックが呼び出された際に返す値を設定
    with patch('builtins.input', return_value='2'):
        assert player_pon() == 'チョキ'

def test_pon_paa():
# return_value
# モックが呼び出された際に返す値を設定
    with patch('builtins.input', return_value='3'):
        assert player_pon() == 'パー'

def test_pon_invalid_input():
# side_effect
# モックが呼ばれた際に呼び出される関数、イテラブル、もしくは発生させる例外 (クラスまたはインスタンス) を設定
    with patch('builtins.input', side_effect=['4', '2']):
        assert player_pon() == 'チョキ'

if __name__ == "__main__":
    pytest.main()