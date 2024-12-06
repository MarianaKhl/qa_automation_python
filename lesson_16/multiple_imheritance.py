import unittest


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


class TestTeamLeadAttributes(unittest.TestCase):
    def setUp(self):
        # create the TeamLead object for testing
        self.teamlead = TeamLead("Tom", 3000, "HR", "Python", 30)

    def test_attributes_from_manager(self):
        # check whether the department attribute (from the Manager class) exists
        self.assertTrue(hasattr(self.teamlead, 'department'), "Attribute 'department' missing from TeamLead")

    def test_attributes_from_developer(self):
        # check whether the programming_language attribute (from the Developer class) exists
        self.assertTrue(hasattr(self.teamlead, 'programming_language'), "Attribute 'programming_language' missing from TeamLead")

    def test_team_size(self):
        # check whether the team_size attribute exists (additional attribute in TeamLead)
        self.assertTrue(hasattr(self.teamlead, 'team_size'), "Attribute 'team_size' missing from TeamLead")


# run tests
if __name__ == "__main__":
    unittest.main()



