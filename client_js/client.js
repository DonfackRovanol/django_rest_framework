const LoginForm = document.getElementById("login-form");
const baseEndpoint = "http://127.0.0.1:8000/api";
const productlist = document.getElementById("product-list")

if (LoginForm){
    LoginForm.addEventListener('submit', handleLogin);
}

function handleLogin(event){
    event.preventDefault();
    const loginEndpoint = `${baseEndpoint}/token/`;

    let loginFormData = new FormData(LoginForm);

    let loginObjectData = Object.fromEntries(loginFormData);
    let bodyJsonData = JSON.stringify(loginObjectData);
   
    const options = {
        method:"POST",
        headers:{
            "content-Type":"application/json"
        },
        body: bodyJsonData
    }

    fetch(loginEndpoint, options)
    .then(response => {
        console.log(response);
        return response.json();
    })
    .then(authData => {
        handleAuthData(authData, getProductList);
    })
    .catch(err => {
        console.log('error', err);
    })
}

function handleAuthData(authData, callback){
    localStorage.setItem('access', authData.access);
    localStorage.setItem('refresh', authData.access);
    if(callback){
        callback()
    }
}

function writeTocontainer(data){
    if(productlist){
        productlist.innerHTML = "<pre>" + JSON.stringify(data, null,4) + "</pre>";
    } 
}

function getProductList(){
    const endpoint = `${baseEndpoint}/create-list/`;
    const option = {
        method :"GET",
        headers:{
            "content-type":"application/json",
            "Authorization":`Bearer ${localStorage.getItem('access')}`
        },
    }
    fetch(endpoint, option)
    .then(response=>response.json())
    .then(data =>{
        writeTocontainer(data)
    })
}