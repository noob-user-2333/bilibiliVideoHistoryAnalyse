import dbProxy
from datetime import datetime
from dbProxy import *
from peewee import  *

class WatchedVideo(BaseModel):
    title = CharField()
    bvid = CharField() #
    author_name = CharField() #
    tag_name = CharField() #
dbProxy.db_proxy.create_tables([WatchedVideo])  # 创建表格