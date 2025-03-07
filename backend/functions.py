import bcrypt
import asyncio

#hashpw хэширует пароль включая в него какую то соль, хз что это говорят для безопасности надо
async def hash_password (password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

#checkpw принимает строку пароля в виде байтов и сравнивает с сохранённым хэшированным паролем, возвращает true or false
async def check_password (hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode(), hashed_password)


if __name__ == '__main__':
    async def main():

        # хэшируем пароль для внесения в бд через ранее прописанную функцию
        entered_pass = "new_password"
        hashed_password = await hash_password(entered_pass)

        # проверяем соответствие пароля
        old_pass = "new_password"
        #а тут надо как-то надо вернуть результат фронтенду пока тут просто принт,
        #чтобы понимать что надо отправить фронтенду
        if await check_password(hashed_password, old_pass):
            print("верный пароль")
        else:
            print("неверный пароль")
    asyncio.run(main())