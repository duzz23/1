from sqlalchemy.orm import (
    declarative_base,
    Session as SessionType,
    sessionmaker,
    scoped_session, relationship,
)
from datetime import date
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
)


DB_URl = "postgresql+psycopg2://surfing:surfing@localhost:5436/surfing_blog"
DB_ECHO = False

engine = create_engine(url=DB_URl, echo=DB_ECHO)
Base = declarative_base(bind=engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

"""Класс создания таблицы prorider_table """
class ProRider(Base):
    __tablename__ = "prorider_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    age = Column(Integer(), nullable=False)
    born = Column(Date)
    board = Column(Integer, ForeignKey("surfboard_table.id"))

    def __str__(self):
        return f'Rider(id={self.id}, name={self.name!r}, age={self.age}, board={self.board!r})'
    def __repr__(self):
        return str(self)

"""Класс создания таблицы surfboard_table """
class SurfBoard(Base):
    __tablename__ = "surfboard_table"
    id = Column(Integer, primary_key=True)
    brand = Column(String(32), nullable=False)
    model = Column(Integer())
    rider_id = relationship("ProRider")

    def __str__(self):
        return f'User(id={self.id}, brand={self.brand!r}, model={self.model})'
    def __repr__(self):
        return str(self)

"""Функция для добавления Райдера"""
def create_user(session: SessionType, name: str, age: int, born:date, board: int) -> ProRider:
    user = ProRider(name=name, age=age, born=born, board=board)
    session.add(user)
    print("user (added)", user)
    session.commit()
    print("seved user", user)
    return user

"""Функция для добавления бордов """
def add_board(session: SessionType, brand: str, model: int) -> SurfBoard:
    boards = SurfBoard(brand=brand, model=model)
    session.add(boards)
    print("board (added)", boards)
    session.commit()
    print("seved board", boards)
    return boards



def main():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    session: SessionType = Session()

    """Заполняю таблицу surfboard_table"""
    add_board(session, "hypto krypto", 1)
    add_board(session, "hypto krypto", 3)
    add_board(session, "hypto krypto", 2)

    """Заполняю таблицу prorider_table"""
    create_user(session, "Andrey", 35, date(1984, 10, 20), 2)

    session.close()


if __name__ == "__main__":
    main()


