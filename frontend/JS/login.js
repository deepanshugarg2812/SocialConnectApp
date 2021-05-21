window.onload = () => {
    //In case user is already logged in
     if(sessionStorage.getItem('username')!=null){
        window.location.href = "home.html";
     }


    let btn = document.getElementsByClassName('btn')[0];
    let username = $('#username');
    let password = $('#password');

    btn.addEventListener('click',() => {
        var obj = {
            'username' : `${username.val()}`,
            'password' : `${password.val()}`
        }

        $.post('http://127.0.0.1:8000/auth_api/login',obj,(response) => {
            if(response.username==null || response.username==undefined){
                alert("Invalid username or password");
            }
            else{
                sessionStorage.setItem('username',response.username);
                window.location.href = "home.html";
            }
        })
    });
}