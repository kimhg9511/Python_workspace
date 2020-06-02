# 튜토리얼 프로젝트 디렉터리 구조

```
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

# 테스트(Coverage)

pytest, coverage 설치

```shell
$ pip install pytest coverage
```

[프로젝트 폴더]/tests 디렉터리 생성

tests/conftest.py (테스트 환경설정)

```python
import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')
# fixture : 
# 테스팅에서 쓰이는 값이나 리소스에 대한 부분
# 미리 준비해 두는 준비 도구 및 재료(ex: 객체, 환경, DB, etc...)
# Pytest에서는 호출되는 함수를 fixture를 이용하여 다른 함수(테스트용)로 바꿔서 호출한다.
@pytest.fixture
def app():
    # file 임시 파일을 생성하고 오픈하여 파일 객체와 경로를 리턴해줍니다.
    # 테스트가 끝나면, 이 임시 파일은 닫히고 삭제됩니다.
    db_fd, db_path = tempfile.mkstemp()
	
    app = create_app({
        # Flask에게 테스트 모드임을 알립니다.
        'TESTING': True,
        # DATABASE 경로를 재정의
        # 데이터베이스 테이블이 생성되고 테스트 데이터가 INSERT 됩니다.
        'DATABASE': db_path, 
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)

# application object가 생성될 때 app fixture로 인하여 app.test_client()가 호출됩니다.
# runner,client 공통으로 서버의 구동 없이 테스트 환경을 구축할 때 사용합니다.
@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```



tests/data.sql (데이터 INSERT 테스트)

```sql
INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
```



tests/test_factory.py (factory 테스트)

```python
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```

