try{
    createUser();
}catch(e){
    // console.log(e);
}


// function to get data from user registration form and send it to backend
function createUser() {
    $('#registerForm')[0].onsubmit = function(e){
        e.preventDefault();

        let data = {
            username: $('#username').val(),
            phoneOrEmail: $('#phoneOrEmail').val(),
            password1: $('#password1').val(),
            password2: $('#password2').val()
        };

        let url = $('#registerUrl')[0].href;
        postRequest(url, data);
    };
}


// function to show message if username is already taken
function showUsernameMsg(msg){
    if(msg === 'Username is already taken'){
        $('#usernameMsg')[0].classList.remove('d-none');
        setTimeout(function(){
            $('#usernameMsg')[0].classList.add('d-none');
        }, 10000);
    }
}


// function to show message if phone number / email is already taken
function showPhoneOrEmailMsg(msg) {
    if(msg === 'Phone number or email is already taken'){
        $('#phoneOrEmailMsg')[0].classList.remove('d-none');
        setTimeout(function () {
            $('#phoneOrEmailMsg')[0].classList.add('d-none');
        }, 10000);
    }
}


// function to show message if passwords donot match
function showPasswordMessage(msg) {
    if(msg === 'Passwords do not match'){
        $('#passwordMsg')[0].classList.remove('d-none');
        setTimeout(function () {
            $('#passwordMsg')[0].classList.add('d-none');
        }, 10000);
    }
}


// function to redirect to home page if user has been created successfully on backend
function registerRedirect(response){
    if(response === 'Account has been created successfully') {
        window.location.href = '/';
    }
}


// function to change type of phone/email input field. if user inputs string, type is changed to email,
// if user inputs number type is changed to tel, for validation purpose
try {
    $('#phoneOrEmail')[0].oninput = function () {
        if(this.value === ''){
            this.type = 'email';
            this.removeAttribute('pattern');
        } else if(this.value >= 0){
            let val = this.value;
            this.value = '';
            this.type = 'tel';
            this.pattern = '[0-9]{11}';
            this.value = val;
        }
};

}catch(err){
    // console.log(err);
}
