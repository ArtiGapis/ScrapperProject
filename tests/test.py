from src.jobs_calculator import highest_salary, highest_intrest
from src.get_configs import all_configs
import random

configer = all_configs
def test_sorting_highest_salary():
    # given
    rand_nr_1 = random.randint(1, 9)
    rand_nr_2 = random.randint(1, 9)
    rand_nr_3 = random.randint(1, 9)
    rand_nr_4 = random.randint(1, 9)
    scores = [rand_nr_1, rand_nr_2, rand_nr_3, rand_nr_4]
    db = [{'City': '', 'Salary': scores[0]},
          {'City': '', 'Salary': scores[1]},
          {'City': '', 'Salary': scores[2]},
          {'City': '', 'Salary': scores[3]}]
    # when
    scores.sort(reverse=True)
    res = highest_salary(db, configer)
    salarys = []
    for salary in res:
        salarys.append(salary['Salary'])
    # then
    assert scores == salarys

def test_sorting_highest_intrest():
    # given
    rand_nr_1 = random.randint(1, 9)
    rand_nr_2 = random.randint(1, 9)
    rand_nr_3 = random.randint(1, 9)
    rand_nr_4 = random.randint(1, 9)
    scores = [rand_nr_1, rand_nr_2, rand_nr_3, rand_nr_4]
    db = [{'City': '', 'Acept': scores[0]},
          {'City': '', 'Acept': scores[1]},
          {'City': '', 'Acept': scores[2]},
          {'City': '', 'Acept': scores[3]}]
    # when
    scores.sort(reverse=True)
    res = highest_intrest(db, configer)
    salarys = []
    for salary in res:
        salarys.append(salary['Acept'])
    # then
    assert scores == salarys

if __name__ == '__main__':
    try:
        test_sorting_highest_salary()
        test_sorting_highest_intrest()

        all_configs.main_logger.info(f'All tests passed')
        configer.console_logger.warning(f'All tests passed')
    except AssertionError as e:
        configer.main_logger.warning(f'Test error: {e!r}')
        configer.console_logger.warning(f'Test error: {e!r}')

