
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

### Validators 
- `@validator` 데코레이터
- Pydantic의 `@validator` 데코레이터를 사용하여 모델 필드에 대한 사용자 정의 검증 함수를 작성할 수 있음
- 이를 통해 복잡한 검증 로직을 구현하거나, 필드 값이 특정 조건을 만족하는지 체크할 수 있음
- 예시
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

### Root Validators 
- `@root_validator` 데코레이터를 사용하여 모델 전체에 대한 검증을 수행할 수 있음
- 이는 모델의 여러 필드 간 관계를 검증할 때 유용함
- 예시
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

### Default Factory 
=- `Field` 함수의 `default_factory` 인자를 사용하여 필드의 기본값을 동적으로 생성할 수 있음
- 이는 매 인스턴스 생성 시마다 새로운 기본값을 생성해야 할 때 유용함.
- 예시
    ```python
    from pydantic import BaseModel, Field
    from datetime import datetime

    class LogEntry(BaseModel):
        timestamp: datetime = Field(default_factory=datetime.now)
    ```

### Field Description (`Field` 함수)
- 앞서 언급한 것처럼, `Field` 함수를 사용하여 필드의 메타데이터(예: 타이틀, 설명, 예제 값 등)를 정의할 수 있음.
- 이 메타데이터는 문서 자동 생성 등에 활용됨.

### Constrained Types
- Pydantic은 길이, 범위, 정규 표현식 검사 등을 위한 제약 조건이 적용된 타입을 제공함.
- 예를 들어, `conint`, `constr` 등이 있으며, 이를 통해 필드 값에 추가적인 제약 조건을 적용할 수 있음.
- 이러한 기능들을 통해 Pydantic 모델의 정의를 더욱 세밀하게 제어하고, 데이터의 검증 및 변환 과정을 보다 풍부하게 구성할 수 있음.
- 예시
    ```python
    from pydantic import BaseModel, constr, conint

    class RestrictedModel(BaseModel):
        limited_str: constr(min_length=2, max_length=10)
        limited_int: conint(gt=0, lt=100)
    ```

### Complex Field Types
- Pydantic은 리스트, 딕셔너리, 유니언 등 복잡한 데이터 타입의 검증을 지원함.
- 예시 
    ```python
    from pydantic import BaseModel
    from typing import List, Dict, Union

    class ComplexModel(BaseModel):
        list_of_ints: List[int]
        string_to_float_map: Dict[str, float]
        complex_union: Union[int, str]
    ```

### Generic Models
- Pydantic 모델은 제네릭을 지원하여, 타입 매개변수를 통해 모델의 유연성을 높일 수 있음.
- 이를 통해 다양한 타입의 데이터를 처리하는 하나의 모델을 정의할 수 있음.
- 예시
    ```python
    from pydantic import BaseModel, GenericModel
    from typing import TypeVar, Generic

    T = TypeVar('T')

    class GenericResponseModel(GenericModel, Generic[T]):
        data: T
        success: bool
    ```

### Custom Data Types
- 사용자 정의 데이터 타입을 생성하여, Pydantic 모델에서 사용할 수 있음. 
- 이를 통해 특수한 검증 로직이나 변환 로직을 데이터 타입에 직접 적용할 수 있음.

### Settings Management
- Pydantic은 환경 변수나 설정 파일을 통한 애플리케이션 설정 관리를 위한 기능을 제공함.
- `BaseSettings` 클래스를 활용하여 설정 값을 모델로 정의하고, 환경변수에서 자동으로 값을 로드할 수 있음
- 예시
    ```python
    from pydantic import BaseSettings

    class AppConfig(BaseSettings):
        app_name: str
        admin_email: str

        class Config:
            env_file = ".env"
    ```

### Model Inheritance
- 모델 간 상속을 통해 코드의 재사용성을 높이고, 모델 정의를 간결하게 유지할 수 있음
- 부모 모델의 필드와 검증 로직을 상속받아 새로운 모델을 쉽게 정의할 수 있음

### Aliases and Field Mapping
- `Field` 함수의 `alias` 매개변수를 사용하여 모델 필드의 외부 이름을 정의할 수 있음
- 이는 JSON과 같은 외부 데이터 소스와 모델을 매핑할 때 유용함.

### Post-Parsing Processing with `@validator`
- `@validator` 데코레이터를 활용한 후처리를 통해, 파싱된 데이터에 추가적인 변환 로직을 적용할 수 있음
- 이는 데이터를 최종적으로 사용하기 전에 필요한 조정을 가능하게 함