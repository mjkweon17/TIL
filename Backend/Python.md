### repr 함수
- 객체의 인쇄 가능한 표현을 문자열로 반환하는 데 사용
- 객체를 개발자가 이해할 수 있는 형태로 표현하기 위해 사용되며, 주로 디버깅과 로깅 목적으로 활용
- 이 메서드는 클래스의 인스턴스를 나타내는 공식적인 문자열을 제공하여, 인스턴스의 주요 정보를 명확하게 전달할 수 있도록 함
- 클래스 내에서 `__repr__` 매직 메서드를 정의함으로써, 해당 클래스의 인스턴스를 `repr()` 함수를 사용해 호출했을 때 반환할 문자열을 사용자 정의할 수 있음
- 예
    ```python
    class Terms(Base):
    __tablename__ = 'Terms'
    terms_id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    title = Column(Text, nullable=False)
    is_active = Column(Boolean, nullable=False, server_default=text("1"))

    def __repr__(self):
        return f"<Terms(terms_id={self.terms_id}, title={self.title}, is_active={self.is_active})>"
    ```
    - `__repr__` 메서드는 `Terms` 인스턴스의 `terms_id`, `title`, 그리고 `is_active` 속성을 포함하는 문자열을 반환
    - 해당 객체의 상태를 명확하게 파악할 수 있게 해줌
    - 예를 들어 `Terms` 인스턴스를 만들고 이를 출력할 경우, 다음과 같은 형태의 문자열이 반환됨
        - <Terms(terms_id=1, title='이용 약관', is_active=True)>
        - 이 문자열은 객체의 주요 속성과 그 값들을 보여주므로, 객체의 현재 상태에 대한 명확한 이해를 도움