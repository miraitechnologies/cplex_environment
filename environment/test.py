from CPEnv import CompiledJssEnvCP

import logging

def main():
    env = CompiledJssEnvCP("instances/la01.txt")
    logging.basicConfig(filename="logs/mylogs.log", filemode='a', level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Jobs data:\n")
    logger.info(env.jobs_data)

    env.reset()
    solution_found, solution, makespan = env.solve_using_cp(list(), 30, 1)

    logger.info("solution")
    logger.info(solution)

    logger.info("Makespan")
    logger.info(makespan)

if __name__ == "__main__":
    main()