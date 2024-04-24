### relationship
- `relationship`은 SQLAlchemy ORM에서 사용하는 키워드
- 두 테이블 간의 관계를 정의하는 데 사용됨
- 이를 통해 객체 관계 매핑(ORM)에서 다른 테이블의 레코드를 객체로 쉽게 접근할 수 있게 해주며, 복잡한 JOIN 연산 없이도 관련된 데이터를 효율적으로 처리할 수 있음
- 예시
    ```python
    class Bookmark(Base):
        __tablename__ = 'Bookmark'
        bookmark_id = Column(Integer, primary_key=True, autoincrement=True)
        page_id = Column(Integer, ForeignKey('Page.page_id'), nullable=False, default=0)
        user_id = Column(Integer, ForeignKey('User.user_id'), nullable=True, default=0)
        anonymous_user_id = Column(Integer, ForeignKey('AnonymousUser.anonymous_user_id'), nullable=True, default=0)
        state = Column(SmallInteger, nullable=False, default=1)
        created_at = Column(DateTime(3), nullable=False, server_default=func.current_timestamp(3))
        updated_at = Column(DateTime(3), nullable=False, server_default=func.current_timestamp(3), onupdate=func.current_timestamp(3))
        title = Column(String(255), nullable=True)
        notes = Column(Text, nullable=False)
        page = relationship("Page")
        user = relationship("User")
        anonymous_user = relationship("AnonymousUser")
    ```
    - `Bookmark` 클래스에 정의된 `relationship`을 사용하면 `Bookmark` 인스턴스를 통해 연결된 `Page`, `User`, `AnonymousUser` 객체에 직접 접근할 수 있음. 각 `relationship` 호출은 해당 클래스의 인스턴스와 `Bookmark` 인스턴스 사이에 참조 관계를 생성함.
    - 예시
        - `page = relationship("Page")`: 이는 `Bookmark` 인스턴스와 `Page` 인스턴스 사이의 관계를 정의함. `ForeignKey`를 통해 `page_id`가 `Page` 테이블의 `page_id`를 참조하고 있음을 나타냄. 이를 통해 특정 `Bookmark` 인스턴스에 대응하는 `Page` 객체에 접근할 수 있게 됨.
        - `user = relationship("User")`: 이는 `Bookmark` 인스턴스와 `User` 인스턴스 사이의 관계를 정의함. 여기서 `user_id` 필드가 `User` 테이블의 `user_id`를 참조함. 결과적으로, 특정 `Bookmark` 인스턴스가 어떤 `User` 객체와 연결되어 있는지 쉽게 파악할 수 있음.
        - `anonymous_user = relationship("AnonymousUser")`: 이는 `Bookmark` 인스턴스와 `AnonymousUser` 인스턴스 사이의 관계를 정의함. `anonymous_user_id` 필드가 `AnonymousUser` 테이블의 `anonymous_user_id`를 참조함. 이를 통해, 익명 사용자에 의해 생성된 북마크와 관련된 `AnonymousUser` 객체에 접근할 수 있음.
    - 이러한 `relationship` 정의를 사용함으로써, 개발자는 관계형 데이터베이스의 복잡성을 추상화하고, 객체 지향적인 방식으로 데이터베이스와의 상호작용을 구현할 수 있음. 이는 데이터베이스 설계를 더욱 유연하게 하며, 코드의 가독성과 유지보수성을 향상시킴.
- relationship을 사용하지 않는다면
    - 직접 쿼리 작성과 실행: relationship 없이, 예를 들어 Bookmark와 관련된 User 정보를 가져오려면, User 테이블에서 user_id를 사용하여 직접 JOIN 쿼리를 작성하고 실행해야 함. 이 과정은 복잡하고 오류가 발생하기 쉬우며, SQL 쿼리에 익숙하지 않은 개발자에게는 더욱 어려울 수 있음.
    - 데이터 접근성 감소: SQLAlchemy의 relationship을 사용하면, Python 객체처럼 관련 객체에 접근할 수 있음. 하지만 이를 사용하지 않으면, 매번 필요한 데이터를 수동으로 쿼리하고, 결과를 애플리케이션 논리 내에서 수동으로 연결해야 함.
    - 코드의 가독성과 유지보수성 감소: relationship을 사용하면, 데이터 모델 간의 관계가 명확하게 코드 내에 표현됨. 이는 코드의 가독성을 높이고, 유지보수를 용이하게 함. 직접 쿼리를 사용하면, 이러한 관계를 코드에서 직접적으로 파악하기 어렵고, 변경사항이 생겼을 때 모든 관련 쿼리를 찾아 수정해야 함.
    - 성능 최적화의 어려움: SQLAlchemy의 relationship은 내부적으로 쿼리 최적화를 수행할 수 있음. 예를 들어, lazy loading, eager loading과 같은 로딩 전략을 사용하여 필요에 따라 데이터 로딩 방식을 조절할 수 있음. 직접 쿼리를 관리할 경우, 이러한 최적화를 수동으로 구현해야 하며, 이는 상당한 노력과 전문 지식을 요구함.
    - 트랜잭션 관리와 일관성 유지의 어려움: relationship을 통해 관리되는 객체 관계는 SQLAlchemy 세션을 통한 트랜잭션 관리의 이점을 누릴 수 있음. 반면, 직접 쿼리를 사용할 경우 트랜잭션 관리를 수동으로 해야 하며, 복잡한 데이터 관계에서 데이터 일관성을 유지하는 것이 더 어려워질 수 있음.
- 예시: relationship을 사용했을 때
    ```python
    # 북마크를 통해 사용자 이름에 접근
    bookmark = session.query(Bookmark).first()
    print(bookmark.user.name)  # 'John Doe' 출력
    ```
- 예시: relationship을 사용하지 않았을 때
    ```python
    # 사용자 정보를 가져오기 위해 JOIN 쿼리 실행
    stmt = select(Bookmark, User).join(User, Bookmark.user_id == User.id).limit(1)
    for bookmark, user in session.execute(stmt):
        print(user.name)  # 'John Doe' 출력
    ````

### backref, back_populates
- `relationship`은 양방향 관계를 정의할 때 양쪽 테이블에 사용될 수 있음. 이를 통해 모델 간의 관계를 보다 명확하게 표현하고, 양쪽 방향에서 관련 객체에 쉽게 접근할 수 있게 됨. 양방향 관계를 설정함으로써, 한 쪽에서 변경이 발생했을 때 다른 쪽도 자동으로 업데이트되는 등의 장점이 있음.
- 양방향 관계는 `backref`와 `back_populates` 옵션을 사용하여 구현할 수 있음.
- `backref`는 관계가 선언된 쪽에서 반대 쪽으로의 접근을 자동으로 추가할 때 사용됨. `backref`는 관계의 반대편에 자동으로 속성을 생성하며, 이를 통해 반대편 모델에서도 관계를 쉽게 참조할 수 있게 됨.
- `back_populates`는 두 모델 간의 관계를 서로 명시적으로 설정할 때 사용됩니다. 이 옵션을 사용하면, 각 모델에서 반대 모델로의 관계를 명확하게 지정해야 함. `back_populates`는 더 명시적이며 복잡한 관계 설정에 유용함.
- 예시
    - `User`와 `Address` 테이블의 양방향 관계
    - `User`와 `Address`가 1:N 관계를 가지며, 양방향 관계를 설정하는 예시
    ```python
    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        addresses = relationship("Address", back_populates="user")

    class Address(Base):
        __tablename__ = 'addresses'
        id = Column(Integer, primary_key=True)
        email = Column(String, nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'))
        user = relationship("User", back_populates="addresses")
    ```
    - `User` 모델의 `addresses` 속성과 `Address` 모델의 `user` 속성은 서로를 참조하여 양방향 관계를 형성함. 이를 통해, `User` 객체에서 해당 사용자의 모든 주소에 쉽게 접근할 수 있으며, `Address` 객체에서도 해당 주소를 소유한 사용자에게 쉽게 접근할 수 있음.

### stmt
- `stmt`는 SQLAlchemy에서 사용되는 변수 이름
- SQL 문(statement)을 나타냄
- SQL 쿼리를 구성하고, 실행하기 위한 명령이나 요청을 표현하는 데 사용되는 SQLAlchemy의 객체 또는 표현식
- `stmt`는 보통 `select()`, `insert()`, `update()`, `delete()` 등의 함수를 사용해 생성되며, 이를 통해 데이터베이스와의 상호작용을 추상화하고, SQL 쿼리를 직접 작성하는 대신 Python 코드로 데이터베이스 작업을 수행할 수 있음.
- 예시
    - `select()` 함수를 사용하여 특정 테이블에서 데이터를 조회하는 쿼리를 만들 수 있음
    ```python
    from sqlalchemy import select

    stmt = select([User.name]).where(User.id == 1)

    result = session.execute(stmt)
    for row in result:
        print(row.name)
    ```
    - 위 코드에서 `stmt`는 `User` 테이블에서 `id`가 1인 사용자의 `name`을 조회하는 SQL 쿼리를 나타냄
    - SQLAlchemy를 사용하면 이러한 `stmt` 객체를 만들어 데이터베이스 쿼리를 보다 쉽고 안전하게 구성할 수 있으며, SQL 삽입 공격 같은 보안 문제를 방지하는 데도 도움이 됨.
    - `session.execute(stmt)`는 `stmt`에 해당하는 SQL 쿼리를 데이터베이스에 보내 실행하고, 그 결과를 받아옴. 이 방식을 통해 SQL 쿼리를 추상화하여 데이터베이스 작업을 수행할 수 있음.

### Alembic
- Python 언어로 작성된 데이터베이션 마이그레이션 도구
- SQLAlchemy ORM을 사용하는 애플리케이션을 위해 만들어졌지만, SQLAlchemy를 사용하지 않는 데이터베이스 프로젝트에도 사용할 수 있음
- 데이터베이스 스키마(migration)를 버전 관리하는 데 사용됨
- Alembic을 사용하면 개발자는 데이터베이스 스키마 변경 사항을 스크립트 형태로 작성하여 이력을 관리할 수 있고, 이를 통해 다양한 버전의 데이터베이스 스키마를 쉽게 배포하고 롤백할 수 있음
- FastAPI에서 Alembic을 사용하는 것은 FastAPI 애플리케이션의 데이터 모델이 시간에 따라 변경될 때 일관성을 유지하고 데이터베이스 마이그레이션을 관리하는 데 있어 매우 유용함

### Alembic 주요 기능
- 버전 관리: Alembic은 코드 베이스 내에서 데이터베이스 스키마의 버전을 관리함. 각 마이그레이션은 순차적으로 적용되며, 각 변경에는 고유한 식별자가 있음.
- 마이그레이션 스크립트 생성: Alembic은 변경 사항을 기반으로 마이그레이션 스크립트를 자동 생성할 수 있음. 개발자는 이 스크립트를 수정하여 필요에 맞게 조정할 수 있음.
- 업그레이드 및 다운그레이드: Alembic을 사용하면 데이터베이스 스키마를 새 버전으로 업그레이드하거나, 필요한 경우 이전 버전으로 다운그레이드할 수 있음.
- 자동 및 수동 마이그레이션: Alembic은 자동으로 마이그레이션 스크립트를 생성할 수 있지만, 복잡한 스키마 변경이나 데이터 변환은 수동으로 스크립트를 작성해야 할 수도 있음
