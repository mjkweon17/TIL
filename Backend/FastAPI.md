## SQLAlchemy / SQLModel

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




## Pydantic

## FastAPI


