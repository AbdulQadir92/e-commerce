
setQuantity();
setShipping();
setTotal();
incrementQuantity();
decrementQuantity();


// function to set quantity
function setQuantity(){
    let quantity = 0;
    $('.item-quantity').each(function (index, item) {
        quantity += Number(item.innerText);
    });
    $('#cartQuantity').text(quantity);
}


// function to set shipping
function setShipping(){
    let shipping = 0;
    $('.item-shipping').each(function (index, item){
        shipping += Number(item.innerText.slice(1));
    });
    $('#cartShipping').text('$'+shipping.toFixed(2));
}


// function to set total
function setTotal() {
    let total = 0;
    $('.item-total').each(function(index, item){
        total += Number(item.innerText.slice(1));
    });
    $('#cartTotal').text('$'+total.toFixed(2));
}


// function to make an increment in quantity, total and items
function incrementQuantity() {
    $('.plus-btn').each(function(index, item){
        item.onclick = function(){
            let mainDiv = this.parentElement.parentElement.parentElement;

            let quantityElement = this.previousElementSibling;
            let quantity = quantityElement.innerText;

            quantity = Number(quantity) + 1;
            quantityElement.innerText = quantity;

            updatePrice(mainDiv, quantity);

            let id = mainDiv.children[0].innerText;
            let url = mainDiv.children[1].children[0].href;

            postRequest(url, {id});
            setTotal();
            setQuantity();
        }
    })
}


// function to make a decrement in quantity, total and items
function decrementQuantity(){
    $('.minus-btn').each(function(index, item){
        item.onclick = function () {
            let mainDiv = this.parentElement.parentElement.parentElement;

            let quantityElement = this.nextElementSibling;
            let quantity = quantityElement.innerText;

            if(quantity > 1){
                quantity = Number(quantity) - 1;
            }else{
                quantity = 1;
                return;
            }
            quantityElement.innerText = quantity;

            updatePrice(mainDiv, quantity);

            let id = mainDiv.children[0].innerText;
            let url = mainDiv.children[1].children[1].href;

            postRequest(url, {id});
            setTotal();
            setQuantity();
        }
    })
}


// function to update subtotal
function updatePrice(mainDiv, quantity){
    let price = mainDiv.children[4].firstElementChild.innerText.slice(1);
    price = parseFloat(price) * quantity;
    mainDiv.children[7].firstElementChild.innerText = '$' + price.toFixed(2);
}


// function to update items
function updateItems(data) {
    $('#cartQuantity').text(data);
}


// function to delete cart item
function deleteCartItem(_this){
    let tr = _this.parentElement.parentElement.parentElement;
    let cartItemId = tr.children[0].innerText;
    let url = tr.children[1].children[2].href;

    postRequest(url, {id: cartItemId});
    tr.innerHTML = '';

    setQuantity();
    setShipping();
    setTotal();
}


