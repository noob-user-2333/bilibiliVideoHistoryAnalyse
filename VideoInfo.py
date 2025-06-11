import dbProxy
from datetime import datetime
from dbProxy import *
from peewee import  *

class VideoInfo(BaseModel):
    bvid = CharField() #
    tag_id = IntegerField()
    tag_name = CharField() #
dbProxy.db_proxy.create_tables([VideoInfo])  # 创建表格