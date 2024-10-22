import logging
import time
import schedule
import threading
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 创建基础类
Base = declarative_base()

# 定义用户模型
class User(Base):
    __tablename__ = 'users'  # 数据库中的表名
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
# 创建数据库表结构（如果不存在则创建）



#生产订单
class MO_MO(Base):
    __tablename__ = 'MO_MO'  # 数据库中的表名
    id = Column(Integer, primary_key=True)
# 定义一个名为name的列，类型为String，长度为50，不能为空
    Mo_Name = Column(String(50), nullable=False)
    type = Column(Integer)
    State = Column(Integer,default=0)




def run():
        
    # 配置日志
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # 连接到 MySQL 数据库
    try:
        engine = create_engine('mysql+pymysql://root:20020318@localhost/huayan')
        logging.info("数据库连接成功")
    except Exception as e:
        logging.error("数据库连接失败", exc_info=True)

    Base.metadata.create_all(engine)
    # 创建会话类
    Session = sessionmaker(bind=engine)
    return Session()

# 查询数据库的函数
def print_sql():
    session = run()
    try:
        users = session.query(User).all()
        logging.info("查询到 %d 条数据", len(users))
        for user in users:
            print(user.name, user.age)
    except Exception as e:
        logging.error("查询数据失败", exc_info=True)
    finally:
        session.close()

#查询MO_MO表里state为0的数据
def print_sql2():
    session = run()
    try:
        users = session.query(MO_MO).filter(MO_MO.State==0).all()
        logging.info("查询到 %d 条数据", len(users))
        # data =  [{"Mo_Name": user.Mo_Name, "State": user.State} for user in users]
        return {"data_list": len(users)}
    except Exception as e:
        logging.error("查询数据失败", exc_info=True)

# 定义一个线程任务函数
def threaded_task():
    # 无限循环
    while True:
        # 运行所有待定的任务
        schedule.run_pending()
        # 休眠1秒
        time.sleep(1)


# 每隔10秒执行一次print_sql2函数
schedule.every(5).seconds.do(print_sql2)





# 主程序
if __name__ == "__main__":
    # 创建一个线程来运行调度任务
    schedule_thread = threading.Thread(target=threaded_task)
    
    # 设置守护线程，主线程退出时该线程自动退出
    schedule_thread.setDaemon(True) 
    # 启动线程
    schedule_thread.start()
    # 主线程中的其他任务可以继续运行，这里可以做其他操作
    while True:
        # 主线程休眠1秒
        print("主线程休眠1秒")
        time.sleep(600)
    
        