<template>
<body>
    <div class="wrapper">
        <h1>Авторизация</h1>
        <div class="centerImg">
            <img class="myImg" src="/Logo.jpg">
        </div>
        <div>
            <h3>Имя</h3>
            <input type="text" v-model="userName">
            <p>{{ error }}</p>
        </div>
        <div>
            <h3>Пароль</h3>
            <input type="password" v-model="userPass">
            <p>{{ error }}</p>
        </div>
        <div>
            <button @click="sendData()">Авторизация</button>
        </div>
        <div>
            <p style="color: white;">Если вы не были ранее зарегистрированы, то можете сделать это здесь - <a href="#/register"
                    style="color:white">Регистрация</a></p>
        </div>
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

.wrapper input {
    margin: 10px;
    width: 30vh;
    height: 5vh;
    border: 0;
    border-bottom: 5px solid rgb(107, 58, 153);
    border-radius: 10px;
    outline: none;
    font-size: larger;
}

.wrapper input:focus{
    border-bottom-color: blueviolet;
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