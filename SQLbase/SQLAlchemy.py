import logging
import time
import schedule
import threading
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from PySide2.QtCore import QThread, Signal

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
#营业额表单
class MO_MO_Summary(Base):
    __tablename__ = 'MO_MO_Summary'  # 数据库中的表名
    id = Column(Integer, primary_key=True)
    Mo_Name = Column(String(50), nullable=False)
    Mo_No = Column(String(50), nullable=False)
    Mo_Type = Column(Integer)
    Mo_State = Column(Integer)
    #时间字段
    Mo_Date = Column(String(50), nullable=False)
    #金额字段
    Mo_Amount = Column(Integer)


    

def insert_data():
    session = run()
    try:
        # 创建一个新用户对象
        users = {MO_MO_Summary(Mo_Name='goods1', Mo_No='123456', Mo_Type=1, Mo_State=1, Mo_Date='2022-01-01', Mo_Amount=1000),
         MO_MO_Summary(Mo_Name='goods2', Mo_No='789012', Mo_Type=2, Mo_State=2, Mo_Date='2022-01-02', Mo_Amount=2000),
         MO_MO_Summary(Mo_Name='goods3', Mo_No='345678', Mo_Type=3, Mo_State=3, Mo_Date='2022-01-03', Mo_Amount=3000),
         MO_MO_Summary(Mo_Name='goods4', Mo_No='901234', Mo_Type=4, Mo_State=4, Mo_Date='2022-01-04', Mo_Amount=4000),
         MO_MO_Summary(Mo_Name='goods5', Mo_No='567890', Mo_Type=5, Mo_State=5, Mo_Date='2022-01-05', Mo_Amount=5000),
         MO_MO_Summary(Mo_Name='goods6', Mo_No='123456', Mo_Type=6, Mo_State=6, Mo_Date='2022-01-06', Mo_Amount=6000),
         MO_MO_Summary(Mo_Name='goods7', Mo_No='789012', Mo_Type=7, Mo_State=7, Mo_Date='2022-01-07', Mo_Amount=7000)}
        
        for user in users:
            # 添加用户对象到会话
            session.add(user)
    except Exception as e:
        logging.error("插入数据失败", exc_info=True)
    finally:
        session.commit()
        session.close()




def run():
        
    # 配置日志
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # 连接到 MySQL 数据库
    try:
        engine = create_engine('mysql+pymysql://root:20020318@localhost/huayan',
                                pool_size=10,       # 连接池中的最大连接数
                                max_overflow=5,     # 超出连接池大小时允许的最大连接数
                                pool_timeout=30,    # 连接超时时间（秒）
                                pool_recycle=1800   # 在连接池中，连接多长时间自动重置（秒）
                                )
        logging.info("数据库连接成功")
    except Exception as e:
        logging.error("数据库连接失败", exc_info=True)

# 创建所有表
    Base.metadata.create_all(engine)
    # 创建会话类
    Session = sessionmaker(bind=engine)
    return Session()





# 创建一个线程类，用于执行数据获取操作  获取线性表
class DataFetchThread(QThread):
    data_fetched = Signal(object)  # 定义一个信号，用于传递获取到的数据
    def run(self):
        # 这里执行耗时的数据获取操作
        data = self.print_MO_MO_Summary()
        self.data_fetched.emit(data)  # 发出信号，将数据传递回主线程
    def print_MO_MO_Summary(self):
        session = run()
        #时间排序获取MO_MO_Summary表里Mo_Amount
        try:
            users = session.query(MO_MO_Summary).order_by(MO_MO_Summary.Mo_Date).all()
            data =  [{"category": user.Mo_Date, "Mo_Amount": user.Mo_Amount} for user in users]
            return {"num": len(users),"data": data}
        except Exception as e:
            logging.error("查询数据失败", exc_info=True)
        finally:
            session.close()

#TODO 获取单个数字表
class DtaFetchThread_1(QThread):
    data_fetched = Signal(object)
    def run(self):
        # 这里执行耗时的数据获取操作
        data = self.print_sql()
        self.data_fetched.emit(data)  # 发出信号，将数据传递回主线程
    def print_sql(self):   
#查询MO_MO表里state为0的数据
        session = run()
        try:
            users = session.query(MO_MO).filter(MO_MO.State==0).all()
            logging.info("查询到 %d 条数据", len(users))
            # data =  [{"Mo_Name": user.Mo_Name, "State": user.State} for user in users]
            return {"data_list": len(users)}
        except Exception as e:
            logging.error("查询数据失败", exc_info=True)
        finally:
            session.close()

class DtaFetchThread_8(QThread):
    data_fetched = Signal(object)
    def run(self):
        # 这里执行耗时的数据获取操作
        data = self.print_sql()
        self.data_fetched.emit(data)  # 发出信号，将数据传递回主线程
    def print_sql(self):   
#查询MO_MO表里state为0的数据
        session = run()
        try:


            head = ["日期", "生产数量", "完成率", "状态"]# 设置表头

            # 填充数据
            production_data = [
                ['2024-10-21', '100', '90%', '进行中'],
                ['2024-10-22', '150', '100%', '已完成'],
                ['2024-10-23', '120', '75%', '延迟'],
                ['2024-10-24', '200', '80%', '进行中'],
                ['2024-10-25', '180', '95%', '已完成'],
                ['2024-10-24', '200', '80%', '进行中'],
                ['2024-10-25', '180', '95%', '已完成'],
                ['2024-10-24', '200', '80%', '进行中'],
                ['2024-10-25', '180', '95%', '已完成'],
            ]
            return {"data_list": production_data, "head": head}
        except Exception as e:
            logging.error("查询数据失败", exc_info=True)
        finally:
            session.close()







# 主程序
if __name__ == "__main__":
    # 创建一个线程来运行调度任务
    
# 创建一个线程，目标函数为threaded_task
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
    
        