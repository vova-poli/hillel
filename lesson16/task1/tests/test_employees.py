import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from employees import TeamLead

def test_teamlead_attributes():
    lead = TeamLead("Іван", 5000, "R&D", "Python", 5)

    assert hasattr(lead, 'name')
    assert hasattr(lead, 'salary')
    assert hasattr(lead, 'department')
    assert hasattr(lead, 'programming_language')
    assert hasattr(lead, 'team_size')
