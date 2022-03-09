
// function to get csrf_token from a cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// csrf_token
const csrftoken = getCookie('csrftoken');


// Ajax request to save data
function postRequest(url, data){
    $.ajax({
        url: url,
        headers: {'X-CSRFToken': csrftoken},
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: function(response){
            console.log(response);

            // try{
            //     appendLis(response.subcategories, response.categoryId);
            // }catch(err){
            //     // console.log(err);
            // }
            //
            // try{
            //     appendMoreCategoriesLis(response.moreCategories, response.subcategoryId);
            // }catch(err){
            //     // console.log(err);
            // }

            try{
                registerRedirect(response);
            }catch(err){
                // console.log(err);
            }

            try{
                loginRedirect(response);
            }catch(err){
                // console.log(err);
            }

            try {
                showUsernameMsg(response);
            }catch(err) {
                // console.log(err);
            }

            try {
                showPhoneOrEmailMsg(response);
            }catch(err) {
                // console.log(err);
            }

            try {
                showPasswordMessage(response);
            }catch(err) {
                // console.log(err);
            }

            try {
                showErrorMessage(response.errorMsg);
            }catch(err) {
                // console.log(err);
            }

            updateWishlistIcon(response.wishlistItemsTotal);
            updateCartIcon(response.cartIconTotal);
            updateItems(response.cartIconTotal);

        },
        error: function(error){
            console.log(error.responseText);
        }
    });
}


// Ajax request to get data
// function getProductData(url){
//     $.ajax({
//         url: url,
//         type: 'GET',
//         success: function (response) {
//             console.log(response);
//         },
//         error: function (error) {
//             console.log(error);
//         }
//     });
// }


// function to update wish list items total in wish list icon in navbar
function updateWishlistIcon(value) {
    $('#wishlistIcon').text(value)
}


// function to update items quantity in cart icon in navbar
function updateCartIcon(value) {
    $('#cartIcon').text(value);
}


// function to show stars based on rating received from backend
function showStars(){
    let stars = $('.stars-holder');
    stars.each(function (index, star) {
        let rating = star.previousElementSibling.innerText;
        for(let i = 0; i < rating; i++){
            star.children[i].classList.add('text-warning');
        }
    })
}
showStars();


// function to redirect to product when a wish list or cart item is clicked
function redirectToProduct(_this){
    let url = _this.parentElement.lastElementChild.children[1].href;
    window.location.href = url;
}


