# coding=utf-8
import os
# 整个项目的根目录绝对路劲
baseDir = os.path.dirname(os.path.dirname(__file__))

# 数据库配置你文件绝对路径
config_path = baseDir + "/config/db_config.ini"

log_file_path = baseDir + "/config/logger.conf"


if __name__ == '__main__':
    print(log_file_path)

