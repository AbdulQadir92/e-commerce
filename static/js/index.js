
redirectToProductDetails();
sortByPrice();


// function to redirect to product details page
function redirectToProductDetails(){
    $('.product-card').each(function (index, product) {
        product.onclick = function () {
            window.location.href = this.children[1].href;
        }
    });
}


// Brand js
function checkedBrandProducts(){
    let checkboxes = $('.more-categories-sidebar input[type=checkbox]');
    checkboxes.each(function (index, item) {
       item.onchange = function () {
           if(this.checked){
               console.log(this.nextElementSibling.href);
               $(this).prop('checked', false);
               window.location.href = this.nextElementSibling.href;
           } else {
               window.location.href = this.nextElementSibling.nextElementSibling.href;
           }
       }
    });
}
checkedBrandProducts();

function sortByPriceBrand(){
    let anchors = $('#sortByPriceUlBrand .nav-item');
    anchors.each(function (index, item) {
        let brand_id;
        item.onclick = function () {
            let url = 'http://127.0.0.1:8000/sort_by_price_brand/';
            let price = this.getAttribute('data-price');

            let checkboxes = $('.more-categories-sidebar input[type=checkbox]');
            checkboxes.each(function (index, item) {
                if(item.checked){
                    brand_id = item.id + '/';
                }
            });

            console.log(url + brand_id + price);
            window.location.href = url + brand_id + price;
        }
    });
    // console.log(anchors);
}
sortByPriceBrand();


// More Categories Js
function redirectToMoreCategory(_this){
    window.location.href = _this.previousElementSibling.previousElementSibling.href;
}


//
function sortByPrice(){
    let lis = $('#sortByPriceUl .nav-item');
    lis.each(function(index, item){
        item.onclick = function(){
            let url = this.parentElement.children[0].href;
            let price = this.getAttribute('data-price');
            console.log(price);
            console.log(url+'/'+price);
        }
    });
}
