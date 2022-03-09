try{
    loginUser();
}catch (e) {
    // console.log(e);
}

// function to login user with phone number or email
function loginUser(){
    $('#loginForm')[0].onsubmit = function (e) {
        e.preventDefault();
        let data = {
            phoneOrEmail: $('#loginPhoneOrEmail').val(),
            password: $('#password').val()
        };
        let url = $('#loginUrl')[0].href;
        postRequest(url, data);
    }
}


// function to show error message when phone/email or password is incorrect
function showErrorMessage(msg){
    if(msg === 'Phone number/email or password is incorrect'){
        $('#loginPhoneOrEmailMsg')[0].classList.remove('d-none');
        $('#loginPasswordMsg')[0].classList.remove('d-none');
        setTimeout(function () {
            $('#loginPhoneOrEmailMsg')[0].classList.add('d-none');
            $('#loginPasswordMsg')[0].classList.add('d-none');
        }, 10000);
    }
    if(msg === 'No account with the given number exists'){
        $('#noAccountExistsMsg')[0].classList.remove('d-none');
        setTimeout(function () {
            $('#noAccountExistsMsg')[0].classList.add('d-none');
        }, 10000)
    }
}


function noAccountExistsMessage(msg){

}


// function to redirect to home page after login
function loginRedirect(response){
    if(response.includes('logged in')) {
        window.location.href = '/';
    }
}


// function to change type of phone/email input field. if user inputs string, type is changed to email,
// if user inputs number type is changed to tel, for validation purpose
try{
    $('#loginPhoneOrEmail')[0].oninput = function(){
        if(this.value === ''){
            this.type = 'email';
            this.removeAttribute('pattern');
        }else if(this.value >= 0){
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



