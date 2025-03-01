<template>
<body>
    <div class="wrapper">
        <h1>Регистрация</h1>
        <div class="centerImg">
            <img class="myImg" src="/Logo.jpg">
        </div>
        <div>
            <h3>Имя</h3>
            <input type="text" v-model="userName" maxlength="15">
            <p>{{ errorName }}</p>
        </div>
        <div>
            <h3>Пароль</h3>
            <input type="password" v-model="userPass" id="pass" maxlength="15">
            <p>{{ errorPass }}</p>
        </div>
        <div>
            <h3>Повторите пароль</h3>
            <input type="password" v-model="re_userPass" id="re_pass" maxlength="15">
            <p>{{ errorPass }}</p>
            <p>{{ re_errorPass }}</p>
        </div>
        <div>
            <button @click="sendData()">Регистрация</button>
            <p>{{ users }}</p>
        </div>
        <div>
            <p>Если вы были уже ранее зарегистрированы, то можете <a href="#/login"
                    style="color:white">авторизоваться</a></p>
        </div>
    </div>
</body>
</template>

<script>
import axios from 'axios' 

export default {
    data() {
        return {
            users: {},
            errorName: '',
            errorPass: '',
            userName: '',
            userPass: '',
            re_userPass: '',
        }
    },
    methods: {
        sendData() {
            if (this.userName == '') {
                this.errorName = 'Имя не введено';
                if (this.userPass == '') {
                    this.errorPass = 'Пароль не введен';
                    return;
                }
                return;
            }

            if (this.userPass == '') {
                this.errorPass = 'Пароль не введен';
                if (this.userName == '') {
                    this.errorName = 'Имя не введено';
                    return;
                }
                return;
            }

            if (this.userPass != this.re_userPass) {
                this.re_errorPass = 'Пароли не совпадают';
                return;
            }

            this.re_userPass = '';
            this.errorName = '';
            this.errorPass = '';

            this.users = {
                name: this.userName,
                pass: this.userPass
            }
        }
    }
}
</script>

<style>
.wrapper button {
    width: 15vh;
    height: 5vh;
    color: whitesmoke;
    background-color: rgba(0, 0, 0, 0.726);
    border-radius: 25px;
    border-color: blueviolet;
    font-size: 1rem;
}

.wrapper button:active{
    background-color: blueviolet;
}

.wrapper p{
    color: rgb(255, 255, 255);
    font-style: italic;
}

.wrapper input {
    margin: 10px;
    width: 30vh;
    height: 5vh;
    border-radius: 10px;
}

.wrapper {
    width: 1000px;
    height: 800px;
    background-color: rgba(135, 133, 255, 0.329);
    border-radius: 50px;
    margin-right: auto;
    margin-left: auto;
    text-align: center;
}

.wrapper h1 {
    color: rgb(255, 255, 255);
    font-weight: lighter;
    text-align: center;
}

.wrapper h3 {
    color: rgb(255, 255, 255);
    font-weight: lighter;
    text-align: center;
}
</style>