import time
import numpy as np
import math
from robot_model import robot_model
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 请提供CSV文件路径，例如：python get_csv_position_and_interpolation.py your_csv_file.csv")
        sys.exit(1)

    csv_path = sys.argv[1]

    robot = robot_model()
    time.sleep(1)

    robot.get_csv_position_and_interpolation(csv_path)
