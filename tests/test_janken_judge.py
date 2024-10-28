# pytest test_judge.py
import pytest
from  src.janken_judge import judge

def test_draw():
    assert judge('グー', 'グー') == 'draw'
    assert judge('チョキ', 'チョキ') == 'draw'
    assert judge('パー', 'パー') == 'draw'

def test_player_win():
    assert judge('チョキ', 'グー') == 'player_win'
    assert judge('パー', 'チョキ') == 'player_win'
    assert judge('グー', 'パー') == 'player_win'

def test_computer_win():
    assert judge('グー', 'チョキ') == 'computer_win'
    assert judge('チョキ', 'パー') == 'computer_win'
    assert judge('パー', 'グー') == 'computer_win'

if __name__ == "__main__":
    pytest.main()