

// function to delete wish list item
function deleteWishlistItem(_this) {
    let tr = _this.parentElement.parentElement.parentElement;
    let productId = _this.parentElement.previousElementSibling.previousElementSibling.innerText;
    let url = _this.parentElement.nextElementSibling.href;

    postRequest(url, {productId});
    tr.innerHTML = '';
}

