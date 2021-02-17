import os
from importlib import reload
import shutil
import numpy as np
import pandas as pd
from pathlib import Path


DAY = 1
MARKING_SCHEME = {'return_element_of_a_list': 2, 'calculate_average': 4,
                  'concatenate_strings': 2, 'check_if_list_contains_item': 2,
                  'save_list_to_csv_file':4, 'count_number_of_csv_files': 2,
                  'report_basic_data_properties': 2, 'get_name_of_town_with_highest_elevation': 4,
                  'plot_a_numeric_attribute': 2}
TOT_SCORE = np.sum(list(MARKING_SCHEME.values()))
TOT_QNS = len(MARKING_SCHEME)


base_folder = Path.cwd().parents[0]
file_basic_prop = os.path.join(base_folder, 'data/power-outages.csv')
elev_file = os.path.join(base_folder, 'data/townships_with_dist_and_elev.csv')
plot = os.path.join(base_folder, 'data/elev_plot.png')

TEST_INPUTS = {'return_element_of_a_list': (['a', 'X', 'z', 10, 30], -1),
               'calculate_average': [i for i in range(10)],
               'concatenate_strings': ('Khama', 'Matekenya'),
               'check_if_list_contains_item': (['Malawi', 'Zambia', 'Mozambique', 'Dunstan'], 'Senegal'),
               'count_number_of_csv_files': base_folder.joinpath('data'),
               'save_list_to_csv_file': [["REG_NAME","REG_CODE","DIST_NAME","ADM_STATUS","DIST_CODE"],
               ["Central","2","Ntchisi","Rural","203"]],
               'report_basic_data_properties': file_basic_prop,
               'get_name_of_town_with_highest_elevation': elev_file,
               'plot_a_numeric_attribute': (elev_file, 'elev_metres')
               }


def get_responses_and_record(student_sol=None, sol=None, outdir=None):
    total_marks = 0
    total_graded = len(TEST_INPUTS)
    for k, v in TEST_INPUTS.items():
        # run function
        try:
            if k == 'return_element_of_a_list':
                i = v[1]
                lst = v[0]
                output = student_sol.return_element_of_a_list(lst, i)

                # check if its correct
                if output == lst[i]:
                    total_marks += MARKING_SCHEME[k]
            elif k == 'calculate_average':
                output = student_sol.calculate_average(v)
                # check if its correct
                if output == np.mean(v):
                    total_marks += MARKING_SCHEME[k]
            elif k == 'concatenate_strings':
                first = v[0]
                last = v[1]
                output = student_sol.concatenate_strings(first, last)
                if output == "{}  {}".format(first, last):
                    total_marks += MARKING_SCHEME[k]

            elif k == 'check_if_list_contains_item':
                item = v[1]
                lst = v[0]
                output = student_sol.check_if_list_contains_item(lst, item)
                if item in lst:
                    actual = 'YES'
                else:
                    actual = 'NO'

                if output == actual:
                    total_marks += MARKING_SCHEME[k]
            elif k == 'count_number_of_csv_files':
                correct = sol.count_number_of_csv_files(input_folder=v)
                output = student_sol.count_number_of_csv_files(input_folder=v)
                if output == correct:
                    total_marks += MARKING_SCHEME[k]
            elif k == 'save_list_to_csv_file':
                out_csv_d = outdir.joinpath("listToCsvDun.csv")
                out_csv_p = outdir.joinpath("listToCsvDunP.csv")

                sol.save_list_to_csv(lst=v, csvfile_path=out_csv_d)
                student_sol.save_list_to_csv(lst=v, csvfile_path=out_csv_p)

                dfd = pd.read_csv(out_csv_d)
                dfp = pd.read_csv(out_csv_p)

                # check if they are the same
                if dfd.shape[0] == dfp.shape[0]:
                    total_marks += MARKING_SCHEME[k]
            elif k == 'report_basic_data_properties':
                print()
                print('Grading function: {}'.format(k))
                s = student_sol.report_basic_data_properties(v)
                d = sol.report_basic_data_properties(v)

                # check if its correct
                for i in s:
                    if isinstance(i, int):
                        if i == d[0]:
                            total_marks += 1

                    if isinstance(i, list):
                        if sorted(i) == sorted(d[1]):
                            total_marks += 1
            elif k == 'get_name_of_town_with_highest_elevation':
                print()
                print('Grading function: {}'.format(k))
                correct = sol.get_name_of_town_with_highest_elevation(csv_file=v)
                output = student_sol.get_name_of_town_with_highest_elevation(csv_file=v)
                # check if its correct
                if output == correct:
                    total_marks += MARKING_SCHEME[k]
            elif k == 'plot_a_numeric_attribute':
                print()
                print('Grading function: {}'.format(k))
                student_sol.plot_a_numeric_attribute(csv_file=elev_file, col_to_plot='elev_metres',
                                                     output_file=plot)
                if os.path.exists(plot):
                    total_marks += MARKING_SCHEME[k]
        except Exception as e:
            total_graded -= 1
            continue

    return total_marks, total_graded


def grade_scripts(candidates_solutions_folder=None):

    # load teacher solutions
    working_dir = Path.cwd()
    instructor_script = working_dir.joinpath("solutions", 'Ex1_Solutions.py')
    shutil.copy(str(instructor_script), str(working_dir.joinpath('Ex1_Solutions.py')))
    try:
        import Ex1_Solutions as sol
        sol = reload(sol)
    except ImportError as e:
        pass
    
    lst = os.listdir(candidates_solutions_folder)
    res = []
    total_submissions = 0
    for l in lst:
        try:
            if l.endswith('py'):
                total_submissions += 1

                # get students name
                print()
                first = l.split('_')[0]
                last = l.split('_')[1][:-3]
                print('========================================')
                print('Grading: {} {}'.format(first, last))
                print('========================================')

                # copy module to mai folder and rename it
                if os.path.exists(os.path.join(working_dir, 'candidate_solutions.py')):
                    os.remove(os.path.join(working_dir, 'candidate_solutions.py'))

                new_solutions_script_path = os.path.join(candidates_solutions_folder, l)
                dest_file = os.path.join(working_dir, 'candidate_solutions.py')
                shutil.copy(new_solutions_script_path, dest_file)

                # run script
                import candidate_solutions as student_sol
                student_sol = reload(student_sol)
                score = get_responses_and_record(student_sol=student_sol, sol=sol, outdir=working_dir)

                # print results
                print('Score: {}/{}, number of questions graded: {}/{}'.format(score[0], TOT_SCORE, score[1], TOT_QNS))

                res.append({'firstName': first, 'lastName': last, 'score': score, 'day': DAY,
                            'totalScore': TOT_SCORE})
        except Exception as e:
            print("GRADING FAILED DUE TO ERROR DESCRIBED BELOW")
            print(e)
            continue

    print()
    print('***********************************************************')
    print('TOTAL PARTICIPANTS GRADED {}'.format(total_submissions))
    print('***********************************************************')
    return res


def main():
    working_dir = Path.cwd().parents[0]
    submissions_folder = working_dir.joinpath("exercise-submissions", "Exercise-1")
    ex1_scores = submissions_folder.joinpath("Ex1.csv")
    grades = grade_scripts(candidates_solutions_folder=submissions_folder)
    df_grades = pd.DataFrame(grades)
    df_grades.to_csv(ex1_scores, index=False)

    
if __name__ == '__main__':
    main()
