addBorderTop();

// function to add item to cart or wish list
function addProductToCartOrWishlist(urlElementId){
        let productId = $('#productId')[0].innerText;
        let url = $(urlElementId)[0].href;
        postRequest(url, {productId});
}


// function to add or remove yellow background to stars on mouse enter and on mouse leave respectively
function chanageStarBackground(){
    let stars = $('.stars-container');
    stars.each(function (index, star) {
        let _stars = star.children;

        // add yellow background to stars on mouse enter
        // _stars[0].onmouseenter = function(){
        //     if(!_stars[0].classList.contains('text-warning')){
        //         _stars[0].classList.add('text-warning');
        //     }
        // };
        //
        // _stars[1].onmouseenter = function(){
        //     if(!_stars[1].classList.contains('text-warning')){
        //         _stars[1].classList.add('text-warning');
        //         _stars[0].classList.add('text-warning');
        //     }
        // };
        //
        // _stars[2].onmouseenter = function(){
        //     if(!_stars[2].classList.contains('text-warning')){
        //         _stars[2].classList.add('text-warning');
        //         _stars[1].classList.add('text-warning');
        //         _stars[0].classList.add('text-warning');
        //     }
        // };
        //
        // _stars[3].onmouseenter = function(){
        //     if(!_stars[3].classList.contains('text-warning')){
        //         _stars[3].classList.add('text-warning');
        //         _stars[2].classList.add('text-warning');
        //         _stars[1].classList.add('text-warning');
        //         _stars[0].classList.add('text-warning');
        //     }
        // };
        //
        // _stars[4].onmouseenter = function(){
        //     if(!_stars[4].classList.contains('text-warning')){
        //         _stars[4].classList.add('text-warning');
        //         _stars[3].classList.add('text-warning');
        //         _stars[2].classList.add('text-warning');
        //         _stars[1].classList.add('text-warning');
        //         _stars[0].classList.add('text-warning');
        //     }
        // };
        //


        // add yellow background to stars on mouse enter
        addYellowBackground(_stars, 4);
        addYellowBackground(_stars, 3);
        addYellowBackground(_stars, 2);
        addYellowBackground(_stars, 1);
        addYellowBackground(_stars, 0);


        // remove yellow background from star on mouse leave
        removeYellowBackground(_stars, 4);
        removeYellowBackground(_stars, 3);
        removeYellowBackground(_stars, 2);
        removeYellowBackground(_stars, 1);

        // remove yellow background from all stars on mouse leave
        star.onmouseleave = function () {
             for(let i = 0; i < star.children.length; i++){
                 if(star.children[i].classList.contains('text-warning')){
                     star.children[i].classList.remove('text-warning');
                 }
             }
        };

    })
}
chanageStarBackground();


// function to add class text-warning to star ( and previous stars ) on mouse enter
function addYellowBackground(_stars, starIndex) {
    _stars[starIndex].onmouseenter = function () {
        if(!_stars[starIndex].classList.contains('text-warning')){
            for(let i = starIndex; i >= 0; i--){
                _stars[i].classList.add('text-warning');
            }
        }
    }
}


// function to remove class text-warning from star on mouse leave
function removeYellowBackground(_stars, starIndex){
    _stars[starIndex].onmouseleave = function(){
        if(_stars[starIndex].classList.contains('text-warning')){
            _stars[starIndex].classList.remove('text-warning');
        }
    };
}


// function to get star rating when an star is clicked
function getRating(){
    $('.product-details-star').each(function (index, star) {
        star.onclick = function () {
            console.log($(this).data('rating'));
        }
    });
}
getRating();


// function to add border top to productDetailsParent when screen width is less than 992 px;
function addBorderTop(){
    let productDetailsParent = $('#productDetailsParent')[0];
    if(window.innerWidth <= 992){
        console.log(productDetailsParent);
        productDetailsParent.classList.add('border-top');
    } else {
        productDetailsParent.classList.remove('border-top');
    }
}

