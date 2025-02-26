<template>

    <body>
        <div class="centerImg">
            <img class="myImg" src="/Logo.jpg">
        </div>
        <h1>Авторизация</h1>
        <div style="max-width: 400px; margin-left: auto; margin-right: auto; padding: 15px;">
            <div class="text-field text-field_floating-3">
                <input class="text-field__input" id="name" name="name" type="text" v-model="userName" placeholder="Имя">
                <label class="text-field__label" for="name">Имя</label>
            </div>
            <div class="text-field text-field_floating-3">
                <input class="text-field__input" id="email" name="email" type="password" v-model="userPass"
                    placeholder="Пароль">
                <label class="text-field__label" for="email">Пароль</label>
            </div>
            <div style="display: flex; justify-content: center; align-items: center;">
                <button class="glow-on-hover" @click="sendData()">Авторизация</button>
            </div>
        </div>
        <div class="centerImg">
            <p><a href="#/register" style="color: black;">Регистрация</a></p>
        </div>
    </body>
</template>

<script>
export default {
    data() {
        return {
            users: {},
            error: '',
            userName: '',
            userPass: ''
        }
    },
    methods: {
        sendData() {
            if (this.userName == '') {
                this.error = 'Имя не введено';
                return;
            }
            if (this.userPass == '') {
                this.error = 'Пароль не введен';
                return;
            }

            this.error = '';

            this.users = {
                name: this.userName,
                pass: this.userPass
            }
        }
    }
}
</script>

<style></style>