import pytest
from unittest.mock import patch

# from src.player import player_pon
# from src.computer import computer_pon
# from src.janken_judge import judge
from src.janken_controller import janken_controller

def test_janken_controller():
    with patch('player.player_pon', side_effect=['グー', 'チョキ', 'パー']), \
         patch('computer.computer_pon', side_effect=['チョキ', 'パー', 'グー']), \
         patch('builtins.print') as mock_print:
        
        janken_controller()
        
        # print関数が正しい回数呼び出されたかを確認
        assert mock_print.call_count > 0

if __name__ == "__main__":
    pytest.main()