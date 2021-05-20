window.onload = () => {
    //In case user is already logged in
    if(sessionStorage.getItem('username')!=null){
        window.location.href = "home.html";
    }

    let btn = document.getElementsByClassName('btn')[0];
    let username = $('#username');
    let password = $('#password');
    let firstName = $('#firstname');
    let lastName = $('#lastname');
    let gender = $('#gender');
    let age = $('#age');

    btn.addEventListener('click',() => {
        var obj = {
            'username' : `${username.val()}`,
            'password' : `${password.val()}`,
            'firstname' : `${firstName.val()}`,
            'lastname' : `${lastName.val()}`,
            'gender' : `${gender.val()}`,
            'age' : `${age.val()}`
        }

        $.post('http://127.0.0.1:8000/auth_api/signup',obj,(response) => {
            alert(response.message + "\n If user is created successfully move to login page");
        })
    });
}