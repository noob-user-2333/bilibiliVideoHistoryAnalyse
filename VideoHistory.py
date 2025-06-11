import dbProxy
from datetime import datetime
from dbProxy import *
from peewee import  *

class VideoHistory(BaseModel):
    pageId = IntegerField()  #
    json = CharField() #
    timestamp = DateTimeField(default=datetime.now)
dbProxy.db_proxy.create_tables([VideoHistory])  # 创建表格