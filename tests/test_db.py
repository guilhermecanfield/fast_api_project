from sqlalchemy import select

from fast_zero.models import User


def test_creat_user(session):
    user = User(
        username='guil_canfield',
        email='guilherme.canfield87@gmail.com',
        password='123@senha',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'guilherme.canfield87@gmail.com')
    )

    assert result.username == 'guil_canfield'
