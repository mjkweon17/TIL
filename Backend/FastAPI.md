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

## Pydantic

### 스키마 이름을 지을 때 고려사항
- 용도 명확화: 스키마의 이름이 그 용도를 명확히 반영해야 함. 예를 들어, 생성(create), 응답(response), 업데이트(update) 등의 용어는 스키마가 어떤 상황에서 사용되는지를 분명히 해줌
- 상속 구조 활용: 기본 스키마(예: BookmarkBase)로부터 상속받아 필요한 추가 필드만 정의함으로서 중복을 최소화하고, 코드의 가동성과 유지보수성을 향상시킬 수 있음
- 일관성 유지: 프로젝트 내에서 스키마 일므을 지을 때 일관된 규칙을 따르면, 코드의 이해도를 높이고, 새로운 스키마를 추가할 때의 예측 가능성을 높일 수 있음.
- 스키마 이름 예시
    - BookmarkBase, BookmarkCreate, BookmarkUpdate, BookmarkResponse, BookmarkList, BookmarkPartialUpdate, BookmarkDeleteResponse, BookmarkDetail, BookmarkSearchResults

### field definitions
- `None`과 `...`
    - 필드 검증 및 기본 값을 어떻게 할지에 따라 선택
    - `None`
        - 선택적 필드의 경우 `Optional[type]과 함께 기본 값으로 `None`을 사용
    - `...`(Ellipsis)
        - 필드가 필수이며 생략될 수 없음을 나타내기 위해 사용
    - 이외에도 필드의 기본값으로 다양한 값을 넣어줄 수 있음


Pydantic에서는 `Field` 함수 외에도 모델의 데이터 검증, 변환, 구성 등을 다루기 위해 여러 유틸리티와 데코레이터를 제공합니다. 이러한 도구들은 모델의 정의를 더 풍부하게 하고, 데이터 처리를 보다 세밀하게 제어할 수 있게 해줍니다. 주요 기능들을 소개합니다:

### orm_mode = True
- Pydantic 모델이 ORM 객체를 읽을 수 있도록 해줌.
- 이 방식을 사용하면 SQLAlchemy 모델과 Pydantic 모델 간의 변환이 용이해짐



### 1. **Validators (`@validator` 데코레이터)**
Pydantic의 `@validator` 데코레이터를 사용하여 모델 필드에 대한 사용자 정의 검증 함수를 작성할 수 있습니다. 이를 통해 복잡한 검증 로직을 구현하거나, 필드 값이 특정 조건을 만족하는지 체크할 수 있습니다.

```python
from pydantic import BaseModel, validator

class UserModel(BaseModel):
    name: str
    age: int

    @validator('age')
    def check_age(cls, value):
        if value < 18:
            raise ValueError('Age must be at least 18')
        return value
```




### 2. **Root Validators (`@root_validator` 데코레이터)**
`@root_validator` 데코레이터를 사용하여 모델 전체에 대한 검증을 수행할 수 있습니다. 이는 모델의 여러 필드 간 관계를 검증할 때 유용합니다.

```python
from pydantic import BaseModel, root_validator

class LocationModel(BaseModel):
    latitude: float
    longitude: float

    @root_validator
    def check_coordinates(cls, values):
        latitude, longitude = values.get('latitude'), values.get('longitude')
        if not (-90 <= latitude <= 90):
            raise ValueError('Latitude must be between -90 and 90.')
        if not (-180 <= longitude <= 180):
            raise ValueError('Longitude must be between -180 and 180.')
        return values
```

### 3. **Default Factory (`default_factory` 인자)**
`Field` 함수의 `default_factory` 인자를 사용하여 필드의 기본값을 동적으로 생성할 수 있습니다. 이는 매 인스턴스 생성 시마다 새로운 기본값을 생성해야 할 때 유용합니다.

```python
from pydantic import BaseModel, Field
from datetime import datetime

class LogEntry(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.now)
```

### 4. **Field Description (`Field` 함수)**
앞서 언급한 것처럼, `Field` 함수를 사용하여 필드의 메타데이터(예: 타이틀, 설명, 예제 값 등)를 정의할 수 있습니다. 이 메타데이터는 문서 자동 생성 등에 활용됩니다.

### 5. **Constrained Types**
Pydantic은 길이, 범위, 정규 표현식 검사 등을 위한 제약 조건이 적용된 타입을 제공합니다. 예를 들어, `conint`, `constr` 등이 있으며, 이를 통해 필드 값에 추가적인 제약 조건을 적용할 수 있습니다.

```python
from pydantic import BaseModel, constr, conint

class RestrictedModel(BaseModel):
    limited_str: constr(min_length=2, max_length=10)
    limited_int: conint(gt=0, lt=100)
```

이러한 기능들을 통해 Pydantic 모델의 정의를 더욱 세밀하게 제어하고, 데이터의 검증 및 변환 과정을 보다 풍부하게 구성할 수 있습니다.



Pydantic은 데이터 검증 및 설정 관리를 위한 파이썬 라이브러리로, 다양한 고급 기능과 유틸리티를 제공합니다. 앞서 언급한 기능 외에도, Pydantic은 여러 고급 사용 사례를 지원하는 기능들을 포함하고 있습니다. 이러한 기능들을 활용하면 보다 강력하고 유연한 데이터 모델링이 가능합니다.

### 6. **Complex Field Types**
Pydantic은 리스트, 딕셔너리, 유니언 등 복잡한 데이터 타입의 검증을 지원합니다. 이를 통해 다양한 데이터 구조를 모델링하고 검증할 수 있습니다.

```python
from pydantic import BaseModel
from typing import List, Dict, Union

class ComplexModel(BaseModel):
    list_of_ints: List[int]
    string_to_float_map: Dict[str, float]
    complex_union: Union[int, str]
```

### 7. **Generic Models**
Pydantic 모델은 제네릭을 지원하여, 타입 매개변수를 통해 모델의 유연성을 높일 수 있습니다. 이를 통해 다양한 타입의 데이터를 처리하는 하나의 모델을 정의할 수 있습니다.

```python
from pydantic import BaseModel, GenericModel
from typing import TypeVar, Generic

T = TypeVar('T')

class GenericResponseModel(GenericModel, Generic[T]):
    data: T
    success: bool
```

### 8. **Custom Data Types**
사용자 정의 데이터 타입을 생성하여, Pydantic 모델에서 사용할 수 있습니다. 이를 통해 특수한 검증 로직이나 변환 로직을 데이터 타입에 직접 적용할 수 있습니다.

### 9. **Settings Management**
Pydantic은 환경 변수나 설정 파일을 통한 애플리케이션 설정 관리를 위한 기능을 제공합니다. `BaseSettings` 클래스를 활용하여 설정 값을 모델로 정의하고, 환경변수에서 자동으로 값을 로드할 수 있습니다.

```python
from pydantic import BaseSettings

class AppConfig(BaseSettings):
    app_name: str
    admin_email: str

    class Config:
        env_file = ".env"
```

### 10. **Model Inheritance**
모델 간 상속을 통해 코드의 재사용성을 높이고, 모델 정의를 간결하게 유지할 수 있습니다. 부모 모델의 필드와 검증 로직을 상속받아 새로운 모델을 쉽게 정의할 수 있습니다.

### 11. **Aliases and Field Mapping**
`Field` 함수의 `alias` 매개변수를 사용하여 모델 필드의 외부 이름을 정의할 수 있습니다. 이는 JSON과 같은 외부 데이터 소스와 모델을 매핑할 때 유용합니다.

### 12. **Post-Parsing Processing with `@validator`**
`@validator` 데코레이터를 활용한 후처리를 통해, 파싱된 데이터에 추가적인 변환 로직을 적용할 수 있습니다. 이는 데이터를 최종적으로 사용하기 전에 필요한 조정을 가능하게 합니다.

Pydantic의 이러한 고급 기능들은 강력한 데이터 검증, 변환, 모델링을 위한 훌륭한 도구를 제공합니다. 이를 통해 코드의 가독성, 안정성, 그리고 유지보수성을 크게 향상시킬 수 있습니다.







## FastAPI


