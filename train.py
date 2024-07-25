import torch
import logging
import random
from environment.CPEnv import CompiledJssEnvCP

def main():
    
    logging.basicConfig(filename="logs/log.log", filemode='a', level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    torch.backends.cudnn.benchmark = True
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    logger.info("Creating environment...")
    env = CompiledJssEnvCP("environment/instances/la01.txt")

    logger.info("Resetting the environment...")
    env.reset()

    logger.info("Solving the problem...")
    found, solution, makespan = env.solve_using_cp(list(), 30, 1)
    
    logger.info("Solution found:")
    logger.info(solution)

    logger.info("Makespan optimal:")
    logger.info(makespan)
    

if __name__ == "__main__":
    main()
