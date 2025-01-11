from sqlalchemy import create_engine, text, String, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Member(Base):
    __tablename__ = "member"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256))
    level = Column(Integer)
    place = Column(String(256))


class DM_Manager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.engine = create_engine(f"mysql+pymysql://root:000000@localhost/{self.db_name}")
        self.session = sessionmaker(bind=self.engine)()

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def insert_table_data(self, **kwargs):
        member = Member(*kwargs)
        self.session.add(member)
        self.session.commit()

    def update_table_data(self, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            member = self.session.query(Member).filter_by(id=id).first()
            if member is not None:
                for key, value in kwargs.items():
                    setattr(member, key, value)
                self.session.commit()
            else:
                pass
        else:
            pass

    def run_table_raw(self, raw_sql: str):
        self.session.execute(text(raw_sql))
        self.session.commit()

    def delete_table(self):
        Base.metadata.drop_all(self.engine)


if __name__ == '__main__':
    db_manager = DM_Manager('nova')
    db_manager.create_table()
    db_manager.insert_table_data(name="OpenStack", level=3, place="test")
    db_manager.update_table_data(id=1, level=6)
    db_manager.run_table_raw("select * from nova.member;")
    # db_manager.delete_table()
