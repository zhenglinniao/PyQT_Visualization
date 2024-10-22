import logging
import sys
# 创建一个 logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # 设置最低日志级别

# 创建文件处理器
file_handler = logging.FileHandler('./log/app.log',encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # 控制台只输出 INFO 及以上级别的日志

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到 logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 全局未捕获异常的处理函数
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # 如果是 KeyboardInterrupt，保持默认的行为，不记录日志
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    # 否则，记录未捕获的异常
    logging.error("全局捕获", exc_info=(exc_type, exc_value, exc_traceback))

# 替换默认的异常处理器
sys.excepthook = handle_exception
