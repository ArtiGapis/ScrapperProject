from src.jobs_calculator import highest_salary
import random

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
    res = highest_salary(db)
    salarys = []
    for salary in res:
        salarys.append(salary['Salary'])
    # then
    assert scores == salarys


if __name__ == '__main__':
    test_sorting_highest_salary()

    print("Test passed")
